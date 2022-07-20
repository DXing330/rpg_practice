import json
import sys
sys.path.append("./RPG2v3_def")
from rpg2_classdefinitions import (Player_PC, Monster_NPC, Pet_NPC,
                                   ItemBag_PC, Spell_PC,
                                   Weapon_PC, Armor_PC,
                                   QuestItems_NPC, Access_NPC)
PREFIX = "RPG2_"
HEROES_FILE = "heroes"
HEROES_MAGIC_FILE = "spellbook"
HEROES_BAG_FILE = "itembag"
HEROES_ALLY_FILE = "heroesally"
HEROES_WEAPONS_FILE = "heroesweapons"
HEROES_ARMOR_FILE = "heroesarmor"
QUEST_FILE = "questitems"
ACCESS_FILE = "accessitems"
# Using a JSON string to save a list of players to a file
#the list only has one type of objects, which is Player
#convert players data to JSON string
def write_object(obj, fileName):
    jsonP = json.dumps(obj.__dict__)
    outfile = open(fileName, "w")
    outfile.write(jsonP)
    outfile.flush()
    outfile.close()

def write_object_list(objs, fileName):
    jsonP = json.dumps([obj.__dict__ for obj in objs])
    outfile = open(fileName,  "w")
    outfile.write(jsonP)
    outfile.flush()
    outfile.close()
    
'''def write_to_files(heroes_party, heroes_magic, heroes_bag, heroes_pet, prefix):
    write_object_list(heroes_party, PREFIX + HEROES_FILE)
    write_object_list(heroes_magic, PREFIX + HEROES_MAGIC_FILE)
    write_object(heroes_bag, PREFIX + HEROES_BAG_FILE)
    write_object(heroes_pet, PREFIX + HEROES_ALLY_FILE)'''

def write_to_files(heroes_party, heroes_magic, heroes_bag, heroes_summon,
                   heroes_weapons, heroes_armor,
                   quest_items, access_items, prefix):
    write_object_list(heroes_party, PREFIX + HEROES_FILE)
    write_object_list(heroes_magic, PREFIX + HEROES_MAGIC_FILE)
    write_object(heroes_bag, PREFIX + HEROES_BAG_FILE)
    write_object_list(heroes_summon, PREFIX + HEROES_ALLY_FILE)
    write_object_list(heroes_weapons, PREFIX + HEROES_WEAPONS_FILE)
    write_object_list(heroes_armor, PREFIX + HEROES_ARMOR_FILE)
    write_object(quest_items, PREFIX + QUEST_FILE)
    write_object(access_items, PREFIX + ACCESS_FILE)


#this function will read a list of heroes from the given filename, sFileNm
#and it will return the list
def read_hero_objects(sFileNm):
    load_hero_list = []
    jsonFile = open(sFileNm, "r")
    #you know you are loading a list, lst
    lst = json.load(jsonFile)
    for e in lst:
        #you know this list contains only one type of Player object
        p = Player_PC(**e)
        load_hero_list.append(p)
    print("Players from ", sFileNm)
    for pp in load_hero_list:
        pp.stats()
    return load_hero_list

#this function will read a list of spells from the given filename, etc.
def read_spell_objects(sFileNm):
    load_spell_list = []
    jsonFile = open(sFileNm, "r")
    #you know you are loading a list, lst
    lst = json.load(jsonFile)
    for e in lst:
        #you know this list contains only one type of Spell object
        p = Spell_PC(**e)
        load_spell_list.append(p)
    print("Spells from ", sFileNm)
    for pp in load_spell_list:
        pp.stats()
    return load_spell_list

#this function will read a list of spells from the given filename, etc.
def read_weapon_objects(sFileNm):
    load_weapon_list = []
    jsonFile = open(sFileNm, "r")
    #you know you are loading a list, lst
    lst = json.load(jsonFile)
    for e in lst:
        #you know this list contains only one type of Spell object
        p = Weapon_PC(**e)
        load_weapon_list.append(p)
    print("Weapons from ", sFileNm)
    for pp in load_weapon_list:
        if pp.user != "None":
            pp.stats()
    return load_weapon_list

#this function will read a list of armor from the given filename, etc.
def read_armor_objects(sFileNm):
    load_armor_list = []
    jsonFile = open(sFileNm, "r")
    #you know you are loading a list, lst
    lst = json.load(jsonFile)
    for e in lst:
        #you know this list contains only one type of Spell object
        p = Armor_PC(**e)
        load_armor_list.append(p)
    print("Armors from ", sFileNm)
    for pp in load_armor_list:
        if pp.user != "None":
            pp.stats()
    return load_armor_list

#this function will read a list of allys from the given filename, etc.
def read_ally_object(sFileNm):
    load_ally_list = []
    jsonFile = open(sFileNm, "r")
    lst = json.load(jsonFile)
    for e in lst:
        p = Pet_NPC(**e)
        load_ally_list.append(p)
    for pp in load_ally_list:
        pp.stats()
    return load_ally_list

#the input will be the file names storing each of those things
'''def read_from_files(heroes, spells, items, ally):
    heroes_list = read_hero_objects(heroes)
    heroes_magic_list = read_spell_objects(spells)
    jsonFile = open(items, "r")
    items_bag = json.load(jsonFile)
    items_bag_obj = ItemBag_PC(**items_bag)
    jsonFile = open(ally, "r")
    aly = json.load(jsonFile)
    pet_obj = Pet_NPC(**aly)

    return heroes_list, heroes_magic_list, items_bag_obj, pet_obj'''

#the input will be the file names storing each of those things
def read_from_files(heroes, spells, items, ally,
                    weapons, armor, quest, access):
    heroes_list = read_hero_objects(heroes)
    heroes_magic_list = read_spell_objects(spells)
    jsonFile = open(items, "r")
    items_bag = json.load(jsonFile)
    items_bag_obj = ItemBag_PC(**items_bag)
    heroes_ally = read_ally_object(ally)
    heroes_weapons = read_weapon_objects(weapons)
    heroes_armor = read_armor_objects(armor)
    jsonFile = open(quest, "r")
    quest_items = json.load(jsonFile)
    quest_items_obj = QuestItems_NPC(**quest_items)
    jsonFile = open(access, "r")
    access = json.load(jsonFile)
    access_obj = Access_NPC(**access)

    return (heroes_list, heroes_magic_list, items_bag_obj, heroes_ally,
            heroes_weapons, heroes_armor, quest_items_obj, access_obj)

#function that will read lists
#this function knows the file names that are being saved
#this function will return the heroes_list, heroes_magic_list, etc.her in order
'''def read():
    return read_from_files(PREFIX + HEROES_FILE,
                    PREFIX + HEROES_MAGIC_FILE,
                    PREFIX + HEROES_BAG_FILE,
                    PREFIX + HEROES_ALLY_FILE)'''

def read():
    return read_from_files(PREFIX + HEROES_FILE,
                           PREFIX + HEROES_MAGIC_FILE,
                           PREFIX + HEROES_BAG_FILE,
                           PREFIX + HEROES_ALLY_FILE,
                           PREFIX + HEROES_WEAPONS_FILE,
                           PREFIX + HEROES_ARMOR_FILE,
                           PREFIX + QUEST_FILE,
                           PREFIX + ACCESS_FILE)
