import copy
import random
import sys
sys.path.append("../RPG2v3_def")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
                                   Spell_PC, Monster_NPC, Weapon_PC,
                                   Armor_PC, QuestItems_NPC, Access_NPC)
import rpg2_party_management_functions as party_func
from rpg2_constants import Constants
from rpg2_constant_lists import List_Constants
from rpg2_constant_quests import Q_Constants
Q = Q_Constants()
L = List_Constants()
C = Constants()
import rpg2_level_up_function as lvlup_func
#hunter will be part of the monster hunter guild
#hunter will be a class that focuses on poison, traps and animal companion
name = "Hunter"
maxhp = C.LVL_UP_HP_MID
atk = C.LVL_UP_ATK_MID
defense = C.LVL_UP_DEF_MID
skill = C.LVL_UP_SKL_HIGH
#not a spell caster
mana = C.LVL_UP_MANA_LOW
#starting stats
hunter = Player_PC("Hunter", 1, 15, 15, 3, 3, 5, 0, 0)
#hunter comes with an animal companion
#this summon will be much more focused on attacking
companion = Pet_NPC("Spirit Animal", 1, 5)
'''#hunters are naturally trained at observation
'observe, will give them and their ally a bonus to attack'
#hunters need to take care of their weapons
'buff, will boost their weapon effect'
#hunters need to be able to deal with poison and injuries
'heal, will greatly decrease poison'
#hunters work with their companions
'command, will allow their ally to perform two actions'
#hunters weaken their prey first
'debuff, decrease enemy stats based on poison'
#hunters use traps and tools
'throw explosive, will send a bomb into the enemy party'
'the bomb can be damaging or poisoning'''


#method to upgrade the spirit companion
def companion_upgrade(p_npc, q_i, a_i):
        if a_i.rank > Q.GOLD and p_npc.stage < 3:
                print ("Looks like you're ready for the next step. ")
        if a_i.rank > Q.MASTER and p_npc.stage < 6:
                print ("You've come a long way. ")
                print ("I think you're ready for the next stage. ")
        print ("I can help you strengthen your BOND or TRAIN. B/T? ")
        if p_npc.stage < C.STAGE_LIMIT:
                if a_i.rank <= Q.GOLD and p_npc.stage >= 2:
                        print ("Looks like you need more experience. ")
                if a_i.rank <= Q.MASTER and p_npc.stage >= 5:
                        print ("You're still lacking. ")
                else:
                        print ("You've done a lot together. ")
                        print ("I can see that your bond is strong. ")
                        print ("Do you want me to help you manifest that bond? ")
                        print ("I'll need ", p_npc.atk ** C.INCREASE_EXPONENT, "mana gem to do it. ")
                        check = input("YES/NO? Y/N? ")
                        if check.upper() == "Y" and q_i.managem >= p_npc.atk ** C.INCREASE_EXPONENT:
                                q_i.managem -= p_npc.atk ** C.INCREASE_EXPONENT
                                lvlup_func.spirit_stage_up(p_npc)
                        else:
                                print ("Come back when you're ready. ")
        elif p_npc.stage == C.STAGE_LIMIT:
                print ("You want to help your companion train? ")
                print ("I'll need ", p_npc.atk * C.INCREASE_EXPONENT, "mana gem to do it. ")
                check = input("YES/NO? Y/N? ")
                if check.upper() == "Y" and q_i.managem >= p_npc.atk * C.INCREASE_EXPONENT:
                        q_i.managem -= p_npc.atk * C.INCREASE_EXPONENT
                        lvlup_func.pet_atk_up(p_npc)
                else:
                        print ("Come back when you're ready. ")
#function that adds the hunter to the party
def add_hunter(h_p, p_npc):
        hro = None
        copy_hero = copy.copy(hunter)
        for hero in h_p:
                if "Hunter" in hero.name:
                        hro = hero
        if hro == None:
                party_func.add_to_party(h_p, copy_hero)
        else:
                print ("You already have a hunter. ")
        cmp = None
        copy_comp = copy.copy(companion)
        for ally in p_npc:
                if "Spirit" in ally.name:
                        cmp = ally
        if cmp == None:
                p_npc.append(copy_comp)

