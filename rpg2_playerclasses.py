import sys
sys.path.append(".")
from rpg2_classdefinitions import Player_PC
##classes that the player can control
#warrior is someone who focuses more on physical attacks than magical ones
#p = Player_PC(name, level, health, maxhealth, atk, defense, skill, mana,
#               atkbonus, defbonus, weapon, armor)
#warrior focuses on high output single target damage
warrior = Player_PC("Warrior", 1, 15, 15, 5, 3, 0, 0, 0, 0, 2, 1)
#mage focuses more on aoe damage
#the mage has starting mana and gains mana every level
mage = Player_PC("Mage", 1, 10, 10, 2, 2, 0, 5)
#cleric focuses more on healing magic, buffs and debuffs
#clerics are blessed and get lots of benefits
cleric = Player_PC("Cleric", 1, 10, 10, 3, 2, 0, 5)
#summoner is someone who binds themselves to a monster
#the summoner mostly relies on their ally to provide aoe buffs or debuffs
summoner = Player_PC("Summoner", 1, 10, 10, 2, 2, 0, 0)
angel = Pet_NPC("Angel", 1, 2)
#ninja focuses on using weapons self-buffs and skills
#ninja has high burst single target damage but needs setting up
ninja = Player_PC("Ninja", 1, 10, 10, 3, 3, 5, 0, 0, 0, 2)
