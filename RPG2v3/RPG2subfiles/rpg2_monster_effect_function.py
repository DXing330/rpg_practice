import copy
import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Monster_NPC, Armor_PC)
from rpg2_constants import Constants
import rpg2_element_function as element_func
import rpg2_equipment_effect_function as ee_func
import rpg2_party_management_functions as party_func
from rpg2_constant_lists import List_Constants
L = List_Constants()
C = Constants()
monsterList = ["Fire", "Water", "Air", "Earth", "Dark",
               "Demon", "Slime", "Skeleton", "Beast", "Elemental", "Troll"]
#function that checks what kind of passives a monster has
def monster_passive_effect(m_npc, p_pc, h_p, m_p):
        for passive in L.MONSTER_PASSIVE_LIST:
                if passive in m_npc.name:
                        if passive == "Fire":
                                p_pc.health -= m_npc.skill
                                print (p_pc.name, "is burned by", m_npc.name)
                        if passive == "Water":
                                p_pc.atkbonus -= min(m_npc.skill, p_pc.atkbonus)
                                print (p_pc.name, "is bogged down by", m_npc.name)
                        if passive == "Air":
                                p_pc.skill -= 1
                                print (p_pc.name, "is distracted by", m_npc.name)
                        if passive == "Earth":
                                m_npc.defense += m_npc.skill
                                print (m_npc.name, "hardens. ")
                        if passive == "Dark":
                                m_npc.skill += 1
                                print ("Darkness swirls around", m_npc.name)
                        if passive == "Demon":
                                for mon in m_p:
                                        m_npc.skill += 1
                                print (m_npc.name, "empowers its allies. ")
                        if passive == "Slime":
                                if m_npc.health > m_npc.skill:
                                        x = random.randint(0, len(m_p))
                                        if x == 0:
                                                m_npc.health = round(m_npc.health/2)
                                                copy_mon = copy.copy(m_npc)
                                                m_p.append(copy_mon)
                                                print (m_npc.name, "splits! ")
                        if passive == "Skeleton":
                                p_pc.defbonus -= min(m_npc.skill, p_pc.defbonus)
                                print (p_pc.name, " feels the ", 
                                       "decaying power of ", m_npc.name)
                        if passive == "Beast":
                                m_npc.atk += m_npc.skill
                                print (m_npc.name, "howls.")
                        if passive == "Elemental":
                                x = random.randint(0, 3)
                                if x == 0:
                                        m_npc.health += m_npc.skill
                                elif x == 1:
                                        m_npc.atk += m_npc.skill
                                elif x == 2:
                                        m_npc.defense += m_npc.skill
                                elif x == 3:
                                        m_npc.skill += 1
                                print (m_npc.name, "pulses erratically. ")
                        if passive == "Troll":
                                m_npc.health += m_npc.skill
                                print (m_npc.name, "regenerates. ")
