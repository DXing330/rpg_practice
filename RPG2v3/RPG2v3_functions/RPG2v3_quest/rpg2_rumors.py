import copy
import random
import sys
sys.path.append("../RPG2v3_def")
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

#function that gives rumors to the player
#if they're interested they can be given items to follow up
def rumors(ib_pc, q_i, a_i):
        x = random.randint(0, a_i.rank)
        if x <= 5:
                print ("Rumors? Leave me alone! I'm trying to drink in peace. ")
        #after you beat the demon king you can hear about the hidden boss the dragon
        elif x == 100 and q_i.dktrophy > 0:
                print ("They say there's a dragon somewhere far away. ")
                print ("I heard that it's way stronger than the Demon King. ")
                print ("How far? Further than you've ever gone before, that's for sure. ")
                if q_i.dscale == 0 and q_i.dktrophy > 0:
                        print ("Proof? Why should I bother...? Wait, are you the legendary hero?! ")
                        print ("Sorry, sir.  Here, take this. It's said to be one of it's scales. ")
                        print ("Test it if you want, it's harder than anything. ")
                        q_i.dscale += 1
        #after you're a legendary hero you can hear about the location of the demon king
        #after you gather the map pieces they tell you the location
        #someone will inform you that you can find the castle now
        elif x == 50 and q_i.dkmap == 4:
                print ("A hooded figure approaches you. ")
                print ("'Looks like you're ready for your final journey.' ")
                print ("'Follow the map and go when you're ready.' ")
                print ("After looking behind you to try to see their face, there's no one there. ")

        #you'll also need to go through the demon king questline
        #collect the map pieces
        elif x == 50 and q_i.dkkey == 1:
                print ("They said they found the Demon King's castle. ")
                print ("But it's protected by a giant gate that no one can get through. ")
                if q_i.dkmap < 4:
                        print ("Where is it?  I don't know, the guy was drawing a map but I don't understand it.")
                        print ("Here, you can take a copy if you want, I don't know what good it'll be though. ")
                        q_i.dkmap += 1
        elif x == 25 and q_i.dkamulet == 0:
                #after you're strong enough people will ask for your help in defeating the demon king
                print ("Hey, you're that new big-shot monster hunter, right? ")
                print ("We're not looking to fight, we want your help. ")
                choice = input("YES/NO? Y/N? ")
                if choice.upper() == "Y":
                        print ("We won't talk here.  But take this. ")
                        print ("Come to our base later, use that to get entry. ")
                        print ("They give you an amulet. ")
                        q_i.dkamulet = 1
                else:
                        print ("If you change your mind, we'll be around. ")
        elif x == 12:
                #after you're rich and strong, people will try to scam you
                print ("Hey, you're that new big-shot monster hunter, right? ")
                print ("We're not looking to fight, we want your help. ")
                choice = input("YES/NO? Y/N? ")
                if choice.upper() == "Y":
                        print ("We're in a tough spot and we could really use some help... ")
                        give = input("YES/NO? ")
                        if give.upper() == "Y":
                                print ("Thanks, you're a live saver. ")
                                ib_pc.coins -= min(C.CHARITY, ib_pc.coins)
                                a_i.posrep += 1
                                x = random.randint(0, negrep)
                                if x >= 0:
                                        print ("Someone runs up from behind and grabs your coins. ")
                                        ib_pc.coins -= min(C.THIEF, ib_pc.coins)
                        elif give.upper() == "N":
                                print ("Hmph, another stuck up hunter, looking down on us regular folk. ")
                                a_i.negrep += 1
                                x = random.randint(0, negrep)
                                if x >= 0:
                                        print ("After they disappear into the crowd, you notice your coin purse is lighter. ")
                                        ib_pc.coins -= min(C.THIEF, ib_pc.coins)
                elif choice.upper() == "N":
                        print ("You don't even bother to hear us out? ")
                        a_i.negrep += 1
        elif x == 11:
                #some people will ask you for help
                print ("Hey, you're that new big-shot monster hunter, right? ")
                print ("We're not looking to fight, we want your help. ")
                choice = input("YES/NO? Y/N? ")
                if choice.upper() == "Y":
                        print ("My daughter got hurt recently and we need a healing potion... ")
                        give = input("YES/NO? ")
                        if give.upper() == "Y" and ib_pc.heal > 0:
                                print ("Thanks, you're a live saver. ")
                                ib_pc.heal -= min(C.CHARITY, ib_pc.heal)
                                a_i.posrep += 1
                        elif give.upper() == "Y" and ib_pc.heal == 0:
                                print ("Is it fun to play with my feelings?! ")
                                a_i.negrep += 1
                        elif give.upper() == "N" and ib_pc.heal == 0:
                                print ("I guess you're working hard just taking care of yourself... ")
                        elif give.upper() == "N" and ib_pc.heal > 0:
                                print ("Why bother fighting monsters if you're just going to leave us to die anyway? ")
                                a_i.negrep += 1
                elif choice.upper() == "N":
                        print ("I guess you're too busy. ")
        else:
                rumors(ib_pc, q_i, a_i)
                                        
