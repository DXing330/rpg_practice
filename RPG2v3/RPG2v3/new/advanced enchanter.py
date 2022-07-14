import copy
import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
                                   Spell_PC, Monster_NPC, Weapon_PC,
                                   Armor_PC, QuestItems_NPC, Access_NPC)
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
