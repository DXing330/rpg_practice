import random
import copy
import sys
sys.path.append("./bossbattles")
sys.path.append("./RPG2v3_def")
sys.path.append("./RPG2v3_battle")
from rpg2_classdefinitions import (Player_PC, Monster_NPC, Pet_NPC, ItemBag_PC)
import rpg2_dg_boss_battle_function as dgboss_func
import rpg2_gs_boss_battle_function as gsboss_func
import rpg2_gs_boss_battle_advanced as agsboss_func
import rpg2_dl_boss_battle_function as dlboss_func
import rpg2_ah_boss_battle_function as ahboss_func
import rpg2_ah_boss_battle_advanced as aahboss_func
import rpg2_sq_boss_battle_function as sqboss_func
import rpg2_ip_boss_battle_function as ipboss_func
import rpg2_ip_boss_battle_advanced as aipboss_func
from rpg2_boss_constants import BOSS_CONSTANTS
B = BOSS_CONSTANTS()
#function the chooses the potential bosses that can be picked
def boss_difficulty(ib_pc):
        x = 0
        if ib_pc.dg_trophy > 0:
                x = 1
        if ib_pc.gs_trophy > 0:
                x = 2
        if ib_pc.ah_trophy > 0:
                x = 3
        if ib_pc.sq_trophy > 0:
                x = 4
        return x
#dgboss_func.boss_battle_phase(heroes_party, monster_party,
#                              hero_pet, heroes_bag, heroes_magic)
#function that picks a boss for the heroes to fight
def random_boss(h_p, m_p, p_npc, ib_pc, s_pc, h_w, h_a):
        print("Are you heroes? ")
        print("Thank GOD for you all. ")
        print("You have to help! ")
        n = boss_difficulty(ib_pc)
        x = random.randint(0, n)
        if x == 0:
                y = random.randint(0, ib_pc.dg_trophy)
                if y >= B.ADVANCED_SPAWN + (ib_pc.dg_trophy/2):
                        print("The demon lord has appeared! ")
                        choice = input("FIGHT  or RUN? F/R? ")
                        if choice.upper() == "F":
                                print("You approach the castle. ")
                                dlboss_func.boss_battle(h_p, m_p, p_npc,
                                                        ib_pc, s_pc, h_w, h_a)
                        else:
                                print("Oh no, what ever will we do? ")
                else:
                        print("It's the demon general nearby. ")
                        choice = input("FIGHT  or RUN? F/R? ")
                        if choice.upper() == "F":
                                print("You approach the castle. ")
                                dgboss_func.boss_battle(h_p, m_p, p_npc,
                                                        ib_pc, s_pc, h_w, h_a)
                        else:
                                print("Oh no, what ever will we do? ")

        elif x == 1:
                y = random.randint(0, ib_pc.gs_trophy)
                if y >= B.ADVANCED_SPAWN + (ib_pc.gs_trophy/2):
                        print("The golden slime is ruining our economy! ")
                        choice = input("FIGHT  or RUN? F/R? ")
                        if choice.upper() == "F":
                                agsboss_func.boss_battle(h_p, m_p, p_npc,
                                                        ib_pc, s_pc, h_w, h_a)
                        else:
                                print("Oh no, what ever will we do? ")
                else:
                        print("The golden slime is ruining our economy! ")
                        choice = input("FIGHT  or RUN? F/R? ")
                        if choice.upper() == "F":
                                gsboss_func.boss_battle(h_p, m_p, p_npc,
                                                        ib_pc, s_pc, h_w, h_a)
                        else:
                                print("Oh no, what ever will we do? ")
        elif x == 2:
                y = random.randint(0, ib_pc.ah_trophy)
                if y >= B.ADVANCED_SPAWN + (ib_pc.ah_trophy/2):
                        print("An acid hydra is terrorizing our swamp! ")
                        choice = input("FIGHT  or RUN? F/R? ")
                        if choice.upper() == "F":
                                print ("You enter the swamp. ")
                                aahboss_func.boss_battle(h_p, m_p, p_npc,
                                                        ib_pc, s_pc, h_w, h_a)
                        else:
                                print("Oh no, what ever will we do? ")
                else:
                        print("An acid hydra is terrorizing our swamp! ")
                        choice = input("FIGHT  or RUN? F/R? ")
                        if choice.upper() == "F":
                                print ("You enter the swamp. ")
                                ahboss_func.boss_battle(h_p, m_p, p_npc,
                                                        ib_pc, s_pc, h_w, h_a)
                        else:
                                print("Oh no, what ever will we do? ")
        elif x == 3:
                '''y = random.randint(0, ib_pc.sq_trophy)
                if y >= B.ADVANCED_SPAWN + (ib_pc.sq_trophy/2):
                        print("A succubus is stealing our men! ")
                        choice = input("FIGHT  or RUN? F/R? ")
                        if choice.upper() == "F":
                                asqboss_func.boss_battle(h_p, m_p, p_npc,
                                                              ib_pc, s_pc)
                        else:
                                print("Oh no, what ever will we do? ")'''

                print("A succubus is stealing our men! ")
                choice = input("FIGHT  or RUN? F/R? ")
                if choice.upper() == "F":
                        print("You approach the castle. ")
                        sqboss_func.boss_battle(h_p, m_p, p_npc,
                                                        ib_pc, s_pc, h_w, h_a)
                else:
                        print("Oh no, what ever will we do? ")
                        
        elif x == 4:
                y = random.randint(0, ib_pc.ip_trophy)
                if y >= B.ADVANCED_SPAWN + (ib_pc.ip_trophy/2):
                        print("A white bird is freezing everything! ")
                        choice = input("FIGHT  or RUN? F/R? ")
                        if choice.upper() == "F":
                                print ("You go up the mountain. ")
                                aipboss_func.boss_battle(h_p, m_p, p_npc,
                                                        ib_pc, s_pc, h_w, h_a)
                        else:
                                print("Oh no, what ever will we do? ")
                elif y < B.ADVANCED_SPAWN:
                        print("A white bird is freezing everything! ")
                        choice = input("FIGHT  or RUN? F/R? ")
                        if choice.upper() == "F":
                                print ("You go up the mountain. ")
                                ipboss_func.boss_battle(h_p, m_p, p_npc,
                                                        ib_pc, s_pc, h_w, h_a)
                        else:
                                print("Oh no, what ever will we do? ")
