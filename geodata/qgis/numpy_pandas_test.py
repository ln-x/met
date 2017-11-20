import numpy as np
import numpy_groupies as npg
import pandas as pd

matrix_zero = np.zeros((2, 1))
matrix_float = np.random.rand(3,2)
matrix_int = np.random.randint(5, size=(2, 2))
matrix = np.array([[1,2,3],[2,10,100],[1,2,20],[2,3,20]])
#print matrix

data = pd.DataFrame(matrix)
print data
#data.columns = ['a', 'b']
#print data [0] #first column
#print data.ix[0] #first row
print ""

#print data.groupby(0)[1].sum()
grouped = data.groupby([0,1])[2].sum()
#grouped = data.groupby([1])[1].sum()
#grouped = data.groupby([7, 9])[3].sum()
print grouped
print grouped[1]




"""
group_idx = np.arange(5).repeat(3)
# group_idx: array([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4])
a = np.arange(group_idx.size)
# a: array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
x = npg.aggregate(group_idx, a) # sum is default
# x: array([ 3, 12, 21, 30, 39])
x = npg.aggregate(group_idx, a, 'prod')
# x: array([ 0, 60, 336, 990, 2184])
"""