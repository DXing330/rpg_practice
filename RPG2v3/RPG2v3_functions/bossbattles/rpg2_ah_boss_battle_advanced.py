import random
import copy
import sys
sys.path.append("../RPG2v3_def")
sys.path.append("../RPG2v3_battle")
from rpg2_classdefinitions import (Player_PC, Monster_NPC, Pet_NPC,
                                   ItemBag_PC, Spell_PC, Weapon_PC,
                                   Armor_PC)
import rpg2_element_function as element_func
import rpg2_equipment_effect_function as ee_func
import rpg2_monster_function as monster_func
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
        monster = Monster_NPC("Hydra Head", C.MONSTER_MAX_HP, 1, 1, 1, "Water", 0)
        return monster

#hydra head action
def ah_head_action(m_npc, h_p, b_p, h_a):
        #the heads will randomly bite or buff themselves
        x = random.randint(0, 2)
        if x == 0:
                if m_npc.atk > 0:
                        hero = party_func.pick_random_healthy_hero(h_p)
                        monster_func.monster_attack(m_npc, hero, h_a, h_p, b_p)
                        hero.poison += m_npc.atk
                        print (m_npc.name, "bites", hero.name)
                else:
                        m_npc.atk += m_npc.skill
                        m_npc.skill += m_npc.skill
                        print (m_npc.name, "coats its fangs with poison. ")
        elif x == 1:
                m_npc.atk += m_npc.skill
                m_npc.skill += m_npc.skill
                print (m_npc.name, "coats its fangs with poison. ")
        elif x == 2:
                for hero in h_p:
                        hero.health -= max(C.MONSTER_MAX_HP/2 - hero.defense - hero.skill, 1)
                m_npc.health -= C.MONSTER_MAX_HP/2
                print (m_npc.name, "bites itself and sprays its acidic blood on the heroes. ")
        
#phase one actions
def ah_phase_one_action(m_npc, h_p, b_p):
        x = random.randint(0, 3)
        if x == 0:                       
                for hero in h_p:
                        if hero.poison > 0:
                                hero.health -= hero.poison
                                hero.atkbonus -= min(hero.poison, hero.atkbonus)
                                print (m_npc.name, "curses the acid to sap the strength of", hero.name)
        elif x == 1:
                for hero in h_p:
                        if hero.poison > 0:
                                hero.health -= hero.poison
                                hero.defbonus -= min(hero.poison, hero.defbonus)
                                print (m_npc.name, "curses the acid to corrode the defense of", hero.name)
        elif x == 2:
                for hero in h_p:
                        if hero.poison > 0:
                                hero.health -= hero.poison
                                hero.skill -= min(hero.poison, hero.skill)
                                print (m_npc.name, "curses the acid to blur the vision of", hero.name)
        elif x == 3:
                for hero in h_p:
                        if hero.poison > 0:
                                hero.health -= hero.poison
                                hero.maxhealth -= hero.poison
                                print (m_npc.name, "curses the acid to sap the life of", hero.name)
        m_npc.dropchance = m_npc.dropchance * B.A_H_DC_UP
        m_npc.skill += len(b_p)
        mon = hydra_head_spawn()
        b_p.append(mon)
        print (m_npc.name, "creates another", mon.name)


#phase one
def ah_phase_one(h_p, b_p, new_h_s, ib_pc, s_pc, h_w, h_a):
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
                                if hero.health > 0 and hero.name != "Totem":
                                        hero.stats()
                                        player_func.player_action(hero, h_p, b_p,
                                                                  ib_pc, s_pc, new_h_s,
                                                                  h_w, h_a)
                                elif hero.health <= 0:
                                        h_p.remove(hero)
                                        
                        player_func.pet_action(new_h_s, h_p, b_p)
                        
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
                                        ah_head_action(monster, h_p, b_p, h_a)
                                elif monster.health <= 0:
                                        b_p.remove(monster)
                                        mon = hydra_head_spawn()
                                        b_p.append(mon)
                                        mon = hydra_head_spawn()
                                        b_p.append(mon)
#phase two actions
def ah_phase_two_action(m_npc, h_p, b_p, h_a):
        #the hydra buffs itself
        m_npc.atk += m_npc.skill
        m_npc.defense += m_npc.skill
        m_npc.dropchance = m_npc.dropchance * B.A_H_DC_UP
        if m_npc.health > 0 and len(b_p) > 1:
                #when the hydra has backup he does aoe effects
                for hero in h_p:
                        if hero.get_poison() > 0:
                                hero.health -= hero.get_poison()
                                hero.atkbonus -= min(hero.poison, hero.atkbonus)
                                hero.defbonus -= min(hero.poison, hero.defbonus)
                                hero.skill -= hero.get_poison()
                                print (m_npc.name, "corrupts the acid on", hero.name)
                        elif hero.get_poison() <= 0:
                                hero.poison += m_npc.skill
                                print (m_npc.name, "sprays acid on", hero.name)
                m_npc.skill += len(b_p)
                bPhase2 = True
        elif m_npc.health > 0 and len(b_p) == 1:
                #when the hydra is alone it begins to attack
                m_npc.skill += len(h_p)
                hero = party_func.pick_random_healthy_hero(h_p)
                armor = party_func.check_equipment(hero, h_a)
                new_atk = ee_func.armor_effect(m_npc, hero, armor, h_p, b_p)
                new_m_atk = element_func.check_element_monster_attack(m_npc, new_atk, armor)
                hero.health -= max((new_m_atk - hero.defense - hero.defbonus), 1)
                hero.poison += m_npc.atk
                hero.health -= hero.poison
                print (m_npc.name, "bites", hero.name)
                m_npc.health += m_npc.skill + m_npc.atk
                print (m_npc.name, "regenerates. ")
                bPhase2 = True
        elif m_npc.health <= 0 and len(b_p) > 1:
                #if the hydra dies the first time it revives
                m_npc.health += max((len(b_p) * C.MONSTER_MAX_HP), ((-2)*m_npc.health))
                m_npc.atk += len(b_p) * m_npc.skill
                while len(b_p) > 1:
                        for mon in b_p:
                                if mon.name != "Acid Hydra":
                                        b_p.remove(mon)
                print (m_npc.name, "eats it's other heads and heals itself. ")
                bPhase2 = True
        elif m_npc.health <= 0 and len(b_p) == 1:
                #if it dies again it tries to save itself
                m_npc.health += m_npc.skill * m_npc.atk
                m_npc.skill = 1
                if m_npc.health > 0:
                        print (m_npc.name, "manages to hang onto life by a thread. ")
                        bPhase2 = True
                elif m_npc.health <= 0:
                        print (m_npc.name, "finally collapses. ")
                        bPhase2 = False
        return bPhase2

        
#phase two
def ah_phase_two(h_p, b_p, new_h_s, ib_pc, s_pc, h_w, h_a):
        bPhase2 = True
        while bPhase2:
                if len(h_p) == 0:
                        print ("The heroes have been routed and flee back to town.")
                        bPhase2 = False

                else:
                        for hero in h_p:
                                if hero.health > 0 and hero.name != "Totem":
                                        hero.stats()
                                        player_func.player_action(hero, h_p, b_p,
                                                                  ib_pc, s_pc, new_h_s,
                                                                  h_w, h_a)
                                elif hero.health <= 0:
                                        h_p.remove(hero)
                        player_func.pet_action(new_h_s, h_p, b_p)
                        for monster in b_p:
                                if monster.health <= 0 and monster.name != "Acid Hydra":
                                        b_p.remove(monster)
                                        mon = hydra_head_spawn()
                                        b_p.append(mon)
                        for monster in b_p:
                                if monster.name == "Acid Hydra":
                                        bPhase2 = ah_phase_two_action(monster, h_p, b_p, h_a)
                                elif monster.health > 0:
                                        ah_head_action(monster, h_p, b_p, h_a)
                                elif monster.health <= 0:
                                        b_p.remove(monster)
                                        mon = hydra_head_spawn()
                                        b_p.append(mon)

#phases will change according to boss hp
#this battle is a dps rush, aiming to kill the slime before it can split too much                                               
def boss_battle(h_p, b_p, h_s, ib_pc, s_pc, h_w, h_a):
        #make a copies of the party as usual
        b_p = []
        Acid_Hydra = copy.copy(A_H)
        Acid_Hydra.health = round(Acid_Hydra.health * (C.BUFF ** ib_pc.ah_trophy))
        b_p.append(Acid_Hydra)
        new_h_p = []
        new_h_s = []
        new_h_w = []
        new_h_a = []
        for hero in h_p:
                copy_hero = copy.copy(hero)
                new_h_p.append(copy_hero)
        for ally in h_s:
                copy_ally = copy.copy(ally)
                new_h_s.append(copy_ally)
        for wpn in h_w:
                copy_weapon = copy.copy(wpn)
                new_h_w.append(copy_weapon)
        for amr in h_a:
                copy_armor = copy.copy(amr)
                new_h_a.append(copy_armor)
        new_b_p = list(b_p)
        #boolean to loop the battle phase until it finishes
        bBattle = True
        while bBattle:
                #check if the battle continues
                if len(new_b_p) == 1:
                        for mon in new_b_p:
                                if mon.name == "Acid Hydra" and mon.health <= 0:
                                        print("The Acid Hydra has been defeated. ")
                                        print ("The heroes watch for awhile to make sure no new heads appear. ")
                                        bBattle = False
                                        ib_pc.coins += round(mon.dropchance)
                                        ib_pc.ah_trophy += 1
                                        new_b_p.remove(mon)
                if len(new_h_p) == 0:
                        print ("The heroes have been routed and flee back to town.")
                        bBattle = False
                elif len(new_b_p) == 0:
                        print("The swamp is safe, relatively speaking. ")
                        
                else:
                        for mon in new_b_p:
                                if mon.name == "Acid Hydra" and mon.health >= (B.A_H_HEALTH * (C.BUFF ** ib_pc.ah_trophy))/2:
                                        print ("You spot the massive monster in the swamp! ")
                                        ah_phase_one(new_h_p, new_b_p, new_h_s, ib_pc,
                                                     s_pc, new_h_w, new_h_a)
                                elif mon.name == "Acid Hydra" and mon.health < (B.A_H_HEALTH * (C.BUFF ** ib_pc.ah_trophy))/2:
                                        print ("It seems to be focusing its regeneration on its main head now! ")
                                        ah_phase_two(new_h_p, new_b_p, new_h_s, ib_pc,
                                                     s_pc, new_h_w, new_h_a)

        if not bBattle:
                #adjust the hp of the heroes after battles
                for hero in h_p:
                        check = None
                        for heero in new_h_p:
                                if hero.name == heero.name:
                                        check = heero
                        #if there is no matching hero then the hero's health goes to zero
                        if check == None:
                                hero.health = 0
                                hero.mana = 0
                        #if there is a matching hero then the hero's health becomes equal
                        elif check != None:
                                hero.health = min(check.health, hero.maxhealth)
                                hero.mana = min(check.mana, hero.maxmana)
