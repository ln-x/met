s = 'Massachusetts Institute of Technology'
numVowels = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1

print('Number of vowels: ' + str(numVowels))