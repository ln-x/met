s = 'abcabcde'
s1 = 'kmfqbzhoufjw' #expected: hou
s2 = 'yoofaudijnlntu' #expected: dijn
s3 = 'abcdefghijklmnopqrstuvwxyz' #expected: abcdefghijklmnopqrstuvwxyz
s4 = 'ufbyjkpcjbqotvtro' #expected: jkp
s5 = 'irolwccgpzhj' #expected: ccgpz
s6 = 'xgthcsromlgzxehjsv' #   ehjsv
s7 = 'znuqngfctmmaebdraevz' # aevz
s8 = 'pyqbxaskgltmnoh' #  glt
s9 = 'tnlunygioehmriagjwkygahy' #ehmr
s10 = 'keqiwojdtpddgqnwt'# ddgq
#s = s5

alph = ''
alph_max = []
index = 0


while s[index] < s[index+1]:
    print s[index]
    alph += s[index]
    index += 1
alph += s[index]

index +=1


print('Longest substring in alphabetical order is: ' + alph)