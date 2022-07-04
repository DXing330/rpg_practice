import random
import sys
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC)
from rpg2_constants import Constants
C = Constants()
#function that adds a hero to the hero party list
def add_to_party(h_p, p_pc):
        #if the party isn't full you can add them
        if len(h_p) < C.PARTY_LIMIT:
                h_p.append(p_pc)
        else:
                print ("The party is already full.")
#function that removes a hero from the hero party list
def remove_from_party(heroes_party):
        try:
                number = int(input("Which hero?"
                                       "(First hero is number 1, etc.)"))
                if 0 < number <= len(heroes_party):
                        heroes_party.pop(number - 1)
                else:
                        print ("That's fine if you changed your mind.")
        except (ValueError, AttributeError):
                print ("That's fine if you changed your mind.")

#function that will pick a hero from the party
def pick_hero(heroes_party):
        hero = None
        try:
                number = int(input("Which hero?"
                                       "(First hero is number 1, etc.)"))
                if 0 < number <= len(heroes_party):
                        hero = heroes_party[(number - 1)]
                else:
                        print ("That's not a real choice.")
                        hero = pick_hero(heroes_party)
        except (ValueError, AttributeError):
                print ("That's not a real choice.")
                hero = pick_hero(heroes_party)
        return hero
#function that picks a random hero from the party with health > 0
def pick_random_healthy_hero(heroes_party):
        hero = None
        #if there's a defender in the party, pick him first
        for player  in heroes_party:
                if player.name == "Defender" and player.health > 0:
                        hero = player
        #if there's no defender then try to pick a random hero
        if hero == None:
                try:
                        if len(heroes_party) > 1:                                        
                                x = random.randint(0, len(heroes_party) - 1)
                                hero = heroes_party[x]
                                if hero.health <=0:
                                        hero = pick_random_healthy_hero(heroes_party)
                                return hero
                        else:
                                hero = heroes_party[0]
                                return hero

                except:
                        print ("The heroes have all been defeated.")
                        hero = Player_PC("nothing", 1, 0, 0, 0, 0, 0, 0, 0)
                        return hero
        else:
                return hero
def pet_pick_random_healthy_hero(heroes_party):
        hero = None
        try:
                if len(heroes_party) > 1:                                        
                        x = random.randint(0, len(heroes_party) - 1)
                        hero = heroes_party[x]
                        if hero.health <=0:
                                hero = pet_pick_random_healthy_hero(heroes_party)
                        return hero
                else:
                        hero = heroes_party[0]
                        return hero

        except:
                print ("The heroes have all been defeated.")
                hero = Player_PC("nothing", 1, 0, 0, 0, 0, 0, 0, 0)
                return hero
#function that picks a random hero from the party who has been injured
def pick_random_healthy_monster(monster_party):
        try:
                if len(monster_party) > 1:
                        x = random.randint(0, len(monster_party) - 1)
                        monster = monster_party[x]
                        if monster.health <= 0:
                                monster = pick_random_healthy_monster(monster_party)
                if len(monster_party) == 1:
                        monster = monster_party[0]
        except:
                monster = Monster_NPC("nothing", 0, 0, 0, 0, "None", 0)
        return monster
#function that picks a monster
def pick_monster(monster_party):
        monster = None
        if len(monster_party) > 1:
                try:
                        x = int(input("Which monster?"
                                          "(First monster is number 1, etc.)"))
                        if 0 < x <= len(monster_party):
                                monster = monster_party[(x - 1)]
                        else:
                                print ("That's not a real choice.")
                                monster = pick_monster(monster_party)
                except (ValueError, AttributeError):
                        print ("That's not a real choice.")
                        monster = pick_monster(monster_party)
        elif len(monster_party) == 1:
                monster = monster_party[0]
        else:
                monster = Monster_NPC("nothing", 0, 0, 0, 0, "None", 0)
        return monster
