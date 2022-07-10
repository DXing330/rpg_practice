import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Monster_NPC)
from rpg2_constants import Constants
from rpg2_boss_constants import BOSS_CONSTANTS
C = Constants()
B = BOSS_CONSTANTS()

Demon_General = Monster_NPC("Demon General", B.DEMON_GENERAL_HEALTH, B.DEMON_GENERAL_ATK,
                            B.DEMON_GENERAL_DEFENSE, B.DEMON_GENERAL_SKILL, "DARK",
                            B.DEMON_GENERAL_DROPCHANCE)
Demon_Lord = Monster_NPC("Demon Lord", B.DEMON_LORD_HEALTH, B.DEMON_LORD_ATK,
                            B.DEMON_LORD_DEFENSE, B.DEMON_LORD_SKILL, "DARK",
                            B.DEMON_LORD_DROPCHANCE)
#function where the monster performs an action
def demon_boss_action(m_npc, p_pc):
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
                                p_pc.health -= max(m_npc.atk, 1)
                                print (m_npc.name, "does a piercing attack against", p_pc.name)
                        elif y == 2:
                                #monster does a strong attack
                                p_pc.health -= max(round(((m_npc.atk*C.CRIT) - p_pc.defense - p_pc.defbonus - p_pc.armor),0), 1)
                                print (m_npc.name, "does a strong attack against", p_pc.name)
                        elif y == 3:
                                #monster will buff themselves
                                m_npc.atk = round(m_npc.atk * C.BUFF, 0) + m_npc.skill
                                m_npc.defense = round(m_npc.defense * C.BUFF, 0)
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
