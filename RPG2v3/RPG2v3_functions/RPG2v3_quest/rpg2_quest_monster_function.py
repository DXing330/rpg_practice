import copy
import random
import sys
sys.path.append("../RPG2v3_def")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
                                   Spell_PC, Monster_NPC, Weapon_PC,
                                   Armor_PC, QuestItems_NPC, Access_NPC)
import rpg2_party_management_functions as party_func
from rpg2_constants import Constants
from rpg2_constant_lists import List_Constants
from rpg2_constant_quests import Q_Constants
L = List_Constants()
C = Constants()
Q = Q_Constants()

e = len(L.ELEMENTS_LIST) - 1
b = len(L.MONSTER_BUFF_LIST) - 1
#function that makes goblins
def goblin_maker():
        x = random.randint(0, 1)
        if x == 0:
                mon = Monster_NPC("Goblin", Q.GOBLIN_HP, Q.GOBLIN_ATK,
                                  Q.GOBLIN_DEF, Q.GOBLIN_SKILL, "Earth",
                                  Q.GOBLIN_DC)
        elif x == 1:
                y = random.randint(0, 1)
                if y == 0:
                        mon = Monster_NPC("Goblin", Q.GOBLIN_HP, Q.GOBLIN_ATK,
                                          Q.GOBLIN_DEF, Q.GOBLIN_SKILL, "Earth",
                                          Q.GOBLIN_DC)
                elif y == 1:
                        mon = Monster_NPC("Hob Goblin", Q.HGOBLIN_HP,
                                          Q.HGOBLIN_ATK, Q.HGOBLIN_DEF,
                                          Q.HGOBLIN_SKILL, "Earth", Q.HGOBLIN_DC)
        return mon


def super_goblin_maker():
        x = random.randint(0, 2)
        if x == 0:
                mon = Monster_NPC("Goblin", Q.GOBLIN_HP, Q.GOBLIN_ATK,
                                  Q.GOBLIN_DEF, Q.GOBLIN_SKILL, "Earth",
                                  Q.GOBLIN_DC)
        elif x == 1:
                mon = Monster_NPC("Hob Goblin", Q.HGOBLIN_HP,
                                  Q.HGOBLIN_ATK, Q.HGOBLIN_DEF,
                                  Q.HGOBLIN_SKILL, "Earth", Q.HGOBLIN_DC)
        elif x == 2:
                y = random.randint(0, 2)
                if y == 0:
                        mon = Monster_NPC("Goblin", Q.GOBLIN_HP, Q.GOBLIN_ATK,
                                          Q.GOBLIN_DEF, Q.GOBLIN_SKILL,
                                          "Earth", Q.GOBLIN_DC)
                elif y == 1:
                        mon = Monster_NPC("Hob Goblin", Q.HGOBLIN_HP,
                                          Q.HGOBLIN_ATK, Q.HGOBLIN_DEF,
                                          Q.HGOBLIN_SKILL, "Earth", Q.HGOBLIN_DC)
                elif y == 2:
                        mon = Monster_NPC("Goblin Champion", Q.CGOBLIN_HP,
                                          Q.CGOBLIN_ATK, Q.CGOBLIN_DEF,
                                          Q.CGOBLIN_SKILL, "Earth",
                                          Q.CGOBLIN_DC)
        return mon

#function that makes orcs
def orc_maker():
        elmnt = random.randint(0, e)
        element = L.ELEMENTS_LIST[elmnt]
        mon = Monster_NPC(element + " Orc",
                          Q.ORC_HP, Q.ORC_ATK,
                          Q.ORC_DEF, Q.ORC_SKILL,
                          element, Q.ORC_DC)
        return mon

def orc_chief():
        elmnt = random.randint(0, e)
        element = L.ELEMENTS_LIST[elmnt]
        mon = Monster_NPC(element + " Orc Chief",
                          Q.CORC_HP, Q.CORC_ATK,
                          Q.CORC_DEF, Q.CORC_SKILL,
                          element, Q.CORC_DC)
        return mon

#function that makes giants
def giant_maker():
        elmnt = random.randint(0, e)
        element = L.ELEMENTS_LIST[elmnt]
        mon = Monster_NPC(element + " Giant",
                          Q.GIANT_HP, Q.GIANT_ATK,
                          Q.GIANT_DEF, Q.GIANT_SKILL,
                          element, Q.GIANT_DC)
        return mon

#function that makes wild elementals
def elemental_maker():
        elmnt = random.randint(0, e)
        element = L.ELEMENTS_LIST[elmnt]
        buf = random.randint(0, b)
        buff = L.MONSTER_BUFF_LIST[buf]
        mon = Monster_NPC(element + "Elemental", 
                          C.MONSTER_MAX_HP, C.MONSTER_MAX_ATK,
                          C.MONSTER_MAX_DEF, C.MONSTER_MAX_SKILL,
                          element, C.MONSTER_MAX_DC, 0, buff)
        return mon
