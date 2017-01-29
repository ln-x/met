# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

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


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if len(lettersGuessed) == 0:
        return False
    else: pass

    count = 0
    for i in lettersGuessed:
        if i in secretWord:
            occurence = secretWord.count(i)
            #print (i, occurence)
            count += occurence
            #count += 1
        else:
            pass

    if count == len(secretWord):
        return True
    else: return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    if len(lettersGuessed) == 0:
        #return False
        return ('_ '*len(secretWord))
    else: pass

    guessedWord = ['_ ']*len(secretWord)

    for i in range(len(lettersGuessed)):
        for j in range(len(secretWord)):
            if lettersGuessed[i] == secretWord[j]:
                guessedWord[j] = secretWord[j]
            else:
                pass

    guessedWordstr = ''
    for i in range(len(guessedWord)):
        guessedWordstr += guessedWord[i]

    return guessedWordstr


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    remainingletters = alphabet
    for letter in lettersGuessed:
        if letter in remainingletters:
            #print (letter)
            remainingletters = remainingletters.replace(letter, "")

    return remainingletters

    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is", len(secretWord), "letters long.")
    #print ('_ '*len(secretWord))

    mistakesMade = 0
    GuessesLeft = 8
    lettersGuessed = []

    while GuessesLeft > 0:
        print ('_ '*13)
        print ("You have", GuessesLeft, "guesses left.")
        print ("Available letters: ", getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ')
        guessInLowerCase = guess.lower()
        if guess in lettersGuessed:
            print ("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(guessInLowerCase)
            if isLetterGuessed(secretWord, guessInLowerCase):
                print ("Good guess: ", getGuessedWord(secretWord, lettersGuessed))

                #print (lettersGuessed)
                if isWordGuessed(secretWord, lettersGuessed):
                    print ('_ '*13)
                    print ("Congratulations, you won!")
                    break

            else:
                print ("Oops! That letter is not in my word: ")
                GuessesLeft -= 1
                if GuessesLeft == 0:
                    print ('_ '*13)
                    print ("Sorry, you ran out of guesses. The word was ", secretWord,".")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()

secretWord = 'apple'
hangman(secretWord)
