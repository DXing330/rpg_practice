import copy
import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
                                   Spell_PC, Monster_NPC, Weapon_PC,
                                   Armor_PC, QuestItems_NPC, Access_NPC)
from rpg2_constants import Constants
import rpg2_party_management_functions as party_func
C = Constants()

#function that will buy your equip for a fair price
#could get better with higher ranks
def equipment_buyer(ib_pc, h_w, h_a, a_npc):
        print ("What did you bring in this time? ")
        print ("I'll look at one group at a time. ")
        print ("If you got nothing for me then LEAVE.")
        choice = input("WEAPONS/ARMOR? W/A? ")
        if choice.upper() == "W":
                for wpn in h_w:
                        wpn.stats()
                print ("Which one do you want to sell? ")
                weapon = party_func.pick_hero(h_w)
                weapon.stats()
                print ("This one, eh? ")
                #price will depend on the quality of the weapon and your rank
                price = 0
                if weapon.effect != "None":
                        price += C.ENCHANT_PRICE
                if weapon.element != "None":
                        price += C.ENCHANT_PRICE
                price += (weapon.strength ** C.INCREASE_EXPONENT) * C.WEAPON_PRICE
                price += (weapon.atk ** C.INCREASE_EXPONENT) * C.WEAPON_PRICE
                print ("I'll pay", price, "for it. ")
                check = input("YES/NO? Y/N ")
                if check.upper() == "Y":
                        ib_pc.coins += price
                        h_w.remove(weapon)
                        print ("I'll find a use for it. ")
                        equipment_buyer(ib_pc, h_w, h_a, a_npc)
                else:
                        print ("Well, what else do you have? ")
                        equipment_buyer(ib_pc, h_w, h_a, a_npc)
        elif choice.upper() == "A":
                for amr in h_a:
                        amr.stats()
                print ("Which one do you want to sell? ")
                armor = party_func.pick_hero(h_a)
                armor.stats()
                print ("This one, eh? ")
                price = 0
                if armor.effect != "None":
                        price += C.ENCHANT_PRICE
                if armor.element != "None":
                        price += C.ENCHANT_PRICE
                price += (armor.strength ** C.INCREASE_EXPONENT) * C.ARMOR_PRICE
                price += (armor.defense ** C.INCREASE_EXPONENT) * C.ARMOR_PRICE
                print ("I'll pay", price, "for it. ")
                check = input("YES/NO? Y/N ")
                if check.upper() == "Y":
                        ib_pc.coins += price
                        h_a.remove(armor)
                        print ("I'll find a use for it. ")
                        equipment_buyer(ib_pc, h_w, h_a, a_npc)
                else:
                        print ("Well, what else do you have? ")
                        equipment_buyer(ib_pc, h_w, h_a, a_npc)
        elif choice.upper() == "L":
                print ("Good luck out there. ")
        else:
                equipment_buyer(ib_pc, h_w, h_a, a_npc)
