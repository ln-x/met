# -*- coding: utf-8 -*-
#!/Users/lnx/miniconda3/bin/python

__author__ = 'lnx'
import numpy as np
from netCDF4 import Dataset

def find_nearest_xy(array1, value1, array2, value2):#, array3):
   array1 = np.array(array1)
   array2 = np.array(array2)
   array_diff = (np.abs(array1 - value1) + np.abs(array2 - value2))   

   # Finding the index of the minimum value
   min_index_flat = np.argmin(array_diff)  # Index in the flattened array
   min_index = np.unravel_index(min_index_flat, array_diff.shape)  # Convert flat index to multidimensional index

   # Getting the minimum value
   min_value = array_diff[min_index]

   # Printing the minimum value and its position
   print("Minimum value:", min_value)
   print("Position (y index, x index):", min_index)

   #idx = .flatten())
   #print(np.argmin((np.abs(array1.flatten() - value1) + np.abs(array2.flatten() - value2))))
   
   return array1[min_index], array2[min_index], min_index #,array3[idx]

#Waehringerguertel/Thurygrund (48.2293, 16.35144, (63, 82))
WAE_LAT = 48.228794
WAE_LON = 16.350213

#AKH - Währinger Gürtel 18-20, 1090 Wien, Allgemeines Krankenhaus Wien (48.22, 16.34674, (60, 81))
AKH_LAT = 48.220738
AKH_LON = 16.346835

#KAN - Kandlgasse 39, 1070 Wien, GRG7 (48.201405, 16.337372, (54, 79))
KAN_LAT = 48.202627
KAN_LON = 16.339107

#JAE - Jägerhausgasse 77, 1120 Wien, HBLFA Schönbrunn Außenstelle (48.161144, 16.304626, (41, 72))
JAE_LAT = 48.161874
JAE_LON = 16.305290

#REW - Industriezentrum NÖ-Süd, Straße 3, Obj. 16, 2355 Wr. Neudorf / Heizwerkstraße 6, 1230 Wien, Rewe International Lager GmbH, 1230 Wien
#(48.139317, 16.36496, (34, 85))
REW_LAT = 48.13948459614933
REW_LON = 16.36521572847398

#check Hohe Warte  ["Wien-Hohe Warte",83,69]  #new: (48.251, 16.356201, (70, 83))
HW_LAT = 48.252083333333
HW_LON = 16.356527777778214

if __name__ == '__main__':
   infilename = "/Users/lnx/DATA/models/BOKU/WRFTEB/IMP_DROP/OBS/ARISirr/D03/D03_t2m_2022-08-10_ARIS_30p_Irrigation.nc"
   
   infile = Dataset(infilename)
   IMPDROP_GRID_ij = find_nearest_xy(infile.variables['lat'], REW_LAT,
                                                   infile.variables['lon'],
                                                   REW_LON)#, infile.variables['t2m'])
   print(IMPDROP_GRID_ij)




"""
#uozone coordinates
RUT_LAT = 48.192142
RUT_LON = 16.624939
CEN_LAT = 48.196613
CEN_LON = 16.382294
WW_LAT = 48.28
WW_LON = 16.23
"""