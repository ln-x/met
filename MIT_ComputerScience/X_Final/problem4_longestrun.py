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
    longest_dec = []
    longest = []
    i = 1
    while L[i] > L[i-1]:
        longest_inc.append(i)
        i += 1
    longest.append(longest_inc)
    while L[i] < L[i-1]:
        longest_dec.append(i)
        i += 1
    longest.append(longest_dec)
    print (max(longest))

    longest = max(longest)

    longest_sum = 0
    for i in longest:
        longest_sum += i

    return longest_sum

print (longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))
#longest run of monotonically increasing numbers in L is [3, 4, 5, 7, 7]
#longest run of monotonically decreasing numbers in L is [10, 4, 3]
# Your function should return the value 26 because the longest run of monotonically increasing integers is longer than the longest run of monotonically decreasing numbers.

L = [5, 4, 10]
#longest run of monotonically increasing numbers in L is [4, 10] and the l
# ongest run of monotonically decreasing numbers in L is [5, 4].
# Your function should return the value 9 because the longest run of monotonically decreasing integers occurs before the longest run of monotonically increasing numbers.
