__author__ = 'lnx'

def swapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    count = 0
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                #print(L)
                count += 1
    print("Final L: ", L, count)

def modSwapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    count = 0
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                #print(L)
                count += 1
    print("Final L: ", L, count)

#L =[1,2,3,4,5,6,7]
#L = [7,6,5,4,3,2,1]
L = [2,3,6,8,2,5,3,7,4]

swapSort(L)
modSwapSort(L)
