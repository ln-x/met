__author__ = 'lnx'

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    #aList_flat = []
    #for i in aList:
    #    #print (i)
    #    if type(i) != list:
    #        aList_flat.append(i)
    #    else:
    #        flatten(i)
        #print (aList_flat)

    #return aList_flat

#aList = [1,2]
#aList = [1,[2,2]]
aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

#[1,'a','cat',2,3,'dog',4,5]



print (flatten(aList))