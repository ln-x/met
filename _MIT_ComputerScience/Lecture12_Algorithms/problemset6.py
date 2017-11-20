__author__ = 'lnx'

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

#L = []
#L = [1]
L = [1,2]
#L = [1,2,3]
#L = [1,2,3,4,5]
e = 2

print (search(L,e), newsearch(L,e))