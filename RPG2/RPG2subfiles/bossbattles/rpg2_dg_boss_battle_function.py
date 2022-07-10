import random
import copy
import sys
sys.path.append("/Users/draco/Documents/RPG/RPG2/RPG2subfiles")
from rpg2_classdefinitions import (Player_PC, Monster_NPC, Pet_NPC,
                                   ItemBag_PC, Spell_PC)
import rpg2_monster_function as monster_func
import rpg2_player_action_function as player_func
import rpg2_party_management_functions as party_func
from rpg2_constants import Constants
C = Constants()
from rpg2_boss_constants import BOSS_CONSTANTS
B = BOSS_CONSTANTS()

D_G = Monster_NPC("Demon General", B.DEMON_GENERAL_HEALTH, B.DEMON_GENERAL_ATK,
                            B.DEMON_GENERAL_DEFENSE, B.DEMON_GENERAL_SKILL, "Dark",
                            B.DEMON_GENERAL_DROPCHANCE)

#make a party with the demon general for the player's to fight
boss_party = []
#special boss actions
def dg_phase_one_action(monster, h_p, b_p, ib_pc):
        if monster.health >= (B.DEMON_GENERAL_HEALTH * (C.BUFF ** ib_pc.dg_trophy)) * 0.9:
                print("Pathetic, you can't even scratch me. ")
                print("I don't know why you humans even bother to oppose me. ")
                bPhase1 = True
        elif (B.DEMON_GENERAL_HEALTH * (C.BUFF ** ib_pc.dg_trophy)) * 0.7 <= monster.health <= (B.DEMON_GENERAL_HEALTH * (C.BUFF ** ib_pc.dg_trophy)) * 0.9:
                if len(b_p) > 1:
                        print("Hmph, hurry up and get rid of them my guards! ")
                        for mon in b_p:
                                if mon.name != "Demon General":
                                        mon.atk += monster.skill
                elif len(b_p) == 1:
                        print("Worthless guards, but no matter.  I have more. ")
                        print("GUARDS!!!")
                        for hero in h_p:
                               mon = monster_func.random_scaled_up_monster(hero)
                               print(mon.name, "appears from the shadows.")
                               b_p.append(mon)
        elif (B.DEMON_GENERAL_HEALTH * (C.BUFF ** ib_pc.dg_trophy)) * 0.5 <= monster.health < (B.DEMON_GENERAL_HEALTH * (C.BUFF ** ib_pc.dg_trophy)) * 0.7:
                if len(b_p) > 1:
                        print("GUARDS! If you can't even deal with these pathetic fools, then I don't need you!")
                        for mon in b_p:
                                if mon.name != "Demon General":
                                        mon.atk += monster.skill
                elif len(b_p) == 1:
                        print("Those guards were even more worthless than you. ")
                        print("No matter though, I have plenty more. ")
                        print("GUARDS!!!!!")
                        for hero in h_p:
                               mon = monster_func.random_scaled_monster(hero)
                               print(mon.name, "rushes in from the hallways.")
                               b_p.append(mon)
        elif monster.health < (B.DEMON_GENERAL_HEALTH * (C.BUFF ** ib_pc.dg_trophy)) * 0.5:
                print("WORTHLESS FOOLS! ")
                for mon in b_p:
                        if mon.name != "Demon General":
                                print("The general  rips apart", mon.name)
                                b_p.remove(mon)
                for mon in b_p:
                        if mon.name != "Demon General":
                                print("The general  rips apart", mon.name)
                                b_p.remove(mon)
                                
#function that controls the basic battle_phase
#the boss battle phase will be a little different
#boss battles will have different phases
#this will be phase one
def dg_phase_one(h_p, b_p, p_npc, ib_pc, s_pc):
        bPhase1 = True
        while bPhase1:
                for mon in b_p:
                        if mon.name == "Demon General" and mon.health < (B.DEMON_GENERAL_HEALTH * (C.BUFF ** ib_pc.dg_trophy))/2:
                                print ("Pathetic guards! ")
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
                                if monster.health <= 0 and monster.name != "Demon General":
                                        b_p.remove(monster)
                        for monster in b_p:
                                if monster.name == "Demon General":
                                        dg_phase_one_action(monster, h_p, b_p, ib_pc)
                                elif monster.health > 0:
                                        hero = party_func.pick_random_healthy_hero(h_p)
                                        monster_func.monster_attack(monster, hero)
                                elif monster.health <= 0 and monster.name != "Demon General":
                                        b_p.remove(monster)
                        for hero in h_p:
                                if hero.health <= 0:
                                        h_p.remove(hero)
                                        
                                
#special boss actions
def dg_phase_two_action(m_npc, h_p, b_p, ib_pc):
        if (B.DEMON_GENERAL_HEALTH * (C.BUFF ** ib_pc.dg_trophy)) * 0.4 < m_npc.health <= (B.DEMON_GENERAL_HEALTH * (C.BUFF ** ib_pc.dg_trophy)) * 0.5:
                print("Even a strong bug is still just a bug. ")
                print("Let me show you my power. ")
                if m_npc.atk < B.DEMON_GENERAL_ATK:
                        m_npc.atk += (B.DEMON_GENERAL_ATK - m_npc.atk)
                        print("You think you can weaken me? ")
                m_npc.atk += m_npc.skill
                print("Dark energy swirls around", m_npc.name)
                hero = party_func.pick_random_healthy_hero(h_p)
                hero.health -= m_npc.atk
                print("Evil energy blasts", hero.name)
        elif (B.DEMON_GENERAL_HEALTH * (C.BUFF ** ib_pc.dg_trophy)) * 0.2 < m_npc.health <= (B.DEMON_GENERAL_HEALTH * (C.BUFF ** ib_pc.dg_trophy)) * 0.4:
                print("Persistent insects! ")
                hero = party_func.pick_random_healthy_hero(h_p)
                hero.health -= (m_npc.atk - hero.defense)
                print("Evil energy blasts", hero.name)
                hero = party_func.pick_random_healthy_hero(h_p)
                hero.health -= (m_npc.atk - hero.defense)
                print("Evil energy blasts", hero.name)
        elif 0 < m_npc.health <= (B.DEMON_GENERAL_HEALTH * (C.BUFF ** ib_pc.dg_trophy)) * 0.2:
                if m_npc.health > 1:
                        print("Wretched fools, you've pushed me to my limits! ")
                        print("I'll show you my final attack! ")
                        m_npc.atk += m_npc.health
                        m_npc.health = 1
                for x in range(0, len(h_p)):
                        hero = party_func.pick_random_healthy_hero(h_p)
                        hero.health -= m_npc.atk
                        print(m_npc.name, "attacks with the last of his energy! ")
        elif m_npc.health <= 0:
                print(m_npc.name, "coughs up blood and falls to the ground.")


#this will be phase two
def dg_phase_two(h_p, b_p, p_npc, ib_pc, s_pc):
        bPhase2 = True
        while bPhase2:
                for mon in b_p:
                        if mon.name == "Demon General" and mon.health <= 0:
                                print("You may have beaten me, but my lord will avenge me! ")
                                print("You have no idea of the true terror of the demon army! ")
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
                                if monster.name == "Demon General":
                                        dg_phase_two_action(monster, h_p, b_p, ib_pc)
                                else:
                                        b_p.remove(monster)
#phases will change according to boss hp
def boss_battle(h_p, b_p, p_npc, ib_pc, s_pc):
        #make a copy of the heroes party and the monster's party
        b_p = []
        Demon_General = copy.copy(D_G)
        Demon_General.health = round(Demon_General.health * (C.BUFF ** ib_pc.dg_trophy))
        b_p.append(Demon_General)
        new_h_p = []
        for hero in h_p:
                copy_hero = copy.copy(hero)
                new_h_p.append(copy_hero)
        new_b_p = list(b_p)
        #boolean to loop the battle phase until it finishes
        bBattle = True
        while bBattle:
                #check to see if the battle continues
                for mon in new_b_p:
                        if mon.name == "Demon General" and mon.health <= 0:
                                print ("The Demonic leader has been defeated. ")
                                print ("The people can breathe a sigh of relief...for now. ")
                                bBattle = False
                if len(new_h_p) == 0:
                        print ("The heroes have been routed and flee back to town.")
                        bBattle = False

                else:
                        for mon in new_b_p:
                                if mon.name == "Demon General" and mon.health >= (B.DEMON_GENERAL_HEALTH * (C.BUFF ** ib_pc.dg_trophy))/2:
                                        print("Hmmm visitors, I tire of your kind. ")
                                        print("Guards, get rid of them. ")
                                        monster = monster_func.random_elite_monster()
                                        print(monster.name, "descends from beside the throne. ")
                                        monster2 = monster_func.random_elite_monster()
                                        print(monster2.name, "descends from beside the throne. ")
                                        new_b_p.append(monster)
                                        new_b_p.append(monster2)
                                        dg_phase_one(new_h_p, new_b_p, p_npc, ib_pc, s_pc)
                                elif mon.name == "Demon General" and mon.health < (B.DEMON_GENERAL_HEALTH * (C.BUFF ** ib_pc.dg_trophy))/2:
                                        print("Enough! I'll deal with you myself! ")
                                        dg_phase_two(new_h_p, new_b_p, p_npc, ib_pc, s_pc)
                                        
        if not bBattle and len(new_h_p) > 0:
                print ("The heroes return victorious. ")
                print ("The villagers rain praise and thanks upon them. ")
                ib_pc.coins += B.DEMON_GENERAL_DROPCHANCE
                ib_pc.dg_trophy += 1
