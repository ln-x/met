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

    list = [1,2]
    list.append([])
    list[2].append(2)
    list[2].append(3)
    list[1] = 0
    #print list

    longest_inc = []
    longest_dec = []
    longest = []
    i = 0
    run_count = 0
    #print len(L)

    while i < (len(L)):
        #print (i, run_count)
        #print (L[i], L[i+1])
        while L[i+1]:
            longest_inc.append([])
            longest_inc[run_count].append(L[i-1])
            longest_inc[run_count].append(L[i])
            i += 1
        longest_inc.append([])
        run_count += 1
        i += 1
        #print i,run_count, longest_inc

    longest = max(longest)

    longest_sum = 0
    if len(longest)== 1:
        return longest
    for i in longest:
        longest_sum += i

    return longest_sum


print (longest_run3([1,2,3])) #single increment ok
#print (longest_run3([3,2,1])) # single increment ok
#print (longest_run3([1,2,1,2,3])) #double increment NO
#print (longest_run3([2,1,3,2,1])) #double decrement NO
#print (longest_run3([2,2,2,2,2])) #same numbers NO
#print (longest_run3([2,3,2,1])) #increment, and decrement - choose first. NO

"""
def strictly_increasing(L):
    return all(x < y for x, y in zip(L, L[1:]))

def strictly_decreasing(L):
    return all(x > y for x, y in zip(L, L[1:]))

print strictly_decreasing(L)
print strictly_increasing(L)
"""