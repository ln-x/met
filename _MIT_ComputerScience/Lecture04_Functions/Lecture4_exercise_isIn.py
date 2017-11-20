def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    #Bisectional search
    #1st test the middle character!
    middle = int((len(aStr)-1)/2)
    #print middle
    #print aStr[middle]

    if len(aStr) == 0:
        return False
    elif aStr[middle] == char:
        return True
    elif len(aStr) == 1:
        return False
    elif len(aStr) == 2:
        if aStr[1] == char:
            return True
        else: return False
    else:
        if aStr[middle] < char:
            aStr = aStr[middle:]
            return isIn(char, aStr)
        else:
            aStr = aStr[:middle]
            return isIn(char, aStr)

print isIn("f", "abcddd")
