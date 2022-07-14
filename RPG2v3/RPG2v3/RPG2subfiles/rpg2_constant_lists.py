class List_Constants:
     def __init__(self):
             ##constants
             self.INTERMEDIATE_ARMOR_EFFECT_LIST = ["Block", "Thorns",
                                                    "Reflect", "Poison",
                                                    "Absorb", "Super Block",
                                                    "Resist Fire", "Resist Water",
                                                    "Resist Earth", "Resist Air",
                                                    "Resist Dark"]
             self.INTERMEDIATE_WEAPON_EFFECT_LIST = ["Attack", "Lifesteal",
                                                     "Poison", "Lucky", "Mana Drain",
                                                     "Slay Fire", "Slay Water",
                                                     "Slay Earth", "Slay Air",
                                                     "Slay Dark"]
             #types of elements
             self.ELEMENTS_LIST = ["Fire", "Water", "Earth",
                                   "Air", "Dark"]
             self.FULL_ELEMENTS_LIST = ["Fire", "Water", "Earth",
                                        "Air", "Light", "Dark"]
             #types of monsters
             self.MONSTER_NAMES_LIST = ["Demon", "Slime", "Skeleton",
                                        "Beast", "Elemental", "Troll"]
             #list of all possible effects a monster can have
             self.MONSTER_PASSIVE_LIST = ["Fire", "Water", "Air",
                                          "Earth", "Dark", "Demon",
                                          "Slime", "Skeleton", "Beast",
                                          "Elemental", "Troll", "Goblin"]
             self.BASIC_ARMOR_EFFECT_LIST = ["Block",
                                             "Resist Fire", "Resist Water",
                                             "Resist Earth", "Resist Air",
                                             "Resist Dark"]
             self.BASIC_WEAPON_EFFECT_LIST = ["Attack", 
                                              "Slay Fire", "Slay Water",
                                              "Slay Earth", "Slay Air",
                                              "Slay Dark"]
             self.UPGRADE_EFFECT_W = ["Attack", "Lifesteal", "Mana Drain",
                                      "Poison", "Lucky", "Skill Drain",
                                      "Explode"]
             self.UPGRADE_EFFECT_A = ["Thorns", "Reflect", "Poison",
                                      "Absorb", "Ethereal", "Revive"]

L = List_Constants()
