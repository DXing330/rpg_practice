import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Monster_NPC, Pet_NPC, ItemBag_PC)
import rpg2_monster_function as monster_func
import rpg2_player_action_function as player_func
import rpg2_party_management_functions as party_func

#function that controls the monster drops after the battle phase
def drop_step(ib_pc, m_p):
        coins = 0
        for monster in m_p:
                coins += monster.dropchance
        ib_pc.coins += coins
        print "You found", coins, "coins."
        #then clear the monster party list for the next fight
        while len(m_p) > 0:
                m_p.pop(0)
#function that controls the basic battle_phase
def battle_phase(h_p, m_p, p_npc, ib_pc, s_pc):
        #make a copy of the heroes party and the monster's party
        new_h_p = list(h_p)
        new_m_p = list(m_p)
        #boolean to loop the battle phase until it finishes
        bBattle = True
        while bBattle:
                #check to see if the battle continues
                if len(new_h_p) == 0:
                        print "The heroes have been routed and flee back to town."
                        bBattle = False
                elif len(new_m_p) == 0:
                        print "The monsters have been defeated."
                        bBattle = False
                else:
                #give the player's actions
                        for hero in new_h_p:
                                if hero.health > 0:
                                        hero.stats()
                                        player_func.player_action(hero, new_m_p, ib_pc, s_pc)
                                elif hero.health < 1:
                                        new_h_p.remove(hero)
                        #then give the pet a turn
                        player_func.pet_action(p_npc, new_h_p, new_m_p)
                        #then give the monster's a turn
                        for monster in new_m_p:
                                if monster.health > 0:
                                        hero = party_func.pick_random_healthy_hero(new_h_p)
                                        monster_func.monster_attack(monster, hero)
                                elif monster.health < 1:
                                        new_m_p.remove(monster)
                        #after the monster attacks, check on the heroes again
                        for hero in new_h_p:
                                if hero.health < 1:
                                        new_h_p.remove(hero)
                                
        #if the battle is over and you win then find out how many coins you get
        if not bBattle and len(new_h_p) > 0:
                drop_step(ib_pc, m_p)

