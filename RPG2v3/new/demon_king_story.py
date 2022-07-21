import copy
import random
import sys
sys.path.append("../RPG2v3_functions/RPG2v3_battle")
sys.path.append("../RPG2v3_functions/RPG2v3_quest")
sys.path.append("../RPG2v3_functions/RPG2v3_def")
from rpg2_classdefinitions import (Player_PC, Monster_NPC,
                                   ItemBag_PC, Spell_PC, Pet_NPC,
                                   Weapon_PC, Armor_PC, QuestItems_NPC,
                                   Access_NPC)
import rpg2_party_management_functions as party_func
from rpg2_constants import Constants
from rpg2_constant_lists import List_Constants
from rpg2_constant_quests import Q_Constants
Q = Q_Constants()
L = List_Constants()
C = Constants()

#function that says the story for the player
#need to keep track of the quest items and access items
def dk_story(qi_npc, a_npc):
    #basic story beats
    #keep track of the stage of the story and the progress
    #as you gain process the story will advance
    #everytime you advance the story the progress resets
    if a_npc.dk_story == 6:
        print ("The hideout is empty. ")
        print ("It seems like the members have been able to move on with their lives. ")
        print ("On the table is an intricate carving showing all the members, with you in the center. ")
        x = random.randint(0, qi_npc.managem + (a_npc.fame ** C.INCREASE_EXPONENT))
        if x == 0:
            print ("As you look closer at the table, you see a letter. ")
            print ("The letter is a thank you to the entire group. ")
            print ("Someone is detailing how much their life has improved since the demon king was slain. ")
            print ("Inside the letter is also a small mana gem. ")
            print ("Apparently they're rich enough now to donate things like this. ")
            gi_npc.managem += 1
    elif a_npc.dk_story == 5:
        if a_npc.dk_story_prog == 0 and qi_npc.dk_trophy == 0:
            print ("As long as the demon king lives they'll never be peace. ")
            print ("We need to find and eliminate him. ")
            print ("Our forces are still hurting from the battles, so we'll need to rely on you again. ")
            print ("I hear some others are looking for him too and sharing information in the taverns. ")
        elif a_npc.dk_story_prog == 0 and qi_npc.dk_trophy == 1:
            print ("I can't believe, you actually did it. ")
            print ("I don't know how to thank you... ")
            print ("I know, I'll write a record for you, and make sure no one ever forgets you. ")
            a_npc.dk_story += 1
    elif a_npc.dk_story == 4:
        if a_npc.dk_story_prog == 0 and qi_npc.dkg_trophy == 4:
            print ("It seems like the last of the demon king generals are rallying another army. ")
            print ("We need to stop them! ")
            print ("Go find and get rid of the last of the generals. ")
        elif a_npc.dk_story_prog == 0 and qi_npc.dkg_trophy == 5:
            print ("Good job taking down that general. ")
            print ("It seems like the last two have managed to join forces though. ")
            print ("On your command we'll go meet their army and try to hold off their minions. ")
            print ("But you're the only ones we can count on to fight them directly. ")
            print ("We all believe in you, good luck. ")
            a_npc.dk_story_prog += 1
        elif a_npc.dk_story_prog == 1 and qi_npc.dkg_trophy == 7:
            print ("We finally did it! We eliminated all the demon king generals! ")
            print ("I could kiss you but there's still one last thing... ")
            print ("It seems like the demon king has gone into hiding to try to regroup. ")
            print ("We'll talk about that later, for now it's time to party! ")
            a_npc.dk_story_prog = 0
            a_npc.dk_story += 1
    elif a_npc.dk_story == 3:
        if a_npc.dk_story_prog == 0:
            print ("The demon king rallied and army and is marching on the city! ")
            print ("We need to stop them!  Hurry up and go! ")
        elif a_npc.dk_story_prog == 0 and qi_npc.dkg_trophy == 3:
            print ("Whew we managed, to push them back for now. ")
            print ("We didn't fully route them yet though, I have a feeling they'll be back soon. ")
            print ("Now is the perfect time to give chase and not give them that chance. ")
            a_npc.dk_story_prog += 1
        elif a_npc.dk_story_prog == 1 and qi_npc.dkg_trophy == 3:
            print ("Come on, we need you if we're going to stand a chance. ")
            print ("As soon as you're ready, we'll give chase. ")
        elif a_npc.dk_story_prog == 1 and qi_npc.dkg_trophy == 4:
            print ("Whew, look at them run. ")
            print ("Look's like the demonic army is splintered. ")
            print ("Thanks to you, the people will be safer. ")
            a_npc.dk_story_prog = 0
            a_npc.dk_story += 1
    elif a_npc.dk_story == 2:
        #you get dkg_trophy by defeating demon king generals
        if a_npc.dk_story_prog == 0 and qi_npc.dkg_trophy == 0:
            print ("The demon king is more on guard now. ")
            print ("We need to prove our strength and take out one of his close generals. ")
            print ("That should put a little bit of fear into his heart. ")
            #this can be an event where you chase Takozheng through tunnels and try to find him
            print ("We should start by attacking the weakest one. ")
        elif a_npc.dk_story_prog == 0 and qi_npc.dkg_trophy == 1:
            print ("Good job, we're started chipping away at the demon king's power. ")
            a_npc.dk_story_prog += 1
        elif a_npc.dk_story_prog == 1 and qi_npc.dkg_trophy == 1:
            print ("Let's target another one, the demon king generals are he main supporters. ")
            print ("If we can remove a few then he'll begin to lose control of the monsters. ")
        elif a_npc.dk_story_prog == 1 and qi_npc.dkg_trophy == 2:
            print ("Great, two down, just five more to go. ")
            a_npc.dk_story_prog = 0
            a_npc.dk_story += 1
    elif a_npc.dk_story == 1:
        print ("I'm sure you've noticed how many demonic armies are running amok. ")
        print ("They're the ones acting as the demon king's arms and legs. ")
        print ("To start hurting the king we'll start with them. ")
        if a_npc.dk_story_prog == 0:
            print ("Go out and attack the demon lords. ")
            print ("They're cocky and will underestimate you, use that to your advantage. ")
        #the progress will increase randomly as you defeat demon lords
        #will need a function that lets you progress
        #can edit the quest function to allow you to choose what kind of storyline to work on
        elif a_npc.dk_story_prog > 0:
            print ("Good job. ")
            print ("The demon king must have noticed that some of his lords have been defeated. ")
            a_npc.dk_story += 1
            a_npc.dk_story_prog = 0
    elif a_npc.dk_story == 0 and a_npc.dk_story_prog == 0:
        print ("Welcome to our little hideout. ")
        if a_npc.rank < 10:
            print ("Before we fully accept you, you'll need to prove your worth. ")
            print ("You can start by helping people and slaying monsters. ")
        elif a_npc.rank >= 10:
            print ("You've done great work, we're happy to have you on our side. ")
            a_npc.dk_story += 1
