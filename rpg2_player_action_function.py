import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC)
import rpg2_party_management_functions as party_func
import rpg2_player_skill_function as pskill_func
import rpg2_pet_action_function as pet_func
from rpg2_constants import Constants
C = Constants()
##function where the player makes a choice of what they want to do in battle
#function that controls what the pet will do during battle
#need to input the pet and both parties
def pet_action(p_npc, h_p, m_p):
        for hero in h_p:
                if hero.name == "Summoner":
                        pet_func.pet_random_action(p_npc, h_p, m_p)
                else:
                        x = random.randint(0, C.PET_ACTION_UP * len(h_p))
                        if x == 0:
                                pet_func.pet_random_action(p_npc, h_p, m_p)


#player attack function
def player_attack(p_pc, m_npc):
        #warrior hits more often
        if p_pc.name == "Warrior" and p_pc.level == C.LEVEL_LIMIT:
                m_npc.health -= max((p_pc.atk + p_pc.weapon + p_pc.atkbonus - m_npc.defense),1)
                print(p_pc.name, "hits", m_npc.name)
                m_npc.health -= max((p_pc.atk + p_pc.weapon + p_pc.atkbonus - m_npc.defense),1)
                print(p_pc.name, "hits", m_npc.name)
                m_npc.health -= max((p_pc.atk + p_pc.weapon + p_pc.atkbonus - m_npc.defense),1)
                print(p_pc.name, "hits", m_npc.name)
        elif p_pc.name == "Warrior":
                m_npc.health -= max((p_pc.atk + p_pc.weapon + p_pc.atkbonus - m_npc.defense),1)
                print(p_pc.name, "hits", m_npc.name)
                m_npc.health -= max((p_pc.atk + p_pc.weapon + p_pc.atkbonus - m_npc.defense),1)
                print(p_pc.name, "hits", m_npc.name)
        #if defender attacks then they can no longer block incoming attacks
        elif p_pc.name == "Defender":
                m_npc.health -= max((p_pc.atk + p_pc.weapon + p_pc.atkbonus + p_pc.armor + p_pc.defense - m_npc.defense),1)
                p_pc.name = "Knight"
                print (p_pc.name, "bashes", m_npc.name, "with their shield. ")
        else:
                m_npc.health -= max((p_pc.atk + p_pc.weapon + p_pc.atkbonus - m_npc.defense),1)
                print(p_pc.name, "hits", m_npc.name)

        
#use item function
def use_item(p_pc, ib_pc):
        print ("What item do you want to use? ")
        check = input("Heal, Mana, Boosts? H/M/B ")
        if check.upper() == "H" and ib_pc.heal >= 1:
                ib_pc.heal -= 1
                print("You feel the pain recede.")
                p_pc.health = min(p_pc.maxhealth, (p_pc.health + (p_pc.maxhealth/2)))
        elif check.upper() == "M" and ib_pc.mana >= 1:
                ib_pc.mana -= 1
                print("You feel your mana pulse with energy.")
                p_pc.mana = round(p_pc.mana * C.BUFF)
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
        for spell in s_pc:
                spell.stats()
        try:
                s = int(input("Which spell do you want to use?"
                              "The first spell is number 1, etc."))
                spell = s_pc[(s - 1)]
                if spell.targets > 1:
                        for monster in m_p:
                                if monster.element == spell.element:
                                        print ("The magic has no effect on", monster.name)
                                else:
                                        monster.health = max((monster.health - (spell.power + p_pc.mana)),0)
                                        print (spell.name, "hits", monster.name)
                if spell.targets == 1:
                        monster = party_func.pick_monster(m_p)
                        if monster.element == spell.element:
                                        print ("The magic has no effect on", monster.name)
                        else:
                                monster.health = max((monster.health - (spell.power + p_pc.mana)),0)
                ib_pc.coins -= ((spell.cost * spell.targets) + spell.power)
                p_pc.mana -= ((spell.cost * spell.targets) + spell.power)
                if ib_pc.coins < 0 or p_pc.mana < (spell.cost * p_pc.atk):
                        print (spell.name, "goes awry.")
                        p_pc.health -= (spell.cost + (spell.power * p_pc.atk))
                        p_pc.stats()
                        ib_pc.coins = max(ib_pc.coins, 0)
        except (ValueError, AttributeError):
                print ("The magic fails.")
#advanced magic is reserved for max level mages
def use_advanced_magic(p_pc, s_pc, m_p):
        for spell in s_pc:
                spell.stats()
        try:
                s = int(input("Which spell do you want to use?"
                              "The first spell is number 1, etc."))
                spell = s_pc[(s - 1)]
                if spell.targets > 1:
                        for monster in m_p:
                                if monster.element == spell.element:
                                        print ("The magic has no effect on", monster.name)
                                else:
                                        monster.health = max((monster.health - (spell.power + p_pc.mana)),0)
                                        print (spell.name, "hits", monster.name)
                if spell.targets == 1:
                        monster = party_func.pick_monster(m_p)
                        if monster.element == spell.element:
                                        print ("The magic has no effect on", monster.name)
                        else:
                                monster.health = max((monster.health - (spell.power + p_pc.mana)),0)
                p_pc.mana -= ((spell.cost * spell.targets) + max((spell.power - p_pc.skill), 0))
                if p_pc.mana < (spell.cost * spell.targets * p_pc.level):
                        print (spell.name, "goes awry.")
                        p_pc.health -= (spell.power + (p_pc.atk * p_pc.mana))
        except (ValueError, AttributeError):
                use_advanced_magic(p_pc, s_pc, m_p)
#need the player, pet, monsters, itembag and spells
#player makes a choice about what to do
def player_action(p_pc, h_p, m_p, ib_pc, s_pc, p_npc):
        print ("What do you do?")
        check = input("Attack, Item, Magic, Skill or Pray? P/A/I/M/S")
        if check.upper() == "A" and len(m_p) > 1:
                monster = party_func.pick_monster(m_p)
                player_attack(p_pc, monster)
        elif check.upper() == "A" and len(m_p) == 1:
                for monster in m_p:
                        player_attack(p_pc, monster)
        elif check.upper() == "I":
                ib_pc.stats()
                use_item(p_pc, ib_pc)
        elif check.upper() == "M":
                if p_pc.name == "Mage" and p_pc.level == C.LEVEL_LIMIT:
                        use_advanced_magic(p_pc, s_pc, m_p)
                elif p_pc.mana > 0:
                        use_magic_attack(p_pc, s_pc, ib_pc, m_p)
                else:
                        print ("You can't do that.")
        elif check.upper() == "S":
                pskill_func.use_skill(p_pc, h_p, m_p, ib_pc, s_pc, p_npc)
        elif check.upper() == "P" or "":
                p_pc.health += p_pc.level + p_pc.skill
                print("A warm and gentle breeze soothes your soul. ")
                if p_pc.name == "Cleric":
                        p_pc.mana += 1
                        p_pc.defense += 1
                        print("Holy light envelops you. ")
        else:
                player_action(p_pc, h_p, m_p, ib_pc, s_pc, p_npc)
