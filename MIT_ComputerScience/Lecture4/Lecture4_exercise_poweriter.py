__author__ = 'lnx'

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    base_exp = base
    if exp == 0:
        base_exp = 1
    else:
        x = 1
        while x < exp:
            base_exp *= base
            x += 1
    return base_exp

print iterPower(-5.82,0)

#test -5.92, 2.47,