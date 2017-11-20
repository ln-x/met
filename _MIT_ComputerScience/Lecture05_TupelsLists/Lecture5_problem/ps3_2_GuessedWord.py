__author__ = 'lnx'

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    if len(lettersGuessed) == 0:
        return ('_ '*len(secretWord))
    else: pass

    #guessedWord = '_ '*len(secretWord)
    guessedWord = ['_ ']*len(secretWord)

    for i in range(len(lettersGuessed)):
        for j in range(len(secretWord)):
            if lettersGuessed[i] == secretWord[j]:
                #where = secretWord.index(lettersGuessed[i])
                guessedWord[j] = secretWord[j]
                print (guessedWord[j], j)
            else:
                pass

    print (guessedWord)
    guessedWordstr = ''
    for i in range(len(guessedWord)):
        guessedWordstr += guessedWord[i]

    return guessedWordstr

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(getGuessedWord(secretWord, lettersGuessed))
print(getGuessedWord('banana', []))

#'_ pp_ e'


"""
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    if len(lettersGuessed) == 0:
        return False
    else: pass

    guessedWord = '_ '*len(secretWord)
    guessedWord = ['_ ']*len(secretWord)

    for i in range(len(lettersGuessed)):
        for j in range(len(secretWord)):
            #if lettersGuessed[i-1] in secretWord:
            print (i,j)
            print (lettersGuessed[i-1])
            if lettersGuessed[i-1] == secretWord[j-1]:


                where = secretWord.index(lettersGuessed[i-1])
                guessedWord[where] = secretWord[where]

            else:
                pass

    print (guessedWord)
    guessedWordstr = ''
    for i in range(len(guessedWord)):
        guessedWordstr += guessedWord[i]

    return guessedWordstr
"""