import sys
sys.path.append(".")
from rpg2_classdefinitions import Player_PC
##classes that the player can control
#warrior is someone who focuses more on physical attacks than magical ones
#p = Player_PC(name, level, health, maxhealth, atk, defense, skill, mana,
#               atkbonus, defbonus, weapon, armor)
#warrior gets a starting sword and armor so his weapon = 2 and armor = 1
warrior = Player_PC("Warrior", 1, 15, 15, 5, 3, 0, 0, 0, 0, 2, 1)
#mage is someone who focuses more on magical attacks than physical attacks
#the mage has starting mana and gains mana every level
mage = Player_PC("Mage", 1, 10, 10, 2, 2, 0, 5)
#cleric is someone who focuses more on healing magic and buffs
cleric = Player_PC("Cleric", 1, 10, 10, 1, 2, 0, 5)
#summoner is someone who binds themselves to a monster
#the summoner mostly relies on their ally for damage
summoner = Player_PC("Summoner", 1, 10, 10, 2, 2, 0, 0)
angel = Pet_NPC("Angel", 1, 2)
