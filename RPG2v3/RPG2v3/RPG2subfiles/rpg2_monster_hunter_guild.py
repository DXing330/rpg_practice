import copy
import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC, Weapon_PC,
                                   Armor_PC)
import rpg2_party_management_functions as party_func
from rpg2_constants import Constants
from rpg2_constant_quests import Q_Constants
from rpg2_constant_lists import List_Constants
L = List_Constants()
C = Constants()
Q = Q_Constants()

#enchanter with the monster hunter guild
#has access to new kinds of enchantments that cost mana gem
def enchanter(h_w, h_a, qi_npc, ai_npc):
        print ("I only work with unenchanted equipment. ")
        print ("Prices will be", C.ENCHANT_PRICE, "mana gems. ")
        if qi_npc.managem >= C.ENCHANT_PRICE:
                choice = input("ARMOR or WEAPONS? A/W? ")
                if choice.upper() == "A":
                        for amr in h_a:
                                amr.stats()
                        armor = party_func.pick_hero(h_a)
                        if armor.effect == "None":
                                print ("What kind of enchantment do you want? ")
                                if ai_npc.rank > Q.MASTER:
                                        print ("Revive: R")
                                enchnt = input("Ethereal: E")
                                if enchnt.upper() == E:
                                        armor.effect = "Ethereal"
                                        qi_npc.managem -= C.ENCHANT_PRICE
                                elif enchnt.upper() == "R" and ai_npc.rank > Q.MASTER:
                                        armor.effect = "Revive"
                                        qi_npc.managem -= C.ENCHANT_PRICE
                                else:
                                        print ("Leave. ")
                        else:
                                print ("Get out if you're not going to listen. ")
                elif choice.upper() == "W":
                        for wpn in h_w:
                                wpn.stats()
                        weapon = party_func.pick_hero(h_w)
                        if weapon.effect == "None":
                                print ("What kind of enchantment do you want? ")
                                if ai_npc.rank > Q.MASTER:
                                        print ("Death: D")
                                enchnt = input("Explode: E")
                                if enchnt.upper() == E:
                                        weapon.effect = "Explode"
                                        qi_npc.managem -= C.ENCHANT_PRICE
                                elif cnchnt.upper() == D and ai_npc.rank > Q.MASTER:
                                        weapon.effect = "Death"
                                        qi_npc.managem -= C.ENCHANT_PRICE
                                else:
                                        print ("Leave. ")
                        else:
                                print ("Get out if you're not going to listen. ")
                else:
                        print ("Good luck out there. ")
                        
#function that upgrades weapons and armor
def equipment_upgrade(h_w, h_a, q_i, a_i):
        q_i.stats()
        print ("What do you want me to work on? ")
        choice = input("WEAPONS or ARMOR? W/A? ")
        if choice.upper() == "W":
                print ("I can only upgrade certain kinds of enchanments. ")
                print ("Fees for weapons depend on how many upgrades you have. ")
                print ("They go from 10, 40, 90, 160, etc. ")
                print ("Priced in mana gems. ")
                print ("The guild pays me the coin I need so I just need the materials from you. ")
                for wpn in h_w:
                        wpn.stats()
                print ("Which one do you want me to change? ")
                weapon = party_func.pick_hero(h_w)
                weapon.stats()
                #check if something is upgradeable
                upgrd = None
                for upgrade in L.UPGRADE_EFFECT_W:
                        if upgrade in weapon.effect:
                                print ("I think I can work with this. ")
                                upgrd = upgrade
                if upgrd == None:
                        print ("Sorry, I'm scared I'll break that one if I try anything. ")
                elif upgrd != None and q_i.managem >= C.WEAPON_PRICE * (weapon.upgrade ** C.INCREASE_EXPONENT) and weapon.upgrade <= a_i.rank:
                        print ("Whew, it seems to still work. ")
                        print ("Hope nothing goes wrong in battle, haha. ")
                        q_i.managem -= C.WEAPON_PRICE * (weapon.upgrade ** C.INCREASE_EXPONENT)
                        weapon.upgrade += 1
                        equipment_upgrade(h_w, h_a, q_i, a_i)
                else:
                        print ("I'll need some experience before I try that. ")
        elif choice.upper() == "A":
                print ("I can only upgrade certain kinds of enchanments. ")
                print ("Fees for armor depend on how many upgrades you have. ")
                print ("They go from 30, 120, 270, 480, etc. ")
                print ("Priced in mana gems. ")
                print ("The guild pays me the coin I need so I just need the materials from you. ")
                for amr in h_a:
                        amr.stats()
                print ("Which one do you want me to change? ")
                armor = party_func.pick_hero(h_a)
                armor.stats()
                upgrd = None
                for upgrade in L.UPGRADE_EFFECT_A:
                        if upgrade in armor.effect:
                                print ("I think I can work with this. ")
                                upgrd = upgrade
                if upgrd == None:
                        print ("Sorry, I'm scared I'll break that one if I try anything. ")
                elif upgrd != None and q_i.managem >= C.ARMOR_PRICE * (armor.upgrade ** C.INCREASE_EXPONENT) and armor.upgrade <= a_i.rank:
                        q_i.managem -= C.ARMOR_PRICE * (armor.upgrade ** C.INCREASE_EXPONENT)
                        armor.upgrade += 1
                        print ("Whew, it seems to still work. ")
                        print ("Hope nothing goes wrong in battle, haha. ")
                        equipment_upgrade(h_w, h_a, q_i, a_i)
                else:
                        print ("I'll need some experience before I try that. ")
        elif choice.upper() == "L":
                print ("Good luck out there. ")
        else:
             equipment_upgrade(h_w, h_a, q_i, a_i)
             
#function that will buy your equip for a fair price
#could get better with higher ranks
def equipment_buyer(ib_pc, h_w, h_a, qi_npc, a_npc):
        print ("What did you bring in this time? ")
        print ("I'll look at one group at a time. ")
        if a_npc.rank > Q.GOLD:
                print ("I found some thing that you might want to BUY. B")
        print ("If you got nothing for me then LEAVE.")
        choice = input("WEAPONS/ARMOR? W/A? ")
        if choice.upper() == "W":
                for wpn in h_w:
                        wpn.stats()
                print ("Which one do you want to sell? ")
                print ("Or do you want me to take them all? ")
                sell = input("One or All? A/O? ")
                if sell.upper() == "A":
                        price = 0
                        for weapon in h_w:
                                if weapon.user == "None":
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
                                for x in range(0, len(h_w)):
                                        for weapon in h_w:
                                                if weapon.user == "None":
                                                        h_w.remove(weapon)
                                print ("I'll find a use for them. ")
                        else:
                                print ("Well, what else do you have? ")
                                equipment_buyer(ib_pc, h_w, h_a, a_npc) 
                if sell.upper() == "O":
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
                print ("Or do you want me to take them all? ")
                sell = input("One or All? A/O? ")
                if sell.upper() == "A":
                        price = 0
                        for armor in h_a:
                                if armor.user == "None":
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
                                for x in range(0, len(h_a)):
                                        for armor in h_a:
                                                if armor.user == "None":
                                                        h_a.remove(armor)
                                print ("I'll find a use for them. ")
                        else:
                                print ("Well, what else do you have? ")
                                equipment_buyer(ib_pc, h_w, h_a, a_npc) 
                if sell.upper() == "O":
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
        elif choice.upper() == "B" and a_npc.rank > Q.GOLD:
                print ("Here's what I've found. ")
                print ("They're all specialized equipment, but I think you could use some. ")
                print ("O = Weapon_PC(Observer, none, none, 1, none, 1)")
                for wpn in h_w:
                        if wpn.user == "Summoner":
                                print ("S =", 
                                       "Weapon_PC(Staff, none, Summon, 1, none, 1)")
                        if wpn.user == "Cleric":
                                print ("C =",
                                       "Weapon_PC(Staff, none, Heal, 1, none, 1)")
                buy = input("Any of them catch your eyes? I'll sell them to you for", C.ENCHANT_PRICE, "mana gems.")
                if buy.upper() == "O" and qi_npc.managem > C.ENCHANT_PRICE:
                        weapon = Weapon_PC("Observer", "None", "None", 1, "None", 1)
                        copy_weapon = copy.copy(weapon)
                        h_w.append(copy_weapon)
                        qi_npc.managem -= C.ENCHANT_PRICE
                        print ("Pleasure doing business with you. ")
                        equipment_buyer(ib_pc, h_w, h_a, a_npc)
                elif buy.upper() == "S" and qi_npc.managem > C.ENCHANT_PRICE:
                        weapon = Weapon_PC("Summon Staff", "None", "Summon", 1, "None", 1)
                        copy_weapon = copy.copy(weapon)
                        h_w.append(copy_weapon)
                        qi_npc.managem -= C.ENCHANT_PRICE
                        print ("Pleasure doing business with you. ")
                        equipment_buyer(ib_pc, h_w, h_a, a_npc)
                elif buy.upper() == "C" and qi_npc.managem > C.ENCHANT_PRICE:
                        weapon = Weapon_PC("Heal Staff", "None", "Heal", 1, "None", 1)
                        copy_weapon = copy.copy(weapon)
                        h_w.append(copy_weapon)
                        qi_npc.managem -= C.ENCHANT_PRICE
                        print ("Pleasure doing business with you. ")
                        equipment_buyer(ib_pc, h_w, h_a, a_npc)
                else:
                        print ("Well I'm sure someone will want them. ")
        else:
                equipment_buyer(ib_pc, h_w, h_a, a_npc)

#function that gives out quest packages
def give_quest(qi_npc, a_npc):
        print ("Lots of work all around. ")
        print ("For you though, this should be fine. ")
        print ("Take this package and deliver it to the city. ")
        qi_npc.package += 1
#function that rewards completed quests
def reward_quest(qi_npc, a_npc):
        print ("Seems like you finished some work. ")
        #gives mana gems according to rank
        qi_npc.managem += qi_npc.rpackage * a_npc.rank
        qi_npc.rpackage = 0
        a_npc.stats()
        qi_npc.stats()
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
                monster_hunter_guild(h_p, ib_pc, h_w, h_a, qi_npc, a_npc)
        elif a_npc.rank >= 1:
                print ("Welcome back. ")
                if a_npc.fame > a_npc.rank ** C.INCREASE_EXPONENT:
                        print ("You've done a bit of work and we've noticed that. ")
                        print ("Here, take this badge, it might open some doors for you. ")
                        a_npc.rank += 1
                print ("The QUEST board and REWARD station are where they usually are. ")
                print ("If you want to visit the ARMORER he's in the back room. ")
                if a_npc.rank > Q.BRONZE:
                        print ("We have a new Tinkerer now if you want to visit him. ")
                if a_npc.rank > Q.SILVER:
                        print ("We have an Enchanter now if you want to visit him. ")
                check = input("Look for a Quest? Claim Reward? Visit Armorer? Q/A/R?")
                if check.upper() == "Q" and qi_npc.package <= a_npc.rank:
                        give_quest(qi_npc, a_npc)
                elif check.upper() == "R" and qi_npc.rpackage > 0:
                        reward_quest(qi_npc, a_npc)
                elif check.upper() == "A":
                        equipment_buyer(ib_pc, h_w, h_a, qi_npc, a_npc)
                elif check.upper() == "T" and a_npc.rank > Q.BRONZE:
                        equipment_upgrade(h_w, h_a, qi_npc, a_npc)
                elif check.upper() == "E" and a_npc.rank > Q.SILVER:
                        enchanter(h_w, h_a, qi_npc, ai_npc)                        
                else:
                        print ("Good luck out there. ")


