__author__ = 'Heidelinde'
from ps4a import *

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    handCopy = hand.copy()
    for i in word:
        if i in handCopy.keys():
             handCopy[i] -= 1
    return handCopy

#print (updateHand({'p': 3, 't': 2, 'c': 2, 'r': 2, 'l': 2, 'a': 2}, 'claptrap'))
#{'p': 1, 't': 1, 'c': 1, 'r': 1, 'l': 1, 'a': 0}
print (updateHand({'d': 1, 'g': 1, 'o': 1}, 'dog'))
#{'d': 0, 'o': 0, 'g': 0}
#print (hand)
#print (updateHand({'w': 1, 'u': 1, 'l': 3, 'p': 1, 'n': 1, 'e': 1, 'm': 1}, 'plum'))