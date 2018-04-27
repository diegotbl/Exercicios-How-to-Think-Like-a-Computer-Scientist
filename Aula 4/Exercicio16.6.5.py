def collide(R1, R2):
    """ Checks if two rectangles collide or not """
    if(R2.corner[1] - R2.height > R1.corner[1]):
        return 0
    elif(R2.corner[0] > R1.corner[0] + R1.width):
        return 0
    elif(R2.corner[1] < R1.corner[1] - R1.height):
        return 0
    elif(R2.corner[0] + R2.width < R1.corner[0]):
        return 0
    return 1

class Rectangle:
    """ A class to manufacture rectangle objects """
    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h
    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

box1 = Rectangle((0, 10), 5, 10)
box2 = Rectangle((6, 10), 6, 5)

print("Is there collision between these two points?\n   {0}"
      .format(collide(box1, box2)))
