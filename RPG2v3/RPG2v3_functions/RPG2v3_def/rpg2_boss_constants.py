import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Monster_NPC)
from rpg2_constants import Constants
C = Constants()
class BOSS_CONSTANTS:
        def __init__(self):
                #constants involved in boss battles
                self.DEMON_GENERAL_HEALTH = 1500
                self.DEMON_GENERAL_ATK = 100
                self.DEMON_GENERAL_DEFENSE = 40 
                self.DEMON_GENERAL_SKILL = 15
                self.DEMON_GENERAL_DROPCHANCE = 10000
                self.DG_DC = self.DEMON_GENERAL_DROPCHANCE
                self.DEMON_LORD_HEALTH = 5000
                self.DEMON_LORD_ATK = 200
                self.DEMON_LORD_DEFENSE = 60
                self.DEMON_LORD_SKILL = 20
                self.DEMON_LORD_DROPCHANCE = 50000
                self.D_L_SPAWN = 10
                self.GOLDEN_SLIME_HEALTH = 50000
                self.G_S_H = self.GOLDEN_SLIME_HEALTH
                self.GOLDEN_SLIME_ATK = 0
                self.GOLDEN_SLIME_DEFENSE = 0 
                self.GOLDEN_SLIME_SKILL = 0
                self.GOLDEN_SLIME_DROPCHANCE = 100000
                self.G_S_EXECUTE_TIMER = 20
                self.G_S_DC_DOWN = 1000
                self.ACID_HYDRA_HEALTH = 5000
                self.A_H_HEALTH = 5000
                self.A_H_ATK = 1
                self.A_H_DEF = 1
                self.A_H_SKL = 1
                self.A_H_DC = 0.5
                self.A_H_DC_UP = 1.2
                self.ADVANCED_SPAWN = 5
                #succubus queen
                self.S_Q_HEALTH = 5000
                self.S_Q_ATK = 100
                self.S_Q_DEF = 50
                self.S_Q_SKL = 10
                self.S_Q_DC = 30000
                #when the sq enrages
                self.S_Q_HPBP = 0.25
                #ice phoenix
                self.I_P_HEALTH = 6000
                self.I_P_ATK = 100
                self.I_P_DEF = 50
                self.I_P_SKL = 1
                self.I_P_DC = 50000
                self.I_P_L = 3
