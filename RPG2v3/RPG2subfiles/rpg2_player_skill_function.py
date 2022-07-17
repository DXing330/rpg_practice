import random
import copy
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC, Weapon_PC,
                                   Armor_PC)
import rpg2_player_action_function as player_func
import rpg2_party_management_functions as party_func
import rpg2_angel_action_function as angel_func
import rpg2_hunter_function as hunt_func
from rpg2_constants import Constants
from rpg2_constant_lists import List_Constants
L = List_Constants()
C = Constants()
#function which controls what skills the player can use
#need the hero, heroes_party, monster_party, pet for now
def use_skill(p_pc, h_p, m_p, ib_pc, s_pc, p_npc, h_w, h_a):
        
        print ("What skill do you want to use? ")
        print ("OBSERVE enemies? O")
        print ("COMMAND? C")
        print ("HEAL Ally? H")
        print ("BUFF? B")
        print ("DEBUFF Enemy? D")
        print ("Summon TOTEM? T")
        print ("Use EXPLOSIVE? E")
        print ("PROTECT your allies? P")
        print ("Try to go for a SNEAK ATTACK? S")
        
        check = input("B/P/O/C/S/H/D/T")
        if check.upper() == "T":
                if p_pc.name == "Summoner" and p_pc.mana > 0:
                        print("What kind of golem do you make? ")
                        print("ATTACK, HEAL, BUFF, DEBUFF? ")
                        choice = input("A/B/D/H? ")
                        if choice.upper() == "A":
                                atkgolem = Player_PC("Totem", 1, p_pc.skill,
                                                     p_pc.skill, p_pc.skill, 0, 0, 0, 0)
                                totem = copy.copy(atkgolem)
                                h_p.append(totem)
                                p_pc.skill -= len(h_p)
                                p_pc.mana -= len(h_p)
                                print (p_pc.name, "summons an attacking totem. ")
                        elif choice.upper() == "B":
                                bufgolem = Player_PC("Totem", 1, p_pc.skill,
                                                     p_pc.skill, 0, 0, p_pc.skill, 0, 0)
                                totem = copy.copy(bufgolem)
                                h_p.append(totem)
                                p_pc.skill -= len(h_p)
                                p_pc.mana -= len(h_p)
                                print (p_pc.name, "summons a buffing totem. ")
                        elif choice.upper() == "D":
                                debufgolem = Player_PC("Totem", 1, p_pc.skill,
                                                       p_pc.skill, 0, 0, 0, p_pc.skill, 0)
                                totem = copy.copy(debufgolem)
                                h_p.append(totem)
                                p_pc.skill -= len(h_p)
                                p_pc.mana -= len(h_p)
                                print (p_pc.name, "summons a debuffing totem. ")
                        elif choice.upper() == "H":
                                healgolem = Player_PC("Totem", 1, p_pc.skill,
                                                      p_pc.skill, 0, p_pc.skill, 0, 0, 0)
                                totem = copy.copy(healgolem)
                                h_p.append(totem)
                                p_pc.skill -= len(h_p)
                                p_pc.mana -= len(h_p)
                                print (p_pc.name, "summons a healing totem. ")
                        else:
                                print("You don't know how to make that kind of totem. ")
                else:
                        print("You don't know how to do that. ")
        elif check.upper() == "O":
                if p_pc.name == "Ninja":
                        p_pc.skill += p_pc.level
                        print (p_pc.name, "observes the enemies weaknesses. ")
                elif p_pc.name == "Tactician":
                        for hero in h_p:
                                if hero.name != "Golem":
                                        hero.skill += 1
                        print (p_pc.name, "estimates the enemies plans. ")
                elif "Hunter" in p_pc.name:
                        p_pc.atkbonus += p_pc.level
                        for ally in p_npc:
                                if "Spirit" in ally.name:
                                        ally.atk += p_pc.level
                for monster in m_p:
                        monster.stats()
                for hero in h_p:
                        hero.stats()
                for ally in p_npc:
                        ally.stats()
                for wpn in h_w:
                        if wpn.user != "None":
                                wpn.stats()
                for amr in h_a:
                        if amr.user != "None":
                                amr.stats()
                        
        elif check.upper() == "C":
                if p_pc.name == "Summoner" and p_pc.level == C.LEVEL_LIMIT:
                        ally = None
                        for aly in p_npc:
                                if aly.name in L.ANGEL_NAMES:
                                        ally = aly
                        print(p_pc.name, "channels energy to their allies.")
                        angel_func.angel_action(ally, h_p, m_p)
                        angel_func.angel_action(ally, h_p, m_p)
                        p_pc.health += min((p_pc.skill + p_pc.level), (p_pc.maxhealth - p_pc.health))
                        p_pc.mana += 1
                elif p_pc.name == "Summoner":
                        ally = None
                        for aly in p_npc:
                                if aly.name in L.ANGEL_NAMES:
                                        ally = aly
                        print(p_pc.name, "channels energy to their allies.")
                        angel_func.angel_action(ally, h_p, m_p)
                elif p_pc.name == "Tactician":
                        p_pc.skill -= 1
                        hero = party_func.pick_hero(h_p)
                        if hero.name != "Tactician":
                                hero.stats()
                                player_func.player_action(hero, h_p, m_p, ib_pc, s_pc, p_npc, h_w, h_a)
                elif "Hunter" in p_pc.name:
                        ally = None
                        for aly in p_npc:
                                if "Spirit" in aly.name:
                                        ally = aly
                        hunt_func.companion_action(ally, h_p, m_p)
                        hunt_func.companion_action(ally, h_p, m_p)
                else:
                        print("Your allies are too focused on the battle.")
                        
        elif check.upper() == "H":
                if p_pc.name == "Cleric":
                        hero = party_func.pick_hero(h_p)
                        hero.health += p_pc.mana + p_pc.skill + p_pc.level + hero.level
                        hero.poison -= min(p_pc.skill + p_pc.level, hero.poison)
                        print (p_pc.name, "heals", hero.name)
                elif p_pc.name == "Ninja" and p_pc.skill > 0:
                        print (p_pc.name, "throws away his weapon and disappears into the shadows.")
                        p_pc.health += min(p_pc.skill, (p_pc.maxhealth - p_pc.health))
                        p_pc.skill = 0
                elif "Hunter" in p_pc.name:
                        hero = party_func.pick_hero(h_p)
                        hero.poison -= min(p_pc.level + p_pc.skill, hero.poison)
                        print (p_pc.name, "checks on ", hero.name,"'s poison.")
                        
                else:
                        if p_pc.skill >= p_pc.level:
                                hero = party_func.pick_hero(h_p)
                                hero.health += min(p_pc.skill, hero.maxhealth - hero.health)
                                hero.poison -= min(p_pc.level, hero.poison)
                                p_pc.skill -= p_pc.level
                        else:
                                hero = party_func.pick_hero(h_p)
                                hero.poison = hero.poison * C.BUFF
                        print (p_pc.name, " tries to heal ", hero.name)
                        
        elif check.upper() == "D":
                if p_pc.name == "Ninja" and p_pc.level == C.LEVEL_LIMIT:
                        monster = party_func.pick_monster(m_p)
                        if p_pc.skill > monster.skill:
                                monster.skill = round(monster.skill/C.BUFF)
                                p_pc.skill -= monster.skill
                                print (p_pc.name, "out-skills", monster.name)
                                p_pc.mana -= 1
                        else:
                                print (monster.name, "out-skills", p_pc.name)
                elif p_pc.name == "Knight" or p_pc.name == "Defender":
                        monster = party_func.pick_monster(m_p)
                        if p_pc.skill > 0:
                                monster.defense -= min(p_pc.skill, monster.defense)
                                print (p_pc.name, "taunts", monster.name)
                        else:
                                print (p_pc.name, "taunts", monster.name)
                                print (monster.name, "ignores the taunt. ")
                elif p_pc.name == "Cleric" and p_pc.skill > 0:
                        monster = party_func.pick_monster(m_p)
                        monster.atk = max((monster.atk-p_pc.mana-p_pc.skill),0)
                        p_pc.mana -= 1
                        p_pc.skill -= 1
                        print ("Holy strands wrap around", monster.name)
                elif "Hunter" in p_pc.name:
                        monster = party_func.pick_monster(m_p)
                        monster.atk -= round(monster.poison ** C.DECREASE_EXPONENT)
                        monster.health -= monster.poison
                        print (p_pc.name, "aggravates the poison inside", monster.name)
                        
                else:
                        print("Nothing happens.")
        elif check.upper() == "B":
                armor = party_func.check_equipment(p_pc, h_a)
                weapon = party_func.check_equipment(p_pc, h_w)
                if p_pc.name == "Ninja" and p_pc.mana > 0:
                        p_pc.skill = round(p_pc.skill * C.BUFF)
                        print (p_pc.name, "sharpens their senses. ")
                        p_pc.mana -= 1
                elif p_pc.name == "Knight" and p_pc.skill > 0:
                        p_pc.defbonus += p_pc.level
                        if armor != None:
                                armor.defense += 1
                                armor.strength += 1
                        p_pc.skill -= round(p_pc.defbonus/p_pc.level)
                        print (p_pc.name, "fortifies their position. ")
                elif p_pc.name == "Defender" and p_pc.skill > 0:
                        p_pc.defbonus += p_pc.level
                        if armor != None:
                                armor.defense += 1
                                armor.strength += 1
                        p_pc.skill -= round(p_pc.defbonus/p_pc.level)
                        print (p_pc.name, "fortifies their position. ")
                elif p_pc.name == "Cleric" and p_pc.mana > 0 and p_pc.skill > 0:
                        hero = party_func.pick_hero(h_p)
                        p_pc.skill -= round(hero.atkbonus/(p_pc.level + p_pc.skill))
                        hero.atkbonus += p_pc.level + p_pc.skill
                        p_pc.mana -= 1
                        print ("Holy light surrounds", hero.name)
                elif "Summoner" in p_pc.name and p_pc.mana > 0:
                        for aly in p_npc:
                                aly.stats()
                        ally = party_func.pick_hero(p_npc)
                        ally.atk += p_pc.level
                        p_pc.mana -= ally.atk//p_pc.level
                        print (p_pc.name, "channels energy to", ally.name)
                elif "Hunter" in p_pc.name:
                        for ally in p_npc:
                                if "Spirit" in ally.name:
                                        ally.atk += p_pc.level
                                        print (p_pc.name, "signals to ", ally.name)
                        if weapon != None:
                                weapon.strength += 1
                                weapon.atk += 1
                                print (p_pc.name, "readies their weapon. ")
                        
                else:
                        if p_pc.skill > round(p_pc.atkbonus/p_pc.level):
                                p_pc.skill -= round(p_pc.atkbonus/p_pc.level)
                                p_pc.atkbonus += p_pc.level
                                print (p_pc.name, "focuses")
                        else:
                                print ("Nothing happens. ")
                        
        elif check.upper() == "S":
                weapon = party_func.check_equipment(p_pc, h_w)
                if p_pc.name == "Ninja":
                        monster = party_func.pick_monster(m_p)
                        monster.health -= p_pc.atk + p_pc.atkbonus + (p_pc.skill * weapon.atk)
                        print (p_pc.name, "appears behind", monster.name, "and strikes.")
                        p_pc.skill -= max((monster.skill + monster.defense), p_pc.skill)
                        weapon.atk = 0
                else:
                        print("The enemies stare at you as you try to run behind them. ")

        elif check.upper() == "P":
                armor = party_func.check_equipment(p_pc, h_a)
                if p_pc.name == "Knight":
                        armor.user = "Defender"
                        p_pc.name = "Defender"
                        p_pc.defbonus += 1
                        print(p_pc.name, "gets ready to block. ")
                elif p_pc.name == "Defender":
                        p_pc.defbonus += 1
                        print(p_pc.name, "gets ready to block. ")
                else:
                        print("Your body fails to shield your allies from view. ")
                        
        elif check.upper() == "E" and "Hunter" in p_pc.name:
                choice = input("Poison or Blast? P/B? ")
                if choice.upper() == "P":
                        bomb = Monster_NPC("Bomb", p_pc.skill * p_pc.level,
                                           0, 0, (p_pc.skill + p_pc.level), "Poison", 0)
                        copy_bomb = copy.copy(bomb)
                        m_p.append(copy_bomb)
                elif choice.upper() == "B":
                        bomb = Monster_NPC("Bomb", p_pc.skill * p_pc.level,
                                           0, 0, (p_pc.skill + p_pc.level), "Blast", 0)
                        copy_bomb = copy.copy(bomb)
                        m_p.append(copy_bomb)

        elif check.upper() == "J":
                if p_pc.name == "Cleric" and p_pc.level == C.LEVEL_LIMIT:
                        print("DIVINE JUDGEMENT STRIKES YOUR FOES")
                        for monster in m_p:
                                monster.health -= (p_pc.mana + p_pc.skill + p_pc.level)
                        p_pc.mana -= len(m_p)
                else:
                        print("The heavens ignore your call.")

        elif check.upper() == "W":
                if p_pc.name == "Mage" and p_pc.level == C.LEVEL_LIMIT:
                        p_pc.health -= max((p_pc.mana - p_pc.skill), len(m_p))
                        for x in range(0, len(m_p)):
                                monster = party_func.pick_random_healthy_monster(m_p)
                                monster.health -= (p_pc.mana + p_pc.level)
                                print("The magic flows wildly and hits", monster.name)
                else:
                        print("Nothing happened. ")
        elif check.upper() == "L":
                if p_pc.name == "Summoner" and p_pc.level == C.LEVEL_LIMIT and p_pc.skill > 0:
                        ally = None
                        for aly in p_npc:
                                if aly.name in L.ANGEL_NAMES:
                                        ally = aly
                        print(ally.name, " is empowered by your call.")
                        for x in range(0, (len(m_p))//2):
                                angel_func.angel_action(ally, h_p, m_p)
                        p_pc.mana -= len(m_p)
                        
                else:
                        print(" You allies briefly glances at you in confusion.")
        
        else:
                use_skill(p_pc, h_p, m_p, ib_pc, s_pc, p_npc, h_w, h_a)
                

