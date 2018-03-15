from netCDF4 import Dataset
import numpy as np

folder = "D:\_URBANIA\METDATA\Maja\KELVIN"
landuse = "LU_Tab_Wien_ref_20120601_V140520.txt"
mean1981_2010 = "V141010z01_vv07-4_ref2m_3D_klima_1981-2010.nc"

'''
x = ["000","000a","001", "001a","010", "010a", "011", "011a", "100", "100a", "101", "101a", "110", "110a", "111", "111a"] #one index ffor each cuboid point
hours = []

print len(x)
print len(x) - 1
print len (range(0,len(x)-1))

for i in range(1,len(x)):
    print i
    #hours[i] = "V141010z01_vv07-4_ref2m_3D\muklimo_V141010z01_vv07-4_ref2m_3D_Wien_V141010z01_" + x[i]
    print hours[i]
'''

fh = Dataset(mean1981_2010, mode='r')