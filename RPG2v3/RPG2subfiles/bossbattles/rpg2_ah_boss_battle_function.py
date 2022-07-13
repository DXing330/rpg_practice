import random
import copy
import sys
sys.path.append("/Users/draco/Documents/RPG/RPG2/RPG2subfiles")
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
#hydra head monster maker
def hydra_head_spawn():
        monster = Monster_NPC("Hydra Head", C.MONSTER_MAX_HP/2, 1, 1, 1, "Water", 0)
        return monster

#hydra head action
def ah_head_action(m_npc, h_p, b_p):
        #the heads will randomly bite or buff themselves
        x = random.randint(0, 2)
        if x == 0:
                if m_npc.atk > 0:
                        hero = party_func.pick_random_healthy_hero(h_p)
                        hero.health -= max((m_npc.atk - hero.defense - hero.defbonus - hero.armor), 1)
                        hero.update_poison(m_npc.atk)
                        print (m_npc.name, "bites", hero.name)
                else:
                        m_npc.atk += m_npc.skill
                        m_npc.skill += 1
                        print (m_npc.name, "coats its fangs with poison. ")
        elif x == 1:
                m_npc.atk += m_npc.skill
                m_npc.skill += 1
                print (m_npc.name, "coats its fangs with poison. ")
        elif x == 2:
                for hero in h_p:
                        hero.health -= max((round(m_npc.health/2) - hero.defense - hero.skill), 1)
                        m_npc.health = round(m_npc.health/2)
                print (m_npc.name, "bites itself and sprays its acidic blood on the heroes. ")
        
#phase one actions
def ah_phase_one_action(m_npc, h_p, b_p):
        x = random.randint(0, 2)
        if x == 0:                       
                for hero in h_p:
                        if hero.get_poison() > 0:
                                hero.health -= hero.get_poison()
                                hero.atk -= min(hero.get_poison(), hero.atk)
                                print (m_npc.name, "curses the acid to sap the strength of", hero.name)
        elif x == 1:
                for hero in h_p:
                        if hero.get_poison() > 0:
                                hero.health -= hero.get_poison()
                                hero.defense -= hero.get_poison()
                                print (m_npc.name, "curses the acid to corrode the defense of", hero.name)
        elif x == 2:
                for hero in h_p:
                        if hero.get_poison() > 0:
                                hero.health -= hero.get_poison()
                                hero.skill -= hero.get_poison()
                                print (m_npc.name, "curses the acid to blur the vision of", hero.name)
        m_npc.dropchance = m_npc.dropchance * B.A_H_DC_UP
        m_npc.skill += len(b_p)
        if len(b_p) <= len(h_p):
                mon = hydra_head_spawn()
                b_p.append(mon)
                print (m_npc.name, "creates another", mon.name)


#phase one
def ah_phase_one(h_p, b_p, p_npc, ib_pc, s_pc):
        bPhase1 = True
        while bPhase1:
                for mon in b_p:
                        if mon.name == "Acid Hydra" and mon.health <= (B.A_H_HEALTH * (C.BUFF ** ib_pc.ah_trophy))/2:
                                print (mon.name, "seems to be running out of energy. ")
                                print ("Its regeneration seems to be slowing. ")
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
                                        mon = hydra_head_spawn()
                                        b_p.append(mon)
                                        mon = hydra_head_spawn()
                                        b_p.append(mon)
                        for monster in b_p:
                                if monster.name == "Acid Hydra":
                                        ah_phase_one_action(monster, h_p, b_p)
                                elif monster.health > 0:
                                        ah_head_action(monster, h_p, b_p)
                                elif monster.health <= 0:
                                        b_p.remove(monster)
                                        mon = hydra_head_spawn()
                                        b_p.append(mon)
                                        mon = hydra_head_spawn()
                                        b_p.append(mon)
#phase two actions
def ah_phase_two_action(m_npc, h_p, b_p):
        if m_npc.health > 0 and len(b_p) > 1:
                for hero in h_p:
                        if hero.get_poison() > 0:
                                hero.health -= hero.get_poison()
                                hero.atk -= min(hero.get_poison(), hero.atk)
                                hero.defense -= hero.get_poison()
                                hero.skill -= hero.get_poison()
                                print (m_npc.name, "corrupts the acid on", hero.name)
                        elif hero.get_poison() <= 0:
                                hero.update_poison(m_npc.skill)
                                print (m_npc.name, "sprays acid on", hero.name)
                #the hydra also buffs itself
                m_npc.dropchance = m_npc.dropchance * B.A_H_DC_UP
                m_npc.atk += m_npc.skill
                m_npc.defense += m_npc.skill
                m_npc.skill += 1
                bPhase2 = True
        elif m_npc.health > 0 and len(b_p) == 1:
                m_npc.atk += m_npc.skill
                m_npc.defense += m_npc.skill
                m_npc.skill += len(h_p)
                hero = party_func.pick_random_healthy_hero(h_p)
                hero.health -= max((m_npc.atk - hero.defense - hero.defbonus - hero.armor), 1)
                hero.update_poison(m_npc.atk)
                hero.health -= hero.get_poison()
                print (m_npc.name, "bites", hero.name)
                m_npc.health += m_npc.skill + m_npc.atk
                print (m_npc.name, "regenerates. ")
                m_npc.dropchance = m_npc.dropchance * B.A_H_DC_UP
                bPhase2 = True
        elif m_npc.health <= 0 and len(b_p) > 1:
                m_npc.health += max((len(b_p) * C.MONSTER_MAX_HP), ((-2)*m_npc.health))
                m_npc.atk += len(b_p) * m_npc.skill
                while len(b_p) > 1:
                        for mon in b_p:
                                if mon.name != "Acid Hydra":
                                        b_p.remove(mon)
                print (m_npc.name, "eats it's other heads and heals itself. ")
                bPhase2 = True
        elif m_npc.health <= 0 and len(b_p) == 1:
                m_npc.health += m_npc.skill
                m_npc.skill = 0
                if m_npc.health > 0:
                        print (m_npc.name, "manages to hang onto life by a thread. ")
                        bPhase2 = True
                elif m_npc.health <= 0:
                        print (m_npc.name, "finally collapses. ")
                        bPhase2 = False
        return bPhase2

        
#phase two
def ah_phase_two(h_p, b_p, p_npc, ib_pc, s_pc):
        bPhase2 = True
        while bPhase2:
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
                                        #if you cut off a head, two more grow
                                        b_p.remove(monster)
                                        mon = hydra_head_spawn()
                                        b_p.append(mon)
                        for monster in b_p:
                                if monster.name == "Acid Hydra":
                                        bPhase2 = ah_phase_two_action(monster, h_p, b_p)
                                elif monster.health > 0:
                                        ah_head_action(monster, h_p, b_p)
                                elif monster.health <= 0:
                                        b_p.remove(monster)
                                        mon = hydra_head_spawn()
                                        b_p.append(mon)

#phases will change according to boss hp
#this battle is a dps rush, aiming to kill the slime before it can split too much                                               
def boss_battle(h_p, b_p, p_npc, ib_pc, s_pc):
        #make a copies of the party as usual
        b_p = []
        Acid_Hydra = copy.copy(A_H)
        Acid_Hydra.health = round(Acid_Hydra.health * (C.BUFF ** ib_pc.ah_trophy))
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
                if len(new_b_p) == 1:
                        for mon in new_b_p:
                                if mon.name == "Acid Hydra" and mon.health <= 0:
                                        print("The Acid Hydra has been defeated. ")
                                        print("The swamp is safe, relatively speaking. ")
                                        bBattle = False
                                        ib_pc.coins += round(mon.dropchance)
                                        ib_pc.ah_trophy += 1
                if len(new_h_p) == 0:
                        print ("The heroes have been routed and flee back to town.")
                        bBattle = False

                else:
                        for mon in new_b_p:
                                if mon.name == "Acid Hydra" and mon.health >= (B.A_H_HEALTH * (C.BUFF ** ib_pc.ah_trophy))/2:
                                        print ("You spot the massive monster in the swamp! ")
                                        ah_phase_one(new_h_p, new_b_p, p_npc, ib_pc, s_pc)
                                elif mon.name == "Acid Hydra" and mon.health < (B.A_H_HEALTH * (C.BUFF ** ib_pc.ah_trophy))/2:
                                        print ("It seems to be focusing its regeneration on its main head now! ")
                                        ah_phase_two(new_h_p, new_b_p, p_npc, ib_pc, s_pc)

                                

