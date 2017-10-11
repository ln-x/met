__author__ = 'lnx'

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here


#Write a Python function that returns the sum of the pairwise products of listA and listB.
# You should assume that listA and listB have the same length and are two lists of integer numbers.
# For example, if listA = [1, 2, 3] and listB = [4, 5, 6],
#  the dot product is 1*4 + 2*5 + 3*6,
# meaning your function should return: 32

#Hint: You will need to traverse both lists in parallel.

    dotprod = 0

    for i in range(len(listA)):
        print (i)
        add = listA[i]*listB[i]
        print (add)
        dotprod = dotprod + add

    return dotprod


listA = [1, 2, 3]
listB = [4, 5, 6]

print (dotProduct(listA, listB))
