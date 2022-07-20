import copy
import random
import sys
sys.path.append("./RPG2v3_def")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
                                   Spell_PC, Monster_NPC, Weapon_PC,
                                   Armor_PC, QuestItems_NPC, Access_NPC)
import rpg2_party_management_functions as party_func
from rpg2_constants import Constants
from rpg2_constant_lists import List_Constants
from rpg2_constant_quests import Q_Constants
Q = Q_Constants()
L = List_Constants()
C = Constants()
sys.path.append("./RPG2v3_quest")
import rpg2_rumors as rumors_func
        
        
#function that gives the player a tutorial
def tutorial():
        print ("What do you want to know about? ")
        choice = input("HEROES, CITY, mage TOWER, MONSTERS, NOTHING ")
        if choice.upper() == "N":
                print ("Come back anytime. ")
        elif choice.upper() == "H":
                check = input("EQUIPMENT, HEROES")
                if check.upper() == "H":
                        hero = input("HERO, CLERIC, KNIGHT, MAGE, NINJA, SUMMONER, TACTICIAN, WARRIOR")
                        if hero.upper() == "H":
                                print ("The Hero is good at everything. He can attack like a warrior. ",
                                       "He can cast spells like a mage. He is beloved by the spirits like a summoner. ")
                        elif hero.upper() == "C":
                                print ("The cleric is good at Healing their allies. ",
                                       "They are also good at Debuffing their enemies. ")
                        elif hero.upper() == "K":
                                print ("The knight is good at Protecting their allies. ",
                                       "They have a big shield and are very tough. ")
                        elif hero.upper() == "M":
                                print ("The mage is good at casting Magic.")
                        elif hero.upper() == "N":
                                print ("The ninja is good at Observing their enemies. ",
                                       "With a WEAPON, they can do a deadly Sneak Attack.",
                                       "It only works once though, after that the enemies will be wary. ")
                        elif hero.upper() == "S":
                                print ("The summoner is good at Commanding the Guardian Angel. ",
                                       "The summoner can also make Totems that will help it give commands.")
                        elif hero.upper() == "T":
                                print ("The tactician is good at Commanding their allies. ",
                                       "They are also good at Observing the enemy. ")
                        elif hero.upper() == "W":
                                print ("The warrior is good at Attacking. ")
                elif check.upper() == "E":
                        print ("You can equip weapons and armors to your team. ",
                               "Some of them may even have special effects. ",
                               "For example, 'POISON' will make the enemies poisoned.",
                               "The damage will slowly add up and take down even the toughest of foes. ")
                tutorial()
        elif choice.upper() == "C":
                check = input("INN, PRACTICE ARENA, STORES")
                if check.upper() == "I":
                        print ("You can rest and recover at the inn. ",
                               "You can meet or say farewell to allies there too. ",
                               "You can change equipment there too. ")
                elif check.upper() == "P":
                        print ("You can train here to become stronger. ",
                               "It costs a bit though. ")
                elif check.upper() == "S":
                        print ("You can buy potions in the stores. ",
                               "Healing ones heal your health, mana ones heal you mana. ",
                               "Buffing ones make you stronger for awhile. ")
                        print ("You can also buy weapons and armors here.",
                               "They're just basic ones though.",
                               "You can also upgrade your equipment here. ",
                               "It costs quite a lot though. ")
                tutorial()
        elif choice.upper() == "T":
                check = input("ALLIES, ENCHANTING, SPELLS")
                if check.upper() == "A":
                        print ("They have an experienced spiritualist that can help you bond with your guardian angel. ",
                               "They can also help you strength your bond. ",
                               "It costs a bit though. ")
                elif check.upper() == "E":
                        print ("They have an experienced enchanter, that can enchant your equipment. ",
                               "They can give it a new element or effect or both. ")
                elif check.upper() == "S":
                        print ("That have an experienced mage, that can train your magic.",
                               "Before that, you should visit their library to learn some spells. ",
                               "Did you know you can name a spell whatever you want ?")
                tutorial()
        elif choice.upper() == "M":
                print ("Monsters are nasty evil things.  No matter how many we drive away more just keep coming. ",
                       "Mostly they're manageable but some are very strong.",
                       "If you Listen to the villagers you might hear rumors of strong monsters. ",
                       "They say that stronger monsters sometimes have special treasures. ")
                tutorial()
        else:
                tutorial()
                

#function that controls the tavern
def tavern(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i):
        print ("What would you like to do? ")
        choice = input("RUMORS/TUTORIAL? R/T ")
        if choice.upper() == "T":
                tutorial()
        elif choice.upper() == "R":
                rumors_func.rumors(ib_pc, q_i, a_i)
