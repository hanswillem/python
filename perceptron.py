#perceptron
class Perceptron(object):
    def __init__(self, numX):
        self.numX = numX
        self.w = [0 for i in range(self.numX)]
        self.c = 0.1
        self.sumRes = 0
    
    def sum(self, x):
        for i in range(self.numX):
            self.sumRes += x[i] * self.w[i] * self.c
        if self.sumRes > 0:
            return 1
        else:
            return 0

    def train(self, x):
        if sum(x) != x[-1]:
            for i in range(self.numX):
                self.w[i] += x[i] * self.c
            print 'new weigths: ' + str(self.w) 
