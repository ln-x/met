__author__ = 'lnx'

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here

    i = 1
    gcd = 0
    while i <= a and i <= b:
        print "while"
        if a%i == 0:
            if b%i == 0:
                print "if"
                gcd = i
        i +=1

    return gcd



print gcdIter(5,12)