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

    def slope_from_another_point(self, Q):
        """ Returns the slope of the line joining the point to another point """
        return (self.y - Q.y) / (self.x - Q.x)

    def get_line_to(self, Q):
        """ Computes the equation of the straight line joining two points.
            The answer is given as a tuple (a, b) and the line equation is
            y = ax + b """
        a = self.slope_from_another_point(Q)
        b = Q.y - a*Q.x
        return (a, b);

P = Point(4, 11)
Q = Point(6, 15)
print("Coefficients of the equation between ({0}, {1}) and ({2}, {3}): {4}"
      .format(P.x, P.y, Q.x, Q.y, P.get_line_to(Q)))
# This method will fail when the point P and Q are the same
