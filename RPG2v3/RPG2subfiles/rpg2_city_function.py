import copy
import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC, Weapon_PC,
                                   Armor_PC)
import rpg2_party_management_functions as party_func
import rpg2_level_up_function as lvlup_func
from rpg2_constants import Constants
C = Constants()
#store the starter characters incase the player recruits them
summoner = Player_PC("Summoner", 1, 10, 10, 2, 2, 2, 2)
cleric = Player_PC("Cleric", 1, 10, 10, 3, 3, 2, 3)
mage = Player_PC("Mage", 1, 10, 10, 2, 2, 2, 5)
warrior = Player_PC("Warrior", 1, 15, 15, 5, 3, 2, 0)
ninja = Player_PC("Ninja", 1, 10, 10, 3, 3, 5, 2)
knight = Player_PC("Knight", 1, 20, 20, 3, 4, 2, 0)
tactician = Player_PC("Tactician", 1, 10, 10, 1, 1, 5, 0)


##functions in the town
#inn function
def inn(ib_pc, h_p, h_w, h_a):
        print ("Welcome back, what would you like to do? ")
        print ("We always have space for weary heroes to SLEEP. ")
        print ("Feel free to use our dining area to TALK.")
        print ("Or you can rent a room for more PRIVACY. ")
        print ("If you're done with everything then go OUT and save the world. ")
        check = input("PRIVATE ROOM/SLEEP/TALK? P/S/T")
        if check.upper() == "S":
                for hero in h_p:
                        hero.stats()
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
                print ("Ninja, Knight, Tactician? N/K/T ")
                choice = input("Warrior, Mage, Cleric, or Summoner? C/M/S/W? ")
                if choice.upper() == "C":
                        hero = copy.copy(cleric)
                        party_func.add_to_party(h_p, hero)
                elif choice.upper() == "M":
                        hero = copy.copy(mage)
                        party_func.add_to_party(h_p, hero)
                elif choice.upper() == "S":
                        hero = None
                        for player in h_p:
                                if player.name == "Summoner":
                                        hero = player
                        if hero == None:
                                hero = copy.copy(summoner)
                                party_func.add_to_party(h_p, hero)
                        else:
                                print("Looks like you already have a summoner on your team. ")
                elif choice.upper() == "W":
                        hero = copy.copy(warrior)
                        party_func.add_to_party(h_p, hero)
                elif choice.upper() == "K":
                        hero = copy.copy(knight)
                        party_func.add_to_party(h_p, hero)
                elif choice.upper() == "N":
                        hero = copy.copy(ninja)
                        party_func.add_to_party(h_p, hero)
                elif choice.upper() == "T":
                        hero = None
                        for player in h_p:
                                if player.name == "Tactician":
                                        hero = player
                        if hero == None:
                                hero = copy.copy(tactician)
                                party_func.add_to_party(h_p, hero)
                        else:
                                print("Looks like you already have a tactician on your team. ")
                inn(ib_pc, h_p, h_w, h_a)
        elif check.upper() == "P":
                print("Would you like to adjust your PARTY or your EQUIPMENT? ")
                chck = input("P/E? ")
                if chck.upper() == "P":
                        choice = input("Would you like to reORDER or REMOVE? O/R? ")
                        if choice.upper() == "O":
                                for player in h_p:
                                        player.stats()
                                print ("Which hero do you want to act last? ")
                                try:
                                        x = int(input("The first hero is 1, etc. "))
                                        #make a copy of the hero, then remove them
                                        #then readd them to the party, so that they're last
                                        hero = copy.copy(h_p[(x-1)])
                                        h_p.pop((x-1))
                                        h_p.append(hero)
                                except (ValueError, AttributeError):
                                        print("That's not a good plan. ")
                        if choice.upper() == "R" and len(h_p) > 1:
                                for player in h_p:
                                        player.stats()
                                print ("Who do you want to send away? ")
                                print ("You may never see them again. ")
                                try:
                                        x = int(input("The first hero is 1, etc. "))
                                        hero = h_p[(x - 1)]
                                        if hero.name == "Hero":
                                                print ("Are you sure you want to kick out the Hero? ")
                                                coyce = input("Y/N? ")
                                                if coyce.upper() == "Y":
                                                        h_p.pop((x-1))
                                                else:
                                                        inn(ib_pc, h_p, h_w, h_a)
                                        else:
                                                #remove the hero from the party
                                                h_p.pop((x-1))
                                except (ValueError, AttributeError):
                                        print("That's not a good plan. ")
                elif chck.upper() == "E":
                        print ("Do you want to adjust WEAPONS or ARMOR? ")
                        choice = input("A/W? ")
                        if choice.upper() == "A":
                                for amr in h_a:
                                        amr.stats()
                                try:
                                        print ("Which armor do you want to reassign? ")
                                        x = int(input("The first one is 1, etc. "))
                                        armor = h_a[(x - 1)]
                                        armor.user = "None"
                                        print ("Which hero do you want to give it to? ")
                                        y = int(input("The first one is 1, etc. "))
                                        hero = h_p[(y - 1)]
                                        armr = None
                                        for amr in h_a:
                                                if amr.user == hero.name:
                                                        armr = amr
                                        if armr == None:
                                                armor.user = hero.name
                                        else:
                                                print (hero.name, "already has an armor. ")
                                except (ValueError, AttributeError):
                                        print("That's not a good plan. ")
                        if choice.upper() == "W":
                                for wpn in h_a:
                                        wpn.stats()
                                try:
                                        print ("Which weapon do you want to reassign? ")
                                        x = int(input("The first one is 1, etc. "))
                                        weapon = h_a[(x - 1)]
                                        weapon.user = "None"
                                        print ("Which hero do you want to give it to? ")
                                        y = int(input("The first one is 1, etc. "))
                                        hero = h_p[(y - 1)]
                                        weapn = None
                                        for wpn in h_a:
                                                if wpn.user == hero.name:
                                                        weapn = amr
                                        if weapn == None:
                                                weapon.user = hero.name
                                        else:
                                                print (hero.name, "already has a weapon. ")
                                except (ValueError, AttributeError):
                                        print("That's not a good plan. ")
                inn(ib_pc, h_p, h_w, h_a)
                
        elif check.upper() == "O" or check.upper() == "L":
                print ("Come back soon. ")
        else:
               inn(ib_pc, h_p, h_w, h_a) 

#practice arena function
def practice_arena(p_pc, ib_pc):
        if p_pc == None:
                return
        p_pc.bstats()
        ib_pc.stats()
        print ("Welcome to the practice arena, I'm in charge here.")
        if p_pc.level < C.LEVEL_LIMIT:
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
                        practice_arena(p_pc, ib_pc)
                elif check.upper() == "Y" and ib_pc.coins < C.LEVEL_PRICE * (p_pc.level ** C.INCREASE_EXPONENT):
                        print ("Looks you have a small coin bag. ")
                else:
                        print ("Come back when you're ready. ")
        elif p_pc.level == C.LEVEL_LIMIT:
                print ("You look like a powerful guy. ")
                print ("What would you like to train? ")
                print ("Attack, Defense, Health, Mana or Skill? ")
                check = input("A/D/H/M/S ")
                if check.upper() == "A" and ib_pc.coins >= C.LEVEL_PRICE * (p_pc.atkbonus ** C.INCREASE_EXPONENT):
                        ib_pc.coins -= C.LEVEL_PRICE * (p_pc.atkbonus ** C.INCREASE_EXPONENT)
                        p_pc.atkbonus += 1
                        print("You're a big guy. ")
                        practice_arena(p_pc, ib_pc)
                elif check.upper() == "D" and ib_pc.coins >= C.STAT_PRICE * (p_pc.defbonus ** C.INCREASE_EXPONENT):
                        ib_pc.coins -= C.STAT_PRICE * (p_pc.defbonus ** C.INCREASE_EXPONENT)
                        p_pc.defbonus += 1
                        print("You're a thick guy now. ")
                        practice_arena(p_pc, ib_pc)
                elif check.upper() == "M" and ib_pc.coins >= C.STAT_PRICE * (p_pc.mana ** C.INCREASE_EXPONENT):
                        ib_pc.coins -= C.STAT_PRICE * (p_pc.mana ** C.INCREASE_EXPONENT)
                        p_pc.mana += 1
                        print("You don't look any different. ")
                        practice_arena(p_pc, ib_pc)
                elif check.upper() == "S" and ib_pc.coins >= C.STAT_PRICE * (p_pc.skill ** C.INCREASE_EXPONENT):
                        ib_pc.coins -= C.STAT_PRICE * (p_pc.skill ** C.INCREASE_EXPONENT)
                        p_pc.skill += 1
                        print("You're a skilled guy now. ")
                        practice_arena(p_pc, ib_pc)
                elif check.upper() == "H" and ib_pc.coins >= p_pc.maxhealth ** C.INCREASE_EXPONENT:
                        ib_pc.coins -= p_pc.maxhealth ** C.INCREASE_EXPONENT
                        p_pc.maxhealth += 1
                        print("You're a big guy. ")
                        practice_arena(p_pc, ib_pc)
                elif check.upper() == "L":
                        print ("Come back soon. ")
                else:
                        practice_arena(p_pc, ib_pc)
                        
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
                                ib_pc.heal += quantity
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
def equipment_store(ib_pc, h_w, h_a):
        ib_pc.stats()
        print ("Do you want a New armor or new weapon? ")
        print ("Or do you want to Upgrade something? ")
        print ("If there's nothing you want, then Leave. ")
        check = input("N/U/L")
        if check.upper() == "N":
                print ("Armor or Weapon? ")
                choice = input("A/W")
                if choice.upper() == "A" and ib_pc.coins >= C.ARMOR_PRICE:
                        ib_pc.coins -= C.ARMOR_PRICE
                        new = Armor_PC("Armor", "None", "Block", 1, "None", 1)
                        h_a.append(new)
                        print ("Here you go. ")
                        print ("Treat it well and it'll save your life someday. ")
                        equipment_store(ib_pc, h_w, h_a)
                elif choice.upper() == "W" and ib_pc.coins >= C.WEAPON_PRICE:
                        ib_pc.coins -= C.WEAPON_PRICE
                        new = Weapon_PC("Weapon", "None", "Attack", 1, "None", 1)
                        h_w.append(new)
                        print ("Here you go. ")
                        print ("Take good care of it. ")
                        equipment_store(ib_pc, h_w, h_a)
                else:
                        print ("Don't waste my time, I'm very busy. ")
        elif check.upper() == "U":
                print ("Armor or Weapon? ")
                choice = input("A/W")
                if choice.upper() == "A":
                        for armor in h_a:
                                armor.stats()
                        print ("Which one do you want me to work on? ")
                        amr = party_func.pick_hero(h_a)
                        amr.stats()
                        print ("What do you want me to work on? ")
                        upgrade = input("Effect Strength/Defense? D/S? ")
                        if upgrade.upper() == "D" and ib_pc.coins >= C.ARMOR_PRICE * (amr.defense ** C.INCREASE_EXPONENT):
                                ib_pc.coins -= C.ARMOR_PRICE * (amr.defense ** C.INCREASE_EXPONENT)
                                amr.defense += 1
                                print ("It looks a bit tougher now. ")
                                equipment_store(ib_pc, h_w, h_a)
                        elif upgrade.upper() == "S" and ib_pc.coins >= C.ARMOR_PRICE * (amr.strength ** C.INCREASE_EXPONENT):
                                ib_pc.coins -= C.ARMOR_PRICE * (amr.strength ** C.INCREASE_EXPONENT)
                                amr.strength += 1
                                print ("It looks a bit stronger now. ")
                                equipment_store(ib_pc, h_w, h_a)
                        else:
                                print ("Don't waste my time, I'm very busy. ")
                elif choice.upper() == "W":
                        for wpn in h_w:
                                wpn.stats()
                        print ("Which one do you want me to work on? ")
                        weapon = party_func.pick_hero(h_w)
                        weapon.stats()
                        print ("What do you want me to work on? ")
                        upgrade = input("Effect Strength/ATK? A/S? ")
                        if upgrade.upper() == "A" and ib_pc.coins >= C.WEAPON_PRICE * (weapon.atk ** C.INCREASE_EXPONENT):
                                ib_pc.coins -= C.WEAPON_PRICE * (weapon.atk ** C.INCREASE_EXPONENT)
                                weapon.atk += 1
                                print ("It looks a bit more deadly now. ")
                                equipment_store(ib_pc, h_w, h_a)
                        elif upgrade.upper() == "S" and ib_pc.coins >= C.WEAPON_PRICE * (weapon.strength ** C.INCREASE_EXPONENT):
                                ib_pc.coins -= C.WEAPON_PRICE * (weapon.strength ** C.INCREASE_EXPONENT)
                                weapon.strength += 1
                                print ("It looks a bit stronger now. ")
                                equipment_store(ib_pc, h_w, h_a)
                        else:
                                print ("Don't waste my time, I'm very busy. ")
        elif check.upper() == "L":
                print ("Come back whenever you're struggling. ")
        else:
                equipment_store(ib_pc, h_w, h_a)
                        
#general town ui where the player chooses what to do in town
def city(ib_pc, h_p, h_w, h_a, a_i):
        ib_pc.stats()
        print ("Welcome to our town. Where would you like to go?")
        #inn will be a place to sleep and recover the player's health
        #practice arena will let the players increase stats and get quests
        #stores will let the player buy potions or equipment
        check = input("LEAVE, INN, PRACTICE ARENA, STORES? L/I/P/S")
        if check.upper() == "L":
                print ("Thanks for stopping by.")
        elif check.upper() == "I":
                inn(ib_pc, h_p, h_w, h_a)
        elif check.upper() == "P":
                print ("Who wants more training?")
                pp_pc = party_func.pick_hero(h_p)
                practice_arena(pp_pc, ib_pc)
        elif check.upper() == "S":
                print ("What kind of store are you looking for?")
                store = input("EQUIPMENT, POTION? E/P ")
                if store.upper() == "E":
                        equipment_store(ib_pc, h_w, h_a)
                elif store.upper() == "P":
                        potion_store(ib_pc)
        else:
                city(ib_pc, h_p, h_w, h_a)
