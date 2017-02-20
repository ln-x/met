__author__ = 'lnx'

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self,othercoordinate):
        if (self.x == othercoordinate.x) and (self.y == othercoordinate.y):
            return True
        else:
            return False

    def __repr__(self):


#Define __repr__, a special method that returns a string that looks like a valid Python expression
# that could be used to recreate an object with the same value. In other words,
# eval(repr(c)) == c given the definition of __eq__ from part 1