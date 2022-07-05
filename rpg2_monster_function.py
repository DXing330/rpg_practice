import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Monster_NPC)
from rpg2_constants import Constants
C = Constants()

#function which creates a strong scaled monster
def random_scaled_elite_monster(p_pc):
        element_list = list(C.ELEMENTS_LIST)
        name_list = list(C.MONSTER_NAMES_LIST)
        element = element_list[random.randint(0, len(element_list)-1)]
        name = name_list[random.randint(0, len(name_list)-1)]
        health = random.randint(C.MONSTER_MAX_HP, C.MONSTER_MAX_HP * (p_pc.atk+p_pc.mana))
        atk = random.randint(C.MONSTER_MAX_ATK, C.MONSTER_MAX_ATK + (p_pc.bonusatk + p_pc.bonusdef + p_pc.mana + p_pc.skill))
        defense = random.randint(C.MONSTER_MAX_DEF, C.MONSTER_MAX_DEF + (p_pc.defense + p_pc.bonusatk + p_pc.bonusdef))
        skill = random.randint(C.MONSTER_MAX_SKILL, C.MONSTER_MAX_SKILL + p_pc.skill)
        dropchance = C.MONSTER_MAX_DROPCHANCE * C.LEVEL_LIMIT
        random_monster = Monster_NPC("Super Elite " + element + " " + name, health, atk, defense, skill, element, dropchance)
        return random_monster
#function which create a strong monster
def random_elite_monster():
        element_list = list(C.ELEMENTS_LIST)
        name_list = list(C.MONSTER_NAMES_LIST)
        element = element_list[random.randint(0, len(element_list)-1)]
        name = name_list[random.randint(0, len(name_list)-1)]
        health = C.MONSTER_MAX_HP
        atk = C.MONSTER_MAX_ATK
        defense = C.MONSTER_MAX_DEF
        skill = C.MONSTER_MAX_SKILL
        dropchance = C.MONSTER_MAX_DROPCHANCE * C.LEVEL_LIMIT
        random_monster = Monster_NPC("Elite " + element + " " + name, health, atk, defense, skill, element, dropchance)
        return random_monster
#function which creates a monster
def random_scaled_up_monster(p_pc):
        element_list = list(C.ELEMENTS_LIST)
        name_list = list(C.MONSTER_NAMES_LIST)
        element = element_list[random.randint(0, len(element_list)-1)]
        name = name_list[random.randint(0, len(name_list)-1)]
        health = random.randint(C.MONSTER_SCALE_HP * p_pc.level, C.MONSTER_MAX_HP)
        atk = random.randint(C.MONSTER_SCALE_ATK * p_pc.level, C.MONSTER_MAX_ATK)
        defense = random.randint(C.MONSTER_SCALE_DEF * p_pc.level, C.MONSTER_MAX_DEF)
        skill = random.randint(p_pc.level, C.MONSTER_MAX_SKILL * p_pc.level)
        dropchance = C.MONSTER_MAX_DROPCHANCE * p_pc.level * p_pc.skill
        random_monster = Monster_NPC(element + " " + name, health, atk, defense, skill, element, dropchance)
        return random_monster
#function which creates a monster that scales to the player's level
def random_scaled_monster(p_pc):
        element_list = list(C.ELEMENTS_LIST)
        name_list = list(C.MONSTER_NAMES_LIST)
        element = element_list[random.randint(0, len(element_list)-1)]
        name = name_list[random.randint(0, len(name_list)-1)]
        health = random.randint(C.MONSTER_MIN_HP, C.MONSTER_SCALE_HP * p_pc.level)
        atk = random.randint(C.MONSTER_MIN_ATK, C.MONSTER_SCALE_ATK * p_pc.level)
        defense = random.randint(C.MONSTER_MIN_DEF, C.MONSTER_SCALE_DEF * p_pc.level)
        skill = random.randint(p_pc.level, C.MONSTER_MAX_SKILL + p_pc.level)
        dropchance = random.randint(0, C.MONSTER_MAX_DROPCHANCE * p_pc.level)
        random_monster = Monster_NPC(element + " " + name, health, atk, defense, skill, element, dropchance)
        return random_monster
#function where the monster performs an action
def monster_attack(m_npc, p_pc):
        if p_pc == None:
                print (m_npc.name, "roars with confidence.")
        else:
                x = random.randint(0, (p_pc.level+p_pc.skill))
                if x >= m_npc.skill:
                        y = random.randint(0, m_npc.skill+m_npc.atk)
                        if y > p_pc.skill:
                        #monster will do a normal attack
                                p_pc.health -= max((m_npc.atk - p_pc.defense - p_pc.defbonus - p_pc.armor), 1)
                                print (m_npc.name, "attacks", p_pc.name)
                        elif y <= p_pc.skill:
                                print (m_npc.name, "misses", p_pc.name)
                if x < m_npc.skill:
                        #monster will do a special attack
                        y = random.randint(1, 5)
                        if y == 1:
                                #monster does an attack that ignores defense
                                p_pc.health -= max((m_npc.atk - p_pc.armor), 1)
                                print (m_npc.name, "does a piercing attack against", p_pc.name)
                        elif y == 2:
                                #monster does a strong attack
                                p_pc.health -= max(round((m_npc.atk*C.CRIT) - p_pc.defense - p_pc.defbonus - p_pc.armor), 1)
                                print (m_npc.name, "does a strong attack against", p_pc.name)
                        elif y == 3:
                                #monster will buff themselves
                                m_npc.atk = round(m_npc.atk * C.BUFF) + m_npc.skill
                                m_npc.defense = round(m_npc.defense * C.BUFF)
                                m_npc.skill = round(m_npc.skill * C.BUFF)
                                print (m_npc.name, "gathers energy.")
                        elif y == 4:
                                #monster will heal themselves
                                m_npc.health += (m_npc.atk + m_npc.defense) + m_npc.skill
                                print (m_npc.name, "seems to regenerate.")
                        elif y == 5:
                                #monster will do a double swing
                                p_pc.health -= max((m_npc.atk - p_pc.defense - p_pc.defbonus - p_pc.armor), 1)
                                p_pc.health -= max((m_npc.atk - p_pc.defense - p_pc.defbonus - p_pc.armor), 1)
                                print (m_npc.name, "rapidly attacks", p_pc.name)
