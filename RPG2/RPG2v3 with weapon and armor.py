import json
import random
import sys
sys.path.append("./RPG2subfiles")
sys.path.append("./RPG2subfiles/bossbattles")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
                                   Spell_PC, Monster_NPC, Weapon_PC,
                                   Armor_PC)
import rpg2_city_function as city_func
import rpg2_party_management_functions as party_func
import rpg2_monster_function as monster_func
import rpg2_battle_phase_function as battle_func
import rpg2_mage_tower_function as magetower_func
import rpg2_save_function as save_func
import rpg2_quest_function as quest_func
from rpg2_constants import Constants
C = Constants()

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

def add_to_party(heroes_party, p_pc):
        #if the party isn't full you can add them
        if len(heroes_party) < C.PARTY_LIMIT:
                heroes_party.append(p_pc)
        else:
                print ("The party is already full.")


##classes that the player can control
#p = Player_PC(name, level, health, maxhealth, atk, defense, skill, mana,
#               atkbonus, defbonus, weapon, armor)
hero = Player_PC("Hero", 1, 15, 15, 5, 4, 5, 5)
#pet
hero_pet = Pet_NPC("Nothing", 1, 0)
heroes_bag = ItemBag_PC(1, 1, 1, 50)

while bChoice:
        print ("Would you like to start a new game?  Or input a save?")
        game = input("NEW GAME, IMPORT SAVE? I/N ")
        if game.upper() == "N":
                add_to_party(heroes_party, hero)
                bChoice = False
                bGame = True

        if game.upper() == "I":
                heroes_list, heroes_magic_list, items_bag_obj, pet_obj, weapons, armor = save_func.read()
                heroes_party = heroes_list
                heroes_magic = heroes_magic_list
                heroes_bag = items_bag_obj
                hero_pet = pet_obj
                heroes_weapons = weapons
                heroes_armor = armor
                bChoice = False
                bGame = True


while bGame:
        monster_party = []
        print("What would you like to do?")
        print("ATTACK nearby monsters?")
        print("LISTEN to the pleas of a nearby village? ")
        print("vist the MAGE TOWER?")
        print("head back to the CITY?")
        print("or perhaps you want to rest and RECORD your adventures?")
        check = input("A/C/L/M/R")
        if check.upper() == "C":
                #if the hero goes to town call the town function
                for hero in heroes_party:
                        print (hero.stats())
                town_func.town(heroes_bag, heroes_party,
                               heroes_weapons, heroes_armor)
        if check.upper() == "A":
                #if you want to fight, then create some monsters to fight
                print("Do you want to fight against the odds? ")
                print("Are you brave enough to face a horde of monsters? ")
                choice = input("Y/N ?")
                #then you fight against a horde of monsters
                if choice.upper() == "Y":
                        x = C.MONSTER_PARTY_LIMIT
                        for y in range(len(heroes_party), x):
                                monster = monster_func.random_scaled_monster(hero)
                                monster_party.append(monster)
                        battle_func.battle_phase(heroes_party, monster_party,
                                                 hero_pet, heroes_bag, heroes_magic,
                                                 heroes_weapons, heroes_armor)
                else:
                        #make the fights equal numbers
                        for hero in heroes_party:
                                monster = monster_func.random_scaled_monster(hero)
                                monster_party.append(monster)
                        battle_func.battle_phase(heroes_party, monster_party,
                                                 hero_pet, heroes_bag, heroes_magic,
                                                 heroes_weapons, heroes_armor)
        if check.upper() == "L":
                print ("Travelers?! You look strong. Please, can you help us? ")
                quest_func.quest(heroes_party, monster_party,
                                 hero_pet, heroes_bag, heroes_magic,
                                 heroes_weapons, heroes_armor)
        if check.upper() == "M":
                magetower_func.mage_tower(heroes_party, hero_pet,
                                          heroes_bag, heroes_magic)
        if check.upper() == "R":
                save_func.write_to_files(heroes_party, heroes_magic,
                                         heroes_bag, hero_pet,
                                         heroes_weapons, heroes_armor,
                                         "RPG2_")
                for hero in heroes_party:
                        hero.stats()
                for spell in heroes_magic:
                        spell.stats()
                for weapon in heroes_weapons:
                        weapons.stats()
                for armor in heroes_armor:
                        armor.stats()
                hero_pet.stats()
                heroes_bag.stats()
                check =  input("Would you like to keep going after you write or STOP?")
                if check.upper() == "S":
                        bGame = False
                        break                        
