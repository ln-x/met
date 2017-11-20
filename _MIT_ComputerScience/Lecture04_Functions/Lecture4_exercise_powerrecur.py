__author__ = 'lnx'

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code he


    base_exp = base
    if exp == 0:
        base_exp = 1
        return base_exp
    else:
        base_exp =  base * recurPower(base, exp -1)
        return base_exp

print recurPower(2,3)

#test -5.92, 2.47,