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
#its special thing is resurrecting itself
I_P = Monster_NPC("Cryo Phoenix", B.I_P_HEALTH, B.I_P_ATK,
                           B.I_P_DEF, B.I_P_SKL, "Dark",
                           B.I_P_DC)
b_p = []

#phoenix maker function
#as the phoenix runs out of lives it grows stronger
def rebirth(x, ib_pc):
        monster = Monster_NPC("Cryo Phoenix",
                              round(B.I_P_HEALTH * (C.BUFF ** ib_pc.ip_trophy)),
                              B.I_P_ATK * (1 + B.I_P_L - x),
                              B.I_P_DEF * (1 + B.I_P_L - x),
                              (1 + B.I_P_L - x) ** 2,
                              "Dark",
                              B.I_P_DC)
        return monster
        
#egg maker function
def egg_maker(x, ib_pc):
        hp = round(B.I_P_HEALTH * (1 + B.I_P_L - x) * (C.BUFF ** ib_pc.ip_trophy))
        atk = 0
        defense = round(B.I_P_DEF * (1 + B.I_P_L - x) * (C.BUFF ** ib_pc.ip_trophy))
        skl = 0
        dc = B.I_P_DC
        egg = Monster_NPC("Frozen Egg", hp, atk, defense, skl, "Dark", dc)
        return egg
#function which picks a hero
def pick_random_hero(h_p):
        if len(h_p) > 0:
                x = random.randint(0, (len(h_p) - 1))
                hero = h_p[x]
        else:
                hero = None
        return hero
#egg actions
def egg_action(m_npc, x, b_p, ib_pc):
        print ("The egg seems to shake a little. ")
        m_npc.skill += 1
        if m_npc.skill >= (1 + B.I_P_L - x) + 1:
                b_p.remove(m_npc)
                monster = rebirth(x, ib_pc)
                b_p.append(monster)
                print ("The egg cracks! ")
                print ("The egg shatters and the Cryo Phoenix emerges! ")

#phoenix actions
def ip_battle_action(m_npc, h_p, x, h_a):
        hero = party_func.pick_random_healthy_hero(h_p)
        armor = party_func.check_equipment(hero, h_a)
        new_atk = ee_func.armor_effect(m_npc, hero, armor, h_p, b_p)
        new_m_atk = element_func.check_element_monster_attack(m_npc, new_atk, armor)
        print("The icy storm rages! ")
        m_npc.atk += m_npc.skill
        m_npc.defense += m_npc.skill
        for hero in h_p:
                hero.health -= m_npc.skill
                hero.atkbonus -= min(m_npc.skill, hero.atkbonus)
                hero.defbonus -= min(m_npc.skill, hero.defbonus)
        fhero = pick_random_hero(h_p)
        if fhero == None:
                print (m_npc.name, "releases a victorious cry! ")
        else:
                fhero.poison += 1
                print (m_npc.name, "freezes", fhero.name)
        hero.health -= max(new_m_atk - hero.defense - hero.defbonus, 1)
        print (m_npc.name, "attacks", hero.name)
        
#phase one
def ip_battle(h_p, b_p, new_h_s, ib_pc, s_pc, h_w, h_a):
        lives = B.I_P_L
        bPhase = True
        while bPhase:

                if len(h_p) == 0:
                        print ("The heroes have all been frozen solid...")
                        bPhase = False

                else:
                        for hero in h_p:
                                if hero.health <= 0:
                                        h_p.remove(hero)
                        for hero in h_p:
                                if hero.poison > 0 and hero.name != "Totem":
                                        hero.poison -= 1
                                        print (hero.name, "tries to break out of the ice. ")
                                elif hero.health > 0 and hero.name != "Totem":
                                        hero.stats()
                                        player_func.player_action(hero, h_p, b_p,
                                                                  ib_pc, s_pc, new_h_s,
                                                                  h_w, h_a)
                                elif hero.health <= 0:
                                        h_p.remove(hero)
                                        
                        player_func.pet_action(new_h_s, h_p, b_p)
                        for mon in b_p:
                                if mon.name == "Cryo Phoenix" and mon.health > 0:
                                        ip_battle_action(mon, h_p, lives, h_a)
                                elif mon.name == "Frozen Egg" and mon.health > 0:
                                        egg_action(mon, lives, b_p, ib_pc)
                for mon in b_p:
                        #the phoenix can revive itself
                        if mon.name == "Cryo Phoenix" and mon.health <= 0 and lives > 0:
                                print (mon.name, "breaks into pieces. ")
                                print ("The frozen shards seem to form into an egg. ")
                                lives -= 1
                                b_p.remove(mon)
                                monster = egg_maker(lives, ib_pc)
                                b_p.append(monster)
                        if mon.name == "Frozen Egg" and mon.health <= 0 and lives > 0:
                                print ("You break the frozen egg into pieces! ")
                                print ("However, the egg shells reform. ")
                                lives -= 1
                                b_p.remove(mon)
                                monster = egg_maker(lives, ib_pc)
                                b_p.append(monster)
                        elif mon.health <= 0 and lives <= 0 and mon.name == "Frozen Egg":
                                bPhase = False
                                print ("At last you break the egg into pieces and there's nothing inside...")
                        elif mon.health <= 0 and lives <= 0 and mon.name == "Cryo Phoenix":
                                bPhase = False
                                print ("At last you break the bird into pieces and nothing seems to happen...")
                                
                        

#phases will change according to boss hp                                              
def boss_battle(h_p, b_p, h_s, ib_pc, s_pc, h_w, h_a):
        #make a copies of the party as usual
        b_p = []
        Cryo_Phoenix = copy.copy(I_P)
        Cryo_Phoenix.health = round(Cryo_Phoenix.health * (C.BUFF ** ib_pc.ip_trophy))
        b_p.append(Cryo_Phoenix)
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
        new_b_p = copy.copy(b_p)
        #boolean to loop the battle phase until it finishes
        bBattle = True
        while bBattle:
                #check if the battle continues
                for mon in new_b_p:
                        if mon.name == "Cryo Phoenix" and mon.health <= 0:
                                print ("Is it really dead? ")
                                bBattle = False
                                ib_pc.coins += B.I_P_DC
                                ib_pc.ip_trophy += 1
                                new_b_p.remove(mon)
                                print ("The heroes slowly begin to walk down. ")
                                break
                        elif mon.name == "Frozen Egg" and mon.health <= 0:
                                print ("Is it really dead? ")
                                bBattle = False
                                ib_pc.coins += B.I_P_DC
                                ib_pc.ip_trophy += 1
                                new_b_p.remove(mon)
                                print ("The heroes slowly begin to walk down. ")
                                break
                if len(new_h_p) == 0:
                        print ("The frozen heroes are eventually discovered. ")
                        print ("They manage to be thawed out at the village and recover. ")
                        bBattle = False
                if len(new_b_p) == 0:
                        print ("The heroes make their way down the mountain. ")
                        break
                else:
                        for mon in new_b_p:
                                if mon.name == "Cryo Phoenix" and mon.health > 0:
                                        print ("The air grows colder around you. ")
                                        ip_battle(new_h_p, new_b_p, new_h_s, ib_pc, s_pc, new_h_w, new_h_a)

        if not bBattle:
                #adjust the hp of the heroes after battles
                for hero in h_p:
                        check = None
                        for heero in new_h_p:
                                if hero.name == heero.name:
                                        check = heero
                        if check == None:
                                        hero.health = 0
                                        hero.mana = 0
                        elif check != None:
                                        hero.health = min(check.health, hero.maxhealth)
                                        hero.mana = min(check.mana, hero.maxmana)
