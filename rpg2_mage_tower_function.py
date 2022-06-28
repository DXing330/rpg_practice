import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC)
import rpg2_party_management_functions as party_func
import rpg2_level_up_function as lvlup_func
from rpg2_constants import Constants
C = Constants()
angel = Pet_NPC("Angel", 1, 2)
##functions in the tower


#function that will allow the pet to be trained and evolved
def summoning_fields(h_p, p_npc, ib_pc):
        p_npc.stats()
        if p_npc.atk == 0:
                print "Looks like you need to summon a new ally."
                for hero in h_p:
                        if hero.name == 'Summoner':
                                print "Here you go, take good care of it."
                                p_npc.name = "Angel"
                                p_npc.stage = 1
                                p_npc.atk = 2
        elif p_npc.stage < C.STAGE_LIMIT:
                print "Aww, what a cute little friend you have."
                print "It looks like it can still get a lot stronger."
                print "Do you want us to help you train it?"
                print "It'll cost you", (p_npc.atk ** p_npc.stage), "coins."
                choice = raw_input("Y/N? ")
                if choice.upper() == "Y" and ib_pc.coins >= (p_npc.atk ** p_npc.stage):
                        ib_pc.coins -= (p_npc.atk ** p_npc.stage)
                        lvlup_func.stage_up(p_npc)
                        print "Whew, channelling spiritual power always tires me out."
                        print "Your ally looks much stronger now."
                else:
                        print "Come back when you're ready."
        elif p_npc.stage == C.STAGE_LIMIT:
                print "That's a mighty strong looking ally you have."
                print "Do you want me to try to strengthen it?"
                print "It'll cost you", (p_npc.atk ** C.INCREASE_EXPONENT), "coins."
                choice = raw_input("Y/N? ")
                if choice.upper() == "Y" and ib_pc.coins >= (p_npc.atk ** C.INCREASE_EXPONENT):
                        ib_pc.coins -= (p_npc.atk ** C.INCREASE_EXPONENT)
                        lvlup_func.pet_atk_up(p_npc)
                else:
                        print "Come back when you're ready."
                        
#UI function where the player chooses what to do
def mage_tower(h_p, p_npc, ib_pc, h_m):
        print "Oh, adventurers. Welcome. What do you need? "
        print ("Would you like to visit our LIBRARY?",
               "Or perhaps you want to hire a TUTOR?",
               "If you have a SUMMONED ALLY we can train it as well.")
        choice = raw_input("L/S/T?")
        if choice.upper() == "S":
                summoning_fields(h_p, p_npc, ib_pc)
        elif choice.upper() == "L":
                print "Sorry, I just heard its been updated, come back soon."
        elif choice.upper() == "T":
                print "Sorry, it seems they're all already booked, come back soon."
        else:
                mage_tower(h_p, p_npc, ib_pc, h_m)
                
