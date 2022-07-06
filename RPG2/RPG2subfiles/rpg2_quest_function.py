import random
import copy
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Monster_NPC, Pet_NPC, ItemBag_PC)
import rpg2_dg_boss_battle_function as dgboss_func
import rpg2_gs_boss_battle_function as gsboss_func
import rpg2_dl_boss_battle_function as dlboss_func
import rpg2_ah_boss_battle_function as ahboss_func
import rpg2_ah_boss_battle_advanced as aahboss_func
from rpg2_boss_constants import BOSS_CONSTANTS
B = BOSS_CONSTANTS()
#dgboss_func.boss_battle_phase(heroes_party, monster_party,
#                              hero_pet, heroes_bag, heroes_magic)
def quest(h_p, m_p, p_npc, ib_pc, s_pc):
        print("Are you heroes? ")
        print("Thank GOD for you all. ")
        print("You have to help! ")
        x = random.randint(0, 2)
        if x == 0:
                y = random.randint(0, ib_pc.dg_trophy)
                if y >= B.D_L_SPAWN:
                        print("The demon lord has appeared! ")
                        choice = input("FIGHT  or RUN? F/R? ")
                        if choice.upper() == "F":
                                dlboss_func.boss_battle(h_p, m_p, p_npc,
                                                              ib_pc, s_pc)
                        else:
                                print("Oh no, what ever will we do? ")
                else:
                        print("It's the demon general nearby. ")
                        choice = input("FIGHT  or RUN? F/R? ")
                        if choice.upper() == "F":
                                dgboss_func.boss_battle(h_p, m_p, p_npc,
                                                              ib_pc, s_pc)
                        else:
                                print("Oh no, what ever will we do? ")

        elif x == 1:
                print("The golden slime is ruining our economy! ")
                choice = input("FIGHT  or RUN? F/R? ")
                if choice.upper() == "F":
                        gsboss_func.boss_battle(h_p, m_p, p_npc,
                                                      ib_pc, s_pc)
                else:
                        print("Oh no, what ever will we do? ")
        elif x == 2:
                y = random.randint(0, ib_pc.ah_trophy)
                if y >= B.ADVANCED_SPAWN:
                        print("An acid hydra is terrorizing our swamp! ")
                        choice = input("FIGHT  or RUN? F/R? ")
                        if choice.upper() == "F":
                                aahboss_func.boss_battle(h_p, m_p, p_npc,
                                                              ib_pc, s_pc)
                        else:
                                print("Oh no, what ever will we do? ")
                elif y < B.ADVANCED_SPAWN:
                        print("An acid hydra is terrorizing our swamp! ")
                        choice = input("FIGHT  or RUN? F/R? ")
                        if choice.upper() == "F":
                                ahboss_func.boss_battle(h_p, m_p, p_npc,
                                                              ib_pc, s_pc)
                        else:
                                print("Oh no, what ever will we do? ")
