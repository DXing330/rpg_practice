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
                self.DEMON_LORD_HEALTH = 5000
                self.DEMON_LORD_ATK = 200
                self.DEMON_LORD_DEFENSE = 60
                self.DEMON_LORD_SKILL = 20
                self.DEMON_LORD_DROPCHANCE = 100000
                self.D_L_SPAWN = 10
                self.GOLDEN_SLIME_HEALTH = 100000
                self.G_S_H = 100000
                self.GOLDEN_SLIME_ATK = 0
                self.GOLDEN_SLIME_DEFENSE = 0 
                self.GOLDEN_SLIME_SKILL = 0
                self.GOLDEN_SLIME_DROPCHANCE = 1000000
                self.G_S_EXECUTE_TIMER = 20
                self.G_S_DC_DOWN = 1000
                self.ACID_HYDRA_HEALTH = 10000
                self.A_H_HEALTH = 10000
                self.A_H_ATK = 1
                self.A_H_DEF = 1
                self.A_H_SKL = 1
                self.A_H_DC = 1
