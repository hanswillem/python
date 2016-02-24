#simulation of the Three Doors Problem
import random

#n = the number of times the game should be simulated
#s = a boolean, if set to True, the player switches doors, if set to False the player sticks to the first picked door
def threeDoors(n, s):
    print 'calculating...'
    wins = 0
    for i in range(n):
        #make an array with three doors
        l = ['door A', 'door B', 'door C']
        #pick a winning door and assign a random door to the player
        winningDoor = random.choice(l)
        pickedDoor01 = random.choice(l)
        #remove winning door and (if they are not the same) remove the picked door from the array
        l.remove(winningDoor)
        if pickedDoor01 in l:
            l.remove(pickedDoor01)
        #the door that should be openend by the host is the door that is left in the array
        #or, if there are more than two left, a random one of the two remaining doors in the array
        openedDoor = random.choice(l)
        #fill the array again
        l = ['door A', 'door B', 'door C']
        #remove the picked door and the opened door
        l.remove(pickedDoor01)
        l.remove(openedDoor)
        #pick the door to which the player switches
        pickedDoor02 = l[0]
        #see if the player wins the game, and if so count the times the player wins
        if s:
            if pickedDoor02 == winningDoor:
                wins += 1.0
        else:
            if pickedDoor01 == winningDoor:
                wins += 1.0
    #return the percentage
    print 'percentage ' + str((wins / n) * 100)

threeDoors(100000, False)
