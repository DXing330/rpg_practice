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
        if a_pc == None:
                new_atk = m_npc.atk
        else:
                new_atk = m_npc.atk - a_pc.defense
                if a_pc.effect == "Block":
                        new_atk -= a_pc.strength
                        print(a_pc.user, "blocks some of energy from the attack of ",
                              m_npc.name)
                elif a_pc.effect == "Thorns" and a_pc.upgrade == 0:
                        m_npc.health -= a_pc.strength + max(p_pc.skill - m_npc.skill, 0)
                        if m_npc.health <= 0:
                                new_atk = 0
                        print ("The spiky armor hurts", m_npc.name)
                elif a_pc.effect == "Thorns":
                        m_npc.health -= a_pc.strength + max(p_pc.skill - m_npc.skill, 0) * a_pc.upgrade
                        if m_npc.health <= 0:
                                new_atk = 0
                        print ("The spiky armor hurts", m_npc.name)
                elif a_pc.effect == "Reflect" and a_pc.upgrade == 0:
                        m_npc.health -= (round((a_pc.strength * m_npc.atk) ** C.DECREASE_EXPONENT)
                                         - m_npc.defense)
                        print (a_pc.user, "reflects some of the energy from the attack of ",
                               m_npc.name)
                elif a_pc.effect == "Reflect":
                        m_npc.health -= (round((a_pc.strength * m_npc.atk *
                                                a_pc.upgrade) ** C.DECREASE_EXPONENT) - m_npc.defense)
                        print (a_pc.user, "reflects some of the energy from the attack of ",
                               m_npc.name)
                elif a_pc.effect == "Poison" and a_pc.upgrade == 0:
                        m_npc.poison += a_pc.strength
                        m_npc.health -= m_npc.poison
                        print (m_npc.name, "is poisoned from attacking", a_pc.user)
                elif a_pc.effect == "Poison":
                        m_npc.poison += a_pc.strength * a_pc.upgrade
                        m_npc.health -= m_npc.poison
                        print (m_npc.name, "is poisoned from attacking", a_pc.user)
                elif a_pc.effect == "Absorb" and a_pc.upgrade == 0:
                        p_pc.health += a_pc.strength
                        if a_pc.element == m_npc.element:
                                p_pc.health += a_pc.strength
                                print (a_pc.user, "absorbs some of the"
                                       "energy from the attack of", m_npc.name)
                        p_pc.health = min(p_pc.health, p_pc.maxhealth)
                elif a_pc.effect == "Absorb":
                        p_pc.health += a_pc.strength * a_pc.upgrade
                        if a_pc.element == m_npc.element:
                                p_pc.health += a_pc.strength * a_pc.upgrade
                                print (a_pc.user, "absorbs some of the"
                                       "energy from the attack of", m_npc.name)
                        p_pc.health = min(p_pc.health, p_pc.maxhealth)
                elif a_pc.effect == "Super Block":
                        new_atk -= (a_pc.strength * C.INCREASE_EXPONENT)
                        print(a_pc.user, "blocks some of energy from the attack of ",
                              m_npc.name)
                elif a_pc.effect == "Ethereal" and a_pc.upgrade == 0:
                        x = random.randint(0, (m_npc.skill ** C.INCREASE_EXPONENT) - p_pc.skill)
                        if x <= a_pc.strength ** C.DECREASE_EXPONENT:
                                new_atk = 0
                                print (a_pc.user, "dodges", m_npc.name)
                elif a_pc.effect == "Ethereal":
                        x = random.randint(0, (m_npc.skill ** C.INCREASE_EXPONENT) - p_pc.skill)
                        if x <= a_pc.strength * a_pc.upgrade:
                                new_atk = 0
                                print (a_pc.user, "dodges", m_npc.name)
                elif a_pc.effect == "Counter":
                        m_npc.health -= max(p_pc.atk + p_pc.atkbonus + a_pc.strength - m_npc.defense, 1)
                        print (p_pc.name, "hits back against", m_npc.name)
                elif a_pc.effect == "Resist Fire":
                        if m_npc.element == "Fire":
                                new_atk = new_atk // C.ELEMENT_BONUS
                                print (a_pc.user, "resists the attack of", m_npc.name)
                elif a_pc.effect == "Resist Water":
                        if m_npc.element == "Water":
                                new_atk = new_atk // C.ELEMENT_BONUS
                                print (a_pc.user, "resists the attack of", m_npc.name)
                elif a_pc.effect == "Resist Earth":
                        if m_npc.element == "Earth":
                                new_atk = new_atk // C.ELEMENT_BONUS
                                print (a_pc.user, "resists the attack of", m_npc.name)
                elif a_pc.effect == "Resist Air":
                        if m_npc.element == "Air":
                                new_atk = new_atk // C.ELEMENT_BONUS
                                print (a_pc.user, "resists the attack of", m_npc.name)
                elif a_pc.effect == "Resist Dark":
                        if m_npc.element == "Dark":
                                new_atk = new_atk // C.ELEMENT_BONUS
                                print (a_pc.user, "resists the attack of", m_npc.name)
                elif a_pc.effect == "Revive" and a_pc.upgrade == 0:
                        if new_atk - p_pc.defbonus - p_pc.defense >= p_pc.health and a_pc.strength > 0:
                                new_atk = 0
                                a_pc.strength -= p_pc.health
                                print (a_pc.user, "narrowly escapes death. ")
                elif a_pc.effect == "Revive":
                        if new_atk - p_pc.defbonus - p_pc.defense >= p_pc.health and a_pc.strength > 0:
                                new_atk = 0
                                a_pc.strength -= p_pc.health // a_pc.upgrade
                                print (a_pc.user, "narrowly escapes death. ")
                        
        return new_atk

def weapon_effect(m_npc, p_pc, w_pc, h_p, m_p):
        if w_pc == None:
                new_atk = p_pc.atk
        else:
                new_atk = p_pc.atk + w_pc.atk
                if w_pc.effect == "Attack" and w_pc.upgrade == 0:
                        new_atk += w_pc.strength
                elif w_pc.effect == "Attack":
                        new_atk += w_pc.strength  * w_pc.upgrade
                elif w_pc.effect == "Death" and w_pc.element == "Dark":
                        x = random.randint(0, max(m_npc.health, m_npc.skill))
                        if x < w_pc.strength:
                                new_atk += min(C.DEATH_ATK, m_npc.health)
                                print ("Death comes for", m_npc.name)
                elif w_pc.effect == "Lifesteal" and w_pc.upgrade == 0:
                        x = max(p_pc.atk + p_pc.atkbonus + w_pc.atk - m_npc.defense, 0)
                        p_pc.health += round(x ** C.DECREASE_EXPONENT) + w_pc.strength
                        p_pc.health = min(p_pc.health, p_pc.maxhealth)
                        print (w_pc.user, "drains the life of ", m_npc.name)
                elif w_pc.effect == "Lifesteal":
                        x = max(p_pc.atk + p_pc.atkbonus + w_pc.atk - m_npc.defense, 0)
                        p_pc.health += round(x ** C.DECREASE_EXPONENT) + w_pc.strength  * w_pc.upgrade
                        p_pc.health = min(p_pc.health, p_pc.maxhealth)
                        print (w_pc.user, "drains the life of ", m_npc.name)
                elif w_pc.effect == "Mana Drain" and w_pc.upgrade == 0:
                        p_pc.mana += round(w_pc.strength ** C.DECREASE_EXPONENT)
                        if m_npc.element == w_pc.element:
                                p_pc.mana += round(w_pc.strength ** C.DECREASE_EXPONENT)
                                print (w_pc.user, "drains the energy of ", m_npc.name)
                elif w_pc.effect == "Mana Drain":
                        p_pc.mana += round((w_pc.strength * w_pc.upgrade) ** C.DECREASE_EXPONENT)
                        if m_npc.element == w_pc.element:
                                p_pc.mana += round((w_pc.strength * w_pc.upgrade) ** C.DECREASE_EXPONENT)
                                print (w_pc.user, "drains the energy of ", m_npc.name)
                elif w_pc.effect == "Poison" and w_pc.upgrade == 0:
                        m_npc.poison += w_pc.strength
                        m_npc.health -= m_npc.poison
                        print (w_pc.user, "poisons", m_npc.name)
                elif w_pc.effect == "Poison":
                        m_npc.poison += w_pc.strength * w_pc.upgrade
                        m_npc.health -= m_npc.poison
                        print (w_pc.user, "poisons", m_npc.name)
                elif w_pc.effect == "Lucky" and w_pc.upgrade == 0:
                        x = random.randint(0, m_npc.skill)
                        if x <= w_pc.strength:
                                new_atk = (p_pc.atk + p_pc.atkbonus) * C.CRIT
                                print (w_pc.user, "gets a lucky critical hit! ")
                elif w_pc.effect == "Lucky":
                        x = random.randint(0, m_npc.skill)
                        if x <= w_pc.strength * w_pc.upgrade:
                                new_atk = (p_pc.atk + p_pc.atkbonus) * C.CRIT
                                print (w_pc.user, "gets a lucky critical hit! ")
                elif w_pc.effect == "Skill Drain" and w_pc.upgrade == 0:
                        if w_pc.strength > 0:
                                m_npc.skill -= min(round(w_pc.strength ** C.DECREASE_EXPONENT),
                                                   m_npc.skill)
                                p_pc.skill += w_pc.strength
                                w_pc.strength -= 1
                                print (w_pc.user, "drains the energy of ", m_npc.name)
                elif w_pc.effect == "Skill Drain":
                        if w_pc.strength > 0:
                                m_npc.skill -= min(round(w_pc.strength ** C.DECREASE_EXPONENT),
                                                   m_npc.skill)
                                p_pc.skill += w_pc.strength
                                w_pc.strength -= 1
                                print (w_pc.user, "drains the energy of ", m_npc.name)
                        elif w_pc.strength <= 0:
                                w_pc.strength += w_pc.upgrade
                elif w_pc.effect == "Slay Fire":
                        if m_npc.element == "Fire":
                                new_atk = (p_pc.atk + p_pc.atkbonus)  * C.ELEMENT_BONUS
                                print (w_pc.user, "performs a super effective hit against", m_npc.name)
                elif w_pc.effect == "Slay Water":
                        if m_npc.element == "Water":
                                new_atk = (p_pc.atk + p_pc.atkbonus) * C.ELEMENT_BONUS
                                print (w_pc.user, "performs a super effective hit against", m_npc.name)
                elif w_pc.effect == "Slay Earth":
                        if m_npc.element == "Earth":
                                new_atk = (p_pc.atk + p_pc.atkbonus) * C.ELEMENT_BONUS
                                print (w_pc.user, "performs a super effective hit against", m_npc.name)
                elif w_pc.effect == "Slay Air":
                        if m_npc.element == "Air":
                                new_atk = (p_pc.atk + p_pc.atkbonus) * C.ELEMENT_BONUS
                                print (w_pc.user, "performs a super effective hit against", m_npc.name)
                elif w_pc.effect == "Slay Dark":
                        if m_npc.element == "Dark":
                                new_atk = (p_pc.atk + p_pc.atkbonus) * C.ELEMENT_BONUS
                                print (w_pc.user, "performs a super effective hit against", m_npc.name)
                elif w_pc.effect == "Explode" and w_pc.upgrade == 0:
                        for mon in m_p:
                                mon.health -= w_pc.strength
                        p_pc.health -= w_pc.strength
                        print (w_pc.user, "performs an explosive attack on the enemy. ")
                elif w_pc.effect == "Explode":
                        for mon in m_p:
                                mon.health -= w_pc.strength * w_pc.upgrade
                        p_pc.health -= w_pc.strength * w_pc.upgrade
                        print (w_pc.user, "performs an explosive attack on the enemy. ")
                elif w_pc.effect == "Summon" and w_pc.user == "Summoner" and w_pc.upgrade == 0:
                        if w_pc.strength > 0:
                                summon = Player_PC("Homunculus", 1,
                                                   w_pc.strength ** C.INCREASE_EXPONENT,
                                                   w_pc.strength ** C.INCREASE_EXPONENT,
                                                   w_pc.strength,
                                                   w_pc.strength,
                                                   w_pc.strength,
                                                   0, 0)
                                h_p.append(summon)
                                w_pc.strength = 0
                                print (w_pc.user, "creates", summon.name)
                        elif w_pc.strength <= 0:
                                w_pc.atk += w_pc.upgrade
                elif w_pc.effect == "Summon" and w_pc.user == "Summoner":
                        if w_pc.strength > 0:
                                summon = Player_PC("Homunculus", 1,
                                                   (w_pc.strength ** C.INCREASE_EXPONENT) * w_pc.upgrade,
                                                   (w_pc.strength ** C.INCREASE_EXPONENT) * w_pc.upgrade,
                                                   w_pc.strength * w_pc.upgrade,
                                                   w_pc.strength * w_pc.upgrade,
                                                   0, 0, 0)
                                h_p.append(summon)
                                w_pc.strength = 0
                                print (w_pc.user, "creates", summon.name)
                        elif w_pc.strength <= 0:
                                w_pc.atk += w_pc.upgrade
                                                   
                if w_pc.name == "Observer":
                        for mon in m_p:
                                mon.stats()
                                
        return new_atk
