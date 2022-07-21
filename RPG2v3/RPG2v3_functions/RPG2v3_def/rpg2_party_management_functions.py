import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC, Weapon_PC,
                                   Armor_PC)
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
        if len(heroes_party) > 1:
                try:
                        number = int(input("Which one?"
                                               "(First one is number 1, etc.)"))
                        if 0 < number <= len(heroes_party):
                                hero = heroes_party[(number - 1)]
                        else:
                                print ("That's not a real choice.")
                                hero = pick_hero(heroes_party)
                except (ValueError, AttributeError):
                        print ("That's not a real choice.")
                        hero = pick_hero(heroes_party)
        elif len(heroes_party) == 1:
                hero = heroes_party[0]
        return hero
#function that picks a random hero from the party with health > 0
def pick_random_healthy_hero(heroes_party):
        hero = None
        #if there's a defender in the party, pick him first
        for player  in heroes_party:
                if "Defender" in player.name and player.health > 0:
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
                        #don't pick golems
                        if hero.health <=0 or hero.name == "Totem":
                                hero = pet_pick_random_healthy_hero(heroes_party)
                        return hero
                else:
                        hero = heroes_party[0]
                        if hero.name != "Totem":
                                return hero
                        else:
                                hero = Player_PC("nothing", 1, 0, 0, 0, 0, 0, 0, 0)
                                return hero

        except:
                print ("The heroes have all been defeated.")
                hero = Player_PC("nothing", 1, 0, 0, 0, 0, 0, 0, 0)
                return hero
def pet_pick_random_injured_hero(heroes_party):
        hero = None
        try:
                if len(heroes_party) > 1:                                        
                        x = random.randint(0, len(heroes_party) - 1)
                        hero = heroes_party[x]
                        #only pick heroes, not golems, heros need to be injured but still conscious
                        if hero.health <=0 or hero.name == "Totem" or hero.health >= hero.maxhealth:
                                hero = pet_pick_random_healthy_hero(heroes_party)
                        return hero
                else:
                        hero = heroes_party[0]
                        if hero.name != "Totem" and hero.health > 0:
                                return hero
                        else:
                                hero = Player_PC("nothing", 1, 0, 0, 0, 0, 0, 0, 0)
                                return hero

        except:
                print ("The heroes have all been defeated.")
                hero = Player_PC("nothing", 1, 0, 0, 0, 0, 0, 0, 0)
                return hero
#function that picks a random monster from the party who has been injured
def pick_random_healthy_monster(monster_party):
        try:
                if len(monster_party) > 1:
                        x = random.randint(0, len(monster_party) - 1)
                        monster = monster_party[x]
                        if monster.health <= 0:
                                monster = pick_random_healthy_monster(monster_party)
                elif len(monster_party) == 1:
                        monster = monster_party[0]
        except:
                monster = Monster_NPC("nothing", 0, 0, 0, 0, "None", 0)
        return monster
def pet_pick_random_monster(monster_party):
        try:
                if len(monster_party) > 1:
                        x = random.randint(0, len(monster_party) - 1)
                        monster = monster_party[x]
                        #don't pick bombs
                        if monster.health <= 0 or "Bomb" in monster.name:
                                monster = pet_pick_random_monster(monster_party)
                elif len(monster_party) == 1:
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
                        monster = monster_party[0]
        elif len(monster_party) == 1:
                monster = monster_party[0]
        else:
                monster = Monster_NPC("nothing", 0, 0, 0, 0, "None", 0)
        return monster
#function that checks for equipment
def check_equipment(hero, equipment_list):
        equipment = None
        for equip in equipment_list:
                if equip.user == hero.name:
                        equipment = equip
        return equipment
#function that picks the lowest health character
def pick_lowest_health(h_p):
        #start with 100% health
        x = 100
        hro = None
        #repeat this process a few times to make sure you pick the lowest health hero
        for z in range(0, len(h_p)):
                #then check each characters health percentage
                for hero in h_p:
                        #make sure to only count health heroes
                        if hero.health > 0 and hero.name != "Totem":
                                #multiply by 100 to get an rounded percentage
                                y = round((hero.health/hero.maxhealth), 2) * 100
                                #if the percentage is lower then pick that hero
                                if y < x:
                                        x = y
                                        hro = hero
        return hro

#function that picks the highest health character
def pick_highest_health(h_p):
        #start with 0% health
        x = 0
        hro = None
        #repeat this process a few times to make sure you pick the highest health hero
        for z in range(0, len(h_p)):
                #then check each characters health percentage
                for hero in h_p:
                        #make sure to only count healthy heroes
                        if hero.health > 0 and hero.name != "Totem":
                                #multiply by 100 to get an rounded percentage
                                y = round((hero.health/hero.maxhealth), 2) * 100
                                #if the percentage is higher then pick that hero
                                if y > x:
                                        x = y
                                        hro = hero
        return hro

#function that lets a monster pick another monster to attack
def pick_different_monster(m_npc, m_p):
        target = None
        if len(m_p) > 1:
                target = pick_random_healthy_monster(m_p)
                if target == m_npc:
                        target = pick_different_monster(m_npc, m_p)
        return target

#function that heals the party to full
def recover(h_p):
        for hero in h_p:
                hero.health = hero.maxhealth
                hero.mana = hero.maxmana
