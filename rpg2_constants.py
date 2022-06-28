class Constants:
     def __init__(self):
             ##constants
             #limit to the amount of heroes in the party
             self.PARTY_LIMIT = 3
             #level limit for heroes
             self.LEVEL_LIMIT = 10
             #base price of leveling up
             self.LEVEL_PRICE = 100
             #exponent to scale the difficulty of increasing levels/stats
             self.INCREASE_EXPONENT = 2
             #level limit for pets
             self.STAGE_LIMIT = 5
             #how often the pet gets more actions
             self.PET_ACTION_UP = 2
             #base price for weapons
             self.WEAPON_PRICE = 10
             #base price for armor
             self.ARMOR_PRICE = 100
             #types of elements
             self.ELEMENTS_LIST = ["Fire", "Water", "Earth", "Air", "Light", "Dark"]
             #types of monsters
             self.MONSTER_NAMES_LIST = ["Demon", "Slime", "Skeleton", "Beast"]
             #max health for basic monster
             self.MONSTER_MAX_HP = 75
             #min health for basic monster
             self.MONSTER_MIN_HP = 15
             #max atk for basic monster
             self.MONSTER_MAX_ATK = 25
             #min atk for basic monster
             self.MONSTER_MIN_ATK = 7
             #max def for basic monster
             self.MONSTER_MAX_DEF = 15
             #min def for basic monster
             self.MONSTER_MIN_DEF = 3
             #max skill for basic monster
             self.MONSTER_MAX_SKILL = 10
             #max dropchance for basic monster
             self.MONSTER_MAX_DROPCHANCE = 10
             #critical hit bonus
             self.CRIT = 1.5
             #healing potion modifier
             #divides max health and adds it to current health
             self.HEAL_POTION = 2

C = Constants()
