import random
import sys
sys.path.append("../RPG2v3_def")
from rpg2_classdefinitions import (Player_PC, Monster_NPC, Armor_PC)
from rpg2_constants import Constants
import rpg2_party_management_functions as party_func
from rpg2_constant_lists import List_Constants
L = List_Constants()
C = Constants()
sys.path.append(".")
import rpg2_monster_effect_function as me_func
import rpg2_element_function as element_func
import rpg2_equipment_effect_function as ee_func


#function which creates a strong scaled monster
def random_scaled_elite_monster(p_pc):
        element_list = list(L.ELEMENTS_LIST)
        name_list = list(L.MONSTER_NAMES_LIST)
        element = element_list[random.randint(0, len(element_list)-1)]
        name = name_list[random.randint(0, len(name_list)-1)]
        health = random.randint(C.MONSTER_MAX_HP, C.MONSTER_MAX_HP * (p_pc.level + p_pc.atk))
        atk = random.randint(C.MONSTER_MAX_ATK, C.MONSTER_MAX_ATK + (p_pc.atkbonus + p_pc.defbonus + p_pc.mana + p_pc.skill))
        defense = random.randint(C.MONSTER_MAX_DEF, C.MONSTER_MAX_DEF + (p_pc.defense + p_pc.atkbonus + p_pc.defbonus))
        skill = random.randint(C.MONSTER_MAX_SKILL, C.MONSTER_MAX_SKILL + p_pc.skill)
        dropchance = C.MONSTER_MAX_DROPCHANCE * C.LEVEL_LIMIT * p_pc.skill
        random_monster = Monster_NPC("Super Elite " + element + " " + name, health, atk, defense, skill, element, dropchance)
        return random_monster
#function which create a strong monster
def random_elite_monster():
        element_list = list(L.ELEMENTS_LIST)
        name_list = list(L.MONSTER_NAMES_LIST)
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
        element_list = list(L.ELEMENTS_LIST)
        name_list = list(L.MONSTER_NAMES_LIST)
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
        element_list = list(L.ELEMENTS_LIST)
        name_list = list(L.MONSTER_NAMES_LIST)
        element = element_list[random.randint(0, len(element_list)-1)]
        name = name_list[random.randint(0, len(name_list)-1)]
        health = random.randint(C.MONSTER_MIN_HP, C.MONSTER_SCALE_HP * p_pc.level)
        atk = random.randint(C.MONSTER_MIN_ATK, C.MONSTER_SCALE_ATK * p_pc.level)
        defense = random.randint(C.MONSTER_MIN_DEF, C.MONSTER_SCALE_DEF * p_pc.level)
        skill = random.randint(p_pc.level, C.MONSTER_MAX_SKILL + p_pc.level)
        dropchance = random.randint(C.MONSTER_MAX_DROPCHANCE, C.MONSTER_MAX_DROPCHANCE * p_pc.level)
        random_monster = Monster_NPC(element + " " + name, health, atk, defense, skill, element, dropchance)
        return random_monster
#function where the monster performs an action
def monster_attack(m_npc, p_pc, h_a, h_p, m_p):
        print (" ")
        #check what kind of effect the monster has
        me_func.monster_passive_effect(m_npc, p_pc, h_p, m_p)
        #account for special monsters
        if m_npc.name == "Bomb":
                if m_npc.health > 0:
                        m_npc.health -= p_pc.skill
                        if m_npc.health <= 0:
                                print (m_npc.name, "explodes! ")
                                if m_npc.element == "Poison":
                                        for mon in m_p:
                                                mon.poison += m_npc.skill
                                        print ("Poison gas surrounds the monsters. ")
                                elif m_npc.element == "Blast":
                                        for mon in m_p:
                                                mon.health -= C.BOMB_DAMAGE
                                                mon.health -= m_npc.skill
                                        print ("Shrapnel pieces fly at the monsters. ")
                                m_p.remove(m_npc)
        else:
                #check if the hero has any special armor
                armor = party_func.check_equipment(p_pc, h_a)
                #check if the armor has any effect
                new_atk = ee_func.armor_effect(m_npc, p_pc, armor, h_p, m_p)
                new_m_npc_atk = element_func.check_element_monster_attack(m_npc, new_atk, armor)
                if p_pc == None:
                        print (m_npc.name, "roars with confidence.")

                else:
                        #randomly pick the monster's actions
                        x = random.randint(0, max((p_pc.level + p_pc.skill), 1))
                        if x >= m_npc.skill * C.INCREASE_EXPONENT:
                                y = random.randint(0, m_npc.skill+m_npc.atk)
                                if y > p_pc.skill ** C.DECREASE_EXPONENT:
                                #monster will do a normal attack
                                        #check if the armor affects the battle
                                        p_pc.health -= max((new_m_npc_atk - p_pc.defense - p_pc.defbonus), 1)
                                        print (m_npc.name, "attacks", p_pc.name)
                                elif y <= p_pc.skill ** C.DECREASE_EXPONENT:
                                        print (m_npc.name, "misses", p_pc.name)
                        if x < m_npc.skill:
                                #monster will do a special attack
                                y = random.randint(1, 5)
                                if y == 1:
                                        #monster does an attack that ignores defense
                                        p_pc.health -= max((new_m_npc_atk), 1)
                                        print (m_npc.name, "does a piercing attack against", p_pc.name)
                                elif y == 2:
                                        #monster does a strong attack
                                        p_pc.health -= max(round((new_m_npc_atk*C.CRIT) - p_pc.defense - p_pc.defbonus), 1)
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
                                        p_pc.health -= max((new_m_npc_atk - p_pc.defense - p_pc.defbonus), 1)
                                        p_pc.health -= max((new_m_npc_atk - p_pc.defense - p_pc.defbonus), 1)
                                        print (m_npc.name, "rapidly attacks", p_pc.name)
