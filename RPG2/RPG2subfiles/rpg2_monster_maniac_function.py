sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC)
#monster collector
#someone who loves monster trophies and will pay well to see yours
#if your skill is less than the sum of your monster parts he'll pay so that they're equal
#makes it easier to train up new characters when switching the party around
def monster_fan_training(p_pc, ib_pc):
	x = 0
	x += (ib_pc.dg_trophy + ib_pc.dl_trophy + ib_pc.gs_trophy +
              ib_pc.ac_trophy + ib_pc.sq_trophy + ib_pc.ip_trophy)
	if p_pc.skill < x:
                print ("There you go, these coins should be enough to train you a bit. ")
                print ("Come back anytime you fight another monster. ")
                print ("Don't forget to show me the trophies. ")
                p_pc.skill = x
        elif p_pc.skill >= x:
                print ("You're already so strong. ")
                print ("I wish I could be like you...")

def monster_maniac(h_p, ib_pc):
        print ("Welcome back! How have you been? ")
        print ("Anymore exciting stories to tell me? ")
        print ("Is that another new trophy I see? ")
        print ("You HAVE to let me take a closer look! ")
        print ("'The man looks over your collection of monster parts.'")
        print ("Ah, I never get tired of seeing these things. ")
        print ("Sometimes I dream of becoming a hero myself just to see the monsters up close. ")
        print ("Anyway, need anything from me? ")
        check = input("TRAINING/CRAFTING? T/C? ")
        if check.upper() == "T":
                hero = party_func.pick_hero(h_p)
                monster_fan_training(hero, ib_pc)
