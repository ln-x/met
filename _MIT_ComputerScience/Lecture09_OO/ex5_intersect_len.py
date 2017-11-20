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

    def intersect(self, b):
        intersect_list = intSet()
        #print (b.vals)
        #print (self.vals)
        for i in range(len(b.vals)):
            for j in range(len(self.vals)):
                #print (i,j)
                if b.vals[i] == self.vals[j]:
                    #print(b.vals[i])
                    intersect_list.insert(b.vals[i])
        return intersect_list

    def __len__(self):
        return len(self.vals)

setA = intSet()
setA.insert(5)
setA.insert(2)
setB = intSet()
setB.insert(5)
setB.insert(4)
print (setA.intersect(setB))
#print setA
#print len(setA)
#print setB
#print len(setB)
#intersecList = intSet.intersect(a,b)
#print intersecList
#setA = [-17,-15,-10,0,12,14,15,19]
#setB = [19,-8,4,5,6,10,18]
#setA = intSet(setA)



#Traceback (most recent call last):
#  File "submission.py", line 36, in intersect
#    for i in a:
#TypeError: 'intSet' object is not iterable

#setA.intersect(setB): {}

#setA: {-20,-11,-6,3,9,10,13}
#setB: {-10,-3,2,3,4,8,15,18,19}
#setA.intersect(setB): {3}

#setA: {-19,-17,-15,-8,1,5,7,8,12}
#setB: {-17,-16,-15,-13,-12,-7,-6,1,7,16}
#setA.intersect(setB): {-17,-15,1,7}
#setB.intersect(setA): {-17,-15,1,7}


#setA: {}
#setB: {}
#setA.intersect(setB): {}