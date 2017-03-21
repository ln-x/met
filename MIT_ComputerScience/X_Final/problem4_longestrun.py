def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    longest_inc = []
    longest_inc2 = []
    longest_dec = []
    longest_dec2 = []

    i = 0
    try:
        while L[i] <= L[i+1]:
            longest_inc.append(L[i])
            i += 1
    except:
        pass
    if L[i-1] < L[i]:
        longest_inc.append(L[i])
    else:
        pass

    try:
        while L[i] >= L[i+1]:
            longest_dec.append(L[i])
            i += 1
    except:
        pass
    if L[i-1] > L[i]:
        longest_dec.append(L[i])
    else:
        pass
    print longest_dec

    try:
        while L[i] <= L[i+1]:
            longest_inc2.append(L[i])
            i += 1
    except:
        pass

    try:
        while L[i] >= L[i+1]:
            longest_dec2.append(L[i])
            i += 1
    except:
        pass
    longest_dec2.append(L[i])

    longest = [longest_inc,longest_dec,longest_inc2,longest_dec2]
    index_max = max(range(len(longest)), key=lambda i: len(longest[i]))
    #print index_max

    longest_sum = 0
    for i in longest[index_max]:
        longest_sum += i

    return longest_sum

print(longest_run([1, 2, 3, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) #65
print(longest_run([3, 3, 3, 3, 3, 3, 3, -10, 1, 2, 3, 4])) #11
#print(longest_run([3, 3, 3, 3, 3])) #15
#print(longest_run([-3, -3, -3, -3, -3])) #15
#print(longest_run([1, 2, 3, 2, 1, -10, -20, 3, 3, 3, 3, 3, 3, 3, 3, 3])) #7
#print(longest_run([1, 2, 3, 2, 1, -10, -20, 3, 4, 5, 7, 7, 8, 9, 11, 11])) #45
#print(longest_run([1, 1, 2, 3, 5, 8, 10, 100, 1000, 10000])) #11130
#print(longest_run([100000, 10000, 1000, 100, 10, 8, 8, 5, 2, 1, 0])) #111134
#print(longest_run([100, 10, 10, 10, 10, 10, 10, 10, 0])) #170
#print(longest_run([-100, -10, -10, -10, -10, -10, -10, -10, 0])) #-170
#print(longest_run([1, 10, 10, 10, 10, 10, 10, 100])) #161
#print(longest_run([-1, -10, -10, -10, -10, -10, -10, -100])) #-161
print(longest_run([1, 2, 1, 2, 1, 2, 1, 2, -1, -2, -1, -2, 10, 20, 10, 20, 100, 200, 100, 0, 100, 0, 100, 0, 0, 100, 0, 0, 0, 100, 1500000, -1500000, 1, -150001]))#1500100

#print(longest_run([1, 2, 3, 4, 5, 6, 7, 8, 9]))
#print(longest_run([1, 2, 3, 4, 5, 0, 10, 1, 2, 3, 4, 5]))
#print (longest_run([1,2,3])) #single increment ok
#print (longest_run([3,2,1])) # single increment ok
#print (longest_run([1,2,1,2,3])) #double increment ok
#print (longest_run([2,1,3,2,1])) #double decrement NO
#print (longest_run([2,2,2,2,2])) #same numbers ok
#print (longest_run([1,2,2,1])) #increment, and decrement - choose first. ok
#print (longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))
#longest run of monotonically increasing numbers in L is [3, 4, 5, 7, 7]
#longest run of monotonically decreasing numbers in L is [10, 4, 3]
# Your function should return the value 26 because the longest run of monotonically increasing integers is longer than the longest run of monotonically decreasing numbers.

#L = [5, 4, 10]
#longest run of monotonically increasing numbers in L is [4, 10] and the l
# ongest run of monotonically decreasing numbers in L is [5, 4].
# Your function should return the value 9 because the longest run of monotonically decreasing integers occurs before the longest run of monotonically increasing numbers.

def longest_run2(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    longest_inc = []
    longest_dec = []
    longest = []
    for i in range(len(L)-2):
        if L[i] < L[i+1]:
            print L[i]
            count = 0
            try:
              while L[i+count] < L[i+count+1]:
                longest_inc.append(L[i])
                count += 1
              longest.append(longest_inc)
              print (longest)
            except:
                pass
        else:
            count = 0
            while L[i+count+1] < L[i+count]:
                print L[i+count+1], count
                longest_dec.append(L[i+count+1])
                count += 1
            longest.append(longest_dec)
            #print (longest)
    print (max(longest))

    longest = max(longest)

    longest_sum = 0
    for i in longest:
        longest_sum += i

    return longest_sum


#print (longest_run2([1,2,3])) #single increment ok
#print (longest_run2([3,2,1])) # single increment ok
#print (longest_run2([1,2,1,2,3])) #double increment NO
#print (longest_run2([2,1,3,2,1])) #double decrement NO
#print (longest_run2([2,2,2,2,2])) #same numbers NO
#print (longest_run2([1,2,2,1])) #increment, and decrement - choose first. NO
#print (longest_run2([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))

#print (longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))
#longest run of monotonically increasing numbers in L is [3, 4, 5, 7, 7]
#longest run of monotonically decreasing numbers in L is [10, 4, 3]
# Your function should return the value 26 because the longest run of monotonically increasing integers is longer than the longest run of monotonically decreasing numbers.

#print (longest_run2([5, 4, 10]))
#longest run of monotonically increasing numbers in L is [4, 10] and the l
# ongest run of monotonically decreasing numbers in L is [5, 4].
# Your function should return the value 9 because the longest run of monotonically decreasing integers occurs before the longest run of monotonically increasing numbers.

def longest_run3(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    longest_inc = []
    longest_dec = []
    longest = []
    i = 0
    for i in range(len(L)-1):
    #while i < len(L):
        try:
            #print (i)
            longest_inc.append(L[i])
            try:
                while (L[i] < L[i+1]):
                    longest_inc.append(L[i+1])
                    i += 1
                    #print (longest_inc)
            except:
                pass
            longest.append(longest_inc)
            #print longest

  # print (max(longest))
        except:
            break

    i = 0
    try:
        longest_dec.append(L[i])
        try:
            while (L[i] > L[i + 1]):
                longest_dec.append(L[i + 1])
                i += 1
                #print (longest_dec)
        except:
            pass
        longest.append(longest_dec)
        # print (max(longest))
    except:
        pass

    longest = max(longest)

    longest_sum = 0
    for i in longest:
        longest_sum += i

    return longest_sum

#print (longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))
#longest run of monotonically increasing numbers in L is [3, 4, 5, 7, 7]
#longest run of monotonically decreasing numbers in L is [10, 4, 3]
# Your function should return the value 26 because the longest run of monotonically increasing integers is longer than the longest run of monotonically decreasing numbers.
#print (longest_run3([1,2,3])) #single increment ok
#print (longest_run3([3,2,1])) # single increment ok
#print (longest_run3([1,2,1,2,3])) #double increment NO
#print (longest_run3([2,1,3,2,1])) #double decrement NO
#print (longest_run3([2,2,2,2,2])) #same numbers NO
#print (longest_run3([1,2,2,1])) #increment, and decrement - choose first. NO


#print (longest_run3([5, 4, 10]))