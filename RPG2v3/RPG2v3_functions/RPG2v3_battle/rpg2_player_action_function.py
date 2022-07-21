import random
import sys
sys.path.append("../RPG2v3_def")
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC, Weapon_PC,
                                   Armor_PC)
import rpg2_party_management_functions as party_func
from rpg2_constants import Constants
from rpg2_constant_lists import List_Constants
L = List_Constants()
C = Constants()

import rpg2_player_skill_function as pskill_func
import rpg2_pet_action_function as pet_func
import rpg2_element_function as element_func
import rpg2_equipment_effect_function as ee_func
import rpg2_monster_effect_function as me_func
##function where the player makes a choice of what they want to do in battle
#function that controls what the pet will do during battle
#need to input the pet and both parties
def pet_action(p_npc, h_p, m_p):
        #check if there is an angel ally
        aaly = None
        comp = None
        for ally in p_npc:
                if "Angel" in ally.name:
                        aaly = ally
        for ally in p_npc:
                if "Spirit" in ally.name:
                        comp = ally
        if aaly != None:
                pet_func.angel_action(aaly, h_p, m_p)
        if comp != None:
                pet_func.companion_action(comp, h_p, m_p)

#player attack function
def player_attack(p_pc, m_npc, h_w, h_a, h_p, m_p):
        print(p_pc.name, "hits", m_npc.name)
        weapon = party_func.check_equipment(p_pc, h_w)
        new_pa = ee_func.weapon_effect(m_npc, p_pc, weapon, h_p, m_p)
        new_atk = element_func.check_element_player_attack(p_pc, new_pa, m_npc, weapon)
        f_atk = me_func.monster_def_buff_effect(m_npc, new_atk, p_pc, h_p, weapon, h_a, m_p)
        #warrior hits more often
        if "Warrior" in p_pc.name and p_pc.level >= C.LEVEL_LIMIT:
                m_npc.health -= f_atk
                print(p_pc.name, "hits", m_npc.name)                        
                new_pa = ee_func.weapon_effect(m_npc, p_pc, weapon, h_p, m_p)
                new_atk = element_func.check_element_player_attack(p_pc, new_pa, m_npc, weapon)
                f_atk = me_func.monster_def_buff_effect(m_npc, new_atk, p_pc, h_p, weapon, h_a, m_p)
                m_npc.health -= f_atk
                print(p_pc.name, "hits", m_npc.name)
                new_pa = ee_func.weapon_effect(m_npc, p_pc, weapon, h_p, m_p)
                new_atk = element_func.check_element_player_attack(p_pc, new_pa, m_npc, weapon)
                f_atk = me_func.monster_def_buff_effect(m_npc, new_atk, p_pc, h_p, weapon, h_a, m_p)
                m_npc.health -= f_atk
                print(p_pc.name, "hits", m_npc.name)
                if "Fierce" in p_pc.name:
                        new_pa = ee_func.weapon_effect(m_npc, p_pc, weapon, h_p, m_p)
                        new_atk = element_func.check_element_player_attack(p_pc, new_pa, m_npc, weapon)
                        f_atk = me_func.monster_def_buff_effect(m_npc, new_atk, p_pc, h_p, weapon, h_a, m_p)
                        m_npc.health -= f_atk
        elif "Warrior" in p_pc.name or "Hero" in p_pc.name:
                m_npc.health -= max((new_atk - m_npc.defense),1)
                print(p_pc.name, "hits", m_npc.name)
                new_pa = ee_func.weapon_effect(m_npc, p_pc, weapon, h_p, m_p)
                new_atk = element_func.check_element_player_attack(p_pc, new_pa, m_npc, weapon)
                f_atk = me_func.monster_def_buff_effect(m_npc, new_atk, p_pc, h_p, weapon, h_a, m_p)
                m_npc.health -= f_atk
        #if defender attacks then they can no longer block incoming attacks
        elif p_pc.name == "Defender":
                m_npc.health -= max((new_atk + p_pc.defense - m_npc.defense),1)
                p_pc.name = "Knight"
                print (p_pc.name, "bashes", m_npc.name, "with their shield. ")
                #if they have the right weapon then they can change back into defender
                if weapon != None:
                        if weapon.effect == "Shield":
                                new_pa = ee_func.weapon_effect(m_npc, p_pc, weapon, h_p, m_p)
                for amr in h_a:
                        if amr.user == "Defender":
                                amr.user = p_pc.name
        else:
                m_npc.health -= f_atk

        
#use item function
def use_item(p_pc, ib_pc):
        print ("What item do you want to use? ")
        check = input("Heal, Mana, Boosts? H/M/B ")
        if check.upper() == "H" and ib_pc.heal >= p_pc.level:
                #health potions restore health and decrease poison
                ib_pc.heal -= p_pc.level
                print("You feel the pain recede.")
                p_pc.health = min(p_pc.maxhealth, (p_pc.health + (p_pc.maxhealth//2)))
                p_pc.poison -= min(p_pc.level, p_pc.poison)
        elif check.upper() == "M" and ib_pc.mana >= p_pc.level:
                ib_pc.mana -= p_pc.level
                print("You feel your mana pulse with energy.")
                p_pc.mana += p_pc.maxmana//2
        elif check.upper() == "B" and ib_pc.buff >= p_pc.level:
                ib_pc.buff -= p_pc.level
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
                        print (spell.name, "hits", monster.name)
                        new_spell_power = element_func.check_element_spell(spell, monster)
                        spell_atk = me_func.monster_buff_check_spell(monster, p_pc, spell, new_spell_power)
                        monster.health -= spell_atk
        elif spell.targets == 1:
                print (spell.name, "hits", monster.name)
                monster = party_func.pick_monster(m_p)
                new_spell_power = element_func.check_element_spell(spell, monster)
                spell_atk = me_func.monster_buff_check_spell(monster, p_pc, spell, new_spell_power)
                monster.health -= spell_atk
        ib_pc.coins -= ((spell.cost * spell.targets) + spell.power)
        p_pc.mana -= ((spell.cost * spell.targets) + spell.power)
        if ib_pc.coins < 0 or p_pc.mana < spell.cost:
                print (spell.name, "goes awry.")
                p_pc.health -= spell.cost * spell.targets * spell.power
                p_pc.stats()
                ib_pc.coins = max(ib_pc.coins, 0)
#advanced magic is reserved for max level mages
def use_advanced_magic(p_pc, s_pc, m_p):
        for spel in s_pc:
                spel.stats()
        spell = party_func.pick_hero(s_pc)
        if spell.targets > 1:
                for monster in m_p:
                        print (spell.name, "hits", monster.name)
                        new_spell_power = element_func.check_element_spell(spell, monster)
                        spell_atk = me_func.monster_buff_check_spell(monster, p_pc, spell, new_spell_power)
                        monster.health -= spell_atk

        elif spell.targets == 1:
                print (spell.name, "hits", monster.name)
                monster = party_func.pick_monster(m_p)
                new_spell_power = element_func.check_element_spell(spell, monster)
                spell_atk = me_func.monster_buff_check_spell(monster, p_pc, spell, new_spell_power)
                monster.health -= spell_atk

        p_pc.mana -= ((spell.cost * spell.targets) + max((spell.power - p_pc.skill), 0))
        if "Arch" in p_pc.name:
                p_pc.mana += ((spell.cost * spell.targets) + spell.power)//2
        if p_pc.mana  * p_pc.level < (spell.cost * spell.targets):
                print (spell.name, "goes awry.")
                p_pc.health -= spell.cost * spell.targets * spell.power

#need the player, pet, monsters, itembag and spells
#player makes a choice about what to do
def player_action(p_pc, h_p, m_p, ib_pc, s_pc, p_npc, h_w, h_a):
        if "Undead" in p_pc.name:
                monster = party_func.pick_monster(m_p)
                player_attack(p_pc, monster, h_w, h_p, m_p)
        elif "Totem" in p_pc.name:
                p_pc.health += 1
        elif p_pc.name != "Undead" and p_pc.name != "Totem":
                print ("What do you do?")
                check = input("Attack, Item, Magic, Skill or Pray? P/A/I/M/S")
                if check.upper() == "A" and len(m_p) > 1:
                        monster = party_func.pick_monster(m_p)
                        player_attack(p_pc, monster, h_w, h_a, h_p, m_p)
                elif check.upper() == "A" and len(m_p) == 1:
                        for monster in m_p:
                                player_attack(p_pc, monster, h_w, h_a, h_p, m_p)
                elif check.upper() == "I":
                        ib_pc.stats()
                        use_item(p_pc, ib_pc)
                elif check.upper() == "M":
                        if "Mage" in p_pc.name and p_pc.level >= C.LEVEL_LIMIT and len(s_pc) > 0:
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
                        p_pc.defbonus += 1
                        print("A warm and gentle breeze soothes your soul. ")
                        if "Cleric" in p_pc.name:
                                p_pc.mana += 1
                                p_pc.poison -= min(p_pc.level, p_pc.poison)
                                print("Holy light envelops you. ")
                else:
                        player_action(p_pc, h_p, m_p, ib_pc, s_pc, p_npc, h_w, h_a)
