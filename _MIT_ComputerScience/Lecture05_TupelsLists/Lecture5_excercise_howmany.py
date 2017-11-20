__author__ = 'Heidelinde'

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    animalnumber = 0

    for value in aDict.items():
        #print value[1]
        #print len(value[1])
        animalnumber += len(value[1])

    return animalnumber

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    for value in aDict.items():
       #print value[1]
       #print len(value[1])
       animalnumber = []
       animalnumber.append((value[0],len(value[1])))

    biggest = max(animalnumber)

    return biggest[0]


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
#print animals
print (how_many(animals))
print (biggest(animals))
