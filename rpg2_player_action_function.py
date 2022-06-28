import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC)
import rpg2_party_management_functions as party_func
from rpg2_constants import Constants
C = Constants()
##function where the player makes a choice of what they want to do in battle
#function that controls what the pet will do during battle
#need to input the pet and both parties
#the pet will heal the heroes in the heroes party as long as they are healthy
#or the pet atk the monsters in the monster party as long as they are healthy
def pet_action(p_npc, h_p, m_p):
        #depending on the stage of the pet it will perform more actions
        for x in range(0, p_npc.stage, C.PET_ACTION_UP):
                try:
                        y = random.randint(0,1)
                        if y == 0:
                                hero = party_func.pick_random_healthy_hero(h_p)
                                hero.health += p_npc.atk
                                print p_npc.name, "uses their healing magic on", hero.name
                        elif y == 1:
                                monster = party_func.pick_random_healthy_monster(m_p)
                                monster.health -= p_npc.atk
                                print p_npc.name, "uses their attacking magic on", monster.name
                except:
                        print p_npc.name, "failed to do anything."


#player attack function
def player_attack(p_pc, m_npc):
        m_npc.health = max((m_npc.health - p_pc.atk - p_pc.weapon - p_pc.atkbonus),0)

        
#use item function
def use_item(p_pc, ib_pc):
        print "What item do you want to use? "
        check = raw_input("Heal, Mana, Boosts? H/M/B ")
        if check.upper() == "H" and ib_pc.heal >= 1:
                ib_pc.heal -= 1
                p_pc.health = min(p_pc.maxhealth, (p_pc.health + (p_pc.maxhealth/2)))
        else:
                print "You can't do that right now."
                
#use skill function
#more skills will be added later
def use_skill(p_pc, m_p):
        print "What skill do you want to use? "
        check = raw_input("Observe? O ")
        if check.upper() == "O":
                for monster in m_p:
                        monster.stats()
        else:
                print "You can't do that right now. "
#need the player, pet, monsters, itembag and spells
#player makes a choice about what to do
def player_action(p_pc, m_p, ib_pc, s_pc):
        print ("What do you do?")
        check = raw_input("Attack, Item, Magic or Skill? A/I/M/S")
        if check.upper() == "A" and len(m_p) > 1:
                monster = party_func.pick_monster(m_p)
                player_attack(p_pc, monster)
        elif check.upper() == "A" and len(m_p) == 1:
                for monster in m_p:
                        player_attack(p_pc, monster)
        elif check.upper() == "I":
                ib_pc.stats()
                use_item(p_pc, ib_pc)
        elif check.upper() == "M":
                print "You can't do that right now."
                #use_magic(p_pc, s_pc, m_p)
        elif check.upper() == "S":
                use_skill(p_pc, m_p)
        else:
                print "You miss your chance."
