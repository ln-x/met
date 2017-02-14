__author__ = 'Heidelinde'

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    handCopy = hand.copy()
    count = 0
    if word in wordList:
        for i in word:
            if i in handCopy.keys():
                handCopy[i] -= 1
                if handCopy[i] == 0:
                    del handCopy[i]
                count += 1
        if count == len(word):
             return True
        else:
            return False
    else:
        return False




wordList = "words.txt"

#isValidWord(kwijibo, {'i': 2, 'j': 1, 'k': 1, 'w': 1, 'o': 1, 'b': 1}, WORDLIST_FILENAME)
print (isValidWord(chayote, {'y': 1, 'a': 1, 'o': 2, 'z': 1, 'u': 2, 'h': 1, 'c': 2, 't': 2}, wordList))


"""
#TEST SUCCESS!
    handCopy = hand.copy()
    count = 0
    if word in wordList:
        for i in word:
            if i in handCopy.keys():
                handCopy[i] -= 1
                if handCopy[i] == 0:
                    del handCopy[i]
                count += 1
        if count == len(word):
             return True
        else:
            return False
"""

"""
    print("hello")

    wordCopy = word.Copy()
    if wordCopy.upper() not in wordList:
        return False
    else:
        handCopy = hand.copy()
        count = 0
        for i in word:
            if i in handCopy.keys():
                handCopy[i] -= 1
                if handCopy[i] == 0:
                    del handCopy[i]
                count += 1
        if count == len(word):
             return True
        else:
            return False
"""