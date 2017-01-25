__author__ = 'lnx'

#print 2%12
#print 6%12
#print 9%12
#print 17%12

def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here


    gcd = 0
    if b == 0:
        gcd = a
    else:
        #print a
        #print b
        c = a % b
        #print "c", c
        gcd = gcdRecur(b, c)

    return gcd



print gcdIter(2,12)
print gcdIter(6,12)
print gcdIter(9,12)
print gcdIter(17,12)