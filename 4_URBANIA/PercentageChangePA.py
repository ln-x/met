import numpy as np

l = 2030-2013
A = np.zeros(l + 1)
A[0] = 56

for i in range(l):
    print A[i], i
    A[i+1] = A[i]*1.01

print A