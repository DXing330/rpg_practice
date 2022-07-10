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
             #exponent to scale the difficulty of increasing levels/stats
             self.INCREASE_EXPONENT = 2
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
             self.PET_HP_BUFF = 0.2
             #how much the pet buff affects atk
             self.PET_ATK_BUFF = 0.15
             #how much the pet buff affects defense
             self.PET_DEF_BUFF = 0.1
             #how much the pet buff affects skill
             self.PET_SKILL_BUFF = 0.05
             #base price for weapons
             self.WEAPON_PRICE = 10
             #base price for armor
             self.ARMOR_PRICE = 100
             #types of elements
             self.ELEMENTS_LIST = ["Fire", "Water", "Earth", "Air", "Dark"]
             self.FULL_ELEMENTS_LIST = ["Fire", "Water", "Earth", "Air", "Light", "Dark"]
             #types of monsters
             self.MONSTER_NAMES_LIST = ["Demon", "Slime", "Skeleton", "Beast", "Elemental"]
             #potential health increase per level for basic monster
             self.MONSTER_SCALE_HP = 20
             #max health for basic monster
             self.MONSTER_MAX_HP = 300
             #potential attack increase per level for basic monster
             self.MONSTER_SCALE_ATK = 7
             #max atk for basic monster
             self.MONSTER_MAX_ATK = 75
             #potential defense increase per level for basic monster
             self.MONSTER_SCALE_DEF = 2
             #max def for basic monster
             self.MONSTER_MAX_DEF = 30
             #max skill for basic monster
             self.MONSTER_MAX_SKILL = 10
             #minimum stats for basic monster
             self.MONSTER_MIN_HP = 10
             self.MONSTER_MIN_ATK = 5
             self.MONSTER_MIN_DEF = 1
             #max dropchance for basic monster
             self.MONSTER_MAX_DROPCHANCE = 5
             #critical hit bonus
             self.CRIT = 1.5
             #buff bonus
             self.BUFF = 1.2
             #healing potion modifier
             #divides max health and adds it to current health
             self.HEAL_POTION = 2
             #base price for a new spell
             self.SPELL_PRICE = 10
             #minimum cost to cast a spell
             self.SPELL_COST = 1

C = Constants()
