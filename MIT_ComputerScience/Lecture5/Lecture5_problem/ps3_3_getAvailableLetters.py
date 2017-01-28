__author__ = 'lnx'

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...##
    #alphabet = ['a','b','c','d','e','f','g','h',]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    remainingletters = alphabet
    for letter in lettersGuessed:
        if letter in remainingletters:
            print (letter)
            remainingletters = remainingletters.replace(letter, "")

            #where = remainingletters.index(letter)
            #print (where)
            #remainingletters.pop(where)

    return remainingletters

    #import string
    #print(string.ascii_lowercase)
    #abcdefghijklmnopqrstuvwxyz


lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
#abcdfghjlmnoqtuvwxyz