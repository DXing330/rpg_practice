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
a = len(C.BASIC_ARMOR_EFFECT_LIST) - 1
b = len(C.BASIC_WEAPON_EFFECT_LIST) - 1
c = len(C.ELEMENTS_LIST) - 1

#function that will generate a random armor
def random_basic_armor():
        armor = Armor_PC("Armor", "None", "None",
                         1, "None", 1)
        x = random.randint(0, a)
        y = random.randint(0, c)
        w = random.randint(1, 2)
        z = random.randint(1, 2)
        effct = C.BASIC_ARMOR_EFFECT_LIST[x]
        elmnt = C.ELEMENTS_LIST[y]
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
        effct = C.BASIC_WEAPON_EFFECT_LIST[x]
        elmnt = C.ELEMENTS_LIST[y]
        weapon.effect = effct
        weapon.element = elmnt
        weapon.strength = w
        weapon.atk = z
        return weapon
