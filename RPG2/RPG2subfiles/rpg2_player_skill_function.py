import random
import copy
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC)
import rpg2_player_action_function as player_func
import rpg2_party_management_functions as party_func
from rpg2_constants import Constants
C = Constants()
#function which controls what skills the player can use
#need the hero, heroes_party, monster_party, pet for now
def use_skill(p_pc, h_p, m_p, ib_pc, s_pc, p_npc):
        
        print ("What skill do you want to use? ")
        print ("OBSERVE enemies? O")
        print ("COMMAND? C")
        print ("HEAL Ally? H")
        print ("BUFF? B")
        print ("DEBUFF Enemy? D")
        print ("Summon GOLEM? G")
        print ("PROTECT your allies? P")
        print ("Try to go for a SNEAK ATTACK? S")
        
        check = input("B/P/O/C/S/H/D/G")
        if check.upper() == "G":
                if p_pc.name == "Summoner" and p_pc.mana > 0:
                        print("What kind of golem do you make? ")
                        print("ATTACK, HEAL, BUFF, DEBUFF? ")
                        choice = input("A/B/D/H? ")
                        if choice.upper() == "A":
                                atkgolem = Player_PC("Golem", 1, p_pc.skill, p_pc.skill, 1, 0, 0, 0)
                                totem = copy.copy(atkgolem)
                                h_p.append(totem)
                                p_pc.skill -= 1
                                p_pc.mana -= 1
                        elif choice.upper() == "B":
                                bufgolem = Player_PC("Golem", 1, p_pc.skill, p_pc.skill, 0, 0, 1, 0)
                                totem = copy.copy(bufgolem)
                                h_p.append(totem)
                                p_pc.skill -= 1
                                p_pc.mana -= 1
                        elif choice.upper() == "D":
                                debufgolem = Player_PC("Golem", 1, p_pc.skill, p_pc.skill, 0, 0, 0, 1)
                                totem = copy.copy(debufgolem)
                                h_p.append(totem)
                                p_pc.skill -= 1
                                p_pc.mana -= 1
                        elif choice.upper() == "H":
                                healgolem = Player_PC("Golem", 1, p_pc.skill, p_pc.skill, 0, 1, 0, 0)
                                totem = copy.copy(healgolem)
                                h_p.append(totem)
                                p_pc.skill -= 1
                                p_pc.mana -= 1
                        else:
                                print("You don't know how to make that kind of golem. ")
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
                for monster in m_p:
                        monster.stats()
                for hero in h_p:
                        hero.stats()
                        
        elif check.upper() == "C":
                if p_pc.name == "Summoner" and p_pc.level == C.LEVEL_LIMIT and p_pc.skill > 0:
                        print(p_pc.name, "calls to", p_npc.name)
                        player_func.pet_action(p_npc, h_p, m_p)
                        player_func.pet_action(p_npc, h_p, m_p)
                        p_pc.health += min((p_pc.skill + p_pc.level), (p_pc.maxhealth - p_pc.health))
                        p_pc.skill -= 1
                elif p_pc.name == "Summoner":
                        print(p_pc.name, "calls to", p_npc.name)
                        player_func.pet_action(p_npc, h_p, m_p)
                elif p_pc.name == "Tactician":
                        p_pc.skill -= 1
                        hero = party_func.pick_hero(h_p)
                        if hero.name != "Tactician":
                                hero.stats()
                                player_func.player_action(hero, h_p, m_p, ib_pc, s_pc, p_npc)
                else:
                        print("Your allies are too focused on the battle.")
                        
        elif check.upper() == "H":
                if p_pc.name == "Cleric":
                        hero = party_func.pick_hero(h_p)
                        hero.health += max(p_pc.mana+p_pc.skill+p_pc.level, 1)
                        hero.poison -= min(p_pc.skill+p_pc.level, hero.poison)
                        print (p_pc.name, "heals", hero.name)
                elif p_pc.name == "Ninja" and p_pc.weapon > 0:
                        print (p_pc.name, "throws away his weapon and disappears into the shadows.")
                        p_pc.health += min(p_pc.skill, (p_pc.maxhealth - p_pc.health))
                        p_pc.skill = 0
                else:
                        if p_pc.skill >= p_pc.level:
                                hero = party_func.pick_hero(h_p)
                                x = hero.poison
                                hero.poison -= min(p_pc.level, x)
                                p_pc.skill -= p_pc.level
                        else:
                                hero = party_func.pick_hero(h_p)
                                hero.poison = hero.poison * C.BUFF
                        print (p_pc.name, " tries to heal", hero.name)
                        
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
                elif p_pc.name == "Cleric":
                        monster = party_func.pick_monster(m_p)
                        monster.atk = max((monster.atk-p_pc.mana-p_pc.skill),0)
                        p_pc.mana -= 1
                        p_pc.skill -= 1
                        print ("Holy strands wrap around", monster.name)
                else:
                        print("Nothing happens.")
        elif check.upper() == "B":
                if p_pc.name == "Ninja":
                        p_pc.skill = round(p_pc.skill * C.BUFF)
                        print (p_pc.name, "sharpens their senses. ")
                        p_pc.mana -= 1
                elif p_pc.name == "Knight" and p_pc.skill > 0:
                        p_pc.defense += p_pc.level + max(p_pc.skill, 1)
                        p_pc.armor += max(p_pc.skill, 1) 
                        p_pc.skill -= 1
                        print (p_pc.name, "fortifies their position. ")
                elif p_pc.name == "Defender" and p_pc.skill > 0:
                        p_pc.defense += max(p_pc.skill, 1)
                        p_pc.armor += 1
                        p_pc.skill -= 1
                        print (p_pc.name, "fortifies their position. ")
                elif p_pc.name == "Cleric":
                        hero = party_func.pick_hero(h_p)
                        hero.atk += p_pc.mana+p_pc.skill
                        p_pc.mana -= 1
                        p_pc.skill -= 1
                        print ("Holy light surrounds", hero.name)
                else:
                        print("Nothing happens.")
                        

        elif check.upper() == "S":
                if p_pc.name == "Ninja":
                        monster = party_func.pick_monster(m_p)
                        monster.health -= p_pc.atk + (p_pc.skill * p_pc.weapon)
                        print (p_pc.name, "appears behind", monster.name, "and strikes.")
                        p_pc.skill -= max((monster.skill + monster.defense), p_pc.skill)
                else:
                        print("The enemies stare at you as you try to run behind them. ")

        elif check.upper() == "P":
                if p_pc.name == "Knight":
                        p_pc.name = "Defender"
                        p_pc.armor = round(p_pc.armor * C.BUFF) + 1
                        p_pc.skill -= min(1, p_pc.skill)
                        print(p_pc.name, "gets ready to block. ")
                elif p_pc.name == "Defender":
                        p_pc.armor += 1
                        print(p_pc.name, "gets ready to block. ")
                else:
                        print("Your body fails to shield your allies from view. ")

        elif check.upper() == "J":
                if p_pc.name == "Cleric" and p_pc.level == C.LEVEL_LIMIT:
                        print("DIVINE JUDGEMENT STRIKES YOUR FOES")
                        for monster in m_p:
                                monster.health -= (p_pc.mana + p_pc.skill + p_pc.level)
                        p_pc.mana = round(p_pc.mana/(C.BUFF ** len(m_p)))
                else:
                        print("The heavens ignore your call.")

        elif check.upper() == "W":
                if p_pc.name == "Mage" and p_pc.level == C.LEVEL_LIMIT:
                        p_pc.health -= (p_pc.mana - p_pc.skill)
                        for x in range(1, len(m_p)):
                                monster = party_func.pick_random_healthy_monster(m_p)
                                monster.health -= (p_pc.mana + p_pc.level)
                                print("The magic flows wildly and hits", monster.name)
                else:
                        print("Nothing happened. ")
        elif check.upper() == "L":
                if p_pc.name == "Summoner" and p_pc.level == C.LEVEL_LIMIT and p_pc.mana > 0 and p_pc.skill > 0:
                        print(p_npc.name, "is empowered by your call.")
                        for x in range(0, len(m_p)):
                                player_func.pet_action(p_npc, h_p, m_p)
                        p_pc.skill -= len(m_p)
                        p_pc.mana -= len(m_p)
                else:
                        print(p_npc.name, "briefly glances at you in confusion.")
        else:
                use_skill(p_pc, h_p, m_p, ib_pc, s_pc, p_npc)
                

