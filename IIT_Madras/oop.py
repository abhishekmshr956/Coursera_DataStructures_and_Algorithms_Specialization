import math
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def translate(self, deltax, deltay):
        self.x += deltax
        self.y += deltay

    def odistance(self):
        d = math.sqrt(self.x * self.x + self.y * self.y)
        return(d)
    
    def __str__(self):
        return(f'({self.x},{self.y})')

origin, A = Point(), Point(3, 5)
print(origin, A)

class Polar:
    def __init__(self, a=0, b=0):
        self.r = math.sqrt(a*a + b*b)
        if a == 0:
            self.theta = math.pi / 2
        else:
            self.theta = math.atan(b/a)
    
    def odistance(self):
        return(self.r)
    
    def translate(self, deltax, deltay):
        x = self.r * math.cos(self.theta)
        y = self.r * math.sin(self.theta)
        x += deltax
        y += deltay
        self.r = math.sqrt(x*x + y*y)
        if x == 0:
            self.theta = math.pi/2
        else:
            self.theta = math.atan(y/x)
