__author__ = 'lnx'

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you.
    f takes in an integer, applies a function, returns another integer
    g takes in an integer, applies a Boolean function,
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """


    L_mutated = []
    for i in L:

        if g(f(i)) == True:
            L_mutated.append(i)
    L[:] = L_mutated
    if L == []:
        return -1
    return max(L)

def f(i):
    return i + 2
def g(i):
    return i > 5

#L = [0, -10, 5, 6, -4]
#L = []
#L = [-9,2]
L = [-100,100000,2,3,7,8,9,]
print(applyF_filterG(L, f, g))
print(L)


#6
#[5, 6]



    #for i in L:
    #  print (i)
    #  print (g(f(i)))
    #  if g(f(i)) == False:
    #        del L[i]
