import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import Player_PC, Pet_NPC
from rpg2_constants import Constants
C = Constants()
#function which controls the levelling up of players
def level_up(p_pc):
        #check if the player is at the level limit
        if p_pc.level < C.LEVEL_LIMIT:
                p_pc.level += 1
                #adjust the player's stats according to their new level
                p_pc.atk += (p_pc.atk/(p_pc.level - 1))
                p_pc.defense += (p_pc.defense/(p_pc.level - 1))
                p_pc.maxhealth += (p_pc.maxhealth/(p_pc.level - 1))
                p_pc.skill += (p_pc.skill/(p_pc.level - 1))
                p_pc.maxmana += (p_pc.maxmana/(p_pc.level - 1))
        #if the player is already max level then nothing happens
        elif p_pc.level == C.LEVEL_LIMIT:
                print ("Sorry, it looks like you're already too strong.")


#function that levels up further
def prestige_level_up(p_pc):
        if p_pc.level < C.LEVEL_LIMIT * C.INCREASE_EXPONENT:
                p_pc.level += 1
                if "Knight" in p_pc.name:
                        p_pc.maxhealth += C.LVL_UP_HP_HIGH
                        p_pc.defense += C.LVL_UP_DEF_HIGH
                elif "Summoner" in p_pc.name:
                        p_pc.maxhealth += C.LVL_UP_HP_LOW
                        p_pc.maxmana += C.LVL_UP_MANA_MID
                elif "Mage" in p_pc.name:
                        p_pc.maxmana += C.LVL_UP_MANA_HIGH
                        p_pc.skill += C.LVL_UP_SKL_MID
                elif "Cleric" in p_pc.name:
                        p_pc.defense += C.LVL_UP_DEF_MID
                        p_pc.skill += C.LVL_UP_SKL_MID
                elif "Warrior" in p_pc.name:
                        p_pc.maxhealth += C.LVL_UP_HP_MID
                        p_pc.atk += C.LVL_UP_ATK_HIGH
                        p_pc.defense += C.LVL_UP_DEF_MID
                elif "Ninja" in p_pc.name:
                        p_pc.atk += C.LVL_UP_HP_LOW
                        p_pc.skill += C.LVL_UP_SKL_HIGH
                elif "Hunter" in p_pc.name:
                        p_pc.maxhealth += C.LVL_UP_HP_MID
                        p_pc.skill += C.LVL_UP_SKL_HIGH
                elif "Tactician" in p_pc.name:
                        p_pc.defense += C.LVL_UP_DEF_LOW
                        p_pc.skill += C.LVL_UP_SKL_HIGH
                elif "Hero" in p_pc.name:
                        p_pc.maxhealth += C.LVL_UP_HP_MID
                        p_pc.atk += C.LVL_UP_ATK_HIGH
                        p_pc.defense += C.LVL_UP_DEF_MID
                        p_pc.skill += C.LVL_UP_SKL_LOW
                        p_pc.maxmana += C.LVL_UP_MANA_MID
        else:
                print ("This is the limit of what I can do for you. ")

#function that changes the player's class into a prestige class
def prestige_class(p_pc):
        if p_pc.name == "Cleric":
                p_pc.name = "High Cleric"
        elif p_pc.name == "Warrior":
                p_pc.name = "Fierce Warrior"
        elif p_pc.name == "Summoner":
                p_pc.name = "Grand Summoner"
        elif p_pc.name == "Mage":
                p_pc.name = "Arch Mage"
        elif p_pc.name == "Knight":
                p_pc.name = "Royal Knight"
        elif p_pc.name == "Ninja":
                p_pc.name = "Shadow Ninja"
        elif p_pc.name == "Tactician":
                p_pc.name = "Master Tactician"
        elif p_pc.name == "Hunter":
                p_pc.name = "Monster Hunter"
        elif p_pc.name == "Hero":
                p_pc.name = "Chosen Hero"


#functions that increase player stats
def skill_up(p_pc):
        p_pc.skill += 1
def atk_up(p_pc):
        p_pc.atkbonus += 1
def def_up(p_pc):
        p_pc.defbonus += 1
def mana_up(p_pc):
        p_pc.mana += 1
#function that will increase the pet's stage
def angel_stage_up(p_npc):
        #check if the pet is at the stage limit
        if p_npc.stage < C.STAGE_LIMIT:
                p_npc.stage += 1
                #adjust the pet's atk according to it's new level
                p_npc.atk += round(p_npc.atk * C.PET_ATK_UP)
                if p_npc.stage == 2:
                        p_npc.name = "Awoken " + p_npc.name
                elif p_npc.stage == 3:
                        p_npc.name = "Mega " + p_npc.name
                elif p_npc.stage == 4:
                        p_npc.name = "Archangel"
                elif p_npc.stage == 5:
                        p_npc.name = "Guardian Angel"
                elif p_npc.stage == 6:
                        p_npc.name = "Legendary Guardian Angel"
        #if the pet is already fully evolved then nothing happens
        elif p_npc.stage == C.STAGE_LIMIT:
                print ("Sorry, it's already too powerful.")
def spirit_stage_up(p_npc):
        if p_npc.stage < C.STAGE_LIMIT:
                p_npc.stage += 1
                p_npc.atk += round(p_npc.atk * C.PET_ATK_UP)
                if p_npc.stage == 3:
                        p_npc.name = "Awoken Spirit"
                elif p_npc.stage == 6:
                        p_npc.name = "Guardian Spirit"
def pet_atk_up(p_npc):
        if p_npc.stage == C.STAGE_LIMIT:
                p_npc.atk += 1
        else:
                print ("It's not ready yet.")
