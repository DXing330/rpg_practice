import copy
import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
                                   Spell_PC, Monster_NPC, Weapon_PC,
                                   Armor_PC, QuestItems_NPC, Access_NPC)
import rpg2_party_management_functions as party_func
import rpg2_quest_battle as battle_func
from rpg2_constants import Constants
from rpg2_constant_lists import List_Constants
L = List_Constants()
C = Constants()
#quest one is goblin hunting
#fight goblins until you get the package back
def quest_one(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i):
        print ("Those damn goblins stole the package. ")
        print ("They can't have gotten too far, go find it! ")
        #make a party to fill with goblin monsters
        g_p = []
        #take away a package to start the quest
        q_i.package -= 1
        #keep track of the current rpackages that the player has
        x = q_i.rpackage
        #the goblin waves will keep increasing until you find the package
        y = len(h_p)
        #after they find another rpackage then the quest is over
        while q_i.rpackage == x:
                for z in range(0, y):
                        mon = goblin_maker()
                        g_p.append(mon)
                print ("You find a pack of goblins. ")
                battle_func.battle_phase(h_p, m_p, p_npc, ib_pc, s_pc, h_w, h_a, q_i)
                y += 1
        if q_i.rpackage > x:
                print ("Thanks. I was a little worried there. ")
                #make sure they only get one rpackage from the quest
                q_i.rpackage = x + 1
                #give them a fame
                a_i.fame += 1

#function that decides what quest to give to the player
#quests can depend on their rank in the guild and fame
def quest(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i):
        #check whether the party has any packages
        if q_i.packages > 0:
                #if so then make a quest
                x = random.randint(0, 1)
                if x == 1:
                        quest_one(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i)
                elif x == 2:
                        quest_two(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i)

