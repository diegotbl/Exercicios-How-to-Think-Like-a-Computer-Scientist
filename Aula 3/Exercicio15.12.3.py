class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def slope_from_origin(self):
        """ Returns the slope of the line joining the origin to the point """
        return self.y / self.x

P = Point(4, 10)
print("Slope of ({0}, {1}) = {2}".format(P.x, P.y, P.slope_from_origin()))
# This method will fail when the point is on the y-axis
