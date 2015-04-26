import math

class Vector(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return 'Vector object'

    #adds given vector to this vector and returns a new vector
    def add(self, v):
        self.v = v
        return Vector(self.x + self.v.x, self.y + self.v.y)

    #subtracts given vector from this vector and returns a new vector
    def sub(self, v):
        self.v = v
        return Vector(self.x - self.v.x, self.y - self.v.y)

    #returns the magnitude
    def mag(self):
        return math.sqrt(self.x**2 + self.y**2)

    #normalizes the vector
    def norm(self):
        self.t_mag = self.mag()
        self.x /= self.t_mag
        self.y /= self.t_mag

    #sets new magnitude
    def mult(self, m):
        self.m = m
        self.x *= self.m
        self.y *= self.m

    #returns the dot product of given vector with this vector
    def dot(self, v):
        self.v = v
        return (self.x * self.v.x) + (self.y * self.v.y)

    #returns the angle between given vector and this vector in radians
    def angle(self, v):
        self.v = v
        return math.acos(self.dot(self.v) / (self.mag() * self.v.mag()))

    #returns the angle in radions
    def heading(self):
        return math.atan(self.y / self.x)


v1 = Vector(3, 4)
print v1.heading()
v1.norm()
print v1.mag()
print v1.heading()
