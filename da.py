# Course: CS 30
# Period: 4
# Date created: 23/10/01
# Date last modified: 23/10/01
# Name: Jacob Leippi
# Description: my text based adventure game
# citation: Mapping code adapted from matt Obrigewitsch
# github.com/mattObrigewitsch
import Enemies
import Inventory
import Weapons
import map
import Menu
import random

# game hasnt start yet so A is equal to false
Game_started = False
userin = "placeholder"
Bag_open = False

Menu.menu()

while userin != "quit": #consistently run the following
    userin = input().lower() #take user input in lower case
    map.axisfinder() #find the X
    map.activeyaxis = map.yaxislist[map.yaxis] #set the activeyaxis to the y axis with the X
    # first ui, introducing the backpack and paths
    if userin == 'start':
        Game_started = True
        print("""
             you awaken in a forest with no recollection of past events.
                      the only thing you have is Backpack
                            with few items in it
            ----- you seem to be in the "middle" of no where -------
             to your (north) there is a forest
             to your (east)  there is a large campsite
             to your (south) there is a great range of mountains
             to your (west)  there is a barren plains
        """)
    if userin == "backpack":
        Inventory.invent(Game_started)
    elif Game_started == True:
        if userin == "test": #test code, n/a
            print("test vacant")
        elif userin == "axistest": #used for testing again, n/a
            map.axisfinder()
            print("yaxis: " + str(map.yaxis))
            print("xaxis: " + str(map.xaxis))
        elif userin == "west": #if user types a
            if map.xaxis != 0: #if the X isnt on the edge
                map.oldev = map.ev #change old event
                map.ev = map.activeyaxis.pop(map.xaxis - 1) #change new event
                map.eventfinder(map.ev) #run eventfinder with new event
        elif userin == "east": #if user types d
            if map.xaxis != len(map.activeyaxis)-1: #if the X isnt on the edge
                map.oldev = map.ev #change old event
                map.ev = map.activeyaxis.pop(map.xaxis + 1) #change new event
                map.eventfinder(map.ev) #run eventfinder with new event
        elif userin == "north": #if user types w
            if map.activeyaxis != map.yaxis0: #if the X isnt on the edge
                try: #try to run the following
                    map.tempyaxis = map.yaxislist[map.yaxis - 1] #create a temporary new y axis
                    map.oldev = map.ev #change old event
                    map.ev = map.tempyaxis.pop(map.xaxis) #change new event
                    map.eventfinder(map.ev) #run eventfinder with new event
                except: #run if the try failed:
                    #the only reason the try should fail is because there is nothing
                    #in the direction
                    print("There is nothing in that direction")
        elif userin == "south": #if user types s
            if map.activeyaxis != map.yaxislist[map.minyaxis]: #if the X isnt on the edge
                try: #try to run the following
                    map.tempyaxis = map.yaxislist[map.yaxis + 1] #create a temporary new y axis
                    map.oldev = map.ev #change old event
                    map.ev = map.tempyaxis.pop(map.xaxis) #change new event
                    map.eventfinder(map.ev) #run eventfinder with new event
                except: #run if the try failed:
                    #the only reason the try should fail is because there is nothing
                    #in the direction
                    print("There is nothing in that direction")
        elif userin == "quit":
            print("ending program, thanks for playing!")
            break
        elif userin == 'help':
            print("""
            - Type START to start the game.

            - Type 'QUIT' to quit the Game.

            - To choose a destination, pathway, or item;
              type the word in the brackets.

            - To Check your Inventory, type 'backpack.'
            """)

    # check if game is started, if false. tells the user to start the game
    elif Game_started is False:
        if userin != 'start':
            print('START THE GAME USING START')
        elif userin != 'help':
            print('START THE GAME USING START')
