import random
import copy
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Monster_NPC, Pet_NPC,
                                   ItemBag_PC, Spell_PC, Weapon_PC,
                                   Armor_PC)
from rpg2_constants import Constants
C = Constants()
#function that decides what the armor does
#armor effect occurs when you are attacked
def armor_effect(m_npc, p_pc, a_pc, h_p, m_p):
        new_atk = m_npc.atk - a_pc.defense
        if a_pc.effect == "Block":
                new_atk -= a_pc.strength
                print(a_pc.user, "blocks some of energy from the attack of ", m_npc.name)
        elif a_pc.effect == "Thorns":
                m_npc.health -= a_pc.strength
                if m_npc.health <= 0:
                        new_atk = 0
        elif a_pc.effect == "Absorb":
                p_pc.health += a_pc.strength
                if a_pc.element == m_npc.element:
                        p_pc.health += a_pc.strength
                        print (a_pc.user, "absorbs some of the"
                               "energy from the attack of", m_npc.name)
        elif a_pc.effect == "Super Block":
                new_atk -= (a_pc.strength * C.INCREASE_EXPONENT)
        elif a_pc.effect == "Ethereal":
                x = random.randint(0, (m_npc.skill ** C.INCREASE_EXPONENT) - p_pc.skill)
                if x <= a_pc.strength ** C.DECREASE_EXPONENT:
                        new_atk = 0
                        print (a_pc.user, "dodges", m_npc.name)
        elif a_pc.effect == "Counter":
                m_npc.health -= max(p_pc.atk + p_pc.atkbonus + a_pc.strength - m_npc.defense, 1)
                print (p_pc.name, "hits back against", m_npc.name)
        return new_atk

def weapon_effect(m_npc, p_pc, w_pc, h_p, m_p):
        new_atk = p_pc.atk + w_pc.atk
        if w_pc.effect == "Attack":
                new_atk += w_pc.strength
                print (w_pc.user, "is empowered by their weapon. ")
        elif w_pc.effect == "Death":
                x = random.randint(m_npc.skill, m_npc.health)
                if x < w_pc.strength:
                        new_atk += C.DEATH_ATK
                        print ("Death comes for", m_npc.name)
        elif w_pc.effect == "Lifesteal":
                x = max(p_pc.atk + p_pc.atkbonus + w_pc.atk - m_npc.defense, 0)
                p_pc.health += round((x + w_pc.strength) ** C.DECREASE_EXPONENT)
                p_pc.health = min(p_pc.health, p_pc.maxhealth)
                print (w_pc.user, "drains the life of ", m_npc.name)
        elif w_pc.effect == "Mana Drain":
                p_pc.mana += round(w_pc.strength ** C.DECREASE_EXPONENT)
                if m_npc.element == w_pc.element:
                        p_pc.mana += round(w_pc.strength ** C.DECREASE_EXPONENT)
                        print (w_pc.user, "drains the energy of ", m_npc.name)
        elif w_pc.effect == "Poison":
                m_npc.poison += w_pc.strength
                m_npc.health -= m_npc.poison
        return new_atk
