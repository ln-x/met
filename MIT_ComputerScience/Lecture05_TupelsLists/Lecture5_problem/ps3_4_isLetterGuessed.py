def isLetterGuessed(secretWord, guess):
    '''
    secretWord: string, the word the user is guessing
    guess: letter guessed by user
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    #if guess == 0:
    #    return False
    #else: pass

    if guess in secretWord:
        return True
    else: return False

print(isLetterGuessed('grapefruit', 'z'))