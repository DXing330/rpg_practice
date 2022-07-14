import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC, Weapon_PC,
                                   Armor_PC)
import rpg2_party_management_functions as party_func
from rpg2_constants import Constants
C = Constants()

monster_party = []
heroes_party = []
heroes_magic = []
heroes_weapons = []
heroes_armor = []
heroes_bag = ItemBag_PC(1, 1, 1, 10)
fireball = Spell_PC("Fireball", 3, 3, "Fire", 11)
rainstorm = Spell_PC("Rainstorm", 2, 3, "Water", 6)
earthspike = Spell_PC("Earthspike", 3, 1, "Earth", 4)
mage = Player_PC("Mage", 1, 10, 10, 2, 2, 0, 5)
warrior = Player_PC("Warrior", 1, 15, 15, 5, 3, 0, 0)
cleric = Player_PC("Cleric", 1, 10, 10, 1, 2, 0, 5)
summoner = Player_PC("Summoner", 1, 10, 10, 2, 2, 0, 0)
knight = Player_PC("Knight", 20, 20, 4, 4, 0, 0)
ninja = Player_PC("Ninja", 1, 10, 10, 3, 3, 5, 0)
heroes_pet = Pet_NPC("Angel", 1, 2)
firemon = Monster_NPC("Mon", 100, 0, 0, 0, "Fire", 0)
watermon = Monster_NPC("Mon", 100, 0, 0, 0, "Water", 0)
earthmon = Monster_NPC("Mon", 100, 0, 0, 0, "Earth", 0)
nonemon = Monster_NPC("Nonemon", 0, 0, 0, 0, "None", 0)
armor = Armor_PC("None", "None", "None", 0, "None", 0)
weapon = Weapon_PC("None", "None", "None", 0, "None", 0)
heroes_magic.append(fireball)
heroes_magic.append(rainstorm)
heroes_magic.append(earthspike)
heroes_party.append(knight)
heroes_party.append(warrior)
heroes_party.append(ninja)
monster_party.append(firemon)
monster_party.append(watermon)
monster_party.append(earthmon)

battle_phase(heroes_party, monster_party, heroes_pet, heroes_bag, heroes_magic)
