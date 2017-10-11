print("Please think of a number between 0 and 100!")
#epsilon = 0.01
numGuesses = 0
low = 0
high = 100
ans = (high + low)/2.0

print('Is your secret number ', ans, '?')
response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.") #input: Python3

while numGuesses <= 50:
    if response == "c":
        print("Game over. Your secret number was:", ans)
        break
    elif response == "h":
        high = ans
        ans = int((high + low)/2.0)
        numGuesses += 1
        print('Is your secret number ', ans, '?')
        response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.") #input: Python3
    elif response == "l":
        low = ans
        ans = int((high + low)/2.0)
        numGuesses += 1
        print('Is your secret number ', ans, '?')
        response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.") #input: Python3
    else:
        print("Sorry, I did not understand your input.")
        print('Is your secret number ', ans, '?')
        response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.") #input: Python3


''''
x = input("Please think of a number between 0 and 100!")
print (type(x))
print (x)
epsilon = 0.01
numGuesses = 0
low = 0
high = x
ans = (high + low)/2.0

print('Is your secret number ', ans,'?')
#response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.") #input: Python3
response = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.") #raw_input: Python2


while x >= epsilon:
    print('Is your secret number ' + str(ans) + '?')
    if response == "c":
        print("Game over. Your secret number was:" + str(ans))
        break
        #print('numGuesses = '+ str(numGuesses))
    elif response == "h":
        high = ans  
    elif response == "l":
        low = ans
    else:
        print("Sorry, I did not understand your input.")
        #response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.") #input: Python3
        response = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.") #raw_input: Python2
    ans = (high + low)/2.0
    numGuesses += 1
    #print (numGuesses)
    #response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.") #input: Python3
    response = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.") #raw_input: Python2
'''
