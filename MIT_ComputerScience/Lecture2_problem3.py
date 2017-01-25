s = 'abcabcde'
s1 = 'kmfqbzhoufjw' #expected: hou
s2 = 'yoofaudijnlntu' #expected: dijn
s3 = 'abcdefghijklmnopqrstuvwxyz' #expected: abcdefghijklmnopqrstuvwxyz
s4 = 'ufbyjkpcjbqotvtro' #expected: jkp !!
s5 = 'irolwccgpzhj' #expected: ccgpz
s6 = 'xgthcsromlgzxehjsv' #   ehjsv
s7 = 'znuqngfctmmaebdraevz' # aevz
s8 = 'pyqbxaskgltmnoh' #  glt !!
s9 = 'tnlunygioehmriagjwkygahy' #ehmr
s10 = 'keqiwojdtpddgqnwt'# ddgq !!
s = s8

alph = ''
alph_max = []
index = 0
lentot = 0

while lentot < len(s):
    alph = ''
    print "index", index
    print "lentot, len(s)", lentot, len(s)
    while s[index] <= s[index+1]:
        print s[index], s[index+1]
        alph += s[index]
        index += 1
        print index, len(s)
        if index == len(s)-1:
            print index, len(s)
            break
    alph += s[index]
    alph_max.append(alph)
    print alph_max
    lentot += len(alph)
    index += 1
    if index == len(s)-1:
            print index, len(s)
            break
    print "lentot, index", lentot, index
    print ''

alph_len = []
print len(alph_max)
for i in range (len(alph_max)):
    print alph_max[i-1]
    alph_len.append(len(alph_max[i]))
print alph_len

max_position = alph_len.index(max(alph_len))

result = alph_max[max_position]

print('Longest substring in alphabetical order is: ' + str(result))