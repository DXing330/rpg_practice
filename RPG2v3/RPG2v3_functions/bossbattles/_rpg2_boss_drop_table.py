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

def dg_drop_table(ib_pc, h_w, h_a):
        x = random.randint(0, ib_pc.dg_trophy)
        if x > B.ADVANCED_SPAWN + (ib_pc.dg_trophy//C.BUFF):
                d_s = Weapon_PC("Demon Sword", "None",
                                   "Command", 1, "Dark", 1)
                copy_weapon = copy.copy(d_s)
                h_w.append(copy_weapon)
                print ("The heroes find the Demon General's sword. ")
        elif x % 3 == 0:
                weapon = random_intermediate_weapon_fulle()
                h_w.append(weapon)
        elif x % 3 == 1:
                armor = random_intermediate_armor_fulle()
                h_a.append(armor)
        elif x % 3 == 2:
                y = random.randint(B.DG_DC/2 , B.DG_DC)
                ib_pc.coins += y
                print ("The heroes find the Demon General's secret treasure trove. ")

def dl_drop_table(ib_pc, h_w, h_a):
        x = random.randint(0, ib_pc.dl_trophy)
        if x > (ib_pc.dl_trophy//C.BUFF):
                d_s = Weapon_PC("Ancient Hero Sword", "None",
                                   "Command", 1, "Light", 1)
                copy_weapon = copy.copy(d_s)
                h_w.append(copy_weapon)
                print ("The heroes find an old hero's sword. ")
        elif x % 3 == 0:
                weapon = random_intermediate_weapon_fulle()
                h_w.append(weapon)
        elif x % 3 == 1:
                armor = random_intermediate_armor_fulle()
                h_a.append(armor)
        elif x % 3 == 2:
                y = random.randint(B.DG_DC/2 , B.DG_DC)
                ib_pc.coins += y
                print ("The heroes find the Demon General's secret treasure trove. ")
                
def gs_drop_table(ib_pc, h_w, h_a):
        x = random.randint(0, ib_pc.gs_trophy)
        if x > (ib_pc.gs_trophy//C.BUFF):
                #make sure they only get one slime staff
                wpn = None
                for weapon in h_w:
                        if "Slime" in weapon.name:
                                wpn = weapon
                if wpn == None:
                        s_s = Weapon_PC("Slime Staff", "None",
                                        "Slime Copy", 1, "None", 1)
                        copy_weapon = copy.copy(s_s)
                        h_w.append(copy_weapon)
                        print ("The heroes find a Slime Staff. ")
                else:
                        print ("There's too much slime to look through. ")
        else:
                s_s = Weapon_PC("Slimey Staff", "None",
                                "None", 1, "None", 1)
                copy_weapon = copy.copy(s_s)
                h_w.append(copy_weapon)
                print ("The heroes find a slimey staff. ")

def ah_drop_table(ib_pc, h_w, h_a):
        x = random.randint(0, ib_pc.ah_trophy)
        if x > (ib_pc.ah_trophy//C.BUFF):
                #make sure they only get one torch
                wpn = None
                for weapon in h_w:
                        if "Hercules" in weapon.name:
                                wpn = weapon
                if wpn == None:
                        h_t = Weapon_PC("Hercules Torch", "None",
                                        "Scorch", 1, "Fire", 1)
                        copy_weapon = copy.copy(h_t)
                        h_w.append(copy_weapon)
                        print ("The heroes find an old hero's weapon. ")
                else:
                        print ("The swamp is too toxic to stay and look for treasure. ")

def sq_drop_table(ib_pc, h_w, h_a):
        x = random.randint(0, ib_pc.sq_trophy)
        if x > (ib_pc.sq_trophy//C.BUFF):
                s_a = Armor_PC("Perfume Amor", "None",
                               "Charm", 1, "Dark", 1)
                copy_armor = copy.copy(s_a)
                h_a.append(copy_armor)
                print ("The heroes find a armor covered in perfume. ")
        else:
                print ("The heroes find a book that they decide is better destroyed. ")

def ip_drop_table(ib_pc, h_w, h_a):
        x = random.randint(0, ib_pc.ip_trophy)
        if x > (ib_pc.ip_trophy//C.BUFF):
                p_a = Armor_PC("Frozen Shell", "None",
                               "Chill", 1, "Dark", 1)
                copy_armor = copy.copy(p_a)
                h_a.append(copy_armor)
                print ("The heroes find a piece of egg that is shaped like armor. ")
        else:
                print ("It's too cold to try to look for treasure. ")


