s = 'bobssachusettechnolbob'
numBob = 0
index = 0

for char in s:
    #print s[index], s[index+1], s[index+2]
    if index == len(s)-2:
      break
    if s[index] == 'b' and s[index+1]== 'o' and s[index+2] == "b":
        numBob += 1
    index += 1

print('Number of times bob occurs is: ' + str(numBob))