import random
import copy
import sys
sys.path.append("../RPG2v3_def")
from rpg2_classdefinitions import (Player_PC, Monster_NPC, Pet_NPC,
                                   ItemBag_PC, Spell_PC, Weapon_PC,
                                   Armor_PC)
from rpg2_constants import Constants
C = Constants()
#fire>air>earth>water>fire is the element cycle
#function that checks for elemental advantage during monster's attack
def check_element_monster_attack(m_npc, m_npc_atk, armor):
        new_atk = m_npc_atk
        if armor == None:
                new_atk = m_npc_atk
        else:
                if m_npc.element == "Fire":
                        if armor.element == "Fire" or armor.element == "Water":
                                new_atk = round(m_npc_atk / C.ELEMENT_BONUS)
                                print (armor.user, "resists the attack of", m_npc.name)
                        elif armor.element == "Light" and "Hero" in armor.user:
                                new_atk = round(m_npc_atk / C.ELEMENT_BONUS)
                                print (armor.user, "resists the attack of", m_npc.name)
                        elif armor.element == "Air":
                                new_atk = round(m_npc_atk * C.ELEMENT_BONUS)
                                print (armor.user, "is weak against the attack of", m_npc.name)
                        else:
                                new_atk = m_npc_atk
                elif m_npc.element == "Air":
                        if armor.element == "Air" or armor.element == "Fire":
                                new_atk = round(m_npc_atk / C.ELEMENT_BONUS)
                                print (armor.user, "resists the attack of", m_npc.name)
                        elif armor.element == "Light" and "Hero" in armor.user:
                                new_atk = round(m_npc_atk / C.ELEMENT_BONUS)
                                print (armor.user, "resists the attack of", m_npc.name)
                        elif armor.element == "Earth":
                                new_atk = round(m_npc_atk * C.ELEMENT_BONUS)
                                print (armor.user, "is weak against the attack of", m_npc.name)
                        else:
                                new_atk = m_npc_atk
                elif m_npc.element == "Earth":
                        if armor.element == "Air" or armor.element == "Earth":
                                new_atk = round(m_npc_atk / C.ELEMENT_BONUS)
                                print (armor.user, "resists the attack of", m_npc.name)
                        elif armor.element == "Light" and "Hero" in armor.user:
                                new_atk = round(m_npc_atk / C.ELEMENT_BONUS)
                                print (armor.user, "resists the attack of", m_npc.name)
                        elif armor.element == "Water":
                                new_atk = round(m_npc_atk * C.ELEMENT_BONUS)
                                print (armor.user, "is weak against the attack of", m_npc.name)
                        else:
                                new_atk = m_npc_atk
                elif m_npc.element == "Water":
                        if armor.element == "Water" or armor.element == "Earth":
                                new_atk = round(m_npc_atk / C.ELEMENT_BONUS)
                                print (armor.user, "resists the attack of", m_npc.name)
                        elif armor.element == "Light" and "Hero" in armor.user:
                                new_atk = round(m_npc_atk / C.ELEMENT_BONUS)
                                print (armor.user, "resists the attack of", m_npc.name)
                        elif armor.element == "Fire":
                                new_atk = round(m_npc_atk * C.ELEMENT_BONUS)
                                print (armor.user, "is weak against the attack of", m_npc.name)
                        else:
                                new_atk = m_npc_atk
                elif m_npc.element == "Dark":
                        if armor.element == "Dark":
                                new_atk = round(m_npc_atk / C.ELEMENT_BONUS)
                                print (armor.user, "resists the attack of", m_npc.name)
                        elif armor.element == "Light" and "Hero" in armor.user:
                                new_atk = round(m_npc_atk * C.ELEMENT_BONUS)
                                print (armor.user, "is weak against the attack of", m_npc.name)
                        elif armor.element == "Light":
                                new_atk = round(m_npc_atk / C.ELEMENT_BONUS)
                                print (armor.user, "resists the attack of", m_npc.name)
                        else:
                                new_atk = m_npc_atk
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
def check_element_player_attack(p_pc, p_pc_atk, m_npc, w_pc):
        if w_pc == None:
                new_atk = p_pc_atk + p_pc.atkbonus
        else:
                new_atk = p_pc_atk + p_pc.atkbonus
                if w_pc.element == "Fire":
                        if m_npc.element == "Fire" or m_npc.element == "Water":
                                new_atk = round(new_atk / C.ELEMENT_BONUS)
                                print (m_npc.name, "resists ", p_pc.name)
                        elif m_npc.element == "Air":
                                new_atk = round(new_atk * C.ELEMENT_BONUS)
                                print (m_npc.name, "is weak against ", p_pc.name)
                elif w_pc.element == "Air":
                        if m_npc.element == "Air" or m_npc.element == "Fire":
                                new_atk = round(new_atk / C.ELEMENT_BONUS)
                                print (m_npc.name, "resists ", p_pc.name)
                        elif m_npc.element == "Earth":
                                new_atk = round(new_atk * C.ELEMENT_BONUS)
                                print (m_npc.name, "is weak against ", p_pc.name)
                elif w_pc.element == "Earth":
                        if m_npc.element == "Air" or m_npc.element == "Earth":
                                new_atk = round(new_atk / C.ELEMENT_BONUS)
                                print (m_npc.name, "resists ", p_pc.name)
                        elif m_npc.element == "Water":
                                new_atk = round(new_atk * C.ELEMENT_BONUS)
                                print (m_npc.name, "is weak against ", p_pc.name)
                elif w_pc.element == "Water":
                        if m_npc.element == "Water" or m_npc.element == "Earth":
                                new_atk = round(new_atk / C.ELEMENT_BONUS)
                                print (m_npc.name, "resists", p_pc.name)
                        elif m_npc.element == "Fire":
                                new_atk = round(new_atk * C.ELEMENT_BONUS)
                                print (m_npc.name, "is weak against", p_pc.name)
                elif w_pc.element == "Dark":
                        if m_npc.element == "Dark":
                                new_atk = min(w_pc.atk - (p_pc_atk + p_pc.atkbonus), 0)
                                print (m_npc.name, "resists", p_pc.name)
                elif w_pc.element == "Light":
                        if m_npc.element == "Dark":
                                new_atk = (new_atk * C.ELEMENT_BONUS)
                                print (m_npc.name, "is weak against", w_pc.user)
        return new_atk
