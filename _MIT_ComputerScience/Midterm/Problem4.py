__author__ = 'lnx'

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''

    #assert type(base) == int
    #assert base > 1
    #assert type(num) == int
    #assert num > 0

    exponent = 0
    #print (base ** exponent == num)
    if base ** exponent == num:
        #print (base, exponent, num)
        return exponent
    while base ** (exponent+1) < num:
        #print (base**(exponent+1))
        exponent += 1

    if abs(base**exponent - num) > abs(base**(exponent+1) - num):
        return exponent+1
    else:
        return exponent



#print (closest_power(3,12)) #returns 2
#print(closest_power(4,12)) #returns 2
#print (closest_power(4,1)) #returns 0
