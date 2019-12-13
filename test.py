userin = 'null'

class Healing:
    # possible atainable healing items in game

    def __init__(self, name = None, amount = None, hpregen = None, Description = None):
        # initialize name
        self.amount = amount
        self.hpregen = hpregen
        self.Description = Description

    def inspect(self):
        print(self.amount)
        print(f'{self.hpregen} is how much this will heal you')


backpack.append(Healing('canten', 'full', 10, 'A canteen full of water')
backpack.append(Healing('Medkit', 'full', 10, 'a full medkit')
