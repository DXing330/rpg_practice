import copy
import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Monster_NPC, Armor_PC,
                                   ItemBag_PC, Spell_PC, Pet_NPC,
                                   Weapon_PC, Armor_PC)
from rpg2_constants import Constants
import rpg2_party_management_functions as party_func
C = Constants()
monsterList = ["Fire", "Water", "Air", "Earth", "Dark",
               "Demon", "Slime", "Skeleton", "Beast", "Elemental", "Troll"]
#function that checks what kind of passives a monster has
def monster_passive_effect(m_npc, p_pc, h_p, m_p):
        for passive in C.MONSTER_PASSIVE_LIST:
                if passive in m_npc.name:
                        if passive == "Fire":
                                p_pc.health -= m_npc.skill
                                print (p_pc.name, "is burned by", m_npc.name)
                        if passive == "Water":
                                p_pc.atkbonus -= min(m_npc.skill, p_pc.atkbonus)
                                print (p_pc.name, "is bogged down by", m_npc.name)
                        if passive == "Air":
                                p_pc.skill -= 1
                                print (p_pc.name, "is distracted by", m_npc.name)
                        if passive == "Earth":
                                m_npc.defense += m_npc.skill
                                print (m_npc.name, "hardens. ")
                        if passive == "Dark":
                                m_npc.skill += 1
                                print ("Darkness swirls around", m_npc.name)
                        if passive == "Demon":
                                for mon in m_p:
                                        m_npc.skill += 1
                                print (m_npc.name, "empowers its allies. ")
                        if passive == "Slime":
                                if m_npc.health > m_npc.skill:
                                        x = random.randint(0, len(m_p))
                                        if x == 0:
                                                m_npc.health = round(m_npc.health/2)
                                                copy_mon = copy.copy(m_npc)
                                                m_p.append(copy_mon)
                                                print (m_npc.name, "splits! ")
                        if passive == "Skeleton":
                                p_pc.defbonus -= min(m_npc.skill, p_pc.defbonus)
                                print (p_pc.name, " feels the ", 
                                       "decaying power of ", m_npc.name)
                        if passive == "Beast":
                                m_npc.atk += m_npc.skill
                                print (m_npc.name, "howls.")
                        if passive == "Elemental":
                                x = random.randint(0, 3)
                                if x == 0:
                                        m_npc.health += m_npc.skill
                                elif x == 1:
                                        m_npc.atk += m_npc.skill
                                elif x == 2:
                                        m_npc.defense += m_npc.skill
                                elif x == 3:
                                        m_npc.skill += 1
                                print (m_npc.name, "pulses erratically. ")
                        if passive == "Troll":
                                m_npc.health += m_npc.skill
                                print (m_npc.name, "regenerates. ")

monster_party = []
heroes_party = []
heroes_magic = []
heroes_weapons = []
heroes_armor = []
heroes_bag = ItemBag_PC(1, 1, 1, 10)
fireball = Spell_PC("Fireball", 3, 3, "Fire", 11)
rainstorm = Spell_PC("Rainstorm", 2, 3, "Water", 6)
earthspike = Spell_PC("Earthspike", 3, 1, "Earth", 4)
mage = Player_PC("Mage", 1, 10, 10, 2, 2, 3, 5, 5)
warrior = Player_PC("Warrior", 1, 15, 15, 5, 3, 3, 0, 0)
cleric = Player_PC("Cleric", 1, 10, 10, 1, 2, 0, 5, 5)
summoner = Player_PC("Summoner", 1, 10, 10, 2, 2, 0, 0, 0)
knight = Player_PC("Knight", 1, 20, 20, 3, 4, 3, 0, 0)
ninja = Player_PC("Ninja", 1, 10, 10, 3, 3, 5, 0, 0)
heroes_pet = Pet_NPC("Angel", 1, 2)
firemon = Monster_NPC("Fire Elemental", 100, 0, 0, 1, "Fire", 0)
watermon = Monster_NPC("Fire Earth", 100, 0, 0, 1, "Water", 0)
earthmon = Monster_NPC("Earth Troll", 100, 0, 0, 1, "Earth", 0)
#watermon = Monster_NPC("Mon", 100, 0, 0, 0, "Water", 0)
#earthmon = Monster_NPC("Mon", 100, 0, 0, 0, "Earth", 0)
nonemon = Monster_NPC("Nonemon", 0, 0, 0, 0, "None", 0)
armor = Armor_PC("None", "None", "None", 0, "None", 0)
weapon = Weapon_PC("None", "None", "None", 0, "None", 0)
heroes_magic.append(fireball)
heroes_magic.append(rainstorm)
heroes_magic.append(earthspike)
heroes_party.append(knight)
heroes_party.append(warrior)
heroes_party.append(ninja)
monster_party.append(firemon)
monster_party.append(watermon)
monster_party.append(earthmon)

#battle_phase(heroes_party, monster_party, heroes_pet, heroes_bag, heroes_magic)
warrior.stats()
monster_passive_effect(firemon, warrior, heroes_party, monster_party)
monster_passive_effect(watermon, warrior, heroes_party, monster_party)
monster_passive_effect(earthmon, warrior, heroes_party, monster_party)
warrior.stats()
