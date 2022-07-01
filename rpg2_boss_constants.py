import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Monster_NPC)
from rpg2_constants import Constants
C = Constants()
class BOSS_CONSTANTS:
        def __init__(self):
                #constants involved in boss battles
                self.DEMON_GENERAL_HEALTH = 1000
                self.DEMON_GENERAL_ATK = 100
                self.DEMON_GENERAL_DEFENSE = 40 
                self.DEMON_GENERAL_SKILL = 15
                self.DEMON_GENERAL_DROPCHANCE = 10000
                self.DEMON_LORD_HEALTH = 10000
                self.DEMON_LORD_ATK = 300
                self.DEMON_LORD_DEFENSE = 80 
                self.DEMON_LORD_SKILL = 30
                self.DEMON_LORD_DROPCHANCE = 100000
