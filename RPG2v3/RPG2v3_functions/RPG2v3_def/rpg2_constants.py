import sys
sys.path.append(".")
from rpg2_constant_lists import List_Constants
L = List_Constants()
class Constants:
     def __init__(self):
             ##constants
             #limit to the amount of heroes in the party
             self.PARTY_LIMIT = 4
             #soft limits amount of monsters in the party
             self.MONSTER_PARTY_LIMIT = 30
             #level limit for heroes
             self.LEVEL_LIMIT = 10
             #base price of leveling up
             self.LEVEL_PRICE = 10
             #base price of going into a prestige class
             self.PRESTIGE_PRICE = 1000
             #price of increasing skill, mana, and defense
             self.STAT_PRICE = 20
             #exponent to scale the difficulty of increasing levels/stats
             self.INCREASE_EXPONENT = 2
             self.DECREASE_EXPONENT = 0.5
             #highest price in a function
             self.PRICE_LIMIT = 1000000
             #highest price to increase a stats
             self.STAT_PRICE_LIMIT = 1000000
             #highest price to increase health
             self.HEALTH_PRICE_LIMIT = 100000
             #level limit for pets
             self.STAGE_LIMIT = 6
             #how often the pet gets more actions
             self.PET_ACTION_UP = 2
             #pet multipliers
             #how much the pet atk increased per level
             self.PET_ATK_UP = 0.5
             #how much the pet buff affects maxhealth
             self.PET_HP_BUFF = 0.8
             #how much the pet buff affects atk
             self.PET_ATK_BUFF = 0.5
             #how much the pet buff affects defense
             self.PET_DEF_BUFF = 0.34
             #how much the pet buff affects skill
             self.PET_SKILL_BUFF = 0.25
             #base price for weapons
             self.WEAPON_PRICE = 10
             #base price for armor
             self.ARMOR_PRICE = 30
             #element bonus
             self.ELEMENT_BONUS = 2
             #potential health increase per level for basic monster
             self.MONSTER_SCALE_HP = 20
             #max health for basic monster
             self.MONSTER_MAX_HP = 300
             #potential attack increase per level for basic monster
             self.MONSTER_SCALE_ATK = 7
             #max atk for basic monster
             self.MONSTER_MAX_ATK = 100
             #potential defense increase per level for basic monster
             self.MONSTER_SCALE_DEF = 2
             #max def for basic monster
             self.MONSTER_MAX_DEF = 20
             #max skill for basic monster
             self.MONSTER_MAX_SKILL = 10
             #minimum stats for basic monster
             self.MONSTER_MIN_HP = 10
             self.MONSTER_MIN_ATK = 5
             self.MONSTER_MIN_DEF = 1
             #max dropchance for basic monster
             self.MONSTER_MAX_DROPCHANCE = 5
             self.MONSTER_MAX_DC = 5
             #critical hit bonus
             self.CRIT = 2
             #buff bonus
             self.BUFF = 1.2
             #healing potion modifier
             #divides max health and adds it to current health
             self.HEAL_POTION = 2
             #base price for a new spell
             self.SPELL_PRICE = 10
             #minimum cost to cast a spell
             self.SPELL_COST = 1
             #base price for enchanting
             self.ENCHANT_PRICE = 100
             #price for potion
             self.POTION_PRICE = 10
             #death weapon effect atk bonus
             self.DEATH_ATK = 9999999
             #bomb trap explosion damage
             self.BOMB_DAMAGE = 100
             #stat increase per level up
             self.LVL_UP_HP_LOW = 10
             self.LVL_UP_HP_MID = 15
             self.LVL_UP_HP_HIGH = 20
             self.LVL_UP_ATK_LOW = 1
             self.LVL_UP_ATK_MID = 3
             self.LVL_UP_ATK_HIGH = 5
             self.LVL_UP_DEF_LOW = 2
             self.LVL_UP_DEF_MID = 3
             self.LVL_UP_DEF_HIGH = 4
             self.LVL_UP_SKL_LOW = 3
             self.LVL_UP_SKL_MID = 4
             self.LVL_UP_SKL_HIGH = 5
             self.LVL_UP_MANA_LOW = 3
             self.LVL_UP_MANA_MID = 4
             self.LVL_UP_MANA_HIGH = 5
             #random event stuff
             self.CHARITY = 100
             self.THIEF = 10000
             #monster buffs
             self.DMG_A = 100
             self.DMG_B = 500

C = Constants()
