import random
import re


# This File defines the many classes insides of my game
class Healing:
    # possible atainable healing items in game

    def __init__(self, name = None, amount = None, hpregen = None, Description = None):
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

    def inspect(self):
        print(self.EnHp)

# Healing Items

Medkit = Healing("Medkit", "full", 50, "A medkit with various items to heal large wounds")
Canteen = Healing("Canteen", "Empty", 0, "A canteen that can hold liquid")

Weapons
Shotgun = Weapons("Shotgun", 8, random.uniform(75,100), "12 Gauge Double Barrelled Shotgun")

Baseball_Bat =  Weapons("Baseball Bat","Ammo", "Damage", "Description")
Flare_Gun = Weapons("Flare Gun", "Ammo", "Damage", "Description")
Utility_knife = Weapons("Utility knife", "Ammo", "Damage", "Description")

# Enemies
Wolf = Enemies("Wolf", "Hp", "Damage", "Description")
Shadow = Enemies("Shadow", "Hp", "Damage", "Description")
Hallucination = Enemies("Hallucination", "Hp", "Damage", "Description")
Bear = Enemies("Bear", "Hp", "Damage", "Description")
Tree = Enemies("Tree", "Hp", "Damage", "Description")
Boss = Enemies("Boss", "Hp", "Damage", "Description")


# Test code

userin = "null"

# while userin != "quit":
    #userin = input().lower()
    #if userin == "medkit":
backpack = []
backpack.append(Medkit.full)
backpack.append(Canteen.full)
print(*backpack, sep = "\n")
