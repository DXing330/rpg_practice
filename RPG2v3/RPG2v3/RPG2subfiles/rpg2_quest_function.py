import copy
import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
                                   Spell_PC, Monster_NPC, Weapon_PC,
                                   Armor_PC, QuestItems_NPC, Access_NPC)
import rpg2_party_management_functions as party_func
import rpg2_quest_battle as battle_func
import rpg2_quest_monster_function as mon_func
from rpg2_constants import Constants
from rpg2_constant_lists import List_Constants
L = List_Constants()
C = Constants()
#quest two is advanced goblin fighting
#fight goblins until the town is saved
def quest_two(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i):
        print ("Those goblins are trying to invade the local village. ")
        print ("We'll need to eliminate them before they get close. ")
        new_h_p = []
        for hro in h_p:
                copy_hero = copy.copy(hro)
                new_h_p.append(copy_hero)
        g_p = []
        q_i.package -= 1
        y = len(h_p)
        #at higher ranks you need to fight more goblins
        for x in range(0, a_i.rank):
                for z in range(0, y):
                        mon = mon_func.super_goblin_maker()
                        g_p.append(mon)
                print ("You see a band of goblins approaching. ")
                battle_func.battle_phase(new_h_p, g_p, p_npc, ib_pc, s_pc, h_w, h_a, q_i)
                for hero in new_h_p:
                        if hero.health <= 0:
                                new_h_p.remove(hero)
                if len(new_h_p) == 0:
                        break
                elif len(new_h_p) > 0:
                        y += len(new_h_p)
        if len(new_h_p) <= 0:
                print ("You ok? We managed to push the goblins back for now. ")
                print ("The fees for saving you will be taken out of your pay, by the way. ")
        elif len(new_h_p) > 0:
                print ("You were a big help, thanks. ")
                q_i.rpackage += 1
                a_i.fame += round(a_i.rank ** C.DECREASE_EXPONENT)
#quest one is goblin hunting
#fight goblins until you get the package back
def quest_one(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i):
        print ("Those damn goblins stole the package. ")
        print ("They can't have gotten too far, go find it! ")
        #make a copy of the heroes party to track if they are defeated
        new_h_p = []
        for hro in h_p:
                copy_hero = copy.copy(hro)
                new_h_p.append(copy_hero)
        #make a party to fill with goblin monsters
        g_p = []
        #take away a package to start the quest
        q_i.package -= 1
        #keep track of the current rpackages that the player has
        x = q_i.rpackage
        #the goblin waves will keep increasing until you find the package
        y = len(h_p)
        #after they find another rpackage then the quest is over
        while q_i.rpackage == x and len(new_h_p) > 0:
                for z in range(0, y):
                        mon = mon_func.goblin_maker()
                        g_p.append(mon)
                print ("You find a pack of goblins. ")
                battle_func.battle_phase(new_h_p, g_p, p_npc, ib_pc, s_pc, h_w, h_a, q_i)
                for hero in new_h_p:
                        if hero.health <= 0:
                                new_h_p.remove(hero)
                y += 1
        #if the heroes lose then they get no reward
        if len(new_h_p) <= 0:
                print ("Damn it, how can you lose to goblins?! ")
                print ("I can't believe I hired you! ")
                q_i.rpackage = x

        elif q_i.rpackage > x:
                print ("Thanks. I was a little worried there. ")
                #make sure they only get one rpackage from the quest
                q_i.rpackage = x + 1
                #give them a fame
                a_i.fame += 1


#function that decides what quest to give to the player
#quests can depend on their rank in the guild and fame
def quest(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i):
        #check whether the party has any packages
        if q_i.package > 0:
                #if so then make a quest
                x = random.randint(0, 2)
                if x == 1 or x == 0:
                        quest_one(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i)
                elif x == 2:
                        quest_two(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i)
        else:
                print ("You don't have an assignment. ")

