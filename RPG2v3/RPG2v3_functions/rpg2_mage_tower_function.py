import copy
import random
import sys
sys.path.append("./RPG2v3_def")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC, Weapon_PC,
                                   Armor_PC)
import rpg2_party_management_functions as party_func
import rpg2_level_up_function as lvlup_func
from rpg2_constants import Constants
C = Constants()
from rpg2_constant_lists import List_Constants
L = List_Constants()
angel = Pet_NPC("Angel", 1, 2)
new_spell = Spell_PC("new", 1, 1, None, 1)
##functions in the tower
#function that will allow the player to change the element of their equipment
#also will allow for basic effects
def equipment_enchanter(ib_pc, h_w, h_a):
        print ("\n This is the enchanting pools. ")
        print ("What would you like us to work on? ")
        print ("And if you're done then LEAVE. ")
        choice = input("WEAPONS or ARMOR? W/A?  \n")
        if choice.upper() == "W" and ib_pc.coins >= C.ENCHANT_PRICE:
                #list the equipments and then have the player pick one to change
                for wpn in h_w:
                        wpn.stats()
                weapon = party_func.pick_hero(h_w)
                weapon.stats()
                #check which part of the equipment should be changed
                print ("Do you want an ELEMENT or an eFFECT enchantment? ")
                check = input("E/F? ")
                #if the weapon doesn't have an element then they can pick a basic element
                if check.upper() == "E" and weapon.element == "None":
                        ib_pc.coins -= C.ENCHANT_PRICE
                        print ("What element of spell do you want?",
                       "Fire, Water, Earth, Air or Dark?")
                        elmnt = input("F/W/E/A/D? ")
                        if elmnt.upper() == "F":
                                weapon.element = "Fire"
                                equipment_enchanter(ib_pc, h_w, h_a)
                        elif elmnt.upper() == "W":
                                weapon.element = "Water"
                                equipment_enchanter(ib_pc, h_w, h_a)
                        elif elmnt.upper() == "E":
                                weapon.element = "Earth"
                                equipment_enchanter(ib_pc, h_w, h_a)
                        elif elmnt.upper() == "A":
                                weapon.element = "Air"
                                equipment_enchanter(ib_pc, h_w, h_a)
                        elif elmnt.upper() == "D":
                                weapon.element = "Dark"
                                equipment_enchanter(ib_pc, h_w, h_a)
                        else:
                                print ("Don't waste our time. ")
                elif check.upper() == "F":
                        ib_pc.coins -= C.ENCHANT_PRICE
                        print ("what effect do you want? ")
                        print ("Attack, Lifesteal or Poison?")
                        efct = input("P/A/L? ")
                        if efct.upper() == "L":
                                weapon.effect = "Lifesteal"
                                equipment_enchanter(ib_pc, h_w, h_a)
                        elif efct.upper() == "P":
                                weapon.effect = "Poison"
                                equipment_enchanter(ib_pc, h_w, h_a)
                        elif efct.upper() == "A":
                                weapon.effect = "Attack"
                                equipment_enchanter(ib_pc, h_w, h_a)
                        else:
                                print ("Don't waste our time. ")
                else:
                        print ("Don't waste our time. ")
        elif choice.upper() == "A" and ib_pc.coins >= C.ENCHANT_PRICE:
                for amr in h_a:
                        amr.stats()
                armor = party_func.pick_hero(h_a)
                armor.stats()
                print ("Do you want an ELEMENT or an eFFECT enchantment? ")
                check = input("E/F? ")
                if check.upper() == "E" and armor.element == "None":
                        ib_pc.coins -= C.ENCHANT_PRICE
                        print ("What element of spell do you want?",
                       "Fire, Water, Earth, Air or Dark?")
                        elmnt = input("F/W/E/A/D? ")
                        if elmnt.upper() == "F":
                                armor.element = "Fire"
                                equipment_enchanter(ib_pc, h_w, h_a)
                        elif elmnt.upper() == "W":
                                armor.element = "Water"
                                equipment_enchanter(ib_pc, h_w, h_a)
                        elif elmnt.upper() == "E":
                                armor.element = "Earth"
                                equipment_enchanter(ib_pc, h_w, h_a)
                        elif elmnt.upper() == "A":
                                armor.element = "Air"
                                equipment_enchanter(ib_pc, h_w, h_a)
                        elif elmnt.upper() == "D":
                                armor.element = "Dark"
                                equipment_enchanter(ib_pc, h_w, h_a)
                        else:
                                print ("Don't waste our time. ")
                elif check.upper() == "F":
                        ib_pc.coins -= C.ENCHANT_PRICE
                        print ("what effect do you want? ")
                        print ("Block, Thorns or Absorb?")
                        efct = input("B/A/T? ")
                        if efct.upper() == "T":
                                armor.effect = "Thorns"
                                equipment_enchanter(ib_pc, h_w, h_a)
                        elif efct.upper() == "Block":
                                armor.effect = "Block"
                                equipment_enchanter(ib_pc, h_w, h_a)
                        elif efct.upper() == "A":
                                armor.effect = "Absorb"
                                equipment_enchanter(ib_pc, h_w, h_a)
                        else:
                                print ("Don't waste our time. ")
                else:
                        print ("Don't waste our time. ")
                        
#function that will allow the player to increase their spell's stats
def upgrade_spell(ib_pc, h_m):
        ib_pc.stats()
        for spell in h_m:
                spell.stats()
        check = input("TRAIN or LEAVE? T/L ")
        if check.upper() == "T":
                print ("Alright, which spell should I help you practice? ")
                spel = party_func.pick_hero(h_m)
                spel.stats
                print (spel.name, "?", "Alright, what part do you want to improve? ")
                choice = input("Power, Targets, Cost? P/T/C? ")
                if choice.upper() == "T" and spel.targets == 1 and ib_pc.coins >= (C.SPELL_PRICE ** C.INCREASE_EXPONENT):
                        ib_pc.coins -= (C.SPELL_PRICE ** C.INCREASE_EXPONENT)
                        spel.targets += 1
                elif choice.upper() == "P" and ib_pc.coins >= (spel.power ** C.INCREASE_EXPONENT):
                        if spel.element == "Dark":
                                print ("Evil magic, huh?  Well, I don't judge. ")
                                ib_pc.coins -= (spel.power ** C.INCREASE_EXPONENT)
                                spel.power += 1
                        else:
                                ib_pc.coins -= (spel.power ** C.INCREASE_EXPONENT)
                                spel.power += 1
                                spel.cost += 1
                elif choice.upper() == "C" and ib_pc.coins >= (spel.power ** C.INCREASE_EXPONENT) and spel.cost > C.SPELL_COST:
                        ib_pc.coins -= (spel.power ** C.INCREASE_EXPONENT)
                        spel.cost -= 1
                else:
                        print ("Don't waste my time if you're not prepared. ")
                upgrade_spell(ib_pc, h_m)
        if check.upper() == "L":
                print ("Come back when you're prepared. ")

#function that will allow new spells to be added
def learn_magic(ib_pc, h_m):
        for spell in h_m:
                spell.stats()
        ib_pc.stats()
        print ("Welcome to the bookstore. Would you like to purchase one of our spellbooks? \n")
        choice = input("Y/N? ")
        if choice.upper() == "Y" and ib_pc.coins >= C.SPELL_PRICE:
                print ("What element of spell do you want?",
                       "Fire, Water, Earth, Air or Dark? \n")
                elmnt = input("F/W/E/A/D? ")
                if elmnt.upper() == "F":
                        ib_pc.coins -= C.SPELL_PRICE
                        copy_spell = copy.copy(new_spell)
                        copy_spell.element = "Fire"
                        h_m.append(copy_spell)
                elif elmnt.upper() == "W":
                        ib_pc.coins -= C.SPELL_PRICE
                        copy_spell = copy.copy(new_spell)
                        copy_spell.element = "Water"
                        h_m.append(copy_spell)
                elif elmnt.upper() == "E":
                        ib_pc.coins -= C.SPELL_PRICE
                        copy_spell = copy.copy(new_spell)
                        copy_spell.element = "Earth"
                        h_m.append(copy_spell)
                elif elmnt.upper() == "A":
                        ib_pc.coins -= C.SPELL_PRICE
                        copy_spell = copy.copy(new_spell)
                        copy_spell.element = "Air"
                        h_m.append(copy_spell)
                elif elmnt.upper() == "D":
                        ib_pc.coins -= C.SPELL_PRICE
                        copy_spell = copy.copy(new_spell)
                        copy_spell.element = "Dark"
                        h_m.append(copy_spell)
                else:
                        print ("Come back soon. ")
                        
        else:
                print ("Come back soon.")

#function that will let the player change their spell names
def adjust_magic_names(h_m):
        print ("It's a quiet room, perfect place to read and edit your spellbooks. ")
        for spell in h_m:
                spell.stats()
        print ("Which spell do you want to rename? ")
        rename = party_func.pick_hero(h_m)
        new_name = input("What would you like to rename that spell to? ")
        rename.name = new_name


        
#function that will allow the player to learn new spells or edit spell names
def library(ib_pc, h_m):
        print ("Welcome to the library.")
        print ("Would you like to go to the BOOKSTORE?")
        print ("Or perhaps you want some quiet STUDY space?")
        print ("If you're done then please LEAVE quietly.")
        choice = input("B/S/L? ")
        if choice.upper() == "B":
                learn_magic(ib_pc, h_m)
        elif choice.upper() == "L":
                print ("Come back soon. ")
        elif choice.upper() == "S":
                adjust_magic_names(h_m)
        else:
                library(ib_pc, h_m)
#function that will allow the pet to be trained and evolved
def summoning_fields(h_p, p_npc, ib_pc):
        for pet in p_npc:
                pet.stats()
        ib_pc.stats()
        if len(p_npc) == 0:
                print ("Looks like you need to summon a new ally.")
                for hero in h_p:
                        if hero.name == 'Summoner' or hero.name == "Hero":
                                print ("Here you go, take good care of it.")
                                angel = Pet_NPC("Angel", 1, 2)
                                copy_ally = copy.copy(angel)
                                p_npc.append(copy_ally)
                #make sure they don't get more than one angel ally
                while len(p_npc) > 1:
                        p_npc.pop(0)
        else:
                ally = party_func.pick_hero(p_npc)
                angel = None
                for name in L.ANGEL_NAMES:
                        if name in ally.name:
                                angel = name
                if angel == None:
                        print ("I'm not sure how you summoned that thing, but we can't work with it. ")
                elif ally.stage < C.STAGE_LIMIT and angel != None:
                        hero = None
                        for p in h_p:
                                if p.name == "Summoner":
                                        hero = p
                        if hero != None:
                                print ("\n Aww, what a cute little friend you have.")
                                print ("It looks like it can still get a lot stronger.")
                                print ("Do you want us to help you train it? ")
                                print ("It'll cost you", (ally.atk ** ally.stage), "coins. \n")
                                choice = input("Y/N? ")
                                if choice.upper() == "Y" and ib_pc.coins >= ally.atk ** ally.stage:
                                        ib_pc.coins -= ally.atk ** ally.stage
                                        lvlup_func.angel_stage_up(ally)
                                        summoning_fields(h_p, p_npc, ib_pc)
                                        print ("Whew, channelling spiritual power always tires me out.")
                                        print ("Your ally looks much stronger now.")
                                else:
                                        print ("Come back when you're ready.")
                        elif hero == None:
                                print ("You need a summoner's magic to make your ally stronger. ")
                elif ally.stage == C.STAGE_LIMIT and angel != None:
                        hero = None
                        for p in h_p:
                                if p.name == "Summoner":
                                        hero = p
                        if hero != None:
                                print (" \n That's a mighty strong looking ally you have.")
                                print ("Do you want me to try to strengthen it? \n")
                                print ("It'll cost you", ((ally.atk * ally.stage) ** C.INCREASE_EXPONENT), "coins.")
                                choice = input("Y/N? ")
                                if choice.upper() == "Y" and ib_pc.coins >= (ally.atk * ally.stage) ** C.INCREASE_EXPONENT:
                                        ib_pc.coins -= (ally.atk * ally.stage) ** C.INCREASE_EXPONENT
                                        lvlup_func.pet_atk_up(ally)
                                        summoning_fields(h_p, p_npc, ib_pc)
                                else:
                                        print ("Come back when you're ready.")
                        elif hero == None:
                                print ("You need a summoner's magic to make your ally stronger. ")
                        
#UI function where the player chooses what to do
def mage_tower(h_p, p_npc, ib_pc, h_m, h_w, h_a):
        print ("Oh, adventurers. Welcome. What do you need?  \n ")
        print ("Would you like to visit our LIBRARY? \n ")
        print ("Or perhaps you want to hire a TUTOR to help you strengthen your magic? \n ")
        print ("If you have a SUMMONED ALLY we can train it as well. \n ")
        print ("We also have an ENCHANTER if you have some equipment.  \n ")
        print ("If you're done with everything here then the DOOR is right there. \n ")
        choice = input("L/E/S/T?")
        if choice.upper() == "S":
                summoning_fields(h_p, p_npc, ib_pc)
        elif choice.upper() == "L":
                library(ib_pc, h_m)
        elif choice.upper() == "T":
                upgrade_spell(ib_pc, h_m)
        elif choice.upper() == "E":
                equipment_enchanter(ib_pc, h_w, h_a)
        elif choice.upper() == "D":
                print ("Good luck saving the world. ")
        else:
                mage_tower(h_p, p_npc, ib_pc, h_m)
                
