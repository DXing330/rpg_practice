import copy
import random
import sys
sys.path.append("./RPG2v3_def")
sys.path.append("./RPG2v3_quest")
sys.path.append("./RPG2v3_battle")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
                                   Spell_PC, Monster_NPC, Weapon_PC,
                                   Armor_PC, QuestItems_NPC, Access_NPC)
import rpg2_party_management_functions as party_func
from rpg2_constants import Constants
from rpg2_constant_lists import List_Constants
from rpg2_constant_quests import Q_Constants
L = List_Constants()
C = Constants()
Q = Q_Constants()
import rpg2_quest_battle as battle_func
import rpg2_quest_monster_function as mon_func
import rpg2_orc_quest as orc_func
import rpg2_giant_quest as giant_func
#quest five is dealing with elementals
def quest_five(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i):
        print ("Seems like the magicians have summoned some wild elementals again. ")
        print ("They're causing havoc around the city. ")
        print ("Hurry up and deal with them. ")
        new_h_p = []
        for hro in h_p:
                copy_hero = copy.copy(hro)
                new_h_p.append(copy_hero)
        e_p = []
        q_i.package -= 1
        y = a_i.rank
        for m in range(0, y):
                for hero in h_p:
                        mon = mon_func.elemental_maker()
                        e_p.append(mon)
        print ("You run to the city. ")
        print ("You see massive clumps of elementals! ")
        battle_func.battle_phase(new_h_p, e_p, p_npc, ib_pc,
                                 s_pc, h_w, h_a, q_i)
        if len(new_h_p) <= 0:
                print ("You look like a mess. ")
                print ("At least we managed to deal with most of the elementals. ")
                print ("The fees for saving you will be taken out of your pay, by the way. ")
        elif len(new_h_p) > 0:
                print ("I knew I could count on you.  Thanks.")
                q_i.rpackage += 1
                a_i.fame += a_i.rank//C.INCREASE_EXPONENT
#quest four is dealing with giants
def quest_four(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i):
        print ("There are reports of some giants fighting nearby. ")
        print ("Something like that is too dangerous to allow. ")
        print ("Go find out why they're fighting and stop them. ")
        new_h_p = []
        for hro in h_p:
                copy_hero = copy.copy(hro)
                new_h_p.append(copy_hero)
        g_p = []
        q_i.package -= 1
        y = len(h_p)
        g = random.randint(2, max(3, len(h_p)))
        for p in range(0, g):
                mon = mon_func.giant_maker()
                g_p.append(mon)
        print ("You see the giants fighting from atop a hill. ")
        print ("After a lot of shouting at them, they pause to take a breather. ")
        print ("Finally noticing your shouts, they stomp over. ")
        print ("The hills shake with every step. ")
        giant_func.giant_quest(new_h_p, g_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i)
        if len(new_h_p) <= 0:
                print ("You look pretty bad. ")
                print ("At least you survived an encounter with giants. ")
                print ("A lot of people aren't that lucky. ")
        elif len(new_h_p) > 0:
                print ("I knew I could count on you.  Thanks.")
                q_i.rpackage += 1
                a_i.fame += a_i.rank
#quest three is orc negotiations
#use skill or force to convince the orcs to calm down
def quest_three(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i):
        print ("The orcs are getting uppity again. ")
        print ("We can't afford another rampage right now. ")
        print ("Go get them to settle down. ")
        new_h_p = []
        for hro in h_p:
                copy_hero = copy.copy(hro)
                new_h_p.append(copy_hero)
        o_p = []
        q_i.package -= 1
        chances = round(a_i.rank ** C.DECREASE_EXPONENT)
        y = len(h_p)
        for p in range(0, a_i.rank):
                for h in range(0, y):
                        mon = mon_func.orc_maker()
                        o_p.append(mon)
        chief = mon_func.orc_chief()
        o_p.insert(0, chief)
        print ("You arrive at the orc encampment. ")
        print ("A massive orc spots you and stomps over. ")
        print ("'What are you doing here?  This is our land!'")
        orc_func.orc_quest(new_h_p, o_p, p_npc, ib_pc, s_pc, h_w, h_a, q_i, chances)
        if len(new_h_p) <= 0:
                print ("You ok? Those orcs can be rough sometimes. ")
                print ("The fees for saving you will be taken out of your pay, by the way. ")
        elif len(new_h_p) > 0:
                print ("You were a big help, thanks. ")
                q_i.rpackage += 1
                a_i.fame += a_i.rank//C.INCREASE_EXPONENT
        
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
        r = a_i.rank//2
        #at higher ranks you need to fight more goblins
        for x in range(0, y):
                for z in range(0, r):
                        mon = mon_func.super_goblin_maker()
                        g_p.append(mon)
                print ("You see a band of goblins approaching. ")
                battle_func.battle_phase(new_h_p, g_p, p_npc, ib_pc,
                                         s_pc, h_w, h_a, q_i)
                for hero in new_h_p:
                        if hero.health <= 0:
                                new_h_p.remove(hero)
                if len(new_h_p) == 0:
                        break
                elif len(new_h_p) > 0:
                        r += a_i.rank//2
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
                y += len(h_p)
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
                x = random.randint(0, a_i.rank)
                if x == 1:
                        quest_one(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i)
                elif x == 2:
                        quest_two(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i)
                elif x == 7:
                        quest_three(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i)
                elif x == 8:
                        quest_five(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i)
                elif x == 10:
                        quest_four(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i)
                        
                else:
                        quest(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i)
        else:
                print ("You don't have an assignment. ")

