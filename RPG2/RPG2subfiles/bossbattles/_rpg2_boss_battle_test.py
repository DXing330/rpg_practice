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
#it's special thing is resurrecting itself
I_P = Monster_NPC("Cryo Phoenix", B.I_P_HEALTH, B.I_P_ATK,
                           B.I_P_DEF, B.I_P_SKL, "Dark",
                           B.I_P_DC)
b_p = []

#phoenix maker function
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
        hp = round(B.I_P_HEALTH * (x + 1) * (C.BUFF ** ib_pc.ip_trophy))
        atk = 0
        defense = round(B.I_P_DEF * (x + 1) * (C.BUFF ** ib_pc.ip_trophy))
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
        if m_npc.skill >= x + 1:
                b_p.remove(m_npc)
                monster = rebirth(x, ib_pc)
                b_p.append(monster)
                print ("The egg cracks! ")
                print ("The egg shatters and the Cryo Phoenix emerges! ")

#phoenix actions
def ip_battle_action(m_npc, h_p, x):
        print("The icy storm rages! ")
        m_npc.atk += m_npc.skill
        m_npc.defense += m_npc.skill
        for hero in h_p:
                hero.health -= m_npc.skill
                hero.atkbonus -= min(m_npc.skill, hero.atkbonus)
                hero.defbonus -= min(m_npc.skill, hero.defbonus)
                hero.atk -= min(m_npc.skill, hero.atk)
                hero.defense -= min(m_npc.skill, hero.defense)
                hero.skill -= min(m_npc.skill, hero.skill)
        fhero = pick_random_hero(h_p)
        if fhero == None:
                print (m_npc.name, "releases a victorious cry! ")
        else:
                fhero.poison += 1
                print (m_npc.name, "freezes", fhero.name)
        hero = party_func.pick_random_healthy_hero(h_p)
        hero.health -= max(m_npc.atk - hero.defense - hero.defbonus - hero.armor, 1)
        print (m_npc.name, "attacks", hero.name)
        
#phase one
def ip_battle(h_p, b_p, p_npc, ib_pc, s_pc):
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
                                if hero.poison > 0 and hero.name != "Golem":
                                        hero.poison -= 1
                                        print (hero.name, "tries to break out of the ice. ")
                                elif hero.health > 0 and hero.name != "Golem":
                                        hero.stats()
                                        player_func.player_action(hero, h_p, b_p,
                                                                  ib_pc, s_pc, p_npc)
                                elif hero.health <= 0:
                                        h_p.remove(hero)
                                        
                        player_func.pet_action(p_npc, h_p, b_p)
                        for mon in b_p:
                                if mon.name == "Cryo Phoenix" and mon.health > 0:
                                        ip_battle_action(mon, h_p, lives)
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
def boss_battle(h_p, b_p, p_npc, ib_pc, s_pc):
        #make a copies of the party as usual
        b_p = []
        Cryo_Phoenix = copy.copy(I_P)
        Cryo_Phoenix.health = round(Cryo_Phoenix.health * (C.BUFF ** ib_pc.ip_trophy))
        b_p.append(Cryo_Phoenix)
        new_h_p = []
        for hero in h_p:
                copy_hero = copy.copy(hero)
                new_h_p.append(copy_hero)
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
                        print ("The air grows colder around you. ")
                        ip_battle(new_h_p, new_b_p, p_npc, ib_pc, s_pc)



heroes_party = []
heroes_magic = []
heroes_bag = ItemBag_PC(10, 10, 10, 100)
fireball = Spell_PC("Fireball", 3, 2, "Fire", 1)
rainstorm = Spell_PC("Rainstorm", 2, 2, "Water", 1)
earthspike = Spell_PC("Earthspike", 3, 1, "Earth", 1)
mage = Player_PC("Mage", 10, 1000, 1000, 20, 200, 0, 50)
warrior = Player_PC("Warrior", 10, 150, 150, 102250, 30, 20, 0, 20, 20, 2, 1)
cleric = Player_PC("Cleric", 10, 100, 100, 30, 20, 20, 30, 20, 20)
summoner = Player_PC("Summoner", 10, 100, 100, 20, 30, 30, 30, 20, 20)
ninja = Player_PC("Ninja", 10, 100, 100, 30, 30, 50, 0, 20, 20, 3)
knight = Player_PC("Knight", 10, 200, 200, 40, 40, 20, 0, 20, 20, 0, 2)
heroes_pet = Pet_NPC("Angel", 6, 64)
heroes_magic.append(fireball)
heroes_magic.append(rainstorm)
heroes_magic.append(earthspike)
heroes_party.append(cleric)
heroes_party.append(warrior)
heroes_party.append(knight)
heroes_party.append(summoner)
boss_battle(heroes_party, b_p, heroes_pet, heroes_bag, heroes_magic)
boss_battle(heroes_party, b_p, heroes_pet, heroes_bag, heroes_magic)
