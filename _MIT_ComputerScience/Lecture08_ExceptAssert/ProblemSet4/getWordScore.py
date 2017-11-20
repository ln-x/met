__author__ = 'Heidelinde'

from ps4a import *

#i = "e"
#print (SCRABBLE_LETTER_VALUES['e'])
#print (SCRABBLE_LETTER_VALUES[i])
#d2[i[0]]

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    for i in word:
        #sum of points of lettesr
        score += SCRABBLE_LETTER_VALUES[i]
    #muliplied by length of word
    #print (len(word))
    score *= len(word)
    #plus 50 if all n are used
    if len(word) == n:
        score += 50

    return score

print (getWordScore("ab", 4))
#print (SCRABBLE_LETTER_VALUES)
