import random
import copy
import sys
sys.path.append("../RPG2v3_def")
sys.path.append("../RPG2v3_battle")
from rpg2_classdefinitions import (Player_PC, Monster_NPC,
                                   Pet_NPC, ItemBag_PC, Spell_PC)
import rpg2_player_action_function as player_func
import rpg2_party_management_functions as party_func
from rpg2_constants import Constants
C = Constants()
from rpg2_boss_constants import BOSS_CONSTANTS
B = BOSS_CONSTANTS()
#this is the boss
G_S = Monster_NPC("Golden Slime", B.GOLDEN_SLIME_HEALTH, B.GOLDEN_SLIME_ATK,
                           B.GOLDEN_SLIME_DEFENSE, B.GOLDEN_SLIME_SKILL, "Water",
                           B.GOLDEN_SLIME_DROPCHANCE)
b_p = []
#smaller slime monster maker
def baby_slime_spawn():
        monster = Monster_NPC("Baby Golden Slime", C.MONSTER_MAX_HP, 0, 0, 0, "Water", 0)
        return monster
#slime monster maker function
def slime_spawn():
        monster = Monster_NPC("Mini Golden Slime", 2 * C.MONSTER_MAX_HP, 0, 0, 0, "Water", 0)
        return monster
#slime monster actions
def gs_slime_action(m_npc, h_p, m_p):
        #slime chooses from a random pool of actions
        x = random.randint(0, 3)
        #the slime can regenerate by absorbing gold from the Golden Slime
        if x == 0:
                for mon in m_p:
                        mon.dropchance -= B.G_S_DC_DOWN
                m_npc.health += m_npc.health
                print (m_npc.name, "absorbs some gold. ")
        #the slime can split into two slimes
        elif x == 1:
                m_npc.health = round(m_npc.health * 0.5)
                mon = copy.copy(m_npc)
                m_p.append(mon)
                print (m_npc.name, "copies itself. ")
        #the slime can explode, hurting the heroes
        elif x == 2:
                for hero in h_p:
                        hero.health -= max((m_npc.health - hero.defense -
                                            hero.defbonus - hero.skill), 0)
                print(m_npc.name, "explodes.")
                m_npc.health = 0

#phase one actions
def gs_phase_one_action(m_npc, h_p, b_p, ib_pc):
        #if the players wait too long to set up then the slime will bounce
        if m_npc.health >= B.G_S_H * (C.BUFF ** ib_pc.gs_trophy) * 0.9 and m_npc.skill >= B.G_S_EXECUTE_TIMER/2:
                for hero in h_p:
                        hero.health -= m_npc.dropchance + m_npc.health
                print(m_npc.name, "bounces! ")
                print("The wave of gold consumes everything nearby. ")
        #every turn the slime remains about 90% hp its timer increases
        elif m_npc.health >= B.G_S_H * (C.BUFF ** ib_pc.gs_trophy) * 0.9:
                m_npc.skill += 1
                print(m_npc.name, "seems to wiggle. ")
        #otherwise the slime will spawn other slimes
        elif B.G_S_H * (C.BUFF ** ib_pc.gs_trophy) * 0.5 <= m_npc.health < B.G_S_H * (C.BUFF ** ib_pc.gs_trophy) * 0.9:
                mon = slime_spawn()
                b_p.append(mon)
                m_npc.dropchance -= B.G_S_DC_DOWN
                m_npc.health -= B.G_S_DC_DOWN
                print(mon.name, "splits off from", m_npc.name)

#phase one
def gs_phase_one(h_p, b_p, new_h_s, ib_pc, s_pc, h_w, h_a):
        bPhase1 = True
        while bPhase1:
                for mon in b_p:
                        if mon.name == "Golden Slime" and mon.dropchance <= 0:
                                bPhase1 = False
                        elif mon.name == "Golden Slime" and mon.health <= (B.GOLDEN_SLIME_HEALTH * (C.BUFF ** ib_pc.gs_trophy))/2:
                                bPhase1 = False
                if len(h_p) == 0:
                        print ("The heroes have been routed and flee back to town.")
                        bPhase1 = False

                else:
                        for hero in h_p:
                                if hero.health > 0 and hero.name != "Totem":
                                        hero.stats()
                                        player_func.player_action(hero, h_p, b_p,
                                                                  ib_pc, s_pc, new_h_s,
                                                                  h_w, h_a)
                                elif hero.health <= 0:
                                        h_p.remove(hero)
                                        
                        player_func.pet_action(new_h_s, h_p, b_p)
                        
                        for monster in b_p:
                                if monster.health <= 0 and monster.name != "Golden Slime":
                                        b_p.remove(monster)
                        for monster in b_p:
                                if monster.name == "Golden Slime":
                                        gs_phase_one_action(monster, h_p, b_p, ib_pc)
                                elif monster.health > 0:
                                        gs_slime_action(monster, h_p, b_p)
                                elif monster.health <= 0 and monster.name != "Golden Slime":
                                        b_p.remove(monster)
#phase two actions
def gs_phase_two_action(m_npc, h_p, b_p):
        if m_npc.health > 0:
                m_npc.dropchance -= B.G_S_DC_DOWN
                m_npc.health -= B.G_S_DC_DOWN
                mon = baby_slime_spawn()
                b_p.append(mon)
                print(mon.name, "splits off from", m_npc.name)
                mon = baby_slime_spawn()
                b_p.append(mon)
                print(mon.name, "splits off from", m_npc.name)
                mon = baby_slime_spawn()
                b_p.append(mon)
                print(mon.name, "splits off from", m_npc.name)
        else:
                print ("The golden slime begins to deflate. ")
        
#phase two
def gs_phase_two(h_p, b_p, new_h_s, ib_pc, s_pc, h_w, h_a):
        bPhase2 = True
        while bPhase2:
                for mon in b_p:
                        if mon.name == "Golden Slime" and mon.dropchance <= 0:
                                bPhase2 = False
                        elif mon.name == "Golden Slime" and mon.health <= 0:
                                bPhase2 = False
                if len(h_p) == 0:
                        print ("The heroes have been routed and flee back to town.")
                        bPhase2 = False

                else:
                        for hero in h_p:
                                if hero.health > 0 and hero.name != "Totem":
                                        hero.stats()
                                        player_func.player_action(hero, h_p, b_p,
                                                                  ib_pc, s_pc, new_h_s,
                                                                  h_w, h_a)
                                elif hero.health <= 0:
                                        h_p.remove(hero)
                        player_func.pet_action(new_h_s, h_p, b_p)
                        for monster in b_p:
                                if monster.health <= 0 and monster.name != "Golden Slime":
                                        b_p.remove(monster)
                        for monster in b_p:
                                if monster.name == "Golden Slime" and monster.health > 0:
                                        gs_phase_two_action(monster, h_p, b_p)
                                elif monster.health > 0:
                                        gs_slime_action(monster, h_p, b_p)
                                elif monster.health <= 0 and monster.name != "Golden Slime":
                                        b_p.remove(monster)
#phases will change according to boss hp
#this battle is a dps rush, aiming to kill the slime before it can split too much                                               
def boss_battle(h_p, b_p, h_s, ib_pc, s_pc, h_w, h_a):
        #make a copies of the party as usual
        b_p = []
        Golden_Slime = copy.copy(G_S)
        #buff the enemy depending on how many times you beat it
        Golden_Slime.health = round(Golden_Slime.health * (C.BUFF ** ib_pc.gs_trophy))
        b_p.append(Golden_Slime)
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
        new_b_p = list(b_p)
        #boolean to loop the battle phase until it finishes
        bBattle = True
        while bBattle:
                #check if the battle continues
                for mon in new_b_p:
                        if mon.name == "Golden Slime" and mon.dropchance <= 0:
                                print("The Golden Slime has escaped. ")
                                print("The heroes return emptyhanded and covered in slime. ")
                                print("The local economy never recovers from the massive influx of gold. ")
                                new_b_p.remove(mon)
                                bBattle = False
                        elif mon.name == "Golden Slime" and mon.dropchance >= B.GOLDEN_SLIME_DROPCHANCE/2 and mon.health <= 0:
                                print("The Golden Slime has been defeated. ")
                                print("The hero's make it out with", mon.dropchance, "coins. ")
                                print("They heroically take the gold far away from this small village.")
                                print("The local economy is saved. ")
                                bBattle = False
                                ib_pc.coins += mon.dropchance
                                ib_pc.gs_trophy += 1
                                new_b_p.remove(mon)
                        elif mon.name == "Golden Slime" and mon.dropchance < B.GOLDEN_SLIME_DROPCHANCE/2 and mon.health <= 0:
                                print("The Golden Slime has been defeated. ")
                                print("The hero's make it out with", mon.dropchance, "coins. ")
                                print("Sadly, the slime split enough to potentially reform. ")
                                print("The locals always fear another massive influx of gold. ")
                                bBattle = False
                                ib_pc.coins += mon.dropchance
                                new_b_p.remove(mon)
                        elif mon.name != "Golden Slime":
                                new_b_p.remove(mon)
                if len(new_h_p) == 0:
                        print ("The heroes have been routed and flee back to town.")
                        bBattle = False
                elif len(new_b_p) == 0:
                        print ("The heroes go back to clean their golden and sticky equipment. ")

                else:
                        for mon in new_b_p:
                                if mon.name == "Golden Slime" and mon.health >= (B.GOLDEN_SLIME_HEALTH * (C.BUFF ** ib_pc.gs_trophy))/2:
                                        print("Glug, glurp, splish! ")
                                        gs_phase_one(new_h_p, new_b_p, new_h_s, ib_pc, s_pc, new_h_w, new_h_a)
                                elif mon.name == "Golden Slime" and mon.health < (B.GOLDEN_SLIME_HEALTH * (C.BUFF ** ib_pc.gs_trophy))/2 and mon.health > 0:
                                        print("Glurgh, Splash, Sploosh! ")
                                        gs_phase_two(new_h_p, new_b_p, new_h_s, ib_pc, s_pc, new_h_w, new_h_a)
        if not bBattle:
                #adjust the hp of the heroes after battles
                for hero in h_p:
                        check = None
                        for heero in new_h_p:
                                if hero.name == heero.name:
                                        check = heero
                        #if there is no matching hero then the hero's health goes to zero
                        if check == None:
                                hero.health = 0
                        #if there is a matching hero then the hero's health becomes equal
                        elif check != None:
                                hero.health = min(check.health, hero.maxhealth)
                                

