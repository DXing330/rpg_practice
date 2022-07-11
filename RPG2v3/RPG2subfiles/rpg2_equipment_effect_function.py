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
def armor_effect(m_npc, p_pc, a_pc):
        new_atk = m_npc.atk
        if a_pc.effect == "Block":
                new_atk = m_npc.atk - a_pc.strength
        elif a_pc.effect == "Thorns":
                m_npc.health -= a_pc.strength
        elif a_pc.effect == "Absorb":
                p_pc.health += a_pc.strength
        elif a_pc.effect == "Super Block":
                new_atk = m_npc.atk - (a_pc.strength ** C.INCREASE_EXPONENT)
        return new_atk

