import random
import copy
import sys
sys.path.append("../RPG2v3_def")
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
                if "Block" in a_pc.effect:
                        new_atk -= a_pc.strength
                        print(a_pc.user, "blocks some of energy from the attack of ",
                              m_npc.name)
                if "Bomb" in a_pc.effect:
                        print (a_pc.user, "releases a shockwave of force when struck. ")
                        if a_pc.upgrade == 0:
                                for mon in m_p:
                                        mon.health -= a_pc.strength
                                p_pc.health -= a_pc.strength
                        else:
                                for mon in m_p:
                                        mon.health -= a_pc.strength * a_pc.upgrade
                                p_pc.health -= a_pc.strength * a_pc.upgrade

                if "Thorns" in a_pc.effect:
                        if a_pc.upgrade > 0:
                                m_npc.health -= (a_pc.strength * a_pc.upgrade) + max(p_pc.skill - m_npc.skill, 0)
                                if m_npc.health <= 0:
                                        new_atk = 0
                                print ("The spiky armor hurts", m_npc.name)
                        else:
                                m_npc.health -= a_pc.strength + max(p_pc.skill - m_npc.skill, 0)
                                if m_npc.health <= 0:
                                        new_atk = 0
                                print ("The spiky armor hurts", m_npc.name)

                if "Reflect" in a_pc.effect:
                        if a_pc.upgrade > 0:
                                m_npc.health -= max((round((a_pc.strength * m_npc.atk *
                                                            a_pc.upgrade) ** C.DECREASE_EXPONENT) - m_npc.defense), 1)
                                print (a_pc.user, "reflects some of the energy from the attack of ",
                                       m_npc.name)
                        else:
                                m_npc.health -= (round((a_pc.strength * m_npc.atk) ** C.DECREASE_EXPONENT)
                                                 - m_npc.defense)
                                print (a_pc.user, "reflects some of the energy from the attack of ",
                                       m_npc.name)
                if "Poison" in a_pc.effect:
                        print (m_npc.name, "is poisoned from attacking", a_pc.user)
                        if a_pc.upgrade > 0:
                                m_npc.poison += a_pc.strength * a_pc.upgrade
                                m_npc.health -= m_npc.poison
                        else:
                                m_npc.poison += a_pc.strength
                                m_npc.health -= m_npc.poison
                if "Absorb" in a_pc.effect:
                        if a_pc.upgrade > 0:
                                p_pc.health += a_pc.strength * a_pc.upgrade
                                if a_pc.element == m_npc.element:
                                        p_pc.health += a_pc.strength * a_pc.upgrade
                                        print (a_pc.user, "absorbs some of the"
                                               "energy from the attack of", m_npc.name)
                        else:
                                p_pc.health += a_pc.strength
                                if a_pc.element == m_npc.element:
                                        p_pc.health += a_pc.strength
                                        print (a_pc.user, "absorbs some of the"
                                               "energy from the attack of", m_npc.name)
                        p_pc.health = min(p_pc.health, p_pc.maxhealth)
                if "Super Block" in a_pc.effect:
                        new_atk -= (a_pc.strength * C.INCREASE_EXPONENT)
                        print(a_pc.user, "blocks some of energy from the attack of ",
                              m_npc.name)

                if "Ethereal" in a_pc.effect:
                        x = random.randint(0, (m_npc.skill ** C.INCREASE_EXPONENT) - p_pc.skill)
                        if a_pc.upgrade > 0:
                                if x <= (a_pc.strength * a_pc.upgrade) ** C.DECREASE_EXPONENT:
                                        new_atk = 0
                                        print (a_pc.user, "dodges", m_npc.name)
                        else:
                                if x <= a_pc.strength ** C.DECREASE_EXPONENT:
                                        new_atk = 0
                                        print (a_pc.user, "dodges", m_npc.name)
                                        
                if "Counter" in a_pc.effect:
                        m_npc.health -= max(p_pc.atk + p_pc.atkbonus + a_pc.strength - m_npc.defense, 1)
                        print (p_pc.name, "hits back against", m_npc.name)
                if "Resist Fire" in a_pc.effect:
                        if m_npc.element == "Fire":
                                new_atk = new_atk // C.ELEMENT_BONUS
                                print (a_pc.user, "resists the attack of", m_npc.name)
                if "Resist Water" in a_pc.effect:
                        if m_npc.element == "Water":
                                new_atk = new_atk // C.ELEMENT_BONUS
                                print (a_pc.user, "resists the attack of", m_npc.name)
                if "Resist Earth" in a_pc.effect:
                        if m_npc.element == "Earth":
                                new_atk = new_atk // C.ELEMENT_BONUS
                                print (a_pc.user, "resists the attack of", m_npc.name)
                if "Resist Air" in a_pc.effect:
                        if m_npc.element == "Air":
                                new_atk = new_atk // C.ELEMENT_BONUS
                                print (a_pc.user, "resists the attack of", m_npc.name)
                if "Resist Dark" in a_pc.effect:
                        if m_npc.element == "Dark":
                                new_atk = new_atk // C.ELEMENT_BONUS
                                print (a_pc.user, "resists the attack of", m_npc.name)
                if "Revive" in a_pc.effect:
                        if a_pc.upgrade > 0:
                                if new_atk - p_pc.defbonus - p_pc.defense >= p_pc.health and a_pc.strength > 0:
                                        new_atk = 0
                                        a_pc.strength -= p_pc.health // a_pc.upgrade
                                        print (a_pc.user, "narrowly escapes death. ")
                        else:
                                if new_atk - p_pc.defbonus - p_pc.defense >= p_pc.health and a_pc.strength > 0:
                                        new_atk = 0
                                        a_pc.strength -= p_pc.health
                                        print (a_pc.user, "narrowly escapes death. ")

                if "Charm" in a_pc.effect:
                        x = random.randint(0, m_npc.skill)
                        if x < a_pc.strength:
                                new_atk = 0
                                a_pc.strength -= 1
                                print ("The smell of ", a_pc.name, "seems to distract ", m_npc.name)
                        else:
                                m_npc.skill -= min(1, m_npc.skill)
                if "Chill" in a_pc.effect:
                        m_npc.health -= a_pc.strength
                        m_npc.atk -= min(a_pc.strength, m_npc.atk)
                        m_npc.defense -= min(a_pc.strength, m_npc.defense)
                        m_npc.skill -= min(a_pc.strength, m_npc.skill)
                        print ("Contact with ", a_pc.name, "chills ", m_npc.name)
                        
        return new_atk

def weapon_effect(m_npc, p_pc, w_pc, h_p, m_p):
        if w_pc == None:
                new_atk = p_pc.atk
        else:
                new_atk = p_pc.atk + w_pc.atk
                if "Attack" in w_pc.effect:
                        if w_pc.upgrade > 0:
                                new_atk += w_pc.strength  * w_pc.upgrade
                        else:
                                new_atk += w_pc.strength

                if "Death" in w_pc.effect and w_pc.element == "Dark":
                        x = random.randint(0, max(m_npc.health, m_npc.skill))
                        if w_pc.upgrade > 0:
                                if x < w_pc.strength * w_pc.upgrade:
                                        new_atk += min(C.DEATH_ATK, m_npc.health)
                                        print ("Death comes for", m_npc.name)
                        else:
                                if x < w_pc.strength:
                                        new_atk += min(C.DEATH_ATK, m_npc.health)
                                        print ("Death comes for", m_npc.name)                

                if "Lifesteal" in w_pc.effect:
                        if w_pc.upgrade > 0:
                                x = max(p_pc.atk + p_pc.atkbonus + w_pc.atk - m_npc.defense, 0)
                                p_pc.health += round(x ** C.DECREASE_EXPONENT) + (w_pc.strength * w_pc.upgrade)
                                p_pc.health = min(p_pc.health, p_pc.maxhealth)
                                print (w_pc.user, "drains the life of ", m_npc.name)
                        else:
                                x = max(p_pc.atk + p_pc.atkbonus + w_pc.atk - m_npc.defense, 0)
                                p_pc.health += round(x ** C.DECREASE_EXPONENT) + w_pc.strength
                                p_pc.health = min(p_pc.health, p_pc.maxhealth)
                                print (w_pc.user, "drains the life of ", m_npc.name)

                if "ManaDrain" in w_pc.effect:
                        if w_pc.upgrade > 0:
                                p_pc.mana += round((w_pc.strength * w_pc.upgrade) ** C.DECREASE_EXPONENT)
                                if m_npc.element == w_pc.element:
                                        p_pc.mana += round((w_pc.strength * w_pc.upgrade) ** C.DECREASE_EXPONENT)
                                        print (w_pc.user, "drains the energy of ", m_npc.name)
                        else:
                                p_pc.mana += round(w_pc.strength ** C.DECREASE_EXPONENT)
                                if m_npc.element == w_pc.element:
                                        p_pc.mana += round(w_pc.strength ** C.DECREASE_EXPONENT)
                                        print (w_pc.user, "drains the energy of ", m_npc.name)

                if "Poison" in w_pc.effect:
                        if w_pc.upgrade > 0:
                                m_npc.poison += w_pc.strength * w_pc.upgrade
                                m_npc.health -= m_npc.poison
                                print (w_pc.user, "poisons", m_npc.name)
                        else:
                                m_npc.poison += w_pc.strength
                                m_npc.health -= m_npc.poison
                                print (w_pc.user, "poisons", m_npc.name)
                                
                if "Lucky" in w_pc.effect:
                        x = random.randint(0, m_npc.skill)
                        if w_pc.upgrade > 0:
                                if x <= w_pc.strength * w_pc.upgrade:
                                        new_atk = (p_pc.atk + p_pc.atkbonus) * C.CRIT
                                        print (w_pc.user, "gets a lucky critical hit! ")
                        else:
                                if x <= w_pc.strength:
                                        new_atk = (p_pc.atk + p_pc.atkbonus) * C.CRIT
                                        print (w_pc.user, "gets a lucky critical hit! ")
                                        
                if "SkillDrain" in w_pc.effect:
                        if w_pc.upgrade > 0:
                                if w_pc.strength > 0:
                                        m_npc.skill -= min(round(w_pc.strength ** C.DECREASE_EXPONENT),
                                                           m_npc.skill)
                                        p_pc.skill += w_pc.strength
                                        w_pc.strength -= 1
                                        print (w_pc.user, "drains the energy of ", m_npc.name)
                                elif w_pc.strength <= 0:
                                        w_pc.strength += w_pc.upgrade
                                        w_pc.upgrade -= 1
                        else:
                                if w_pc.strength > 0:
                                        m_npc.skill -= min(round(w_pc.strength ** C.DECREASE_EXPONENT),
                                                           m_npc.skill)
                                        p_pc.skill += w_pc.strength
                                        w_pc.strength -= 1
                                        print (w_pc.user, "drains the energy of ", m_npc.name)
                                elif w_pc.strength <= 0:
                                        p_pc.skill += 1
                                        
                if "Slay Fire" in w_pc.effect:
                        if m_npc.element == "Fire":
                                new_atk = (p_pc.atk + p_pc.atkbonus)  * C.ELEMENT_BONUS
                                print (w_pc.user, "performs a super effective hit against", m_npc.name)
                if "Slay Water" in w_pc.effect:
                        if m_npc.element == "Water":
                                new_atk = (p_pc.atk + p_pc.atkbonus) * C.ELEMENT_BONUS
                                print (w_pc.user, "performs a super effective hit against", m_npc.name)
                if "Slay Earth" in w_pc.effect:
                        if m_npc.element == "Earth":
                                new_atk = (p_pc.atk + p_pc.atkbonus) * C.ELEMENT_BONUS
                                print (w_pc.user, "performs a super effective hit against", m_npc.name)
                if "Slay Air" in w_pc.effect:
                        if m_npc.element == "Air":
                                new_atk = (p_pc.atk + p_pc.atkbonus) * C.ELEMENT_BONUS
                                print (w_pc.user, "performs a super effective hit against", m_npc.name)
                if "Slay Dark" in w_pc.effect:
                        if m_npc.element == "Dark":
                                new_atk = (p_pc.atk + p_pc.atkbonus) * C.ELEMENT_BONUS
                                print (w_pc.user, "performs a super effective hit against", m_npc.name)
                if "Explode" in w_pc.effect:
                        if w_pc.upgrade > 0:
                                for mon in m_p:
                                        mon.health -= w_pc.strength * w_pc.upgrade
                                p_pc.health -= w_pc.strength * w_pc.upgrade
                                print (w_pc.user, "performs an explosive attack on the enemy. ")
                        else:
                                for mon in m_p:
                                        mon.health -= w_pc.strength
                                p_pc.health -= w_pc.strength
                                print (w_pc.user, "performs an explosive attack on the enemy. ")

                if "Summon" in w_pc.effect and w_pc.user == "Summoner":
                        if w_pc.upgrade > 0:
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
                        else:
                                if w_pc.strength > 0:
                                        summon = Player_PC("Homunculus", 1,
                                                           w_pc.strength ** C.INCREASE_EXPONENT,
                                                           w_pc.strength ** C.INCREASE_EXPONENT,
                                                           w_pc.strength,
                                                           w_pc.strength,
                                                           0, 0, 0)
                                        h_p.append(summon)
                                        w_pc.strength = 0
                                        print (w_pc.user, "creates", summon.name)
                                elif w_pc.strength <= 0:
                                        w_pc.atk += w_pc.upgrade
                #the hidden dagger weapon lets the ninja perform another sneak attack
                if "Hidden Dagger" in w_pc.effect and w_pc.user == "Ninja":
                        if w_pc.upgrade > 0:
                                if w_pc.atk == 0 and w_pc.strength > 0:
                                        w_pc.atk += w_pc.strength * w_pc.upgrade
                                        w_pc.strength = 0
                        else:
                                if w_pc.atk == 0 and w_pc.strength > 0:
                                        w_pc.atk += w_pc.strength
                                        w_pc.strength = 0
                #the healing staff lets the cleric heal while attacking
                if "Heal" in w_pc.effect and w_pc.user == "Cleric":
                        if w_pc.upgrade > 0:
                                hero = party_func.pick_lowest_health(h_p)
                                hero.health += (w_pc.strength * w_pc.upgrade) + p_pc.skill
                                print (w_pc.user, "heals", hero.name)
                        else:
                                hero = party_func.pick_lowest_health(h_p)
                                hero.health += w_pc.strength + p_pc.skill
                                print (w_pc.user, "heals", hero.name)
                if "Shield" in w_pc.effect and w_pc.user == "Knight":
                        if w_pc.strength > 0:
                                p_pc.name = "Defender"
                                w_pc.user = "Defender"
                                w_pc.strength -= 1
                                print (p_pc.name, "gets ready to block. ")
                #necromancer lets you revive an enemy that you're about to defeat
                #the undead is meant to be a strong beater but very tanky
                if "Necromancer" in w_pc.effect:
                        x = m_npc.health - (new_atk + p_pc.atkbonus - m_npc.defense)
                        if w_pc.upgrade > 0:
                                if x <= 0 and w_pc.strength > 0:
                                        undead = Player_PC("Undead", 1,
                                                           m_npc.health,
                                                           m_npc.health,
                                                           m_npc.atk * w_pc.strength * w_pc.upgrade,
                                                           0, 0, 0, 0)
                                        h_p.append(undead)
                                        w_pc.strength -= 1
                        else:
                                if x <= 0 and w_pc.strength > 0:
                                        undead = Player_PC("Undead", 1,
                                                           m_npc.health,
                                                           m_npc.health,
                                                           m_npc.atk * w_pc.strength,
                                                           0, 0, 0, 0)
                                        h_p.append(undead)
                                        w_pc.strength -= 1

                if "Command" in w_pc.effect and "Hero" in w_pc.user:
                        if w_pc.strength > 0:
                                for hero in h_p:
                                        hero.skill += w_pc.strength
                                w_pc.strength -= 1
                                print ("The Hero's presence encourages their allies. ")
                        else:
                                w_pc.strength += 1
                if "Scorch" in w_pc.effect:
                        x = m_npc.health - (new_atk + p_pc.atkbonus - m_npc.defense)
                        if x <= 0 and w_pc.strength > 0:
                                m_p.remove(m_npc)
                                print (w_pc.user, "burns ", m_npc.name, "into ashes. ")
                                w_pc.strength -= 1
                if "Slime Copy" in w_pc.effect:
                        if w_pc.strength > 0:
                                copy_hero = Player_PC(p_pc.name, 1, w_pc.strength,
                                                      w_pc.strength ** C.INCREASE_EXPONENT,
                                                      0, 0, 0, 0, 0)
                                w_pc.strength = 0
                                h_p.append(copy_hero)
                                print (w_pc.user, "summons a slime copy of themselves. ")
                if "Observer" in w_pc.name:
                        for mon in m_p:
                                mon.stats()
                                
        return new_atk
