# Course: CS 30
# Period: 4
# Date created: 23/10/01
# Date last modified: 23/10/01
# Name: Jacob Leippi
# Description: my text based adventure game
import SOUTH
import EAST
import NORTH
import Enemies
import Inventory
import Weapons


"""
-------------------------------------------------------------------------------
    mechanics
                        -day and night system:
                        ex. create a timer
                        x = x + 1 idk
                        -health system:
                        ex. you encounter a wolf type defend to defend
                        hp = health - (variable)
                        -damage system:
                        ex. you encounter a wolf type attack to attack
                        enemy_hp = wolf_hp - (variable)
                        -rng based pathway system
                        ex. if you go a certian pathway and go back, that
                        pathway may change

-------------------------------------------------------------------------------
===============================================================================
-------------------------------------------------------------------------------
"""

userin = "null"
print("""
                                 WELCOME TO

oooooooooooo  .oooooo..o   .oooooo.         .o.       ooooooooo.   oooooooooooo
`888'     `8 d8P'    `Y8  d8P'  `Y8b       .888.      `888   `Y88. `888'     `8
 888         Y88bo.      888              .8"888.      888   .d88'  888
 888oooo8     `"Y8888o.  888             .8' `888.     888ooo88P'   888oooo8
 888    "         `"Y88b 888            .88ooo8888.    888          888    "
 888       o oo     .d8P `88b    ooo   .8'     `888.   888          888       o
o888ooooood8 8""88888P'   `Y8bood8P'  o88o     o8888o o888o        o888ooooood8

               ooooooooooooo ooooo   ooooo oooooooooooo
               8'   888   `8 `888'   `888' `888'     `8
                    888       888     888   888
                    888       888ooooo888   888oooo8
                    888       888     888   888    "
                    888       888     888   888       o
                    o888o     o888o   o888o o888ooooood8

oooooooooooo   .oooooo.   ooooooooo.   oooooooooooo  .oooooo..o ooooooooooooo
`888'     `8  d8P'  `Y8b  `888   `Y88. `888'     `8 d8P'    `Y8 8'   888   `8
 888         888      888  888   .d88'  888         Y88bo.           888
 888oooo8    888      888  888ooo88P'   888oooo8     `"Y8888o.       888
 888    "    888      888  888`88b.     888    "         `"Y88b      888
 888         `88b    d88'  888  `88b.   888       o oo     .d8P      888
o888o         `Y8bood8P'  o888o  o888o o888ooooood8 8""88888P'      o888o
                                -- START --
                                -- HELP  --
                                -- QUIT  --
""")

A = False
while userin != 'quit':
    userin = input().lower()

    if userin == 'help':
        print("""
        - Type START to start the game.

        - Type 'QUIT' to quit the Game.

        - To choose a destination, pathway, or item;
          type the word in the brackets.

        - To Check your Inventory, type 'backpack.'
        """)

    if userin == 'start':
        A = True
        print("""
        I     you awaken in a forest with no recollection of past events.     I
        I                    you check your (backpack).                       I
        I                                                                     I
        I     inside there is a (canteen) that holds a small amount of water. I
        I                    right now it is empty.                           I
        I        you look in each direction and see 3 Possible Paths.         I
        I---------------------------------------------------------------------I
        I                        waterfall (South)                            I
        I---------------------------------------------------------------------I
        i                         campsite (East)                             I
        I---------------------------------------------------------------------I
        I               venture deeper into the trees (North)                 I
        I---------------------------------------------------------------------I
        """)


    if userin == 'backpack':
        if A == True:
            for key, value in Inventory.Backpack.items():
                print(f"\t{key}")

    if A == True:
        if userin == 'south':
            SOUTH.Path()
        if userin == 'east':
            EAST.Path()
        if userin == 'north':
            NORTH.Path()

    if A == False:
        if userin != 'start':
            print('START THE GAME USING START')
        elif userin != 'help':
            print('START THE GAME USING START')
