import random
import copy
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Monster_NPC,
                                   Pet_NPC, ItemBag_PC, Spell_PC, Statuses_NPC)
import rpg2_player_action_function as player_func
import rpg2_party_management_functions as party_func
from rpg2_constants import Constants
C = Constants()
from rpg2_boss_constants import BOSS_CONSTANTS
B = BOSS_CONSTANTS()
#this is the boss
A_H = Monster_NPC("Acid Hydra", B.A_H_HEALTH, B.A_H_ATK,
                           B.A_H_DEF, B.A_H_SKL, "Water",
                           B.A_H_DC)
b_p = []
#smaller slime monster maker
def baby_slime_spawn():
        monster = Monster_NPC("Baby Acid Hydra", C.MONSTER_MAX_HP/2, 0, 0, 0, "Water", 0)
        return monster
#slime monster maker function
def slime_spawn():
        monster = Monster_NPC("Mini Acid Hydra", C.MONSTER_MAX_HP, 0, 0, 0, "Water", 0)
        return monster
#slime monster actions
def gs_slime_action(m_npc, h_p, m_p):
        #slime chooses from a random pool of actions
        x = random.randint(0, 3)
        #the slime can regenerate by absorbing gold from the Acid Hydra
        if x == 0:
                for mon in m_p:
                        mon.dropchance -= B.G_S_DC_DOWN
                m_npc.health += m_npc.health
                print (m_npc.name, "absorbs some gold. ")
        #the slime can split into two slimes
        elif x == 1:
                m_npc.health = round(m_npc.health * 0.5)
                mon = copy.copy(m_npc)
                m_p.append(mon)
                print (m_npc.name, "copies itself. ")
        #the slime can explode, hurting the heroes
        elif x == 2:
                for hero in h_p:
                        hero.health -= max((m_npc.health - hero.defense - hero.defbonus -
                                            hero.armor - hero.skill), 0)
                print(m_npc.name, "explodes.")
                m_npc.health = 0
        elif x == 3:
                print(m_npc.name, "bounces and wiggles around. ")
#phase one actions
def ah_phase_one_action(m_npc, h_p, b_p):
        hero = party_func.pick_random_healthy_hero(h_p)
        hero.update_poison(m_npc.skill)
        hero.health -= max((m_npc.atk - hero.defense - hero.defbonus - hero.armor), 1)
        hero.health -= max((hero.get_poison()), 0)

        



#phase one
def ah_phase_one(h_p, b_p, p_npc, ib_pc, s_pc):
        bPhase1 = True
        while bPhase1:
                for mon in b_p:
                        if mon.name == "Acid Hydra" and mon.health <= B.A_H_HEALTH/2:
                                bPhase1 = False
                if len(h_p) == 0:
                        print ("The heroes have been routed and flee back to town.")
                        bPhase1 = False

                else:
                        for hero in h_p:
                                if hero.health > 0 and hero.name != "Golem":
                                        hero.stats()
                                        player_func.player_action(hero, h_p, b_p,
                                                                  ib_pc, s_pc, p_npc)
                                elif hero.health <= 0:
                                        h_p.remove(hero)
                                        
                        player_func.pet_action(p_npc, h_p, b_p)
                        
                        for monster in b_p:
                                if monster.health <= 0 and monster.name != "Acid Hydra":
                                        b_p.remove(monster)
                        for monster in b_p:
                                if monster.name == "Acid Hydra" and monster.health > 0:
                                        ah_phase_one_action(monster, h_p, b_p)
                                elif monster.health > 0:
                                        ah_slime_action(monster, h_p, b_p)
                                elif monster.health <= 0:
                                        b_p.remove(monster)
#phase two actions
def ah_phase_two_action(m_npc, h_p, b_p):

        
#phase two
def ah_phase_two(h_p, b_p, p_npc, ib_pc, s_pc):
        bPhase2 = True
        while bPhase2:
                for mon in b_p:
                        if mon.name == "Acid Hydra" and mon.dropchance <= 0:
                                bPhase2 = False
                        elif mon.name == "Acid Hydra" and mon.health <= 0:
                                bPhase2 = False
                if len(h_p) == 0:
                        print ("The heroes have been routed and flee back to town.")
                        bPhase2 = False

                else:
                        for hero in h_p:
                                if hero.health > 0 and hero.name != "Golem":
                                        hero.stats()
                                        player_func.player_action(hero, h_p, b_p,
                                                                  ib_pc, s_pc, p_npc)
                                elif hero.health <= 0:
                                        h_p.remove(hero)
                        player_func.pet_action(p_npc, h_p, b_p)
                        for monster in b_p:
                                if monster.health <= 0 and monster.name != "Acid Hydra":
                                        b_p.remove(monster)
                        for monster in b_p:
                                if monster.name == "Acid Hydra":
                                        ah_phase_two_action(monster, h_p, b_p)
                                elif monster.health > 0:
                                        ah_slime_action(monster, h_p, b_p)
                                elif monster.health <= 0:
                                        b_p.remove(monster)
#phases will change according to boss hp
#this battle is a dps rush, aiming to kill the slime before it can split too much                                               
def boss_battle(h_p, b_p, p_npc, ib_pc, s_pc):
        #make a copies of the party as usual
        b_p = []
        Acid_Hydra = copy.copy(A_H)
        b_p.append(Acid_Hydra)
        new_h_p = []
        for hero in h_p:
                copy_hero = copy.copy(hero)
                new_h_p.append(copy_hero)
        new_b_p = list(b_p)
        #boolean to loop the battle phase until it finishes
        bBattle = True
        while bBattle:
                #check if the battle continues
                for mon in new_b_p:
                        if mon.name == "Acid Hydra" and mon.health <= 0:
                                print("The Acid Hydra has been defeated. ")
                                bBattle = False
                                ib_pc.coins += mon.dropchance
                                ib_pc.ah_trophy += 1
                if len(new_h_p) == 0:
                        print ("The heroes have been routed and flee back to town.")
                        bBattle = False

                else:
                        for mon in new_b_p:
                                if mon.name == "Acid Hydra" and mon.health >= B.A_H_HEALTH/2:
                                        ah_phase_one(new_h_p, new_b_p, p_npc, ib_pc, s_pc)
                                elif mon.name == "Acid Hydra" and mon.health < B.A_H_HEALTH/2:
                                        ah_phase_two(new_h_p, new_b_p, p_npc, ib_pc, s_pc)

                                

