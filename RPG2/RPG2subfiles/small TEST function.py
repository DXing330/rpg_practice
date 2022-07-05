import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC)
import rpg2_party_management_functions as party_func
from rpg2_constants import Constants
C = Constants()
new_spell = Spell_PC("new", 0, 1, None, 0)
#function that will allow the player to increase their spell's stats
def upgrade_magic(ib_pc, h_m):
        ib_pc.stats()
        for spell in h_m:
                spell.stats()
        print ("Alright, which spell should I help you practice? ")
        try:
                x = int(input("First spell is 1, etc, etc. "))
                spel = h_m[(x - 1)]
                print ("That spell?  Alright, what part do you want to improve? ")
                choice = input("Power, Targets, Cost? P/T/C? ")
                if choice.upper() == "T" and spel.targets == 1 and ib_pc.coins >= (C.SPELL_PRICE ** C.INCREASE_EXPONENT):
                        ib_pc.coins -= (C.SPELL_PRICE ** C.INCREASE_EXPONENT)
                        spel.targets += 1
                elif choice.upper() == "P" and ib_pc.coins >= (spel.power ** C.INCREASE_EXPONENT):
                        ib_pc.coins -= (spel.power ** C.INCREASE_EXPONENT)
                        spel.power += 1
                        spel.cost += 1
                elif choice.upper() == "C" and ib_pc.coins >= (spel.power ** C.INCREASE_EXPONENT) and spel.cost > C.SPELL_COST:
                        ib_pc.coins -= (spel.power ** C.INCREASE_EXPONENT)
                        spel.cost -= 1
                else:
                        print ("Don't waste my time if you're not prepared. ")
        except (ValueError, AttributeError):
                print ("Don't waste my time if you're not prepared. ")

heroes_magic = []
fireball = Spell_PC("Fireball", 3, 2, "Fire", 11)
rainstorm = Spell_PC("Rainstorm", 2, 2, "Water", 6)
earthspike = Spell_PC("Earthspike", 3, 1, "Earth", 4)
heroes_magic.append(fireball)
heroes_magic.append(rainstorm)
heroes_magic.append(earthspike)
heroes_bag = ItemBag_PC(1, 1, 1, 1000)

upgrade_magic(heroes_bag, heroes_magic)
upgrade_magic(heroes_bag, heroes_magic)
upgrade_magic(heroes_bag, heroes_magic)
upgrade_magic(heroes_bag, heroes_magic)
upgrade_magic(heroes_bag, heroes_magic)
upgrade_magic(heroes_bag, heroes_magic)
upgrade_magic(heroes_bag, heroes_magic)
upgrade_magic(heroes_bag, heroes_magic)
upgrade_magic(heroes_bag, heroes_magic)
