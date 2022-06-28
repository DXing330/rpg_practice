import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Monster_NPC)
from rpg2_constants import Constants
C = Constants()
#function which creates a monster
def random_monster():
        element_list = list(C.ELEMENTS_LIST)
        name_list = list(C.MONSTER_NAMES_LIST)
        element = element_list[random.randint(0, len(element_list)-1)]
        name = name_list[random.randint(0, len(name_list)-1)]
        health = random.randint(C.MONSTER_MIN_HP, C.MONSTER_MAX_HP)
        atk = random.randint(C.MONSTER_MIN_ATK, C.MONSTER_MAX_ATK)
        defense = random.randint(C.MONSTER_MIN_DEF, C.MONSTER_MAX_DEF)
        skill = random.randint(0, C.MONSTER_MAX_SKILL)
        dropchance = random.randint(0, C.MONSTER_MAX_DROPCHANCE)
        random_monster = Monster_NPC(name, health, atk, defense, skill, element, dropchance)
        return random_monster
#function which creates a monster that scales to the player's level
def random_scaled_monster(p_pc):
        element_list = list(C.ELEMENTS_LIST)
        name_list = list(C.MONSTER_NAMES_LIST)
        element = element_list[random.randint(0, len(element_list)-1)]
        name = name_list[random.randint(0, len(name_list)-1)]
        health = random.randint(C.MONSTER_MIN_HP, C.MONSTER_MIN_HP * p_pc.level)
        atk = random.randint(C.MONSTER_MIN_ATK, C.MONSTER_MIN_ATK * p_pc.level)
        defense = random.randint(C.MONSTER_MIN_DEF, C.MONSTER_MIN_DEF * p_pc.level)
        skill = random.randint(0, C.MONSTER_MAX_SKILL)
        dropchance = random.randint(0, C.MONSTER_MAX_DROPCHANCE)
        random_monster = Monster_NPC(name, health, atk, defense, skill, element, dropchance)
        return random_monster
#function where the monster performs an action
def monster_attack(m_npc, p_pc):
        if p_pc == None:
                print m_npc.name, "roars with confidence."
        else:
                x = random.randint(0, p_pc.level)
                if x >= m_npc.skill:
                        #monster will do a normal attack
                        p_pc.health -= max((m_npc.atk - p_pc.defense - p_pc.defbonus - p_pc.armor), 1)
                        print m_npc.name, "attacks", p_pc.name
                if x < m_npc.skill:
                        #monster will do a special attack
                        y = random.randint(1, 2)
                        if y == 1:
                                #monster does an attack that ignores defense
                                p_pc.health -= m_npc.atk
                                print m_npc.name, "does a piercing attack against", p_pc.name
                        if y == 2:
                                #monster does a strong attack
                                p_pc.health -= max(((m_npc.atk*C.CRIT) - p_pc.defense - p_pc.defbonus - p_pc.armor), 1)
                                print m_npc.name, "does a strong attack against", p_pc.name

