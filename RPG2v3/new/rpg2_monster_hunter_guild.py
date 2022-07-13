import copy
import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC, Weapon_PC,
                                   Armor_PC)
import rpg2_party_management_functions as party_func
from rpg2_constants import Constants
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

#function that gives out quest packages
def give_quest(qi_npc, a_npc):
        print ("Lots of work all around. ")
        print ("For you though, this should be fine. ")
        print ("Take this package and deliver it to the city. ")
        qi_npc.packages += 1
#function that rewards completed quests
def reward_quest(qi_npc, a_npc):
        print ("Seems like you finished some work. ")
        #gives mana gems according to rank
        qi_npc.managem += qi_npc.rpackages * a_npc.rank
        qi_npc.rpackages = 0
#function that controls the monster hunter guild
#a place to obtain and go on quests
#if you increase your rank and fame you get access to more things
#need to input the heroes party and their items and equipment
def monster_hunter_guild(h_p, ib_pc, h_w, h_a, qi_npc, a_npc):
        if a_npc.rank == 0 and ib_pc.dg_trophy == 0:
                print ("Welcome.  Do you have a request for us? ")
                print ("Wait who are you again? I don't recognize you. ")
                print ("Sorry, please leave, we're very busy. ")
        elif a_npc.rank == 0 and ib_pc.dg_trophy > 0:
                print ("Welcome.  Do you have a request for us? ")
                print ("Oh, I see you've beaten a demon general, not an easy feat. ")
                print ("You should join us, we need more people like you. ")
                a_npc.rank += 1
                a_npc.fame += 1
        elif a_npc.rank >= 1:
                print ("Welcome back. What would you like to do? ")
                print ("The QUEST board and REWARD station are where they usually are. ")
                print ("If you want to visit the ARMORER he's in the back room. ")
                check = input("Look for a Quest? Claim Reward? Visit Armorer? Q/A/R?")
                if check.upper() == "Q" and qi_npc.packages <= a_npc.rank:
                        give_quest(qi_npc, a_npc)
                elif check.upper() == "R" and qi_npc.rpackages > 0:
                        reward_quest(qi_npc, a_npc)
                elif check.upper() == "A":
                        equipment_buyer(ib_pc, h_w, h_a, a_npc)
                        
                else:
                        print ("Good luck out there. ")


