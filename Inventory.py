userin = "placeholder"

Backpack = {
    'canteen': {
        'amount': 'full',
        'hpregen': '10'
        },
    'medkit': {
        'amount': 'full',
        'hpregen': '10'
        },
}

BackpackL = []
for item in Backpack:
    BackpackL.append(item)

def invent(Game_started):
    # checks if the user has start the game and then shows the user their backpack
    if Game_started is True:
        print("""
                  - you've opened up your backpack -
        """)
        for key in Backpack:
            print("                          -"+ f"\t{key}" + " -")
        print("""
            - to close your backpack type (close backpack) -
        """)
        Bag_open = True
