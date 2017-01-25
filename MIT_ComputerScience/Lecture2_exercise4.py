'''
num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num)
'''
'''
numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))
'''
num = 10
while True:
   if num < 7:
        print('Breaking out of loop')
        break
   print(num)
   num -= 1
print('Outside of loop')
