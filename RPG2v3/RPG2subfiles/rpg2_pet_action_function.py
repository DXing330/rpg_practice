import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC)
import rpg2_party_management_functions as party_func
import rpg2_player_skill_function as pskill_func
from rpg2_constants import Constants
C = Constants()
#function that controls what the pet will do during battle
#need to input the pet and both parties
def pet_random_action(p_npc, h_p, m_p):
        z = random.randint(0, p_npc.stage)
        if z == 0:
                hero = party_func.pet_pick_random_injured_hero(h_p)
                hero.health = min((hero.health + round(p_npc.atk ** C.PET_HP_BUFF)), hero.maxhealth)
                print (p_npc.name, "uses their healing magic on", hero.name)
                hero = party_func.pet_pick_random_injured_hero(h_p)
                hero.health = min((hero.health + round(p_npc.atk ** C.PET_HP_BUFF)), hero.maxhealth)
                print (p_npc.name, "uses their healing magic on", hero.name)
        elif z == 1:
                monster = party_func.pick_random_healthy_monster(m_p)
                monster.health -= max((p_npc.atk - monster.defense), 1)
                print (p_npc.name, "uses their attacking magic on", monster.name)
                hero = party_func.pet_pick_random_injured_hero(h_p)
                hero.health = min((hero.health + round(p_npc.atk ** C.PET_HP_BUFF)), hero.maxhealth)
                print (p_npc.name, "uses their healing magic on", hero.name)
        elif z == 2:
                hero = party_func.pet_pick_random_healthy_hero(h_p)
                hero.maxhealth += round(p_npc.atk ** C.PET_HP_BUFF)
                hero.atk += round(p_npc.atk ** C.PET_ATK_BUFF)
                hero.defense += round(p_npc.atk ** C.PET_DEF_BUFF)
                hero.skill += round(p_npc.atk ** C.PET_SKILL_BUFF)
                print (p_npc.name, "uses their blessing magic on", hero.name)
        elif z == 3:
                monster = party_func.pick_random_healthy_monster(m_p)
                monster.atk = max(monster.atk - round(p_npc.atk ** C.PET_ATK_BUFF), 0)
                monster.defense = max(monster.defense - round(p_npc.atk ** C.PET_DEF_BUFF), 0)
                print (p_npc.name, "uses their weakening magic on", monster.name)
        elif z == 4:
                hero = party_func.pet_pick_random_healthy_hero(h_p)
                hero.maxhealth += round(p_npc.atk ** C.PET_HP_BUFF)
                hero.atk += round(p_npc.atk ** C.PET_ATK_BUFF)
                hero.defense += round(p_npc.atk ** C.PET_DEF_BUFF)
                hero.skill += round(p_npc.atk ** C.PET_SKILL_BUFF)
                print (p_npc.name, "uses their blessing magic on", hero.name)
                hero = party_func.pet_pick_random_healthy_hero(h_p)
                hero.maxhealth += round(p_npc.atk ** C.PET_HP_BUFF)
                hero.atk += round(p_npc.atk ** C.PET_ATK_BUFF)
                hero.defense += round(p_npc.atk ** C.PET_DEF_BUFF)
                hero.skill += round(p_npc.atk ** C.PET_SKILL_BUFF)
                print (p_npc.name, "uses their blessing magic on", hero.name)
        elif z == 5:
                monster = party_func.pick_random_healthy_monster(m_p)
                monster.atk = max(monster.atk - round(p_npc.atk ** C.PET_ATK_BUFF), 0)
                monster.defense = max(monster.defense - round(p_npc.atk ** C.PET_DEF_BUFF), 0)
                print (p_npc.name, "uses their weakening magic on", monster.name)
                monster = party_func.pick_random_healthy_monster(m_p)
                monster.atk = max(monster.atk - round(p_npc.atk ** C.PET_ATK_BUFF), 0)
                monster.defense = max(monster.defense - round(p_npc.atk ** C.PET_DEF_BUFF), 0)
                print (p_npc.name, "uses their weakening magic on", monster.name)
        elif z == 6:
                print (p_npc.name, "uses their legendary spell on the battlefield. ")
                for hero in h_p:
                        if hero.name != "Golem":
                                hero.maxhealth += round(p_npc.atk ** C.PET_HP_BUFF)
                                hero.atk += round(p_npc.atk ** C.PET_ATK_BUFF)
                                hero.defense += round(p_npc.atk ** C.PET_DEF_BUFF)
                                hero.skill += round(p_npc.atk ** C.PET_SKILL_BUFF)
                                hero.health = min(hero.health + round(p_npc.atk ** C.PET_HP_BUFF), hero.maxhealth)
                for monster in m_p:
                        monster.atk = max(monster.atk - round(p_npc.atk ** C.PET_ATK_BUFF), 0)
                        monster.defense = max(monster.defense - round(p_npc.atk ** C.PET_DEF_BUFF), 0)
                        
                        
