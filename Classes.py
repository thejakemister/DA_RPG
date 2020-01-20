# Course: CS 30
# Period: 4
# Date created: 23/10/01
# Date last modified: 23/10/01
# Name: Jacob Leippi
# Description: my text based adventure game

import random
import re

itempickup = 0
pack = []

# This File defines the many classes insides of my game
class Healing:
    # possible atainable healing items in game

    def __init__(self, name, amount, hpregen, Description):
        # initialize name
        self.name = name
        self.amount = amount
        self.hpregen = hpregen
        self.Description = Description
        self.full = name, amount, hpregen, Description

    def inspect(self):
        print(self.amount)
        print(f"{self.hpregen} is how much this will heal you")

class Weapons:
    # possible attatinable weapons in game

    def __init__(self, name, Ammo, Damage, Description):
        # initialize name
        self.name = name
        self.Ammo = Ammo
        self.Damage = Damage
        self.Description = Description
        self.full = name, Ammo, Damage, Description

    def inspect(self):
        print(f"{self.Ammo} shots left")
        print(f"{self.Damage} wow you did this much damage")

class Enemies:
    # all Enemies

    def __init__(self, name, EnHp, Damage, Description):
        self.name = name
        self.EnHp = EnHp
        self.Damage = Damage
        self.Description = Description
        self.full = name, EnHp, Damage, Description

    def inspect(self):
        print(self.EnHp)
# ------------------------------------------------------------------------------
# Healing Items

Medkit = Healing("Medkit", "full", 50,"A medkit with various items to heal large wounds")
Canteen = Healing("Canteen", "Empty", 0, "A canteen that can hold liquid")
# ------------------------------------------------------------------------------
# Weapons
Shotgun = Weapons("Shotgun", 8, random.uniform(75,100),
"12 Gauge Double Barrelled Shotgun")
Baseball_Bat =  Weapons("Baseball Bat","Ammo", "Damage", "Description")
Flare_Gun = Weapons("Flare Gun", "Ammo", "Damage", "Description")
Utility_knife = Weapons("Utility knife", "Ammo", "Damage", "Description")
# ------------------------------------------------------------------------------
# Enemies
Wolf = Enemies("Wolf", "Hp", "Damage", "Description")
Shadow = Enemies("Shadow", "Hp", "Damage", "Description")
Hallucination = Enemies("Hallucination", "Hp", "Damage", "Description")
Bear = Enemies("Bear", "Hp", "Damage", "Description")
Tree = Enemies("Tree", "Hp", "Damage", "Description")
Boss = Enemies("Boss", "Hp", "Damage", "Description")
# ------------------------------------------------------------------------------
pack.append(Canteen.full)

# user is prompted with a yes or no question


def prompt(userin, itempickup):
    print("yes        no")
    if userin == "yes":
        print("youve picked the item")
        if itempickup == 1:
            pack.append(Medkit.full)
            itempickup = 0
        elif itempickup == 2:
            pack.append(shotgun.full)
            itempickup = 0
        elif itempickup == 3:
            pack.append(baseball_bat.full)
            itempickup = 0
        elif itempickup == 4:
            pack.append(flare_gun.full)
            itempickup = 0
        elif itempickup == 5:
            pack.append(Utility_knife.full)
            itempickup = 0
        elif itempickup == 6:
            Cl.Canteen = Cl.Healing("Canteen", "full", 25, "A canteen that is full of water")
            itempickup = 0
            print(pack)
    elif userin == "no":
        print("you leave it")

def backpack(Bag_open, userin):
    print("youve opened your backpack")
    print(pack)
    if userin == "exit backpack":
        bag_open = False
