import random
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
def use_skill(p_pc, h_p, m_p, p_npc):
        print ("What skill do you want to use? ")
        print ("Observe enemies? O")
        print ("Command Summoned Ally? C")
        print ("Heal Ally? H")
        print ("Buff Ally? B")
        print ("Debuff Enemy? D")
        print ("Transmute fresh monster parts into GOLD? T")
        
        check = input("B/P/O/C/H/T")
        if check.upper() == "O":
                for monster in m_p:
                        monster.stats()
                        
        elif check.upper() == "C":
                if p_pc.name == "Summoner" and p_pc.level == C.LEVEL_LIMIT:
                        print(p_pc.name, "calls to", p_npc.name)
                        player_func.pet_action(p_npc, h_p, m_p)
                        player_func.pet_action(p_npc, h_p, m_p)
                        p_pc.health += p_pc.skill + p_pc.level
                elif p_pc.name == "Summoner":
                        print(p_pc.name, "calls to", p_npc.name)
                        player_func.pet_action(p_npc, h_p, m_p)
                else:
                        print(p_npc.name, "is too focused on the battle.")
                        
        elif check.upper() == "H":
                if p_pc.name == "Cleric":
                        hero = party_func.pick_hero(h_p)
                        hero.health += p_pc.mana+p_pc.skill
                        print (p_pc.name, "heals", hero.name)
                else:
                        print("Nothing happens.")
                        
        elif check.upper() == "D":
                if p_pc.name == "Cleric":
                        monster = party_func.pick_monster(m_p)
                        monster.atk = max((monster.atk-p_pc.mana-p_pc.skill),0)
                        p_pc.mana -= 1
                        print ("Holy strands wrap around", monster.name)
                else:
                        print("Nothing happens.")
        elif check.upper() == "B":
                if p_pc.name == "Cleric":
                        hero = party_func.pick_hero(h_p)
                        hero.atk = (hero.atk+p_pc.mana+p_pc.skill)
                        p_pc.mana -= 1
                        print ("Holy light surrounds", hero.name)
                else:
                        print("Nothing happens.")
                        
        elif check.upper() == "T":
                if p_pc.name == "Mage" and p_pc.mana > 0:
                        monster = party_func.pick_monster(m_p)
                        monster.dropchance += p_pc.level+p_pc.skill
                        p_pc.mana -= 1
                        print (p_pc.name, "changes some fresh", monster.name, "blood, into GOLD.")
                else:
                        print("You don't know how to do that. ")
                        
        elif check.upper() == "J":
                if p_pc.name == "Cleric" and p_pc.level == C.LEVEL_LIMIT:
                        print("DIVINE JUDGEMENT STRIKES YOUR FOES")
                        for monster in m_p:
                                monster.health -= (p_pc.mana + p_pc.skill + p_pc.level)
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
                if p_pc.name == "Summoner" and p_pc.level == C.LEVEL_LIMIT:
                        print(p_npc.name, "is empowered by your call.")
                        for x in range(1, len(m_p)):
                                player_func.pet_action(p_npc, h_p, m_p)
                else:
                        print(p_npc.name, "briefly glances at you in confusion.")
        else:
                use_skill(p_pc, h_p, m_p, p_npc)
                        
