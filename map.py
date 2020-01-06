# Course: CS 30
# Period: 4
# Date created: 23/10/01
# Date last modified: 23/10/01
# Name: Jacob Leippi
# Description: my text based adventure game

import random

yaxis0 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ']
yaxis1 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ']
yaxis2 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ']
yaxis3 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ']
yaxis4 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ']
yaxis5 = [' . ',' . ',' . ',' . ',' X ',' . ',' . ',' . ',' . ']
yaxis6 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ']
yaxis7 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ']
yaxis8 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ']
yaxis9 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ']
yaxis10 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ']

#creates a multidimensional array
yaxislist = [yaxis0, yaxis1, yaxis2, yaxis3, yaxis4, yaxis5,yaxis6, yaxis7,
yaxis8, yaxis9, yaxis10]
minyaxis = len(yaxislist)-1 #finds the value of the lowest y-axis

#variable incantations
userin = 'placeholder'
global searchinterval, xaxis, yaxis
oldev = ' . '
ev = ' . '
searchinterval = 0
yaxis = 0
activeyaxis = yaxis0
tempyaxis = yaxis0
RNG = 1

#sets up axisfinder, a function which locates the X on the grid
def axisfinder():
    global searchinterval, xaxis, yaxis #recieves globals
    xnotfound = True # sets boolean to false
    searchinterval = 0 # resets searchinterval
    yaxis = 0 #resets yaxis
    xaxis = 0 #resets xaxis
    while xnotfound and searchinterval <= 1000: # sets while criteria
        try: #if it can run the following:
            #sets x to be equal to the index of the currently searched list
            xaxis = yaxislist[searchinterval].index(' X ')
            yaxis = searchinterval # yaxis is equal to currently searched yaxis
            xnotfound = False # boolean set to false to cancel while
        except: #if the previous could not be run:
            searchinterval = searchinterval + 1 #add 1 to search interval

#prints the world map with a revieved value of the minimum yaxis to be printed
def worlddisplay(minyaxisnum):
    interval = 0 #incantates interval
    #while the interval is smaller than the accepted value:
    while interval <= minyaxisnum:
        print(*yaxislist[interval], sep='') #print the yaxis w/o any list stuff
        interval = interval + 1 #add 1 to interval

def eventfinder(eventcode):
    if eventcode == ' . ':
        #this would be a nested function if I was allowed to use them
        if "north" in userin or "south" in userin: #only runs next lines if met
            tempyaxis.insert(xaxis, ' X ') #if going up or down insert a new X
            del activeyaxis[xaxis] #delete old X
        activeyaxis.insert(xaxis, oldev) #insert the missing map part
        print("there is nothing here (yet)")
    if eventcode == ' N ':
        if "north" in userin or "south" in userin:#only runs next lines if met
            tempyaxis.insert(xaxis, ' X ')#if going up or down insert a new X
            del activeyaxis[xaxis]#delete old X
        activeyaxis.insert(xaxis, oldev)#insert the missing map part
        print("youre at a waterfall")
    if eventcode == ' E ':
        if "north" in userin or "south" in userin:#only runs next lines if met
            tempyaxis.insert(xaxis, ' X ')#if going up or down insert a new X
            del activeyaxis[xaxis]#delete old X
        activeyaxis.insert(xaxis, oldev)#insert the missing map part
        print("damn, you in the middle of no-where")
    if eventcode == ' S ':
        RNG = random.uniform(0, 1)
        if "north" in userin or "south" in userin:#only runs next lines if met
            tempyaxis.insert(xaxis, ' X ')#if going up or down insert a new X
            del activeyaxis[xaxis]#delete old X
        activeyaxis.insert(xaxis, oldev)#insert the missing map part
        if RNG <= 0.5:
            print("Youre in the mountains")
        if RNG > 0.5:
            print("Jacob Gilbertson found you")
            print("Game over")
    if eventcode == ' W ':
        if "north" in userin or "south" in userin:#only runs next lines if met
            tempyaxis.insert(xaxis, ' X ')#if going up or down insert a new X
            del activeyaxis[xaxis]#delete old X
        activeyaxis.insert(xaxis, oldev)#insert the missing map part
        print("Youre in Jacob Gilbertsons house")
    if eventcode == ' B ':
        if "north" in userin or "south" in userin:#only runs next lines if met
            tempyaxis.insert(xaxis, ' X ')#if going up or down insert a new X
            del activeyaxis[xaxis]#delete old X
        activeyaxis.insert(xaxis, oldev)#insert the missing map part
        print("Youre in Matt Obrigewitsch's Basement")
    if eventcode == ' Exit ':
        if "north" in userin or "south" in userin:#only runs next lines if met
            tempyaxis.insert(xaxis, ' X ')#if going up or down insert a new X
            del activeyaxis[xaxis]#delete old X
        activeyaxis.insert(xaxis, oldev)#insert the missing map part
        print("youve excaped")
