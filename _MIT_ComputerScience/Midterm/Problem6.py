__author__ = 'lnx'

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    # Your code here

    for i in L:
        print (i)
        i.reverse()
        print (i)

    L.reverse()


L = [[1, 2], [3, 4], [5, 6, 7]]

deep_reverse(L)

print (L)

# then deep_reverse(L)
# mutates L to be [[7, 6, 5], [4, 3], [2, 1]]