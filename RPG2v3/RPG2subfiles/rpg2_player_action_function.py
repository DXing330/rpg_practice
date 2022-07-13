import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC, Weapon_PC,
                                   Armor_PC)
import rpg2_party_management_functions as party_func
import rpg2_player_skill_function as pskill_func
import rpg2_pet_action_function as pet_func
import rpg2_element_function as element_func
import rpg2_equipment_effect_function as ee_func
from rpg2_constants import Constants
C = Constants()
##function where the player makes a choice of what they want to do in battle
#function that controls what the pet will do during battle
#need to input the pet and both parties
def pet_action(p_npc, h_p, m_p):
        for hero in h_p:
                if hero.name == "Summoner":
                        pet_func.pet_random_action(p_npc, h_p, m_p)
                elif hero.name == "Hero":
                        hero.maxhealth += round(p_npc.atk ** C.PET_HP_BUFF)
                        hero.atkbonus += round(p_npc.atk ** C.PET_ATK_BUFF)
                        hero.defbonus += round(p_npc.atk ** C.PET_DEF_BUFF)
                        hero.skill += round(p_npc.atk ** C.PET_SKILL_BUFF)
                        hero.poison -= min(p_npc.stage, hero.poison)
                        print (p_npc.name, "uses their blessing magic on", hero.name)                        
                elif hero.name == "Golem":
                        if hero.atk > 0:
                                monster = party_func.pick_random_healthy_monster(m_p)
                                monster.health -= max((p_npc.atk - monster.defense), 1)
                                print (p_npc.name, "uses their attacking magic on", monster.name)
                        elif hero.skill > 0:
                                hero = party_func.pet_pick_random_healthy_hero(h_p)
                                hero.maxhealth += round(p_npc.atk ** C.PET_HP_BUFF)
                                hero.atkbonus += round(p_npc.atk ** C.PET_ATK_BUFF)
                                hero.defbonus += round(p_npc.atk ** C.PET_DEF_BUFF)
                                hero.skill += round(p_npc.atk ** C.PET_SKILL_BUFF)
                                print (p_npc.name, "uses their blessing magic on", hero.name)
                        elif hero.defense > 0:
                                hero = party_func.pet_pick_random_injured_hero(h_p)
                                hero.poison -= min(p_npc.stage, hero.poison)
                                hero.health = min((hero.health + p_npc.atk), hero.maxhealth)
                                print (p_npc.name, "uses their healing magic on", hero.name)
                        elif hero.mana > 0:
                                monster = party_func.pick_random_healthy_monster(m_p)
                                monster.atk = max(monster.atk - round(p_npc.atk ** C.PET_ATK_BUFF), 0)
                                monster.defense = max(monster.defense - round(p_npc.atk ** C.PET_DEF_BUFF), 0)
                                print (p_npc.name, "uses their weakening magic on", monster.name)
                else:
                        x = random.randint(0, C.PET_ACTION_UP * len(h_p) * len(m_p))
                        if x == 0:
                                pet_func.pet_random_action(p_npc, h_p, m_p)


#player attack function
def player_attack(p_pc, m_npc, h_w, h_p, m_p):
        weapon = party_func.check_equipment(p_pc, h_w)
        new_pa = ee_func.weapon_effect(m_npc, p_pc, weapon, h_p, m_p)
        new_atk = element_func.check_element_player_attack(p_pc, new_pa, m_npc, weapon)
        #warrior hits more often
        if p_pc.name == "Warrior" and p_pc.level == C.LEVEL_LIMIT:
                m_npc.health -= max((new_atk - m_npc.defense),1)
                print(p_pc.name, "hits", m_npc.name)
                new_pa = ee_func.weapon_effect(m_npc, p_pc, weapon, h_p, m_p)
                new_atk = element_func.check_element_player_attack(p_pc, new_pa, m_npc, weapon)
                m_npc.health -= max((new_atk - m_npc.defense),1)
                print(p_pc.name, "hits", m_npc.name)
                new_pa = ee_func.weapon_effect(m_npc, p_pc, weapon, h_p, m_p)
                new_atk = element_func.check_element_player_attack(p_pc, new_pa, m_npc, weapon)
                m_npc.health -= max((new_atk - m_npc.defense),1)
                print(p_pc.name, "hits", m_npc.name)
        elif p_pc.name == "Warrior" or p_pc.name == "Hero":
                m_npc.health -= max((new_atk - m_npc.defense),1)
                print(p_pc.name, "hits", m_npc.name)
                new_pa = ee_func.weapon_effect(m_npc, p_pc, weapon, h_p, m_p)
                new_atk = element_func.check_element_player_attack(p_pc, new_pa, m_npc, weapon)
                m_npc.health -= max((new_atk - m_npc.defense),1)
                print(p_pc.name, "hits", m_npc.name)
        #if defender attacks then they can no longer block incoming attacks
        elif p_pc.name == "Defender":
                m_npc.health -= max((new_atk + p_pc.defense - m_npc.defense),1)
                p_pc.name = "Knight"
                print (p_pc.name, "bashes", m_npc.name, "with their shield. ")
        else:
                m_npc.health -= max((new_atk - m_npc.defense),1)
                print(p_pc.name, "hits", m_npc.name)

        
#use item function
def use_item(p_pc, ib_pc):
        print ("What item do you want to use? ")
        check = input("Heal, Mana, Boosts? H/M/B ")
        if check.upper() == "H" and ib_pc.heal >= 1:
                #health potions restore health and decrease poison
                ib_pc.heal -= 1
                print("You feel the pain recede.")
                p_pc.health = min(p_pc.maxhealth, (p_pc.health + (p_pc.maxhealth/2)))
                p_pc.poison -= min(p_pc.level, p_pc.poison)
        elif check.upper() == "M" and ib_pc.mana >= 1:
                ib_pc.mana -= 1
                print("You feel your mana pulse with energy.")
                p_pc.mana += p_pc.level
        elif check.upper() == "B" and ib_pc.buff >= 1:
                ib_pc.buff -= 1
                print("Adrenaline races through your veins.")
                p_pc.atk = round(p_pc.atk * C.BUFF)
        else:
                print ("You can't do that right now.")
                

#magic function
#needs the players, spells and monsters
def use_magic_attack(p_pc, s_pc, ib_pc, m_p):
        ib_pc.stats()
        for spel in s_pc:
                spel.stats()
        spell = party_func.pick_hero(s_pc)
        if spell.targets > 1:
                for monster in m_p:
                        new_spell_power = element_func.check_element_spell(spell, monster)
                        monster.health -= min(new_spell_power + p_pc.mana, monster.health)
                        print (spell.name, "hits", monster.name)
        elif spell.targets == 1:
                monster = party_func.pick_monster(m_p)
                new_spell_power = element_func.check_element_spell(spell, monster)
                monster.health -= min(new_spell_power + p_pc.mana, monster.health)
                print (spell.name, "hits", monster.name)
        ib_pc.coins -= ((spell.cost * spell.targets) + spell.power)
        p_pc.mana -= ((spell.cost * spell.targets) + spell.power)
        if ib_pc.coins < 0 or p_pc.mana < spell.cost:
                print (spell.name, "goes awry.")
                p_pc.health -= (spell.cost + (spell.power * p_pc.atk))
                p_pc.stats()
                ib_pc.coins = max(ib_pc.coins, 0)
#advanced magic is reserved for max level mages
def use_advanced_magic(p_pc, s_pc, m_p):
        for spel in s_pc:
                spel.stats()
        spell = party_func.pick_hero(s_pc)
        if spell.targets > 1:
                for monster in m_p:
                        new_spell_power = element_func.check_element_spell(spell, monster)
                        monster.health -= min(new_spell_power + p_pc.mana, monster.health)
                        print (spell.name, "hits", monster.name)
        elif spell.targets == 1:
                monster = party_func.pick_monster(m_p)
                new_spell_power = element_func.check_element_spell(spell, monster)
                monster.health -= min(new_spell_power + p_pc.mana, monster.health)
                print (spell.name, "hits", monster.name)

        p_pc.mana -= ((spell.cost * spell.targets) + max((spell.power - p_pc.skill), 0))
        if p_pc.mana < (spell.cost * spell.targets * p_pc.level):
                print (spell.name, "goes awry.")
                p_pc.health -= (spell.power + (p_pc.atk * p_pc.mana))

#need the player, pet, monsters, itembag and spells
#player makes a choice about what to do
def player_action(p_pc, h_p, m_p, ib_pc, s_pc, p_npc, h_w, h_a):
        print ("What do you do?")
        check = input("Attack, Item, Magic, Skill or Pray? P/A/I/M/S")
        if check.upper() == "A" and len(m_p) > 1:
                monster = party_func.pick_monster(m_p)
                player_attack(p_pc, monster, h_w, h_p, m_p)
        elif check.upper() == "A" and len(m_p) == 1:
                for monster in m_p:
                        player_attack(p_pc, monster, h_w, h_p, m_p)
        elif check.upper() == "I":
                ib_pc.stats()
                use_item(p_pc, ib_pc)
        elif check.upper() == "M":
                if p_pc.name == "Mage" and p_pc.level == C.LEVEL_LIMIT and len(s_pc) > 0:
                        use_advanced_magic(p_pc, s_pc, m_p)
                elif p_pc.mana > 0 and len(s_pc) > 0:
                        use_magic_attack(p_pc, s_pc, ib_pc, m_p)
                else:
                        print ("You can't do that.")
        elif check.upper() == "S":
                pskill_func.use_skill(p_pc, h_p, m_p, ib_pc, s_pc, p_npc, h_w, h_a)
        elif check.upper() == "P":
                p_pc.health += p_pc.level
                p_pc.atkbonus += 1
                print("A warm and gentle breeze soothes your soul. ")
                if p_pc.name == "Cleric":
                        p_pc.mana += 1
                        p_pc.defbonus += 1
                        p_pc.poison -= min(p_pc.level, p_pc.poison)
                        print("Holy light envelops you. ")
        else:
                player_action(p_pc, h_p, m_p, ib_pc, s_pc, p_npc, h_w, h_a)
