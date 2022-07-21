import json
import random
import sys
sys.path.append("./RPG2v3_functions")
sys.path.append("./RPG2v3_functions/RPG2v3_def")
sys.path.append("./RPG2v3_functions/RPG2v3_battle")
sys.path.append("./RPG2v3_functions/RPG2v3_quest")
sys.path.append("./RPG2v3_functions/bossbattles")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
                                   Spell_PC, Monster_NPC, Weapon_PC,
                                   Armor_PC, QuestItems_NPC, Access_NPC)
import rpg2_city_function as city_func
import rpg2_party_management_functions as party_func
import rpg2_monster_function as monster_func
import rpg2_battle_phase_function as battle_func
import rpg2_mage_tower_function as magetower_func
import rpg2_save_function as save_func
import rpg2_random_boss_function as boss_func
import rpg2_monster_hunter_guild as mh_func
import rpg2_quest_function as quest_func
import rpg2_tavern as tavern_func
from rpg2_constants import Constants
C = Constants()
from rpg2_constant_lists import List_Constants
L = List_Constants()
from rpg2_constant_quests import Q_Constants
Q = Q_Constants()
##game where you will control a party of heroes who fight against monsters
##booleans
#will ask for the player's starting hero and start the game
bChoice = True
#will be the while loop for the game
bGame = False

#start with an empty party
heroes_party = []
#also have an empty spell list
heroes_magic = []
#also have a weapon and armor list
heroes_weapons = []
heroes_armor = []
heroes_allies = []


##classes that the player can control
#p = Player_PC(name, level, health, maxhealth, atk, defense, skill, mana,
#               atkbonus, defbonus, weapon, armor)
hero = Player_PC("Hero", 1, 15, 15, 5, 4, 2, 2, 2)
hero_sword = Weapon_PC("LS", "Hero", "Attack", 1, "Light", 1)
hero_armor = Armor_PC("LA", "Hero", "Block", 1, "Light", 1)
#pet
heroes_bag = ItemBag_PC(1, 1, 1, 50)
q_items = QuestItems_NPC()
a_items = Access_NPC()

while bChoice:
        print ("Would you like to start a new game?  Or input a save? \n ")
        game = input("NEW GAME, IMPORT SAVE? I/N \n")
        if game.upper() == "N":
                print ("A fresh start.  \n ")
                party_func.add_to_party(heroes_party, hero)
                heroes_weapons.append(hero_sword)
                heroes_armor.append(hero_armor)
                bChoice = False
                bGame = True

        elif game.upper() == "I":
                try:
                        heroes_list, heroes_magic_list, items_bag_obj, allies, weapons, armor, quest, access = save_func.read()
                        heroes_party = heroes_list
                        heroes_magic = heroes_magic_list
                        heroes_bag = items_bag_obj
                        heroes_bag.stats()
                        heroes_allies = allies
                        heroes_weapons = weapons
                        heroes_armor = armor
                        q_items = quest
                        a_items = access
                        bChoice = False
                        bGame = True
                except:
                        print ("Looks like we don't have any records for you.  \n ")
                        print ("Don't worry, we can start now.  \n ")
                        party_func.add_to_party(heroes_party, hero)
                        heroes_weapons.append(hero_sword)
                        heroes_armor.append(hero_armor)
                        bChoice = False
                        bGame = True


while bGame:
        monster_party = []
        print("What would you like to do? \n ")
        print("ATTACK nearby monsters? \n ")
        print("LISTEN to the pleas of a nearby village?  \n ")
        print("vist the MAGE TOWER? \n ")
        print("go to the HUNTER GUILD? \n ")
        print("enter the TAVERN?  \n ")
        print("WORK on your assignment \n ")
        print("head back to the CITY? \n ")
        print("or perhaps you want to rest and RECORD your adventures? \n ")
        check = input("A/C/H/L/M/R/T/W \n")
        if check.upper() == "C":
                #if the hero goes to town call the town function
                city_func.city(heroes_bag, heroes_party,
                               heroes_weapons, heroes_armor,
                               a_items)
        elif check.upper() == "A":
                #make the fights equal numbers
                for hero in heroes_party:
                        monster = monster_func.random_scaled_monster(hero)
                        monster_party.append(monster)
                battle_func.battle_phase(heroes_party, monster_party,
                                         heroes_allies, heroes_bag, heroes_magic,
                                         heroes_weapons, heroes_armor)
        elif check.upper() == "L":
                print ("Travelers?! You look strong. Please, can you help us?  \n")
                boss_func.random_boss(heroes_party, monster_party,
                                      heroes_allies, heroes_bag, heroes_magic,
                                      heroes_weapons, heroes_armor)
        elif check.upper() == "M":
                magetower_func.mage_tower(heroes_party, heroes_allies,
                                          heroes_bag, heroes_magic,
                                          heroes_weapons, heroes_armor)
        elif check.upper() == "H":
                mh_func.monster_hunter_guild(heroes_party, heroes_bag,
                                             heroes_allies, heroes_weapons, 
                                             heroes_armor, q_items, a_items)
        elif check.upper() == "W":
                quest_func.quest(heroes_party, heroes_bag, heroes_magic,
                                 heroes_allies, heroes_weapons, heroes_armor,
                                 q_items, a_items)
        elif check.upper() == "R":
                save_func.write_to_files(heroes_party, heroes_magic,
                                         heroes_bag, heroes_allies,
                                         heroes_weapons, heroes_armor,
                                         q_items, a_items, 
                                         "RPG2_ \n ")
                for hero in heroes_party:
                        hero.stats()
                for spell in heroes_magic:
                        spell.stats()
                for weapon in heroes_weapons:
                        weapon.stats()
                for armor in heroes_armor:
                        armor.stats()
                for ally in heroes_allies:
                        ally.stats()
                heroes_bag.stats()
                q_items.stats()
                a_items.stats()
                check =  input("Would you like to keep going after you write or STOP? \n")
                if check.upper() == "S":
                        bGame = False
                        break
        elif check.upper() == "T":
                tavern_func.tavern(heroes_party, heroes_bag, heroes_magic,
                                   heroes_allies, heroes_weapons, heroes_armor,
                                   q_items, a_items)
