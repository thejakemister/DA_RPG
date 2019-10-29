# Course: CS 30
# Period: 4
# Date created: 23/10/01
# Date last modified: 23/10/01
# Name: Jacob Leippi
# Description: my text based adventure game
"""
===============================================================================
-------------------------------------------------------------------------------
Imports

inventory
weapon
enemies
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
Story:

Game starts

you awake in a forest (paint detail picture)
-------------------------------------------------------------------------------
"""
a = "null"

print('to start, TYPE start')

while a != "quit":
    a = str(input())



    if a == "start":
        print(
        """
        I     you awaken in a forest with no recollection of past events.     I
        I                    you check your backpack                          I
        I                                                                     I
        I     inside there is a canteen that holds a small amount of water.   I
        I                    right now it is empty.                           I
        I        you look in each direction and see 3 Possible Paths.         I
        I---------------------------------------------------------------------I
        I                        waterfall (South)                            I
        I---------------------------------------------------------------------I
        i                         campsite (East)                             I
        I---------------------------------------------------------------------I
        I               venture deeper into the trees (North)                 I
        I---------------------------------------------------------------------I
        """
        )
