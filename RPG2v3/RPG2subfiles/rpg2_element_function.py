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
                        new_atk = round(m_npc.atk / C.ELEMENT_BONUS) - armor.defense
                        print (armor.user, "resists the attack of", m_npc.name)
                elif armor.element == "Air":
                        new_atk = round(m_npc.atk * C.ELEMENT_BONUS) - armor.defense
                        print (armor.user, "is weak against the attack of", m_npc.name)
                else:
                        new_atk = m_npc.atk - armor.defense
        elif m_npc.element == "Air":
                if armor.element == "Air" or armor.element == "Fire" or armor.element == "Light":
                        new_atk = round(m_npc.atk / C.ELEMENT_BONUS) - armor.defense
                        print (armor.user, "resists the attack of", m_npc.name)
                elif armor.element == "Earth":
                        new_atk = round(m_npc.atk * C.ELEMENT_BONUS) - armor.defense
                        print (armor.user, "is weak against the attack of", m_npc.name)
                else:
                        new_atk = m_npc.atk - armor.defense
        elif m_npc.element == "Earth":
                if armor.element == "Air" or armor.element == "Earth" or armor.element == "Light":
                        new_atk = round(m_npc.atk / C.ELEMENT_BONUS)
                        print (armor.user, "resists the attack of", m_npc.name) - armor.defense
                elif armor.element == "Water":
                        new_atk = round(m_npc.atk * C.ELEMENT_BONUS) - armor.defense
                        print (armor.user, "is weak against the attack of", m_npc.name)
                else:
                        new_atk = m_npc.atk - armor.defense
        elif m_npc.element == "Water":
                if armor.element == "Water" or armor.element == "Earth" or armor.element == "Light":
                        new_atk = round(m_npc.atk / C.ELEMENT_BONUS) - armor.defense
                        print (armor.user, "resists the attack of", m_npc.name)
                elif armor.element == "Fire":
                        new_atk = round(m_npc.atk * C.ELEMENT_BONUS) - armor.defense
                        print (armor.user, "is weak against the attack of", m_npc.name)
                else:
                        new_atk = m_npc.atk - armor.defense
        elif m_npc.element == "Dark":
                if armor.element == "Dark":
                        new_atk = round(m_npc.atk / C.ELEMENT_BONUS) - armor.defense
                        print (armor.user, "resists the attack of", m_npc.name)
                elif armor.element == "Light":
                        new_atk = round(m_npc.atk * C.ELEMENT_BONUS * C.ELEMENT_BONUS) - armor.defense
                        print (armor.user, "is weak against the attack of", m_npc.name)
                else:
                        new_atk = m_npc.atk
        return new_atk
#checks elements for spells
def check_element_spell(s_pc, m_npc):
        if s_pc.element == "Fire":
                if m_npc.element == "Fire" or m_npc.element == "Water":
                        new_atk = round(s_pc.power / C.ELEMENT_BONUS)
                        print (m_npc.name, "resists ", s_pc.name)
                elif m_npc.element == "Air":
                        new_atk = round(s_pc.power * C.ELEMENT_BONUS)
                        print (m_npc.name, "is weak against ", s_pc.name)
                else:
                        new_atk = s_pc.power
        elif s_pc.element == "Air":
                if m_npc.element == "Air" or m_npc.element == "Fire":
                        new_atk = round(s_pc.power / C.ELEMENT_BONUS)
                        print (m_npc.name, "resists ", s_pc.name)
                elif m_npc.element == "Earth":
                        new_atk = round(s_pc.power * C.ELEMENT_BONUS)
                        print (m_npc.name, "is weak against ", s_pc.name)
                else:
                        new_atk = s_pc.power
        elif s_pc.element == "Earth":
                if m_npc.element == "Air" or m_npc.element == "Earth":
                        new_atk = round(s_pc.power / C.ELEMENT_BONUS)
                        print (m_npc.name, "resists ", s_pc.name)
                elif m_npc.element == "Water":
                        new_atk = round(s_pc.power * C.ELEMENT_BONUS)
                        print (m_npc.name, "is weak against ", s_pc.name)
                else:
                        new_atk = s_pc.power
        elif s_pc.element == "Water":
                if m_npc.element == "Water" or m_npc.element == "Earth":
                        new_atk = round(s_pc.power / C.ELEMENT_BONUS)
                        print (m_npc.name, "resists", s_pc.name)
                elif m_npc.element == "Fire":
                        new_atk = round(s_pc.power * C.ELEMENT_BONUS)
                        print (m_npc.name, "is weak against", s_pc.name)
                else:
                        new_atk = s_pc.power
        elif s_pc.element == "Dark":
                if m_npc.element == "Dark":
                        new_atk = -s_pc.power
                        print (m_npc.name, "resists", s_pc.name)
                else:
                        new_atk = s_pc.power
        return new_atk
#checks elements for player attacks
def check_element_player_attack(p_pc, m_npc, w_pc):
        if w_pc.element == "Fire":
                if m_npc.element == "Fire" or m_npc.element == "Water":
                        new_atk = round((p_pc.atk + p_pc.atkbonus) / C.ELEMENT_BONUS) + w_pc.atk
                        print (m_npc.name, "resists ", p_pc.name)
                elif m_npc.element == "Air":
                        new_atk = round((p_pc.atk + p_pc.atkbonus) * C.ELEMENT_BONUS) + w_pc.atk
                        print (m_npc.name, "is weak against ", p_pc.name)
                else:
                        new_atk = (p_pc.atk + p_pc.atkbonus) + w_pc.atk
        elif w_pc.element == "Air":
                if m_npc.element == "Air" or m_npc.element == "Fire":
                        new_atk = round((p_pc.atk + p_pc.atkbonus) / C.ELEMENT_BONUS) + w_pc.atk
                        print (m_npc.name, "resists ", p_pc.name)
                elif m_npc.element == "Earth":
                        new_atk = round((p_pc.atk + p_pc.atkbonus) * C.ELEMENT_BONUS) + w_pc.atk
                        print (m_npc.name, "is weak against ", p_pc.name)
                else:
                        new_atk = (p_pc.atk + p_pc.atkbonus) + w_pc.atk
        elif w_pc.element == "Earth":
                if m_npc.element == "Air" or m_npc.element == "Earth":
                        new_atk = round((p_pc.atk + p_pc.atkbonus) / C.ELEMENT_BONUS) + w_pc.atk
                        print (m_npc.name, "resists ", p_pc.name)
                elif m_npc.element == "Water":
                        new_atk = round((p_pc.atk + p_pc.atkbonus) * C.ELEMENT_BONUS) + w_pc.atk
                        print (m_npc.name, "is weak against ", p_pc.name)
                else:
                        new_atk = (p_pc.atk + p_pc.atkbonus) + w_pc.atk
        elif w_pc.element == "Water":
                if m_npc.element == "Water" or m_npc.element == "Earth":
                        new_atk = round((p_pc.atk + p_pc.atkbonus) / C.ELEMENT_BONUS) + w_pc.atk
                        print (m_npc.name, "resists", p_pc.name)
                elif m_npc.element == "Fire":
                        new_atk = round((p_pc.atk + p_pc.atkbonus) * C.ELEMENT_BONUS) + w_pc.atk
                        print (m_npc.name, "is weak against", p_pc.name)
                else:
                        new_atk = (p_pc.atk + p_pc.atkbonus) + w_pc.atk
        elif w_pc.element == "Dark":
                if m_npc.element == "Dark":
                        new_atk = min(w_pc.atk - (p_pc.atk + p_pc.atkbonus), 0)
                        print (m_npc.name, "resists", p_pc.name)
                else:
                        new_atk = (p_pc.atk + p_pc.atkbonus) + w_pc.atk
        elif w_pc.element == "Light":
                if m_npc.element == "Dark" and p_pc.name == "Hero":
                        new_atk = ((p_pc.atk + p_pc.atkbonus) * C.ELEMENT_BONUS * C.ELEMENT_BONUS) + w_pc.atk
                        print (m_npc.name, "is weak against", w_pc.user)
                else:
                        new_atk = (p_pc.atk + p_pc.atkbonus) + w_pc.atk
        else:
                new_atk = (p_pc.atk + p_pc.atkbonus) + w_pc.atk
        return new_atk
