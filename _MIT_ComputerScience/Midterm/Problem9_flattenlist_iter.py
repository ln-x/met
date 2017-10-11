__author__ = 'lnx'

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    #aList_Copy = []
    #print (aList)
    #aList_Copy = []
    #print (aList_Copy)

    aList_flat = []
    for i in aList:
        #print (i)
        if type(i) != list:
            aList_flat.append(i)
        else:
            for j in i:
                if type(j) != list:
                    aList_flat.append(j)
                else:
                    for k in j:
                        if type(k) != list:
                            aList_flat.append(k)
                        else:
                            for m in k:
                                aList_flat.append(m)
        #print (aList_flat)

    return aList_flat

#aList = [1,2]
#aList = [1,[2,2]]
aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

#[1,'a','cat',2,3,'dog',4,5]



print (flatten(aList))