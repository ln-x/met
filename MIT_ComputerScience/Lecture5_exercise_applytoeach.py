__author__ = 'Heidelinde'

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]

def timesFive(a):
    return a * 5

def plusOne(a):
    return a+1

def squared(a):
    return a*a

#applyToEach(testList, timesFive)
#applyToEach(testList,abs)
#applyToEach(testList,plusOne)
applyToEach(testList,squared)
print(testList)