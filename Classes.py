import random

backpack = []

# This File defines the many classes insides of my game
class Healing:
    # possible atainable healing items in game

    def __init__(self, amount, hpregen, Description):
        # initialize name
        self.amount = amount
        self.hpregen = hpregen
        self.Description = Description

    def inspect(self):
        print(self.amount)
        print(f'{self.hpregen} is how much this will heal you')

class Weapons:
    # possible attatinable weapons in game

    def __init__(self, Ammo, Damage, Description):
        # initialize name
        self.Ammo = Ammo
        self.Damage = Damage
        self.Description = Description

    def inspect(self):
        print(f'{self.Ammo} shots left')
        print(f'{self.Damage} wow you did this much damage')

class Enemies:
    # all Enemies

    def __init__(self, EnHp, Damage, Description):
        self.EnHp = EnHp
        self.Damage = Damage
        self.Description = Description

    def inspect(self):
        print(self.EnHp)

# Healing Items
Canteen = Healing('full', 10, 'A canteen full of water')
Medkit = Healing('full', 50, 'A medkit with various items to heal large wounds')

# Weapons
Shotgun = Weapons( 8, random.uniform(75,100), '12 Gauge Double Barrelled Shotgun')

Baseball_Bat =  Weapons("Ammo", "Damage", "Description")
Flare_Gun = Weapons( "Ammo", "Damage", "Description")
Utility_knife = Weapons( "Ammo", "Damage", "Description")

# Enemies

Wolf = Enemies("Hp", "Damage", "Description")
Shadow = Enemies("Hp", "Damage", "Description")
Hallucination = Enemies("Hp", "Damage", "Description")
Bear = Enemies("Hp", "Damage", "Description")
Tree = Enemies("Hp", "Damage", "Description")
Boss = Enemies("Hp", "Damage", "Description")

# Test code
userin = 'null'

while userin != 'quit':
    userin = input().lower()
    a = isinstance(userin, Healing)
    print (a)
