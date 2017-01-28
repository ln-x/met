__author__ = 'Heidelinde'

def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    #print aTup
    #print aTup[1], aTup[2]

    odd_index = []

    for i in range(len(aTup)):
        if i%2 == 0:
            odd_index.append(i)
    #print odd_index

    #for i in aTup:

    odd = []
    for j in odd_index:
       #print j, aTup[j]
       odd.append(aTup[j])
       mytuple = ()
       mytuple = (mytuple, aTup[j])

    #print mytuple
    #print odd
    print tuple(odd)
    return tuple(odd)

print oddTuples((1,2,3,4,5))