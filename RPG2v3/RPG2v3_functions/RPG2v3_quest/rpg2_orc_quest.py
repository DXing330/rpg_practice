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
L = List_Constants()
C = Constants()
Q = Q_Constants()
sys.path.append(".")
import rpg2_quest_battle as battle_func
import rpg2_quest_monster_function as mon_func

#function that controls the test of flight
def test_of_flight(p_pc, m_npc):
        outcome = 0
        print ("Your equipment is remove and you're led to a cliff. ")
        print ("The orc chief stands beside you. ")
        print ("'Do you dare to test your bravery against me? Puny man?' ")
        choice = input("AGREE/REFUSE A/R? ")
        if choice.upper() == "R":
                outcome = -1
                print ("'Pathetic. '")
                print ("'Are we going to let these cowards tell us what to do?! '")
                print ("The surrounding orcs roar with confidence. ")
        elif choice.upper() == "A":
                print ("'Heh, I like your guts. '")
                test = True
                while test:
                        check = input("JUMP? J")
                        if check.upper() == "J":
                                x = random.randint(0, (p_pc.maxhealth//2))
                                y = random.randint(0, (Q.CORC_HP)//2)
                                m_npc.health -= y
                                #the player can use tricks to cushion their fall
                                p_pc.health -= max(x - p_pc.skill//2, 1) 
                                print ("You both jump off the cliff. ")
                                m_npc.hstats()
                                p_pc.hstats()
                        if m_npc.health <= 0:
                                test = False
                        if p_pc.health <= 0:
                                test = False
                if not test:
                        if m_npc.health <= 0 and p_pc.health > 0:
                                print ("'You're a real man! '")
                                print ("'Let's play again sometime. '")
                                outcome = 2
                        elif m_npc.health <= 0 and p_pc.health <= 0:
                                print ("'Not bad. '")
                                print ("'We'll say this is a draw. '")
                                outcome = 1
                                p_pc.health = 1
                        elif m_npc.health > 0 and p_pc.health <= 0:
                                print ("'Pathetic. '")
                                print ("'See what we're up against boys?! '")
                                print ("The surrounding orcs roar with confidence. ")
                                outcome = 0
                                p_pc.health = 1
        return outcome
#function that controls the test of fight
def test_of_fight(p_pc, m_npc):
        outcome = 0
        g_p = []
        #fight against a group of goblins
        print ("Your equipment is remove and you're led to a cage filled with goblins. ")
        print ("The orc chief stands beside another cage. ")
        print ("'Do you dare to test your might against me? Puny man?' ")
        #pick the amount of goblins to fight
        try:
                choice = int(input("How many goblins do you want to fight? "))
                for x in range(0, choice):
                        mon = mon_func.super_goblin_maker()
                        g_p.append(mon)                        
        except:
                print ("That's not a real choice. ")
                test_of_fight(p_pc, m_npc)
        health = 0
        atk = 0
        for mon in g_p:
                health += mon.health
                atk += mon.atk
        goblin_party_one = Monster_NPC("Goblins", health, atk, Q.GOBLIN_DEF,
                                   Q.GOBLIN_SKILL, "Earth", 0)
        goblin_party_two = Monster_NPC("Goblins", health, atk, Q.GOBLIN_DEF,
                                   Q.GOBLIN_SKILL, "Earth", 0)
        test = True
        while test:
                check = input("ATTACK? A?")
                if check.upper() == "A":
                        goblin_party_one.health -= p_pc.atk + p_pc.atkbonus - goblin_party_two.defense
                        p_pc.health -= max((goblin_party_one.atk - p_pc.defense - p_pc.defbonus), 1)
                        goblin_party_two.health -= m_npc.atk - goblin_party_two.defense
                        m_npc.health -= max((goblin_party_one.atk - m_npc.defense), 1)
                        print ("A brawl occurs. ")
                if m_npc.health <= 0:
                        test = False
                if p_pc.health <= 0:
                        test = False
                if goblin_party_one.health <= 0:
                        test = False
                if goblin_party_two.health <= 0:
                        test = False
        if not test:
                if m_npc.health <= 0 and p_pc.health > 0:
                        print ("'You're a real man! '")
                        print ("'Let's play again sometime. '")
                        outcome = 3
                elif m_npc.health <= 0 and p_pc.health <= 0:
                        print ("'Not bad. '")
                        print ("'We'll say this is a draw. '")
                        outcome = 1
                        p_pc.health = 1
                elif m_npc.health > 0 and p_pc.health > 0 and goblin_party_one.health <= 0 and goblin_party_two.health <= 0:
                        print ("'Not bad. '")
                        print ("'We'll say this is a draw. '")
                        outcome = 1
                elif m_npc.health > 0 and p_pc.health > 0 and goblin_party_two.health > 0:
                        print ("'You're pretty quick. '")
                        outcome = 2
                elif m_npc.health > 0 and p_pc.health > 0 and goblin_party_one.health > 0:
                        print ("'Boring '")
                        print ("'Why didn't you pick a more challenging number?' ")
                        outcome = 0
                elif m_npc.health > 0 and p_pc.health <= 0:
                        print ("'Pathetic. '")
                        print ("'See what we're up against boys?! '")
                        print ("The surrounding orcs roar with confidence. ")
                        outcome = 0
                        p_pc.health = 1
        return outcome
#function that controls the test of might
def test_of_might(p_pc, m_npc):
        outcome = 0
        print ("Your equipment is remove and you're led to a table. ")
        print ("The orc chief sits down on one side an places his elbow on the table. ")
        print ("'Do you dare to test your might against me? Puny man?' ")
        p_pc.stats()
        m_npc.stats()
        choice = input("SIT/REFUSE? S/R?")
        if choice.upper() == "S":
                print ("'Heh, I like your guts. '")
                test = True
                while test:
                        check = input("SLAP? S")
                        if check.upper() == "S":
                                x = random.randint((p_pc.atk + p_pc.atkbonus)//2 ,
                                                   (p_pc.atk + p_pc.atkbonus))
                                y = random.randint((m_npc.atk)//2, m_npc.atk)
                                m_npc.health -= x
                                #players can use tricks during the slap battle
                                p_pc.health -= y - max((p_pc.defense + p_pc.defbonus), p_pc.skill)
                                print ("You slap each other across the face. ")
                                m_npc.hstats()
                                p_pc.hstats()
                        if m_npc.health <= 0:
                                test = False
                        if p_pc.health <= 0:
                                test = False
                if not test:
                        if m_npc.health <= 0 and p_pc.health > 0:
                                print ("'You're a real man! '")
                                print ("'Let's play again sometime. '")
                                outcome = 2
                        elif m_npc.health <= 0 and p_pc.health <= 0:
                                print ("'Not bad. '")
                                print ("'We'll say this is a draw. '")
                                outcome = 1
                                p_pc.health = 1
                        elif m_npc.health > 0 and p_pc.health <= 0:
                                print ("'Pathetic. '")
                                print ("'See what we're up against boys?! '")
                                print ("The surrounding orcs roar with confidence. ")
                                outcome = 0
                                p_pc.health = 1
        elif choice.upper() == "R":
                outcome = -1
                print ("'Pathetic. '")
                print ("'Are we going to let these cowards tell us what to do?! '")
                print ("The surrounding orcs roar with confidence. ")
        return outcome
                                
                
#function that controls the orc village
def orc_quest(h_p, o_p, p_npc, ib_pc, s_pc, h_w, h_a, q_i, c):
        #decide how many chances the orcs give you to impress them
        #chances depend on your rank
        print ("There are ", len(o_p), "orcs standing and ready to fight. ")
        c_list = []
        if len(h_p) <= 0:
                print ("You flee from the raging orcs. ")
        elif len(o_p) <= 0:
                print ("You've managed to make them settle down. ")
        elif len(o_p) > 0:
                for a in range(0, c):
                        counter = Pet_NPC("none", 1, 1)
                        c_list.append(counter)
                print ("You have ", len(c_list), "chances to impress left. ")
                number_orcs = len(o_p)
                #make a choice about whether to use force or diplomacy
                choice = input("FIGHT or CONTEST? F/C? ")
                if choice.upper() == "F":
                        print ("'That's more like it! Come on boys! It's time to fight! '")
                        #if you fight then you fight the remaining orcs
                        battle_func.battle_phase(h_p, o_p,
                                                 p_npc, ib_pc,
                                                 s_pc, h_w,
                                                 h_a, q_i)
                elif choice.upper() == "C" and len(c_list) == 0:
                        print ("'Enough games! Prove yourself worthy of our respect through battle! '")
                        battle_func.battle_phase(h_p, o_p,
                                                 p_npc, ib_pc,
                                                 s_pc, h_w,
                                                 h_a, q_i)
                elif choice.upper() == "C" and len(c_list) > 0:
                        c_list.pop()
                        print ("'Ha, you dare to challenge us to a contest? '")
                        contest = random.randint(0, 2)
                        if contest == 0:
                                print ("'Fine then, prove your might. '")
                                for hro in h_p:
                                        hro.stats()
                                hero = party_func.pick_hero(h_p)
                                orc = mon_func.orc_chief()
                                outcome = test_of_might(hero, orc)
                                if outcome > 0:
                                        for x in range(0, outcome * len(h_p)):
                                                o_p.pop()
                                        number_orcs = len(o_p)
                                        print ("Some orcs are impressed by you and sit down. ")
                                        print ("There are ", number_orcs, "orcs standing and ready to fight. ")
                                        orc_quest(h_p, o_p, p_npc, ib_pc, s_pc, h_w, h_a, q_i, len(c_list))
                                elif outcome < 0:
                                        for x in range(0, len(h_p)):
                                                mon = mon_func.orc_maker()
                                                o_p.append(mon)
                                        number_orcs = len(o_p)
                                        print ("Some orcs are disgusted by you and stand up. ")
                                        print ("There are ", number_orcs, "orcs standing and ready to fight. ")
                                        orc_quest(h_p, o_p, p_npc, ib_pc, s_pc, h_w, h_a, q_i, len(c_list))
                                elif outcome == 0:
                                        print ("There are ", number_orcs, "orcs standing and ready to fight. ")
                                        orc_quest(h_p, o_p, p_npc, ib_pc, s_pc, h_w, h_a, q_i, len(c_list))
                        elif contest == 1:
                                print ("'Fine then, prove your might. '")
                                for hro in h_p:
                                        hro.stats()
                                hero = party_func.pick_hero(h_p)
                                orc = mon_func.orc_chief()
                                outcome = test_of_fight(hero, orc)
                                if outcome > 0:
                                        for x in range(0, outcome * len(h_p)):
                                                o_p.pop()
                                        number_orcs = len(o_p)
                                        print ("Some orcs are impressed by you and sit down. ")
                                        print ("There are ", number_orcs, "orcs standing and ready to fight. ")
                                        orc_quest(h_p, o_p, p_npc, ib_pc, s_pc, h_w, h_a, q_i, len(c_list))
                                elif outcome == 0:
                                        print ("There are ", number_orcs, "orcs standing and ready to fight. ")
                                        orc_quest(h_p, o_p, p_npc, ib_pc, s_pc, h_w, h_a, q_i, len(c_list))
                        elif contest == 2:
                                print ("'Fine then, prove your might. '")
                                for hro in h_p:
                                        hro.stats()
                                hero = party_func.pick_hero(h_p)
                                orc = mon_func.orc_chief()
                                outcome = test_of_flight(hero, orc)
                                if outcome > 0:
                                        for x in range(0, outcome * len(h_p)):
                                                o_p.pop()
                                        number_orcs = len(o_p)
                                        print ("Some orcs are impressed by you and sit down. ")
                                        print ("There are ", number_orcs, "orcs standing and ready to fight. ")
                                        orc_quest(h_p, o_p, p_npc, ib_pc, s_pc, h_w, h_a, q_i, len(c_list))
                                elif outcome == 0:
                                        print ("There are ", number_orcs, "orcs standing and ready to fight. ")
                                        orc_quest(h_p, o_p, p_npc, ib_pc, s_pc, h_w, h_a, q_i, len(c_list))
                else:
                        orc_quest(h_p, o_p, p_npc, ib_pc, s_pc, h_w, h_a, q_i, c)
