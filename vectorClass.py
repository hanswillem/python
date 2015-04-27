class Vector(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return 'Vector(' + str(self.x) +', ' + str(self.y) + ')'

    def add(self, v):
        self.v = v
        self.x += self.v.x
        self.y += self.v.y

    def sub(self, v):
        self.v = v
        self.x -= self.v.x
        self.y -= self.v.y

    def mag(self):
        return math.sqrt(self.x**2 + self.y**2)

    def norm(self):
        self.t_mag = self.mag()
        self.x /= self.t_mag
        self.y /= self.t_mag

    def mult(self, m):
        self.m = m
        self.x *= self.m
        self.y *= self.m

    def dot(self, v):
        self.v = v
        return (self.x * self.v.x) + (self.y * self.v.y)

    def angle(self, v):
        self.v = v
        return math.acos(self.dot(self.v) / (self.mag() * self.v.mag()))

    def heading(self):
        return math.atan(self.y / self.x)
