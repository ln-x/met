def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    # FILL IN YOUR CODE HERE

    trans = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si',
             '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu', '10': 'shi'}


    num = int(us_num)
    man_num = ''
    if num < 11:
        man_num = trans[us_num]
    elif num < 20:
        man_num = trans['10'] + " " + trans[str(num-10)]
    elif num < 100:
        if num%10 == 0:
            man_num = trans[str(num // 10)] + " " + trans['10']
        else:
            man_num = trans[str(num//10)] + " " + trans['10']+ " " + trans[str(num%10)]

    return man_num



print (convert_to_mandarin('36')) #will return: san shi liu
print (convert_to_mandarin('20')) #will return: er shi
print (convert_to_mandarin('16')) #will return: shi liu

