class List_Constants:
     def __init__(self):
             ##constants
             self.BASIC_ARMOR_EFFECT_LIST = ["Block", "Thorns",
                                             "Reflect", "Poison",
                                             "Absorb", "Super Block",
                                             "Resist Fire", "Resist Water",
                                             "Resist Earth", "Resist Air",
                                             "Resist Dark"]
             self.BASIC_WEAPON_EFFECT_LIST = ["Attack", "Lifesteal",
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
                                          "Elemental", "Troll"]

L = List_Constants()
