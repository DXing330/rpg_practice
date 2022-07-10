import random
import copy
import sys
sys.path.append("./bossbattles")
from rpg2_classdefinitions import (Player_PC, Monster_NPC, Pet_NPC,
                                   ItemBag_PC, Spell_PC)
import rpg2_dg_boss_battle_function as dgboss_func
import rpg2_gs_boss_battle_function as gsboss_func
import rpg2_gs_boss_battle_advanced as agsboss_func
import rpg2_dl_boss_battle_function as dlboss_func
import rpg2_ah_boss_battle_function as ahboss_func
import rpg2_ah_boss_battle_advanced as aahboss_func
from rpg2_boss_constants import BOSS_CONSTANTS
B = BOSS_CONSTANTS()
#function the chooses the potential bosses that can be picked
def quest_difficulty(ib_pc):
        x = 0
        if ib_pc.dg_trophy > 0:
                x = 1
        if ib_pc.gs_trophy > 0:
                x = 2
        return x
#dgboss_func.boss_battle_phase(heroes_party, monster_party,
#                              hero_pet, heroes_bag, heroes_magic)
#function that picks a boss for the heroes to fight
def quest(h_p, m_p, p_npc, ib_pc, s_pc):
        print("Are you heroes? ")
        print("Thank GOD for you all. ")
        print("You have to help! ")
        n = quest_difficulty(ib_pc)
        x = random.randint(0, n)
        if x == 0:
                y = random.randint(0, ib_pc.dg_trophy)
                if y >= B.ADVANCED_SPAWN:
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
                y = random.randint(0, ib_pc.gs_trophy)
                if y >= B.ADVANCED_SPAWN:
                        print("The golden slime is ruining our economy! ")
                        choice = input("FIGHT  or RUN? F/R? ")
                        if choice.upper() == "F":
                                agsboss_func.boss_battle(h_p, m_p, p_npc,
                                                              ib_pc, s_pc)
                        else:
                                print("Oh no, what ever will we do? ")
                else:
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
                else:
                        print("An acid hydra is terrorizing our swamp! ")
                        choice = input("FIGHT  or RUN? F/R? ")
                        if choice.upper() == "F":
                                ahboss_func.boss_battle(h_p, m_p, p_npc,
                                                              ib_pc, s_pc)
                        else:
                                print("Oh no, what ever will we do? ")


monster_party = []
heroes_party = []
heroes_magic = []
heroes_bag = ItemBag_PC(2, 2, 2, 10)
fireball = Spell_PC("Fireball", 3, 3, "Fire", 3)
rainstorm = Spell_PC("Rainstorm", 2, 3, "Water", 2)
earthspike = Spell_PC("Earthspike", 3, 1, "Earth", 2)
mage = Player_PC("Mage", 1, 10, 10, 2, 2, 0, 5)
warrior = Player_PC("Warrior", 1, 15, 15, 5, 3, 0, 0, 0, 0, 2, 1)
cleric = Player_PC("Cleric", 1, 10, 10, 1, 2, 0, 5)
summoner = Player_PC("Summoner", 1, 10, 10, 2, 2, 0, 0)
heroes_pet = Pet_NPC("Awoken Angel", 2, 4)
firemon = Monster_NPC("Mon", 100, 0, 0, 0, "Fire", 0)
watermon = Monster_NPC("Mon", 100, 0, 0, 0, "Water", 0)
earthmon = Monster_NPC("Mon", 100, 0, 0, 0, "Earth", 0)
heroes_magic.append(fireball)
heroes_magic.append(rainstorm)
heroes_magic.append(earthspike)
heroes_party.append(cleric)
heroes_party.append(mage)
heroes_party.append(summoner)
monster_party.append(firemon)
monster_party.append(watermon)
monster_party.append(earthmon)

quest(heroes_party, monster_party, heroes_pet, heroes_bag, heroes_magic)
