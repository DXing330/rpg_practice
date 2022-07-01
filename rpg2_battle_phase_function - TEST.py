import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Monster_NPC, Pet_NPC, ItemBag_PC, Spell_PC)
import rpg2_monster_function as monster_func
import rpg2_player_action_function as player_func
import rpg2_party_management_functions as party_func

#function that controls the monster drops after the battle phase
def drop_step(ib_pc, m_p):
        coins = 0
        for monster in m_p:
                coins += monster.dropchance
        ib_pc.coins += coins
        print ("You found", coins, "coins.")
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
                        print ("The heroes have been routed and flee back to town.")
                        bBattle = False
                elif len(new_m_p) == 0:
                        print ("The monsters have been defeated.")
                        bBattle = False
                else:
                #give the player's actions
                        for hero in new_h_p:
                                if hero.health > 0:
                                        hero.stats()
                                        player_func.player_action(hero, new_h_p, new_m_p,
                                                                  ib_pc, s_pc, p_npc)
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

monster_party = []
heroes_party = []
heroes_magic = []
heroes_bag = ItemBag_PC(2, 2, 2, 10)
fireball = Spell_PC("Fireball", 3, 3, "Fire", 3)
rainstorm = Spell_PC("Rainstorm", 2, 3, "Water", 2)
earthspike = Spell_PC("Earthspike", 3, 1, "Earth", 2)
mage = Player_PC("Mage", 1, 10, 10, 2, 2, 0, 5)
warrior = Player_PC("Warrior", 1, 15, 15, 5, 3, 0, 0, 0, 0, 2, 1)
cleric = Player_PC("Cleric", 1, 10, 10, 1, 2, 0, 5)
summoner = Player_PC("Summoner", 1, 10, 10, 2, 2, 0, 0)
heroes_pet = Pet_NPC("Awoken Angel", 2, 4)
firemon = Monster_NPC("Mon", 100, 0, 0, 0, "Fire", 0)
watermon = Monster_NPC("Mon", 100, 0, 0, 0, "Water", 0)
earthmon = Monster_NPC("Mon", 100, 0, 0, 0, "Earth", 0)
heroes_magic.append(fireball)
heroes_magic.append(rainstorm)
heroes_magic.append(earthspike)
heroes_party.append(cleric)
heroes_party.append(mage)
heroes_party.append(summoner)
monster_party.append(firemon)
monster_party.append(watermon)
monster_party.append(earthmon)

battle_phase(heroes_party, monster_party, heroes_pet, heroes_bag, heroes_magic)
