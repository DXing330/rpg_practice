import copy
import random
import sys
sys.path.append("../RPG2v3_def")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
                                   Spell_PC, Monster_NPC, Weapon_PC,
                                   Armor_PC, QuestItems_NPC, Access_NPC)
from rpg2_constants import Constants
import rpg2_party_management_functions as party_func
C = Constants()
from rpg2_constant_lists import List_Constants
L = List_Constants()
a = len(L.BASIC_ARMOR_EFFECT_LIST) - 1
b = len(L.BASIC_WEAPON_EFFECT_LIST) - 1
c = len(L.ELEMENTS_LIST) - 1
d = len(L.INTERMEDIATE_ARMOR_EFFECT_LIST) - 1
e = len(L.INTERMEDIATE_WEAPON_EFFECT_LIST) - 1
f = len(L.FULL_ELEMENTS_LIST) - 1

#function that will generate a random armor
def random_basic_armor():
        armor = Armor_PC("Armor", "None", "None",
                         1, "None", 1)
        x = random.randint(0, a)
        y = random.randint(0, c)
        w = random.randint(1, 2)
        z = random.randint(1, 2)
        effct = L.BASIC_ARMOR_EFFECT_LIST[x]
        elmnt = L.ELEMENTS_LIST[y]
        armor.effect = effct
        armor.element = elmnt
        armor.strength = w
        armor.defense = z
        return armor

#fulle is for the full element list, including light
def random_basic_armor_fulle():
        armor = Armor_PC("Armor", "None", "None",
                         1, "None", 1)
        x = random.randint(0, a)
        y = random.randint(0, f)
        w = random.randint(1, 2)
        z = random.randint(1, 2)
        effct = L.BASIC_ARMOR_EFFECT_LIST[x]
        elmnt = L.FULL_ELEMENTS_LIST[y]
        armor.effect = effct
        armor.element = elmnt
        armor.strength = w
        armor.defense = z
        return armor

def random_intermediate_armor():
        armor = Armor_PC("Armor", "None", "None",
                         1, "None", 1)
        x = random.randint(0, d)
        y = random.randint(0, c)
        w = random.randint(1, 2)
        z = random.randint(1, 2)
        effct = L.INTERMEDIATE_ARMOR_EFFECT_LIST[x]
        elmnt = L.ELEMENTS_LIST[y]
        armor.effect = effct
        armor.element = elmnt
        armor.strength = w
        armor.defense = z
        return armor

def random_intermediate_armor_fulle():
        armor = Armor_PC("Armor", "None", "None",
                         1, "None", 1)
        x = random.randint(0, d)
        y = random.randint(0, f)
        w = random.randint(1, 2)
        z = random.randint(1, 2)
        effct = L.INTERMEDIATE_ARMOR_EFFECT_LIST[x]
        elmnt = L.FULL_ELEMENTS_LIST[y]
        armor.effect = effct
        armor.element = elmnt
        armor.strength = w
        armor.defense = z
        return armor

#function that will generate a random weapon
def random_basic_weapon():
        weapon = Weapon_PC("Weapon", "None", "None",
                           1, "None", 1)
        x = random.randint(0, b)
        y = random.randint(0, c)
        w = random.randint(1, 3)
        z = random.randint(1, 3)
        effct = L.BASIC_WEAPON_EFFECT_LIST[x]
        elmnt = L.ELEMENTS_LIST[y]
        weapon.effect = effct
        weapon.element = elmnt
        weapon.strength = w
        weapon.atk = z
        return weapon

def random_basic_weapon_fulle():
        weapon = Weapon_PC("Weapon", "None", "None",
                           1, "None", 1)
        x = random.randint(0, b)
        y = random.randint(0, f)
        w = random.randint(1, 3)
        z = random.randint(1, 3)
        effct = L.BASIC_WEAPON_EFFECT_LIST[x]
        elmnt = L.FULL_ELEMENTS_LIST[y]
        weapon.effect = effct
        weapon.element = elmnt
        weapon.strength = w
        weapon.atk = z
        return weapon

#function that will generate a random weapon
def random_intermediate_weapon():
        weapon = Weapon_PC("Weapon", "None", "None",
                           1, "None", 1)
        x = random.randint(0, e)
        y = random.randint(0, c)
        w = random.randint(1, 3)
        z = random.randint(1, 3)
        effct = L.INTERMEDIATE_WEAPON_EFFECT_LIST[x]
        elmnt = L.ELEMENTS_LIST[y]
        weapon.effect = effct
        weapon.element = elmnt
        weapon.strength = w
        weapon.atk = z
        return weapon

def random_intermediate_weapon_fulle():
        weapon = Weapon_PC("Weapon", "None", "None",
                           1, "None", 1)
        x = random.randint(0, e)
        y = random.randint(0, f)
        w = random.randint(1, 3)
        z = random.randint(1, 3)
        effct = L.INTERMEDIATE_WEAPON_EFFECT_LIST[x]
        elmnt = L.FULL_ELEMENTS_LIST[y]
        weapon.effect = effct
        weapon.element = elmnt
        weapon.strength = w
        weapon.atk = z
        return weapon

def drop_table(m_npc, ib_pc, h_w, h_a):
        x = random.randint(0, 6)
        y = random.randint(1, max(m_npc.dropchance, 1))
        if x == 0:
                ib_pc.coins += m_npc.dropchance
                print ("The heroes found", m_npc.dropchance, "coins.")
        elif x == 1:
                ib_pc.heal += y
                print ("The heroes found", y, "heal potions. ")
        elif x == 2:
                ib_pc.mana += y
                print ("The heroes found", y, "mana potions. ")
        elif x == 3:
                ib_pc.buff += y
                print ("The heroes found", y, "buff potions. ")
        elif x == 4:
                ib_pc.heal += 1
                print ("The heroes found a heal potion. ")
        elif x == 5:
                ib_pc.mana += 1
                print ("The heroes found a mana potion. ")
        elif x == 6:
                ib_pc.buff += 1
                print ("The heroes found a buff potion. ")


def quest_drop_table(m_npc, ib_pc, h_w, h_a, q_i):
        x = random.randint(0, 29)
        y = random.randint(1, max(m_npc.dropchance, 1))
        if x == 0 or x == 16 or x == 23:
                ib_pc.coins += m_npc.dropchance
                print ("The heroes found", m_npc.dropchance, "coins.")
        elif x == 1 or x == 17 or x == 24:
                ib_pc.heal += y
                print ("The heroes found", y, "heal potions. ")
        elif x == 2 or x == 18 or x == 25:
                ib_pc.mana += y
                print ("The heroes found", y, "mana potions. ")
        elif x == 3 or x == 19 or x == 26:
                ib_pc.buff += y
                print ("The heroes found", y, "buff potions. ")
        elif x == 4 or x == 20 or x == 27:
                ib_pc.heal += 1
                print ("The heroes found a heal potion. ")
        elif x == 5 or x == 21 or x == 28:
                ib_pc.mana += 1
                print ("The heroes found a mana potion. ")
        elif x == 6 or x == 22 or x == 29:
                ib_pc.buff += 1
                print ("The heroes found a buff potion. ")
        elif 7 <= x <= 14:
                ib_pc.coins += C.ENCHANT_PRICE + (m_npc.dropchance * C.ARMOR_PRICE)
                print ("The heroes find an old coin purse. ")
        elif x == 15:
                print ("The heroes find the package. ")
                q_i.rpackage += 1
                
