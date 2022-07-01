import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC)
import rpg2_party_management_functions as party_func
import rpg2_level_up_function as lvlup_func
from rpg2_constants import Constants
C = Constants()
summoner = Player_PC("Summoner", 1, 10, 10, 2, 2, 0, 0)
cleric = Player_PC("Cleric", 1, 10, 10, 1, 2, 0, 5)
mage = Player_PC("Mage", 1, 10, 10, 2, 2, 0, 5)
warrior = Player_PC("Warrior", 1, 15, 15, 5, 3, 0, 0, 0, 0, 2, 1)
##functions in the town
#inn function
def inn(p_pc, ib_pc, h_p):
        print ("Welcome back, what would you like to do? ")
        check = input("REST/TALK? R/T")
        if check.upper() == "R":
                for hero in h_p:
                        hero.stats
                        hero.health = hero.maxhealth
                if ib_pc.coins >= len(h_p):
                        ib_pc.coins -= len(h_p)
                        print ("Thank you for your patronage.")
                elif ib_pc.coins < len(h_p):
                        print ("I'll put it on your tab I guess. ")
                        print ("If you save the world then I'll wipe your tab. ")
        elif check.upper() == "T":
                print ("We have a lot of adventurers passing through here.")
                print ("Lots of them are looking for friends.")
                print ("If you want, I can try to help you connect with one.")
                choice = input("Warrior, Mage, Cleric, or Summoner? C/M/S/W? ")
                if choice.upper() == "C":
                        party_func.add_to_party(h_p, cleric)
                elif choice.upper() == "M":
                        party_func.add_to_party(h_p, mage)
                elif choice.upper() == "S":
                        party_func.add_to_party(h_p, summoner)
                elif choice.upper() == "W":
                        party_func.add_to_party(h_p, warrior)
                inn(p_pc, ib_pc, h_p)
        else:
                print ("Come back soon. ")

#practice arena function
def practice_arena(p_pc, ib_pc):
        if p_pc == None:
                return
        print (p_pc.bstats())
        print ("Welcome to the practice arena, I'm in charge here.")
        print ("Tell me, what do you want to work on? GENERAL TRAINING or SPECIFIC TRAINING? ")
        choice = input("G/S? ")
        if choice.upper() == "G" and p_pc.level < C.LEVEL_LIMIT:
                print ("Looks like you have a lot to work on.")
                print ("Let's start with some basic training.")
                print ("It will be extremely painful.")
                print ("Financially speaking.  And physically of course. ")
                print ("Right now it'll cost you", C.LEVEL_PRICE * (p_pc.level ** C.INCREASE_EXPONENT), "coins.")
                check = input("Want to train? Y/N ")
                if check.upper() == "Y" and ib_pc.coins >= C.LEVEL_PRICE * (p_pc.level ** C.INCREASE_EXPONENT):
                        ib_pc.coins -= C.LEVEL_PRICE * (p_pc.level ** 2)
                        lvlup_func.level_up(p_pc)
                        print ("Looks like you're a bit stronger now. ")
                elif check.upper() == "Y" and ib_pc.coins < C.LEVEL_PRICE * (p_pc.level ** C.INCREASE_EXPONENT):
                        print ("Looks you have a small coin bag. ")
                else:
                        print ("Come back when you're ready. ")
        if choice.upper() == "S":
                print ("You look like a powerful guy. ")
                print ("What would you like to train? ")
                print ("Attack, Defense, Mana or Skill? ")
                check = input("A/D/M/S ")
                if check.upper() == "A" and ib_pc.coins >= C.LEVEL_PRICE * (p_pc.atkbonus ** C.INCREASE_EXPONENT):
                        ib_pc.coins -= C.LEVEL_PRICE * (p_pc.atkbonus ** C.INCREASE_EXPONENT)
                        p_pc.atkbonus += 1
                        print("You're a big guy. ")
                        practice_arena(p_pc, ib_pc)
                elif check.upper() == "D" and ib_pc.coins >= C.LEVEL_PRICE * (p_pc.defbonus ** C.INCREASE_EXPONENT):
                        ib_pc.coins -= C.LEVEL_PRICE * (p_pc.defbonus ** C.INCREASE_EXPONENT)
                        p_pc.defbonus += 1
                        print("You're a thick guy now. ")
                        practice_arena(p_pc, ib_pc)
                elif check.upper() == "M" and p_pc.level == C.LEVEL_LIMIT and ib_pc.coins >= C.LEVEL_PRICE * (p_pc.mana ** C.INCREASE_EXPONENT):
                        ib_pc.coins -= C.LEVEL_PRICE * (p_pc.mana ** C.INCREASE_EXPONENT)
                        p_pc.mana += 1
                        print("You don't look any different. ")
                        practice_arena(p_pc, ib_pc)
                elif check.upper() == "S" and ib_pc.coins >= C.LEVEL_PRICE * (p_pc.skill ** C.INCREASE_EXPONENT):
                        ib_pc.coins -= C.LEVEL_PRICE * (p_pc.skill ** C.INCREASE_EXPONENT)
                        p_pc.skill += 1
                        print("You're a skilled guy now. ")
                        practice_arena(p_pc, ib_pc)
                else:
                        print ("Come back soon. ")
                        
#potion store function
def potion_store(ib_pc):
        print ("What kind of potions do you want?")
        #all potions cost one coin
        check = input("Health, Mana, or Boost? H/M/B")
        if check.upper() == "H":
                try:
                        quantity = int(input("How many do you want? "))
                        if ib_pc.coins >= quantity:
                                ib_pc.coins -= quantity
                                ib_pc.health += quantity
                                print ("Thank you for your patronage.")
                        else:
                                print ("You can't afford that.")
                except ValueError:
                        print ("Please don't waste my time.")
        elif check.upper() == "M":
                try:
                        quantity = int(input("How many do you want? "))
                        if ib_pc.coins >= quantity:
                                ib_pc.coins -= quantity
                                ib_pc.mana += quantity
                                print ("Thank you for your patronage.")
                        else:
                                print ("You can't afford that.")
                except ValueError:
                        print ("Please don't waste my time.")
        elif check.upper() == "B":
                try:
                        quantity = int(input("How many do you want? "))
                        if ib_pc.coins >= quantity:
                                ib_pc.coins -= quantity
                                ib_pc.buff += quantity
                                print ("Thank you for your patronage.")
                        else:
                                print ("You can't afford that.")
                except ValueError:
                        print ("Please don't waste my time.")
        else:
                print ("Come back soon.")
#equipment store
def equipment_store(p_pc, ib_pc):
        if p_pc == None:
                return
        print (p_pc.estats())
        print ("Do you want a new armor or new weapon? ")
        check = input("A/W")
        if check.upper() == "A":
                try:
                        quality = int(input("What quality level? "))
                        if ib_pc.coins >= (C.ARMOR_PRICE ** quality):
                                ib_pc.coins -= (C.ARMOR_PRICE ** quality)
                                p_pc.armor = quality
                        else:
                                print ("You can't afford that.")
                except ValueError:
                        print ("Don't waste my time.")
        elif check.upper() == "W":
                try:
                        quality = int(input("What quality level? "))
                        if ib_pc.coins >= (C.WEAPON_PRICE ** quality):
                                ib_pc.coins -= (C.WEAPON_PRICE ** quality)
                                p_pc.weapon = quality
                        else:
                                print ("You can't afford that.")
                except ValueError:
                        print ("Don't waste my time.")
        else:
                print ("Come back soon.")
#general town ui where the player chooses what to do in town
def town(p_pc, ib_pc, h_p):
        ib_pc.stats()
        print ("Welcome to our town. Where would you like to go?")
        #inn will be a place to sleep and recover the player's health
        #practice arena will let the players increase stats and get quests
        #stores will let the player buy potions or equipment
        check = input("LEAVE, INN, PRACTICE ARENA, STORES? L/I/P/S")
        if check.upper() == "L":
                print ("Thanks for stopping by.")
        elif check.upper() == "I":
                inn(p_pc, ib_pc, h_p)
        elif check.upper() == "P":
                print ("Who wants more training?")
                pp_pc = party_func.pick_hero(h_p)
                practice_arena(pp_pc, ib_pc)
        elif check.upper() == "S":
                print ("What kind of store are you looking for?")
                store = input("EQUIPMENT, POTION? E/P ")
                if store.upper() == "E":
                        print ("Who needs to buy some new equipment? ")
                        #e_pc is the hero who will go to the equipment store
                        e_pc = party_func.pick_hero(h_p)
                        equipment_store(e_pc, ib_pc)
                elif store.upper() == "P":
                        potion_store(ib_pc)
        else:
                town(p_pc, ib_pc, h_p)
