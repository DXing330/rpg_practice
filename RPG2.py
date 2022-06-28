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
herosbag = ItemBag_PC(1, 1, 1, 10)

while bChoice:
        print ("Would you like to start a new game?  Or input a save?")
        game = raw_input("NEW GAME, SAVE? N/S ")
        if game.upper() == "N":
                print ("What character would you like to start with?")
                choice = raw_input("Cleric, Mage, Summoner, Warrior? C/M/S/W")
                if choice.upper() == "C":
                        add_to_party(heroes_party, cleric)
                        hero_one = cleric
                        bChoice = False
                        bGame = True
                elif choice.upper() == "M":
                        add_to_party(heroes_party, mage)
                        hero_one = mage
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
                        print "Please make a choice."
        if game.upper() == "S":
                print "Which character would you like to import? "
                choice = raw_input("Cleric, Mage, Summoner, Warrior? C/M/S/W")
                if choice.upper() == "C":
                        try:
                                print "What are the cleric's stats?"
                                print "(name, level, health, maxhealth, atk, defense, skill, mana, atkbonus, defbonus, weapon, armor) "
                                name = raw_input("NAME?" )
                                level = int(raw_input("LEVEL? "))
                                maxhealth = int(raw_input("MAX HEALTH? "))
                                atk = int(raw_input("ATK? "))
                                defense = int(raw_input("DEF? "))
                                skill = int(raw_input("SKILL? "))
                                mana = int(raw_input("MANA? "))
                                atkbonus = int(raw_input("ATKBONUS? "))
                                defbonus = int(raw_input("DEFBONUS? "))
                                weapon = int(raw_input("WEAPON? "))
                                armor = int(raw_input("ARMOR? "))
                                cleric = Player_PC(name, min(level,C.LEVEL_LIMIT), health, maxhealth, atk, defense,
                                                   skill, mana, atkbonus, defbonus, weapon, armor)
                                add_to_party(heroes_party, cleric)
                                bChoice = False
                                bGame = True
                        except ValueError, AttributeError:
                                print "That's not an option. "
                if choice.upper() == "M":
                        try:
                                print "What are the mages's stats?"
                                print "(name, level, health, maxhealth, atk, defense, skill, mana, atkbonus, defbonus, weapon, armor) "
                                name = raw_input("NAME?" )
                                level = int(raw_input("LEVEL? "))
                                maxhealth = int(raw_input("MAX HEALTH? "))
                                atk = int(raw_input("ATK? "))
                                defense = int(raw_input("DEF? "))
                                skill = int(raw_input("SKILL? "))
                                mana = int(raw_input("MANA? "))
                                atkbonus = int(raw_input("ATKBONUS? "))
                                defbonus = int(raw_input("DEFBONUS? "))
                                weapon = int(raw_input("WEAPON? "))
                                armor = int(raw_input("ARMOR? "))
                                mage = Player_PC(name, min(level,C.LEVEL_LIMIT), health, maxhealth, atk, defense,
                                                   skill, mana, atkbonus, defbonus, weapon, armor)
                                add_to_party(heroes_party, mage)
                                bChoice = False
                                bGame = True
                        except ValueError, AttributeError:
                                print "That's not an option. "
                if choice.upper() == "S":
                        try:
                                print "What are the summoner's stats?"
                                print "(name, level, health, maxhealth, atk, defense, skill, mana, atkbonus, defbonus, weapon, armor) "
                                name = raw_input("NAME?" )
                                level = int(raw_input("LEVEL? "))
                                maxhealth = int(raw_input("MAX HEALTH? "))
                                atk = int(raw_input("ATK? "))
                                defense = int(raw_input("DEF? "))
                                skill = int(raw_input("SKILL? "))
                                mana = int(raw_input("MANA? "))
                                atkbonus = int(raw_input("ATKBONUS? "))
                                defbonus = int(raw_input("DEFBONUS? "))
                                weapon = int(raw_input("WEAPON? "))
                                armor = int(raw_input("ARMOR? "))
                                summoner = Player_PC(name, min(level,C.LEVEL_LIMIT), health, maxhealth, atk, defense,
                                                   skill, mana, atkbonus, defbonus, weapon, armor)
                                add_to_party(heroes_party, summoner)
                                print "What are the summoner's summoned ally's stats? "
                                print "(name, stage, atk)"
                                pet_name = raw_input("NAME? ")
                                stage = raw_input("STAGE? ")
                                pet_atk = raw_input("ATK? ")
                                hero_pet = Pet_NPC(pet_name, min(stage,C.STAGE_LIMIT), pet_atk)
                                bChoice = False
                                bGame = True
                        except ValueError, AttributeError:
                                print "That's not an option. "
                if choice.upper() == "W":
                        try:
                                print "What are the warrior's stats?"
                                print "(name, level, health, maxhealth, atk, defense, skill, mana, atkbonus, defbonus, weapon, armor) "
                                name = raw_input("NAME?" )
                                level = int(raw_input("LEVEL? "))
                                maxhealth = int(raw_input("MAX HEALTH? "))
                                atk = int(raw_input("ATK? "))
                                defense = int(raw_input("DEF? "))
                                skill = int(raw_input("SKILL? "))
                                mana = int(raw_input("MANA? "))
                                atkbonus = int(raw_input("ATKBONUS? "))
                                defbonus = int(raw_input("DEFBONUS? "))
                                weapon = int(raw_input("WEAPON? "))
                                armor = int(raw_input("ARMOR? "))
                                warrior = Player_PC(name, min(level,C.LEVEL_LIMIT), health, maxhealth, atk, defense,
                                                   skill, mana, atkbonus, defbonus, weapon, armor)
                                add_to_party(heroes_party, warrior)
                                bChoice = False
                                bGame = True
                        except ValueError, AttributeError:
                                print "That's not an option. "
                else:
                        print "Please make a choice."


while bGame:
        monster_party = []
        check = raw_input("What do you want to do?"
                           "ATTACK monsters, EXPLORE, go to the MAGE TOWER or find a TOWN?"
                           "A/E/M/T")
        if check.upper() == "T":
                #if the hero goes to town call the town function
                for hero in heroes_party:
                        print hero.stats()
                town_func.town(hero_one, herosbag, heroes_party)
        if check.upper() == "A":
                #if you want to fight, then create some monsters to fight
                #make the fights equal numbers
                for hero in heroes_party:
                        monster = monster_func.random_scaled_monster(hero)
                        monster_party.append(monster)
                battle_func.battle_phase(heroes_party, monster_party, hero_pet, herosbag, heroes_magic)
        if check.upper() == "M":
                magetower_func.mage_tower(heroes_party, hero_pet, herosbag, heroes_magic)
                
