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

D_L = Monster_NPC("Demon Lord", B.DEMON_LORD_HEALTH, B.DEMON_LORD_ATK,
                            B.DEMON_LORD_DEFENSE, B.DEMON_LORD_SKILL, "Dark",
                            B.DEMON_LORD_DROPCHANCE)

#make a party with the demon LORD for the player's to fight
boss_party = []
#special boss actions
def dl_phase_one_action(monster, h_p, b_p, ib_pc):
        monster.defense += monster.skill
        monster.atk += monster.skill
        monster.skill += 1
        if monster.health >= (B.DEMON_LORD_HEALTH * (C.BUFF ** ib_pc.dl_trophy)) * 0.9:
                if len(b_p) > 1:
                        print("*Yawns*")
                        print("Guards, wake me up if anything interesting happens. ")
                if len(b_p) == 1:
                        print("You made quick work of them, I suppose. ")
                        print("You'll have to do better than that though to get my attention. ")
                        for hero in h_p:
                               mon = monster_func.random_elite_monster()
                               print(mon.name, "appears from the shadows.")
                               b_p.append(mon)
        elif (B.DEMON_LORD_HEALTH * (C.BUFF ** ib_pc.dl_trophy)) * 0.7 <= monster.health <= (B.DEMON_LORD_HEALTH * (C.BUFF ** ib_pc.dl_trophy)) * 0.9:
                if len(b_p) > 1:
                        print("Hmmm, so you're not as weak as the rest. ")
                        print("Guards, show them the strength of the demon army! ")
                        for mon in b_p:
                                if mon.name != "Demon Lord":
                                        mon.atk += monster.skill
                                        hero = party_func.pick_random_healthy_hero(h_p)
                                        monster_func.monster_attack(monster, hero)
                elif len(b_p) == 1:
                        print("So you've beaten them. ")
                        print("I'm not quite impressed yet though. ")
                        print("Guards!")
                        for hero in h_p:
                               mon = monster_func.random_elite_monster()
                               print(mon.name, "appears from the shadows.")
                               b_p.append(mon)
        elif (B.DEMON_LORD_HEALTH * (C.BUFF ** ib_pc.dl_trophy)) * 0.5 <= monster.health < (B.DEMON_LORD_HEALTH * (C.BUFF ** ib_pc.dl_trophy)) * 0.7:
                if len(b_p) > 1:
                        print("Fight hard my guards. ")
                        print("Let me see the enemies potential. ")
                        for mon in b_p:
                                if mon.name != "Demon Lord":
                                        mon.atk += monster.skill
                                        hero = party_func.pick_random_healthy_hero(h_p)
                                        monster_func.monster_attack(monster, hero)
                elif len(b_p) == 1:
                        print("So you're stronger than those guards. ")
                        print("If you keep this up I may have to fight myself. ")
                        for hero in h_p:
                               mon = monster_func.random_elite_monster()
                               print(mon.name, "rushes in from the hallways.")
                               b_p.append(mon)
        elif monster.health < (B.DEMON_LORD_HEALTH * (C.BUFF ** ib_pc.dl_trophy)) * 0.5:
                print("I want to enjoy this. ")
                for mon in b_p:
                        if mon.name != "Demon Lord":
                                print("The Lord  rips apart", mon.name)
                                b_p.remove(mon)
                for mon in b_p:
                        if mon.name != "Demon Lord":
                                print("The Lord  rips apart", mon.name)
                                b_p.remove(mon)
                                
#function that controls the basic battle_phase
#the boss battle phase will be a little different
#boss battles will have different phases
#this will be phase one
def dl_phase_one(h_p, b_p, p_npc, ib_pc, s_pc):
        bPhase1 = True
        while bPhase1:
                for mon in b_p:
                        if mon.name == "Demon Lord" and mon.health <= 0:
                                bPhase1 = False
                        elif mon.name == "Demon Lord" and mon.health < (B.DEMON_LORD_HEALTH * (C.BUFF ** ib_pc.dl_trophy))/2:
                                print ("Hmm, my blood. ")
                                bPhase1 = False
                if len(h_p) == 0:
                        print ("Boring. ")
                        print ("Come back after you've trained another ten years. ")
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
                                if monster.health <= 0 and monster.name != "Demon Lord":
                                        b_p.remove(monster)
                        for monster in b_p:
                                if monster.name == "Demon Lord":
                                        dl_phase_one_action(monster, h_p, b_p, ib_pc)
                                elif monster.health > 0:
                                        hero = party_func.pick_random_healthy_hero(h_p)
                                        monster_func.monster_attack(monster, hero)
                                elif monster.health <= 0 and monster.name != "Demon Lord":
                                        b_p.remove(monster)
                        for hero in h_p:
                                if hero.health <= 0:
                                        h_p.remove(hero)
                                        
                                
#special boss actions
def dl_phase_two_action(monster, h_p, b_p, ib_pc):
        m_npc.atk += m_npc.skill
        m_npc.defense += m_npc.skill
        m_npc.skill += len(h_p)
        print("Dark energy swirls around", m_npc.name)
        if (B.DEMON_LORD_HEALTH * (C.BUFF ** ib_pc.dl_trophy)) * 0.4 < m_npc.health <= (B.DEMON_LORD_HEALTH * (C.BUFF ** ib_pc.dl_trophy)) * 0.5:
                print("Come! You've piqued my interest! ")
                print("Now let me be a good host. ")
                if m_npc.atk < B.DEMON_LORD_ATK:
                        m_npc.atk += m_npc.skill
                        m_npc.skill += len(h_p)
                        print("Crafty, aren't you? ")
                hero = party_func.pick_random_healthy_hero(h_p)
                hero.health -= max((m_npc.atk - max(hero.armor, hero.skill)), m_npc.skill)
                print("Evil energy blasts", hero.name)
                hero = party_func.pick_random_healthy_hero(h_p)
                hero.health -= max((m_npc.atk - max(hero.armor, hero.skill)), m_npc.skill)
                print("Evil energy blasts", hero.name)
        elif (B.DEMON_LORD_HEALTH * (C.BUFF ** ib_pc.dl_trophy)) * 0.1 < m_npc.health <= (B.DEMON_LORD_HEALTH * (C.BUFF ** ib_pc.dl_trophy)) * 0.4:
                print("So you can keep up so far? ")
                print("Excellent, let's pick up the pace! ")
                m_npc.health += m_npc.skill
                print(m_npc.name, "regenerates! ")
                for hero in h_p:
                        hero.health -= max((m_npc.atk - max(hero.armor, hero.skill)), m_npc.skill)
                        print("Evil energy blasts", hero.name)
        elif 0 < m_npc.health <= (B.DEMON_LORD_HEALTH * (C.BUFF ** ib_pc.dl_trophy)) * 0.1:
                m_npc.skill += len(h_p)
                if m_npc.health > 1:
                        print("You've done great, now let's see if you can finish it! ")
                        print("I'll show you my final attack! ")
                        m_npc.atk += m_npc.health
                        m_npc.health = 1
                for hero in h_p:
                        hero.health -= max(m_npc.atk, m_npc.skill)
                        print(m_npc.name, "attacks with the last of his energy! ")
        elif m_npc.health <= 0:
                print(m_npc.name, "laughes and coughs up blood.")
#this will be phase two
def dl_phase_two(h_p, b_p, p_npc, ib_pc, s_pc):
        bPhase2 = True
        while bPhase2:
                for mon in b_p:
                        if mon.name == "Demon Lord" and mon.health <= 0:
                                print("You may have beaten me, but there will be another. ")
                                print("A thousand generals will fight for my seat! ")
                                print("I only wish I could live to see it. ")
                                bPhase2 = False
                if len(h_p) == 0:
                        print ("Come back anytime.")
                        print ("I'll be waiting. ")
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
                                if monster.name == "Demon Lord":
                                        dl_phase_two_action(monster, h_p, b_p, ib_pc)
                                elif monster.name != "Demon Lord":
                                        b_p.remove(monster)
#phases will change according to boss hp
def boss_battle(h_p, b_p, p_npc, ib_pc, s_pc):
        #make a copy of the heroes party and the monster's party
        b_p = []
        Demon_Lord = copy.copy(D_L)
        Demon_Lord.health = round(Demon_Lord.health * (C.BUFF ** ib_pc.dl_trophy))
        b_p.append(Demon_Lord)
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
                        if mon.name == "Demon Lord" and mon.health <= 0:
                                print ("The Demonic leader has been defeated. ")
                                print ("The people can breathe a sigh of relief...for now. ")
                                bBattle = False
                if len(new_h_p) == 0:
                        print ("The heroes have been routed and flee back to town.")
                        bBattle = False

                else:
                        for mon in new_b_p:
                                if mon.name == "Demon Lord" and mon.health >= (B.DEMON_LORD_HEALTH * (C.BUFF ** ib_pc.dl_trophy))/2:
                                        print("Ugh, heroes. I'm bored just looking at you. ")
                                        print("Guards, get rid of them. ")
                                        for hero in h_p:
                                                mon = monster_func.random_elite_monster()
                                                new_b_p.append(mon)
                                                print (mon.name, "descends from beside the throne. ")
                                        dl_phase_one(new_h_p, new_b_p, p_npc, ib_pc, s_pc)
                                elif mon.name == "Demon Lord" and mon.health < (B.DEMON_LORD_HEALTH * (C.BUFF ** ib_pc.dl_trophy))/2:
                                        print("Amazing, you're strong enough to make me bleed! ")
                                        dl_phase_two(new_h_p, new_b_p, p_npc, ib_pc, s_pc)
        if not bBattle and len(new_h_p) > 0:
                print ("The heroes return victorious. ")
                print ("The villagers rain praise and thanks upon them. ")
                ib_pc.coins += B.DEMON_LORD_DROPCHANCE
                ib_pc.dl_trophy += 1
