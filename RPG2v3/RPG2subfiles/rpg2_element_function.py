import random
import copy
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Monster_NPC, Pet_NPC,
                                   ItemBag_PC, Spell_PC, Weapon_PC,
                                   Armor_PC)
from rpg2_constants import Constants
C = Constants()
#fire>air>earth>water>fire is the element cycle
#function that checks for elemental advantage during monster's attack
def check_element_monster_attack(m_npc, armor):
        if m_npc.element == "Fire":
                if armor.element == "Fire" or armor.element == "Water" or armor.element == "Light":
                        new_atk = round(m_npc.atk / C.ELEMENT_BONUS)
                        print (armor.name, "resists the attack of", m_npc.name)
                elif armor.element == "Air":
                        new_atk = round(m_npc.atk * C.ELEMENT_BONUS)
                        print (armor.name, "is weak against the attack of", m_npc.name)
                else:
                        new_atk = m_npc.atk
        elif m_npc.element == "Air":
                if armor.element == "Air" or armor.element == "Fire" or armor.element == "Light":
                        new_atk = round(m_npc.atk / C.ELEMENT_BONUS)
                        print (armor.name, "resists the attack of", m_npc.name)
                elif armor.element == "Earth":
                        new_atk = round(m_npc.atk * C.ELEMENT_BONUS)
                        print (armor.name, "is weak against the attack of", m_npc.name)
                else:
                        new_atk = m_npc.atk
        elif m_npc.element == "Earth":
                if armor.element == "Air" or armor.element == "Earth" or armor.element == "Light":
                        new_atk = round(m_npc.atk / C.ELEMENT_BONUS)
                        print (armor.name, "resists the attack of", m_npc.name)
                elif armor.element == "Water":
                        new_atk = round(m_npc.atk * C.ELEMENT_BONUS)
                        print (armor.name, "is weak against the attack of", m_npc.name)
                else:
                        new_atk = m_npc.atk
        elif m_npc.element == "Water":
                if armor.element == "Water" or armor.element == "Earth" or armor.element == "Light":
                        new_atk = round(m_npc.atk / C.ELEMENT_BONUS)
                        print (armor.name, "resists the attack of", m_npc.name)
                elif armor.element == "Fire":
                        new_atk = round(m_npc.atk * C.ELEMENT_BONUS)
                        print (armor.name, "is weak against the attack of", m_npc.name)
                else:
                        new_atk = m_npc.atk
        elif m_npc.element == "Dark":
                if armor.element == "Dark":
                        new_atk = round(m_npc.atk / C.ELEMENT_BONUS)
                        print (armor.name, "resists the attack of", m_npc.name)
                elif armor.element == "Light":
                        new_atk = round(m_npc.atk * C.ELEMENT_BONUS * C.ELEMENT_BONUS)
                        print (armor.name, "is weak against the attack of", m_npc.name)
                else:
                        new_atk = m_npc.atk
        return new_atk
#checks elements for spells
def check_element_monster_attack(s_pc, m_npc):
