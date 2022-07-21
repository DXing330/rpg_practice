import random
import copy
import sys
sys.path.append("../RPG2v3_def")
sys.path.append("../RPG2v3_battle")
from rpg2_classdefinitions import (Player_PC, Monster_NPC, Pet_NPC,
                                   ItemBag_PC, Spell_PC, Weapon_PC,
                                   Armor_PC)
import rpg2_element_function as element_func
import rpg2_equipment_effect_function as ee_func
import rpg2_monster_function as monster_func
import rpg2_player_action_function as player_func
import rpg2_party_management_functions as party_func
from rpg2_constants import Constants
C = Constants()
from rpg2_boss_constants import BOSS_CONSTANTS
B = BOSS_CONSTANTS()
#this is the boss
#its special mechanic messing with the monster party order
#another monster will be a charmer
S_Q = Monster_NPC("Succubus Queen", B.S_Q_HEALTH, B.S_Q_ATK,
                           B.S_Q_DEF, B.S_Q_SKL, "Dark",
                           B.S_Q_DC)
b_p = []
#succubus illusion maker
def illusion_maker():
        monster = Monster_NPC("Beauty", 1, 1, 1, 0, "Dark", 0)
        return monster
def sq_illusion_maker():
        monster = Monster_NPC("Sucubus Queen", 1, 1, 1, 0, "Dark", 0)
        return monster
#illusion action
def monster_action(m_npc, h_p):
        hero = party_func.pick_random_healthy_hero(h_p)
        hero.poison += 1
        x = random.randint(0, 3)
        if x == 0:
                print (m_npc.name, "blows a kiss at ", hero.name)
        elif x == 1:
                print (m_npc.name, "winks at ", hero.name)
        elif x == 2:
                print (m_npc.name, "waves at ", hero.name)
        elif x == 3:
                print (m_npc.name, "beckons", hero.name)
#phase one actions
def sq_phase_one_action(m_npc, h_p, b_p, ib_pc):
        if m_npc.health < B.S_Q_HEALTH * (C.BUFF ** ib_pc.sq_trophy):
                print ("Don't be so rough. We have plenty of time. ")
        print ("Come on out girls, greet our new friends. ")
        for hero in h_p:
                if hero.name != "Totem":
                        mon = illusion_maker()
                        b_p.append(mon)
                        print (mon.name, "steps out from behind a curtain and smiles at", hero.name)
                elif hero.name == "Totem":
                        hero.health -= m_npc.atk
                        print (m_npc.name, "kickes ", hero.name, "aside.")
                        print ("Sorry we don't allow toys from outside. ")
        print ("Now it looks like we have enough girls. ")
        print ("Don't worry, there's plenty to go around. ")
        print ("See any that catch your eye? ")
        hero = party_func.pick_random_healthy_hero(h_p)
        hero.poison += m_npc.skill
        print (m_npc.name, "sprays some perfume around", hero.name)
        print ("Don't you just smell lovely now? ")
        for hro in h_p:
                if hro.name != "Totem":
                        hro.poison += 1
                        print ("The perfume's scent spreads to ", hro.name)
        
#phase one
#the succubus will try to lure the heroes to her side
def sq_phase_one(h_p, b_p, new_h_s, ib_pc, s_pc, h_w, h_a):
        bPhase1 = True
        while bPhase1:
                for mon in b_p:
                        if mon.name == "Succubus Queen" and mon.health == B.S_Q_HEALTH * (C.BUFF ** ib_pc.sq_trophy):
                                if ib_pc.sq_trophy == 0:
                                        print ("New visitors? ")
                                        print ("Please make yourselves comfortable. ")
                                elif ib_pc.sq_trophy < B.ADVANCED_SPAWN:
                                        print ("You again? ")
                                        print ("Want to play nice this time? ")
                                elif ib_pc.sq_trophy >= B.ADVANCED_SPAWN:
                                        x = random.randint(0, ib_pc.sq_trophy)
                                        if x < B.ADVANCED_SPAWN + (ib_pc.sq_trophy/2):
                                                print ("I've about had it with you! ")
                                                print ("You always ruin it when I'm having a good time. ")
                                                print ("STOP FOLLOWING ME! ")
                                                sq_phase_two(h_p, b_p, new_h_s, ib_pc, s_pc, h_w, h_a)
                                        else:
                                                print ("Ugh, you again. Please just relax. ")
                                                print ("You know that I just want to have a little fun. ")
                        if mon.name == "Succubus Queen" and mon.health <= (B.S_Q_HEALTH * (C.BUFF ** ib_pc.sq_trophy)) * B.S_Q_HPBP:
                                print ("And I was being so nice to you too. ")
                                print ("I just wanted to have a bit of fun. ")
                                bPhase1 = False
                                
                if len(h_p) == 0:
                        print ("The heroes have been routed and flee back to town.")
                        bPhase1 = False

                else:
                        for hero in h_p:
                                if hero.poison > hero.skill + hero.level:
                                        h_p.remove(hero)
                                        print (hero.name, "can't resist anymore. ")
                                        print (hero.name, "runs into the mob of pleasure. ")
                                elif hero.health > 0 and hero.name != "Totem":
                                        hero.stats()
                                        player_func.player_action(hero, h_p, b_p,
                                                                  ib_pc, s_pc, new_h_s,
                                                                  h_w, h_a)
                                elif hero.health <= 0:
                                        h_p.remove(hero)
                                        
                        player_func.pet_action(new_h_s, h_p, b_p)
                        
                        for mon in b_p:
                                if mon.health > 0 and mon.name == "Succubus Queen":
                                        monster_action(mon, h_p)
                                        sq_phase_one_action(mon, h_p, b_p, ib_pc)
                                elif mon.health > 0 and mon.name != "Succubus Queen":
                                        monster_action(mon, h_p)
                                elif mon.health <= 0 and mon.name != "Succubus Queen":
                                        b_p.remove(mon)
                                        
                for mon in b_p:
                        if mon.name == "Succubus Queen" and mon.health <= (B.S_Q_HEALTH * (C.BUFF ** ib_pc.sq_trophy)) * B.S_Q_HPBP:
                                print ("And I was being so nice to you too. ")
                                print ("I just wanted to have a bit of fun. ")
                                bPhase1 = False


                        
                        
#phase two actions
#in phase two the sq will make illusions, making it harder to hit her
def sq_phase_two_action(m_npc, h_p, b_p, h_a):
        print ("Seems like you're just interested in me. ")
        print ("Then how about some more of me? ")
        x = random.randint(0, len(b_p))
        mon = sq_illusion_maker()
        b_p.insert(x, mon)
        m_npc.atk += m_npc.skill
        m_npc.skill += 1
        hero = party_func.pick_random_healthy_hero(h_p)
        armor = party_func.check_equipment(hero, h_a)
        new_atk = ee_func.armor_effect(m_npc, hero, armor, h_p, b_p)
        new_m_atk = element_func.check_element_monster_attack(m_npc, new_atk, armor)
        hero.health -= max((new_m_atk - hero.defense - hero.defbonus), 1)
        print (m_npc.name, "slashes at", hero.name)
        hero.atk -= min(m_npc.skill, hero.atk)
        print (m_npc.name, " uses their poison claws to make", hero.name, "drowsy. ")
        hero = party_func.pick_random_healthy_hero(h_p)
        armor = party_func.check_equipment(hero, h_a)
        new_atk = ee_func.armor_effect(m_npc, hero, armor, h_p, b_p)
        new_m_atk = element_func.check_element_monster_attack(m_npc, new_atk, armor)
        hero.health -= max((new_m_atk - hero.defense - hero.defbonus), 1)
        print (m_npc.name, "slashes at", hero.name)
        hero.defense -= min(m_npc.skill, hero.defense)
        print (m_npc.name, " uses their poison claws to make", hero.name, "relaxed. ")
        
#phase two
#the succubus will try to attack and knock out the heroes
def sq_phase_two(h_p, b_p, new_h_s, ib_pc, s_pc, h_w, h_a):
        bPhase2 = True
        while bPhase2:
                                
                if len(h_p) == 0:
                        print ("The heroes have been defeated and dragged deeper into the castle. ")
                        bPhase2 = False

                else:
                        for hero in h_p:
                                if hero.poison > hero.skill + hero.level:
                                        h_p.remove(hero)
                                        print (hero.name, "can't resist anymore. ")
                                        print (hero.name, "runs into the mob of pleasure. ")
                                elif hero.health > 0 and hero.name != "Totem":
                                        hero.stats()
                                        player_func.player_action(hero, h_p, b_p,
                                                                  ib_pc, s_pc, new_h_s,
                                                                  h_w, h_a)
                                elif hero.health <= 0:
                                        h_p.remove(hero)
                                        
                        player_func.pet_action(new_h_s, h_p, b_p)

                        for mon in b_p:
                                if mon.name == "Succubus Queen" and mon.health > 0:
                                        sq_phase_two_action(mon, h_p, b_p)
                                elif mon.name != "Succubus Queen" and mon.health > 0:
                                        monster_action(mon, h_p)
                                elif mon.health <= 0 and mon.name != "Succubus Queen":
                                        b_p.remove(mon)

                for mon in b_p:
                        if mon.name == "Succubus Queen" and mon.health <= 0:
                                print ("Fine, I was tired out this stupid town anyway! ")
                                print ("I hope I never see you again! ")
                                bPhase2 = False

#phases will change according to boss hp
#this battle is a dps rush, aiming to kill the slime before it can split too much                                               
def boss_battle(h_p, b_p, h_s, ib_pc, s_pc, h_w, h_a):
        #make a copies of the party as usual
        b_p = []
        Succubus_Queen = copy.copy(S_Q)
        Succubus_Queen.health = round(Succubus_Queen.health * (C.BUFF ** ib_pc.sq_trophy))
        b_p.append(Succubus_Queen)
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
                        if mon.name == "Succubus Queen" and mon.health <= 0:
                                print("The Succubus Queen has been defeated. ")
                                print("The men are safe... ")
                                print("from the monsters. ")
                                print("Whether they're safe from their wives is another story. ")
                                bBattle = False
                                ib_pc.coins += round(mon.dropchance)
                                ib_pc.sq_trophy += 1
                                new_b_p.remove(mon)
                        elif mon.name != "Succubus Queen":
                                new_b_p.remove(mon)
                if len(new_h_p) == 0:
                        print ("The heroes are eventually found asleep by the road. ")
                        print ("Their minds are dazed but after awhile they recover. ")
                        bBattle = False
                elif len(new_b_p) == 0:
                        print ("The heroes return with some fancy and valuable perfumes. ")

                else:
                        for mon in new_b_p:
                                if mon.name == "Succubus Queen" and mon.health >= (B.S_Q_HEALTH * (C.BUFF ** ib_pc.sq_trophy)) * B.S_Q_HPBP:
                                        print ("The smell of perfume is overpowering as you enter the castle. ")
                                        sq_phase_one(new_h_p, new_b_p, new_h_s, ib_pc,
                                                     s_pc, new_h_w, new_h_a)
                                elif mon.name == "Succubus Queen" and mon.health < (B.S_Q_HEALTH * (C.BUFF ** ib_pc.sq_trophy)) * B.S_Q_HPBP and mon.health > 0:
                                        print ("The Succubus Queen reveals her true form! ")
                                        print ("Her wings stretch and her claws extend! ")
                                        sq_phase_two(new_h_p, new_b_p, new_h_s, ib_pc,
                                                     s_pc, new_h_w, new_h_a)

        if not bBattle:
                #adjust the hp of the heroes after battles
                for hero in h_p:
                        check = None
                        for heero in new_h_p:
                                if hero.name == heero.name:
                                        check = heero
                        if check == None:
                                        hero.health = 0
                                        hero.mana = 0
                        elif check != None:
                                        hero.health = min(check.health, hero.maxhealth)
                                        hero.mana = min(check.mana, hero.maxmana)
