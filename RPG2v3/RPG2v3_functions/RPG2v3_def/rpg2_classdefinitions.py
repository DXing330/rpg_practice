##an rpg that focuses on team vs team battling
##classes
#player object
class Player_PC:
        def __init__(self, name, level, health, maxhealth,
                     atk, defense, skill, mana, maxmana, 
                     atkbonus = 0, defbonus = 0, 
                     poison = 0):
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
                self.maxmana = maxmana
                #bonus atk that can be increased through quests
                self.atkbonus = atkbonus
                #bonus defense that can be increase through quests
                self.defbonus = defbonus
                #status effects that can be modified by the monsters or player skills
                #self.statusObj = Statuses_NPC(0)
                self.poison = poison
                
        def hstats(self):
                print ("Health:", self.health)

        def stats(self):
                print (self.name, self.level,
                      self.health, self.maxhealth,
                      self.atk, self.defense,
                      self.skill, self.mana, self.maxmana, 
                      self.atkbonus, self.defbonus, "\n")
                if self.poison > 0:
                        print ("POISON:", self.poison, "\n")
        def sstats(self):
                print (self.level, self.maxhealth, self.atk, self.defense)
        #bonus stats
        def bstats(self):
                print ("MAX HEALTH:", self.maxhealth, "SKILL:", self.skill, "MANA:", self.maxmana,
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
                print(self.name, ", STAGE:", self.stage, ", ATK:", self.atk, "\n")
class ItemBag_PC:
        def __init__(self, heal, mana, buff, coins,
                     dg_trophy = 0, gs_trophy = 0,
                     dl_trophy = 0, ah_trophy = 0,
                     sq_trophy = 0, ip_trophy = 0):
                #potions that restore health
                self.heal = heal
                #potions that restore mana
                self.mana = mana
                #potions that buff stats
                self.buff = buff
                #currency to buy things
                #ex. potions, weapons, armors, spells, etc.
                self.coins = coins
                #trophy gained from defeating a boss
                self.dg_trophy = dg_trophy
                self.gs_trophy = gs_trophy
                self.dl_trophy = dl_trophy
                self.ah_trophy = ah_trophy
                self.sq_trophy = sq_trophy
                self.ip_trophy = ip_trophy
        def stats(self):
                print("Heal Potions:", self.heal, "Mana Potions:", self.mana,
                      "Boost Potions:", self.buff, "COINS:", self.coins)
        def trophycase(self):
                print("Demon General Trophies:", self.dg_trophy, "Golden Slime Trophies:", self.gs_trophy,
                      "Demon Lord Trophies:", self.dl_trophy, "Acid Hydra Trophies:", self.ah_trophy,
                      "Succubus Queen Trophies:", self.sq_trophy, "Cryo Phoenix Trophies:",
                      self.ip_trophy)
class Spell_PC:
        def __init__(self, name, power, targets, element, cost):
                #name of the spell
                self.name = name
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
                print (self.name, "Power:", self.power, "Targets:", self.targets,
                       "Element:", self.element, "Cost:", self.cost, "\n")

class Monster_NPC:
        def __init__(self, name, health, atk, defense, skill,
                     element, dropchance, poison = 0,
                     buff = None):
                self.name = name
                self.health = health
                self.atk = atk
                self.defense = defense
                self.skill = skill
                self.element = element
                #how many coins are dropped after battle
                self.dropchance = dropchance
                self.poison = poison
                self.buff = buff
        def stats(self):
                print(self.name, self.health, self.atk, self.defense, self.skill, "\n")
                if self.poison > 0:
                        print ("POISON:", self.poison, "\n")
                if self.buff != None:
                        print ("Buff:", self.buff, "\n")
        def hstats(self):
                print ("Health:", self.health)


class Weapon_PC:
        def __init__(self, name, user, effect, strength, element, atk, upgrade = 0):
                #the name of the weapon
                self.name = name
                #user of the weapon
                self.user = user
                #what kind of effect the weapon will have
                self.effect = effect
                #how strong the weapon effect will be
                self.strength = strength
                #what element the weapon is
                self.element = element
                #how much atk the weapon will give
                self.atk = atk
                self.upgrade = upgrade
        def stats(self):
                print("Name:", self.name, ", Owner:", self.user, ", Effect:", self.effect,
                      ", Power:", self.strength, ", Element:", self.element, 
                      ", Attack:", self.atk, "\n")
                if self.upgrade > 0:
                        print ("Upgrades:", self.upgrade, "\n")

class Armor_PC:
        def __init__(self, name, user, effect, strength, element, defense, upgrade = 0):
                #the name of the armor
                self.name = name
                #the user of the armor
                self.user = user
                #what kind of effect the armor will have
                self.effect = effect
                #how strong the effect will be
                self.strength = strength
                self.element = element
                #how much defense the armor will give
                self.defense = defense
                self.upgrade = upgrade
        def stats(self):
                print("Name:", self.name, ", Owner:", self.user, ", Effect:", self.effect,
                      ", Power:", self.strength, ", Element:", self.element, 
                      ", Defense:", self.defense, "\n")
                if self.upgrade > 0:
                        print ("Upgrades:", self.upgrade, "\n")
#used during quests
class QuestItems_NPC:
        def __init__(self, package = 0, rpackage = 0, managem = 0):
                #packages to be delivered by request of the guild
                self.package = package
                #packages to be returned to the guild
                self.rpackage = rpackage
                #items used for certain upgrades
                #reward for completing quests
                self.managem = managem
        def stats(self):
                print ("Packages:", self.package, "Mana Gems:", self.managem, "\n")
#obtained through gameplay and allows access to new content
class Access_NPC:
        def __init__(self, fame = 0, rank = 0, posrep = 0, negrep = 0):
                #affects what kind of quests you can take
                self.fame = fame
                #affects what kind of facilities you can use at the monster hunter guild
                self.rank = rank
                #affects certain events
                #rep is for reputation
                self.posrep = posrep
                self.negrep = negrep
        def stats(self):
                print ("Fame:", self.fame, ", Rank:", self.rank, "+:", self.posrep,
                       "-:", self.negrep, "\n")
