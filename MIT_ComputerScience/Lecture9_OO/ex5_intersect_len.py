__author__ = 'lnx'

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, a):
        intersect_list = intSet()
        for i in a:
            if i in self.vals:
                    intersect_list.insert(i)
        return intersect_list

    def __len__(self):
        return len(self.vals)

a = intSet()
a.insert(1)
a.insert(2)
print (a)
print len(a)

b = [2,4]
intersecList = intSet.intersect(a,b)
print intersecList

#setA: {-17,-15,-10,0,12,14,15,19}
#setB: {-19,-8,4,5,6,10,18}
#Traceback (most recent call last):
#  File "submission.py", line 36, in intersect
#    for i in a:
#TypeError: 'intSet' object is not iterable

#setA: {-20,-11,-6,3,9,10,13}
#setB: {-10,-3,2,3,4,8,15,18,19}
#setA.intersect(setB): {3}

#setA: {-19,-17,-15,-8,1,5,7,8,12}
#setB: {-17,-16,-15,-13,-12,-7,-6,1,7,16}
#setA.intersect(setB): {-17,-15,1,7}
#setB.intersect(setA): {-17,-15,1,7}

#setA: {-17,-15,-10,0,12,14,15,19}
#setB: {-19,-8,4,5,6,10,18}
#setA.intersect(setB): {}

#setA: {}
#setB: {}
#setA.intersect(setB): {}