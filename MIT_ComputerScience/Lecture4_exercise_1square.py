__author__ = 'Heidelinde'

def square(x):
    '''
    x: int or float.
    '''
    result = x**2
    return result

print (square(4))


def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    result = a*x**2 + b*x + c
    return result

print (evalQuadratic(1,1,1,1))
