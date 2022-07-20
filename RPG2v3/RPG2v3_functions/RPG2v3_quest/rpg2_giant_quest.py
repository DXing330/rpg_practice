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
L = List_Constants()
C = Constants()
Q = Q_Constants()
sys.path.append(".")
import rpg2_quest_battle as battle_func
import rpg2_quest_monster_function as mon_func

#function that controls the giant quest
def giant_quest(h_p, g_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i):
        print ("You see", len(g_p), "giants.")
        print ("'What are you shouting about little thing? '")
        choice = input("I want to FIGHT too. / Please STOP fighting. ")
        if choice.upper() == "F":
                print ("The giant laughs before raising its club to smash. ")
                print ("'It's been awhile since an insect challenged me. '")
                battle_func.battle_phase(h_p, g_p, p_npc, ib_pc,
                                         s_pc, h_w, h_a, q_i)
        elif choice.upper() == "S":
                print ("'Why? '")
                answer = input("WHY are you fighting?/You're bothering PEOPLE.")
                if answer.upper() == "W":
                        x = random.randint(0, 1)
                        if x == 0 or x == 1:
                                print ("'He ate my sheep. ' accuses one giant.")
                                option = input("We'll BUY you a new one./"
                                               "It's just ONE sheep./Let us HELP you fight."
                                               "B/O/H")
                                if option.upper() == "B":
                                        print ("'I want a whole flock! '")
                                        agree = input("YES/NO? Y/N? ")
                                        if agree.upper() == "Y" and ib_pc.coins > Q.GIANT_FLOCK * (len(g_p)//2):
                                                print ("You hand over enough coins to buy a flock. ")
                                                print ("The other giants also demand that you buy them things. ")
                                                ib_pc.coins -= Q.GIANT_FLOCK * (len(g_p)//2)
                                                print ("'Some of you are alright after all. Thanks. '")
                                                print ("The giants leave satisfied. ")
                                        else:
                                                print ("'I knew talking was a waste of time. '")
                                                print ("'Let's get rid of these pests first! '")
                                                battle_func.battle_phase(h_p, g_p, p_npc, ib_pc,
                                                                         s_pc, h_w, h_a, q_i)
                                elif option.upper() == "H":
                                        print ("'Like you would be any help, you're just a distraction. '")
                                        print ("'Better get rid of you first. '")
                                        battle_func.battle_phase(h_p, g_p, p_npc, ib_pc,
                                                         s_pc, h_w, h_a, q_i)
                                elif option.upper() == "O":
                                        y = random.randint(0, 1)
                                        if y == 0:
                                                print ("'Hmph, I suppose I have plenty more. '")
                                                g_p.pop()
                                                print ("One giant leaves. ")
                                                print ("The others continue fighting. ")
                                                battle_func.battle_phase(h_p, g_p, p_npc, ib_pc,
                                                                         s_pc, h_w, h_a, q_i)
                                        elif y == 1:
                                                print ("The giant's angry roar attracts more giants. ")
                                                mon = mon_func.giant_maker()
                                                g_p.append(mon)
                                                battle_func.battle_phase(h_p, g_p, p_npc, ib_pc,
                                                                         s_pc, h_w, h_a, q_i)
                                else:
                                        battle_func.battle_phase(h_p, g_p, p_npc, ib_pc,
                                                                 s_pc, h_w, h_a, q_i)   
                                                
                        elif x == 1:
                                print ("'He hit me in his sleep. ' accuses one giant. ")
                                option = input("Will an APOLOGY suffice?/"
                                               "Get OVER it./ Two WRONGS don't make a right.")
                                if option.upper() == "O":
                                        y = random.randint(0, 1)
                                        if y == 0:
                                                print ("'I guess I'm still tired. Yawn. '")
                                                print ("The giants all yawn and fall asleep. ")
                                                print ("The weight of them all laying down knocks you off your feet. ")
                                                print ("After a few moments the hills are peaceful except for giant snores. ")
                                        elif y == 1:
                                                print ("The giant's angry roar attracts more giants. ")
                                                mon = mon_func.giant_maker()
                                                g_p.append(mon)
                                                mon = mon_func.giant_maker()
                                                g_p.append(mon)
                                                battle_func.battle_phase(h_p, g_p, p_npc, ib_pc,
                                                                         s_pc, h_w, h_a, q_i)
                                elif option.upper() == "A":
                                        print ("I want some of those sweet heal potions! ")
                                        give = input("YES/NO? Y/N ")
                                        if give.upper() == "Y" and ib_pc.heal > Q.GIANT_FLOCK:
                                                ib_pc.heal -= Q.GIANT_FLOCK
                                                print ("'Ah I love that taste. '")
                                                print ("The giant tosses handfuls of potions into it's mouth. ")
                                                print ("The other giants also demand potions. ")
                                                print ("After they've all drank their fill they leave happy. ")
                                        else:
                                                print ("'I can smell them on you! '")
                                                print ("The giants raise their clubs at you. ")
                                                battle_func.battle_phase(h_p, g_p, p_npc, ib_pc,
                                                                         s_pc, h_w, h_a, q_i)
                                elif option.upper() == "W":
                                        y = random.randint(0, 2)
                                        if y == 0:
                                                print ("'Condescending insects! '")
                                                print ("The giants raise their clubs at you. ")
                                                battle_func.battle_phase(h_p, g_p, p_npc, ib_pc,
                                                                         s_pc, h_w, h_a, q_i)
                                        elif y == 1:
                                                print ("One of the giants frowns and begins to lecture. ")
                                                print ("Eventually the other giants get bored and leave. ")
                                                g_p.clear()
                                                print ("The remaining lecturering giant roars with indignation. ")
                                                mon = mon_func.giant_maker()
                                                g_p.append(mon)
                                                battle_func.battle_phase(h_p, g_p, p_npc, ib_pc,
                                                                         s_pc, h_w, h_a, q_i)
                                        elif y == 2:
                                                if len(g_p) % 2 == 0:
                                                        print ("The giants think and then conclude they need more . ")
                                                        mon = mon_func.giant_maker()
                                                        g_p.append(mon)
                                                        battle_func.battle_phase(h_p, g_p, p_npc, ib_pc,
                                                                                 s_pc, h_w, h_a, q_i)
                                                elif len(g_p) % 2 == 1:
                                                        print ("The giants roar of anger attracts more giants. ")
                                                        mon = mon_func.giant_maker()
                                                        g_p.append(mon)
                                                        mon = mon_func.giant_maker()
                                                        g_p.append(mon)
                                                        battle_func.battle_phase(h_p, g_p, p_npc, ib_pc,
                                                                                 s_pc, h_w, h_a, q_i)
                                                        
                                                
                                else:
                                        battle_func.battle_phase(h_p, g_p, p_npc, ib_pc,
                                                                 s_pc, h_w, h_a, q_i)
                                        
                                        
                        
                elif answer.upper() == "P":
                        print ("'Why should we care about that? '")
                        option = input("EXPLAIN/BEG B/E")
                        if option.upper() == "B":
                                g_p.pop()
                                print ("One of the giants seems to take pity and leave. ")
                                print ("The rest laugh and raise their clubs. ")
                                battle_func.battle_phase(h_p, g_p, p_npc, ib_pc,
                                                         s_pc, h_w, h_a, q_i)

                        elif option.upper() == "E":
                                x = 0
                                y = 0
                                for hero in h_p:
                                        x += hero.skill
                                for giant in g_p:
                                        y += giant.skill
                                h = random.randint(x//2, x)
                                g = random.randint(y//2, y)
                                if h > g:
                                        print ("After a lengthy debate, some the giants nod. ")
                                        leave = random.randint(1, (len(g_p) - 1))
                                        for num in range(0, leave):
                                                g_p.pop()
                                        print ("The unconvinced giants raise their clubs. ")
                                        battle_func.battle_phase(h_p, g_p, p_npc, ib_pc,
                                                                 s_pc, h_w, h_a, q_i)
                                elif h == g:
                                        print ("After a lengthy debate, one giant nods. ")
                                        g_p.pop()
                                        print ("The unconvinced giants raise their clubs. ")
                                        battle_func.battle_phase(h_p, g_p, p_npc, ib_pc,
                                                                 s_pc, h_w, h_a, q_i)
                                elif h < g:
                                        print ("After a lengthy debate, more giants arrive. ")
                                        mon = mon_func.giant_maker()
                                        g_p.append(mon)
                                        print ("The giant's are not convinced and raise their clubs. ")
                                        battle_func.battle_phase(h_p, g_p, p_npc, ib_pc,
                                                                 s_pc, h_w, h_a, q_i)
                        else:
                                battle_func.battle_phase(h_p, g_p, p_npc, ib_pc,
                                                 s_pc, h_w, h_a, q_i)
                                
                else:
                        battle_func.battle_phase(h_p, g_p, p_npc, ib_pc,
                                                 s_pc, h_w, h_a, q_i)
        else:
                giant_quest(h_p, g_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i)
                        

