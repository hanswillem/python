#simulation of the Three Doors Problem
#n = the number of times the game should be simulated
#s = a boolean, if set to True, the player switches doors, if set to False the player sticks to the first picked door

import random
import matplotlib.pyplot as plt 

def threeDoors(n, s):
    print 'calculating...'
    l = ['door A', 'door B', 'door C']
    percentage = []
    wins = 0.0

    for i in range(1, n + 1):
        winningDoor = random.choice(l)
        playerPick01 = random.choice(l)
        openedDoor = random.choice([j for j in l if j != winningDoor and j != playerPick01])

        if s:
            playerPick02 = [j for j in l if j != playerPick01 and j != openedDoor][0]
            if playerPick02 == winningDoor:
                wins += 1
        else:
            if playerPick01 == winningDoor:
                wins += 1

        percentage.append((wins / i) * 100)

    print 'percentage of wins: ' + str((wins / n) * 100)
    plt.ylim(0, 100)
    plt.plot(percentage)
    plt.show()

threeDoors(10000, True)
