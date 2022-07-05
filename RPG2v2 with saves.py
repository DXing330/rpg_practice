import json
import random
import sys
sys.path.append("./RPG2subfiles")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
                                   Spell_PC, Monster_NPC)
import rpg2_town_function as town_func
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

def add_to_party(heroes_party, p_pc):
        #if the party isn't full you can add them
        if len(heroes_party) < C.PARTY_LIMIT:
                heroes_party.append(p_pc)
        else:
                print ("The party is already full.")


##classes that the player can control
#p = Player_PC(name, level, health, maxhealth, atk, defense, skill, mana,
#               atkbonus, defbonus, weapon, armor)
#warrior is someone who focuses more on physical attacks than magical ones
#warrior gets a starting sword and armor so his weapon = 2 and armor = 1
warrior = Player_PC("Warrior", 1, 15, 15, 5, 3, 0, 0, 0, 0, 2, 1)
#mage is someone who focuses more on magical attacks than physical attacks
#the mage has starting mana and gains mana every level
mage = Player_PC("Mage", 1, 10, 10, 2, 2, 0, 5)
#cleric is someone who focuses more on healing magic and buffs
cleric = Player_PC("Cleric", 1, 10, 10, 3, 2, 0, 0)
#summoner is someone who binds themselves to a monster
#the summoner mostly relies on their ally for damage
summoner = Player_PC("Summoner", 1, 10, 10, 2, 2, 0, 0)
#p = Pet_NPC(self, name, stage, atk)
hero_pet = Pet_NPC("Nothing", 1, 0)
angel = Pet_NPC("Angel", 1, 2)
#ib = ItemBag_PC(self, health, mana, buff, coins)
heroes_bag = ItemBag_PC(1, 1, 1, 10)

while bChoice:
        print ("Would you like to start a new game?  Or input a save?")
        game = input("NEW GAME, IMPORT SAVE? I/N ")
        if game.upper() == "N":
                print ("What character would you like to start with?")
                choice = input("Cleric, Mage, Summoner, Warrior? C/M/S/W")
                if choice.upper() == "C":
                        add_to_party(heroes_party, cleric)
                        hero_one = cleric
                        bChoice = False
                        bGame = True
                elif choice.upper() == "M":
                        add_to_party(heroes_party, mage)
                        hero_one = mage
                        fireball = Spell_PC("Fireball", 1, 3, "Fire", 3)
                        heroes_magic.append(fireball)
                        bChoice = False
                        bGame = True
                elif choice.upper() == "S":
                        add_to_party(heroes_party, summoner)
                        hero_one = summoner
                        hero_pet = angel
                        bChoice = False
                        bGame = True
                elif choice.upper() == "W":
                        add_to_party(heroes_party, warrior)
                        hero_one = warrior
                        bChoice = False
                        bGame = True
                else:
                        print ("Please make a choice.")
        if game.upper() == "I":
                heroes_list, heroes_magic_list, items_bag_obj, pet_obj = save_func.read()
                heroes_party = heroes_list
                heroes_magic = heroes_magic_list
                heroes_bag = items_bag_obj
                hero_pet = pet_obj
                hero_one = heroes_party[0]
                bChoice = False
                bGame = True


while bGame:
        monster_party = []
        print("What would you like to do?")
        print("ATTACK nearby monsters?")
        print("EXPLORE the dangerous wilds?")
        print("LISTEN to the pleas of a nearby village? ")
        print("vist the MAGE TOWER?")
        print("head back to the CITY?")
        print("or perhaps you want to rest and RECORD your adventures?")
        check = input("A/C/E/L/M/R")
        if check.upper() == "C":
                #if the hero goes to town call the town function
                for hero in heroes_party:
                        print (hero.stats())
                town_func.town(hero_one, heroes_bag, heroes_party)
        if check.upper() == "A":
                #if you want to fight, then create some monsters to fight
                print("Do you want to fight against the odds? ")
                print("Are you brave enough to face a horde of monsters? ")
                choice = input("Y/N ?")
                #then you fight against a horde of monsters
                if choice.upper() == "Y":
                        x = C.MONSTER_PARTY_LIMIT
                        for y in range(0, x):
                                for hero in heroes_party:
                                        monster = monster_func.random_scaled_monster(hero)
                                        monster_party.append(monster)
                        battle_func.battle_phase(heroes_party, monster_party, hero_pet, heroes_bag, heroes_magic)
                else:
                        #make the fights equal numbers
                        for hero in heroes_party:
                                monster = monster_func.random_scaled_monster(hero)
                                monster_party.append(monster)
                        battle_func.battle_phase(heroes_party, monster_party, hero_pet, heroes_bag, heroes_magic)
        if check.upper() == "E":
                choice = input("Would you like to travel very far away? Y/N? ")
                if choice.upper == "Y":
                        x = random.randint(len(heroes_party), C.MONSTER_PARTY_LIMIT)
                        for y in range(0, x):
                                monster = monster_func.random_elite_monster()
                                monster_party.append(monster)
                        for hero in heroes_party:
                                elite_monster = monster_func.random_scaled_elite_monster(hero)
                                monster_party.append(elite_monster)
                        battle_func.battle_phase(heroes_party, monster_party, hero_pet, heroes_bag, heroes_magic)
                else:
                        for hero in heroes_party:
                                monster = monster_func.random_scaled_up_monster(hero)
                                monster_party.append(monster)
                        battle_func.battle_phase(heroes_party, monster_party, hero_pet, heroes_bag, heroes_magic)
        if check.upper() == "L":
                print ("Travelers?! You look strong. Please, can you help us? ")
                quest_func.quest(heroes_party, monster_party, hero_pet, heroes_bag, heroes_magic)
        if check.upper() == "M":
                magetower_func.mage_tower(heroes_party, hero_pet, heroes_bag, heroes_magic)
        if check.upper() == "R":
                for hero in heroes_party:
                        print (hero.stats())
                for spell in heroes_magic:
                        print (spell.stats())
                hero_pet.stats()
                heroes_bag.stats()
                check =  input("Would you like to keep going after you write or STOP?")
                save_func.write_to_files(heroes_party, heroes_magic, heroes_bag, hero_pet, "RPG2_")
                if check.upper() == "S":
                        bGame = False
                        break                        
