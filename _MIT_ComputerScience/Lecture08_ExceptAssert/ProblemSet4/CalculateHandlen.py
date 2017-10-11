__author__ = 'Heidelinde'

def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """

    handlength = 0
    for letter in hand.keys():
        for j in range(hand[letter]):
            #print(letter)       # print all on the same line
            handlength += 1

    return handlength

print (calculateHandlen({'y': 1, 'a': 1, 'o': 2}))