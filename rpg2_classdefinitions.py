##an rpg that focuses on team vs team battling
##classes
#player object
class Player_PC:
        def __init__(self, name, level, health, maxhealth,
                     atk, defense, skill, mana,
                     atkbonus = 0, defbonus = 0, 
                     weapon = 0, armor = 0):
                #player's name, usually represented by their class
                self.name = name
                #player's level, will increase through quests
                #this will increase the player's health, atk and defense
                self.level = level
                #player's health, how much damage they can take and still fight
                #recovered through resting or potions
                self.health = health
                #player's maximum health
                self.maxhealth = maxhealth
                #player's atk, affects how much damage they deal
                self.atk = atk
                #player's def, affects how much damage they can reduce when hit
                self.defense = defense
                #stats which affects certain things like dodging or using special attacks
                self.skill = skill
                #resource used when casting spells
                #recovered by resting or through potions
                self.mana = mana
                #bonus atk that can be increased through quests
                self.atkbonus = atkbonus
                #bonus defense that can be increase through quests
                self.defbonus = defbonus
                #weapon that can be found/purchased, effect's attack
                self.weapon = weapon
                #armor that can be found/purchased, effect's defense
                self.armor = armor

        def stats(self):
                print (self.name, self.level,
                      self.health, self.maxhealth,
                      self.atk, self.defense,
                      self.skill, self.mana,
                      self.atkbonus, self.defbonus, 
                      self.weapon, self.armor)
        def sstats(self):
                print (self.level, self.maxhealth, self.atk, self.defense)
        #equipment stats
        def estats(self):
                print ("WEAPON ATK:", self.weapon, "ARMOR DEF:", self.armor)
        #bonus stats
        def bstats(self):
                print ("SKILL:", self.skill, "MANA:", self.mana,
                       "BONUS ATK:", self.atkbonus, "BONUS DEF:", self.defbonus)
class Pet_NPC:
        def __init__(self, name, stage, atk):
                #pet's species
                self.name = name
                #pet's evolution stage, increased through quests
                #this affects their atk and what kind of actions they can take
                self.stage = stage
                #affects the power of pet actions
                self.atk = atk
        def stats(self):
                print(self.name, self.stage, self.atk)
class ItemBag_PC:
        def __init__(self, health, mana, buff, coins):
                #potions that restore health
                self.health = health
                #potions that restore mana
                self.mana = mana
                #potions that buff stats
                self.buff = buff
                #currency to buy things
                #ex. potions, weapons, armors, spells, etc.
                self.coins = coins
        def stats(self):
                print("Health Potions:", self.health, "Mana Potions:", self.mana,
                      "Boost Potions:", self.buff, "COINS:", self.coins)
class Spell_PC:
        def __init__(self, power, targets, element, cost):
                #how strong the spell is
                #can be increased through training
                self.power = power
                #how many enemies the spell can hit at one time
                self.targets = targets
                #what element the spells is
                #each element has stengths and weaknesses
                self.element = element
                #the mana cost of the spell
                self.cost = cost
        def stats(self):
                print ("Power:", self.power, "Targets:", self.targets,
                       "Element:", self.element, "Cost:", self.cost)

class Monster_NPC:
        def __init__(self, name, health, atk, defense, skill, element, dropchance):
                self.name = name
                self.health = health
                self.atk = atk
                self.defense = defense
                self.skill = skill
                self.element = element
                #probability that the monster drops an item after being defeated
                self.dropchance = dropchance
        def stats(self):
                print(self.health, self.atk, self.defense, self.skill, self.element)

