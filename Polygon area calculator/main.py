import math

# Base class

class Polygon:

def _init_(self, sides):

self.sides = sides

def area(self):

pass # To be implemented in derived classes

# Derived class for Triangle

class Triangle(Polygon):

def _init_(self, base, height):

super()._init_(3) # A triangle has 3 sides

self.base = base

self.height = height

def area(self):

return 0.5 * self.base * self.height

# Derived class for Rectangle

class Rectangle(Polygon):

def _init_(self, width, height):

super()._init_(4) # A rectangle has 4 sides

self.width = width

self.height = height

def area(self):

return self.width * self.height

# Derived class for Square (inherits from Rectangle)

class Square(Rectangle):

def _init_(self, side):

super()._init_(side, side) # Square is a special case of Rectangle

# Derived class for Regular Pentagon (using formula)

class Pentagon(Polygon):

def _init_(self, side):

super()._init_(5) # Pentagon has 5 sides

self.side = side

def area(self):

return (5 * self.side**2) / (4 * math.tan(math.pi / 5))

# Testing the classes

t = Triangle(10, 5)

print("Triangle Area:", t.area())

r = Rectangle(4, 6)

print("Rectangle Area:", r.area())

s = Square(4)

print("Square Area:", s.area())

p = Pentagon(5)

print("Pentagon Area:", round(p.area(), 2))