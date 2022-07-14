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
from rpg2_constant_lists import List_Constants
L = List_Constants()
from rpg2_boss_constants import BOSS_CONSTANTS
B = BOSS_CONSTANTS()
a = len(L.BASIC_ARMOR_EFFECT_LIST) - 1
b = len(L.BASIC_WEAPON_EFFECT_LIST) - 1
c = len(L.ELEMENTS_LIST) - 1
d = len(L.INTERMEDIATE_ARMOR_EFFECT_LIST) - 1
e = len(L.INTERMEDIATE_WEAPON_EFFECT_LIST) - 1
f = len(L.FULL_ELEMENTS_LIST) - 1

#function that will generate a random equipment
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


                
