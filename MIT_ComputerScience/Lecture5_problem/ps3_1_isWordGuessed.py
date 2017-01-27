def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    #print (len(lettersGuessed))
    if len(lettersGuessed) == 0:
        return False
    else: pass

    count = 0
    for i in lettersGuessed:
        if i in secretWord:
            count += 1
            print (i)
        else:
            pass

    print (count, len(secretWord))
    if count == len(secretWord):
        return True
    else: return False

#secretWord = 'apple'
#lettersGuessed = ['p', 'p', 'l', 'e', 'a']
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(isWordGuessed(secretWord, lettersGuessed))

#print (isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
#print (isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
#print (isWordGuessed('grapefruit', []))
#print (isWordGuessed('coconut', ['z', 'x', 'q', 'c', 'o', 'c', 'o', 'n', 'u', 't']))
#print(isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
print(isWordGuessed('grapefruit', ['z', 'x', 'q', 'g', 'r', 'a', 'p', 'e', 'f', 'r', 'u', 'i', 't']))

#False

'''
#All letters have to be equal!

    #print (len(lettersGuessed))
    if len(lettersGuessed) == 0:
        return False
    else: pass

    for i in lettersGuessed:
        if i in secretWord:
            pass
        else:
            return False
    return True
'''