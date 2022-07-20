import random
import copy
import sys
sys.path.append("../RPG2v3_def")
sys.path.append("../RPG2v3_battle")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC, Weapon_PC,
                                   Armor_PC)
import rpg2_party_management_functions as party_func
import rpg2_monster_function as monster_func
import rpg2_drop_table as drop_func
import rpg2_player_action_function as player_func
#function that lets giants hit each other
def giant_atk(m_npc, h_a, h_p, m_p):
        #first decide who to hit based on party size
        if len(m_p) > 1:
                x = random.randint(0, len(m_p))
                if x > 0:
                        #if they hit another giant make sure they don't hit themselves
                        target = party_func.pick_different_monster(m_npc, m_p)
                        if target != m_npc:
                                target.health -= m_npc.atk - target.defense
                                print (m_npc.name, "whacks", target.name)
                elif x == 0:
                        #if they hit the heroes then function as normal
                        hero = party_func.pick_random_healthy_hero(h_p)
                        monster_func.monster_attack(m_npc, hero, h_a, h_p, m_p)
        elif len(m_p) == 1:
                #when the giant is alone he attacks the party
                hero = party_func.pick_random_healthy_hero(h_p)
                monster_func.monster_attack(m_npc, hero, h_a, h_p, m_p)
#function that controls the monster drops after the battle phase
def drop_step(ib_pc, m_p, h_w, h_a, q_i):
        for mon in m_p:
                drop_func.quest_drop_table(mon, ib_pc, h_w, h_a, q_i)
        #then clear the monster party list for the next fight
        while len(m_p) > 0:
                m_p.pop(0)
#function that controls the basic battle_phase
def battle_phase(h_p, m_p, h_s, ib_pc, s_pc, h_w, h_a, q_i):
        #make a copy of the heroes party and the monster's party
        new_h_p = []
        new_h_s = []
        new_h_w = []
        new_h_a = []
        for hero in h_p:
                copy_hero = copy.copy(hero)
                new_h_p.append(copy_hero)
        for ally in h_s:
                copy_ally = copy.copy(ally)
                new_h_s.append(copy_ally)
        for wpn in h_w:
                copy_weapon = copy.copy(wpn)
                new_h_w.append(copy_weapon)
        for amr in h_a:
                copy_armor = copy.copy(amr)
                new_h_a.append(copy_armor)
        new_m_p = list(m_p)
        #boolean to loop the battle phase until it finishes
        bBattle = True
        while bBattle:
                #check to see if the battle continues
                if len(new_h_p) == 0:
                        h_p.clear()
                        print ("The heroes have been routed and flee back to town.")
                        bBattle = False
                elif len(new_m_p) == 0:
                        print ("The monsters have been defeated.")
                        bBattle = False
                else:
                #give the player's actions
                        for hero in new_h_p:
                                if hero.health > 0 and hero.name != "Totem":
                                        hero.stats()
                                        player_func.player_action(hero, new_h_p, new_m_p,
                                                                  ib_pc, s_pc, new_h_s,
                                                                  new_h_w, new_h_a)
                                elif hero.health <= 0:
                                        new_h_p.remove(hero)
                        #then give the pet a turn
                        player_func.pet_action(new_h_s, new_h_p, new_m_p)
                        #then check if the monster's are still alive
                        for x in range(0, len(m_p)):
                                for monster in new_m_p:
                                        if monster.health <= 0:
                                                new_m_p.remove(monster)
                        #also check if the heroes killed themselves somehow
                        for hero in new_h_p:
                                if hero.health <= 0:
                                        new_h_p.remove(hero)
                        #then give the monster's a turn
                        for monster in new_m_p:
                                if monster.health <= 0 and "Bomb" in monster.name:
                                        monster_func.monster_attack(monster, hero, new_h_a, new_h_p, new_m_p)
                                        new_m_p.remove(monster)
                                elif monster.health <= 0:
                                        new_m_p.remove(monster)
                                elif monster.health > 0 and "Giant" in monster.name:
                                        giant_atk(monster, new_h_a, new_h_p, new_m_p)
                                elif monster.health > 0:
                                        hero = party_func.pick_random_healthy_hero(new_h_p)
                                        monster_func.monster_attack(monster, hero, new_h_a, new_h_p, new_m_p)
                        #after the monster attacks, check on the heroes again
                        for hero in new_h_p:
                                if hero.health <= 0:
                                        new_h_p.remove(hero)
                        #also check on the monsters incase they blew up
                        for x in range(0, len(m_p)):
                                for monster in new_m_p:
                                        if monster.health <= 0 and "Bomb" in monster.name:
                                                monster_func.monster_attack(monster, hero, new_h_a, new_h_p, new_m_p)
                                                new_m_p.remove(monster)
                                        elif monster.health <= 0:
                                                new_m_p.remove(monster)
                                
        #if the battle is over and you win then find out how many coins you get
        if not bBattle and len(new_h_p) > 0:
                #adjust the hp of the heroes after battles
                for hero in h_p:
                        check = None
                        for heero in new_h_p:
                                if hero.name == heero.name:
                                        check = heero
                        #if there is no matching hero then the hero's health goes to zero
                        if check == None and hero.name != "Knight":
                                hero.health = 0
                                hero.mana = 0
                        #if there is a matching hero then the hero's health becomes equal
                        elif check != None:
                                hero.health = min(check.health, hero.maxhealth)
                                hero.mana = min(check.mana, hero.maxmana)
                        #knight could have another name so check that
                        elif check == None and hero.name == "Knight":
                                for heeero in new_h_p:
                                        if heeero.name == "Defender":
                                                hero.health = min(heeero.health, hero.maxhealth)
                                                hero.mana = min(heeero.mana, hero.maxmana)
                for hero in h_p:
                        if hero.health == 0:
                                h_p.remove(hero)
                drop_step(ib_pc, m_p, h_w, h_a, q_i)
        if not bBattle and len(new_h_p) == 0:
                h_p.clear()


