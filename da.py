# Course: CS 30
# Period: 4
# Date created: 23/10/01
# Date last modified: 23/10/01
# Name: Jacob Leippi
# Description: my text based adventure game
# citation: Mapping code adapted from matt Obrigewitsch
# github.com/mattObrigewitsch
import Classes
import Map
import Menu
import random


# game hasnt start yet so A is equal to false
Game_started = False
userin = "placeholder"
Bag_open = False

Menu.menu()


while userin != "quit": #consistently run the following
    userin = input().lower() #take user input in lower case
    Map.axisfinder() #find the X
    Map.activeyaxis = Map.yaxislist[Map.yaxis] #set the activeyaxis to the y axis with the X
    # first ui, introducing the backpack and paths
    if userin == 'start':
        Game_started = True
        print(
        """
             you awaken in a forest with no recollection of past events.
                      the only thing you have is a (Backpack)
                            with a (canten) in it
            ----- you seem to be in the "middle" of no where -------
            -  to your (north) there is a forest

            -  to your (east)  there is a large campsite

            -  to your (south) there is a great range of mountains

            -  to your (west)  there is a barren plains

        """)

    if Game_started == True:
        if userin == "backpack":
            Bag_open = True
            Classes.backpack(Bag_open, userin)
        elif Game_started == True:
            if userin == "test": #test code, n/a
                print("test vacant")
            elif userin == "axistest": #used for testing again, n/a
                Map.axisfinder()
                print("yaxis: " + str(Map.yaxis))
                print("xaxis: " + str(Map.xaxis))
            elif userin == "west": #if user types west
                if Map.xaxis != 0: #if the X isnt on the edge
                    Map.oldev = Map.ev #change old event
                    Map.ev = Map.activeyaxis.pop(Map.xaxis - 1) #change new event
                    Map.eventfinder(Map.ev) #run eventfinder with new event
            elif userin == "east": #if user types east
                if Map.xaxis != len(Map.activeyaxis)-1: #if the X isnt on the edge
                    Map.oldev = Map.ev #change old event
                    Map.ev = Map.activeyaxis.pop(Map.xaxis + 1) #change new event
                    print("You went east")
                    Map.eventfinder(Map.ev) #run eventfinder with new event
            elif userin == "north": #if user types North
                if Map.activeyaxis != Map.yaxis0: #if the X isnt on the edge
                    try: #try to run the following
                        Map.tempyaxis = Map.yaxislist[Map.yaxis - 1] #create a temporary new y axis
                        Map.oldev = Map.ev #change old event
                        Map.ev = Map.tempyaxis.pop(Map.xaxis) #change new event
                        Map.eventfinder(Map.ev) #run eventfinder with new event
                    except: #run if the try failed:
                        #the only reason the try should fail is because there is nothing
                        #in the direction
                        print('nothing')
            elif userin == "south": #if user types south
                if Map.activeyaxis != Map.yaxislist[Map.minyaxis]: #if the X isnt on the edge
                    try: #try to run the following
                        Map.tempyaxis = Map.yaxislist[Map.yaxis + 1] #create a temporary new y axis
                        Map.oldev = Map.ev #change old event
                        Map.ev = Map.tempyaxis.pop(Map.xaxis) #change new event
                        Map.eventfinder(Map.ev) #run eventfinder with new event
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
    else:
        if userin != 'start':
            print('START THE GAME USING START')
        elif userin != 'help':
            print('START THE GAME USING START')
