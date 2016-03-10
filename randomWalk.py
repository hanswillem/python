import random
import math
import matplotlib.pyplot as plt

class randomWalk(object):
    def __init__(self):
        self.locx = 0
        self.locy = 0
        self.stepList = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.l = []
        
    def move(self, numSteps):
        for i in range(numSteps):
            self.step = random.choice(self.stepList)
            self.locx += self.step[0]
            self.locy += self.step[1]
            self.l.append(math.sqrt(self.locx**2 + self.locy**2))

        plt.title('Random Walk')
        plt.xlabel('number of steps')
        plt.ylabel('distance froms start position')
        plt.ylim(0, 100)
        plt.plot(range(numSteps), self.l)
        plt.show()
        
    def dist(self):
        return math.sqrt(self.locx**2 + self.locy**2)

w1 = randomWalk()
w1.move(1000)
