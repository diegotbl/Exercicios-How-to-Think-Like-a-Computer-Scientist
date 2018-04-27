class Shape:
    geometric_type = 'Generic Shape'

    def area(self):
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type

class Polygon(Shape): # base class for polygons
    geometric_type = 'Polygon'

class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side

class Rectangle(Polygon):
    geometric_type = 'Rectangle'
    def __init__(self, a, b):
        self.side = a
        self.side2 = b

    def area(self):
        if self.get_geometric_type() == 'Square':
            return self.side ** 2
        return self.side * self.side2

class Square(RegularPolygon, Rectangle):
    geometric_type = 'Square'

rect = Rectangle(3, 5)
print(rect.area())
print(rect.get_geometric_type())

# We see that when we create the object square the constructor executed is the
# one from RegularPolygon because it has priority.
square = Square(12)
# But when we run the method area() the one executed comes from Rectangle
# because RegularPolygon doesn't have an method area(). It's clear the concepts
# of mro and method overwriting.
print(square.area())
print(square.get_geometric_type())
print(square.__class__.__mro__)
