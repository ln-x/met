# -*- coding: utf-8 -*-
from netCDF4 import Dataset

outpath ='/media/lnx/Norskehavet/WRF-TEB-NC_Files/201508/'
file = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201508/Ref_Heidi_Lu_2015_1stRun/wrfout_d03_2015-08-05_18_00_00.nc'
file1 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201508/Sprawl_2050_2ndRun/wrfout_d03_2015-08-05_18_00_00.nc'
file2 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201508/Dense_2050_3rdRun_Optimized_city/wrfout_d03_2015-08-05_18_00_00.nc'

f = Dataset(file, mode='r')
f1 = Dataset(file1, mode='r')
f2 = Dataset(file2, mode='r')

lon = f.variables['XLONG'][1]  #lon (199x)135x174
lat = f.variables['XLAT'][1]   #lat (199x)135x174
LU = f.variables['LU_INDEX'][1]

lon1 = f1.variables['XLONG'][1]  #lon (199x)135x174
lat1 = f1.variables['XLAT'][1]   #lat (199x)135x174
LU1 = f1.variables['LU_INDEX'][1]

lon2 = f2.variables['XLONG'][1]  #lon (199x)135x174
lat2 = f2.variables['XLAT'][1]   #lat (199x)135x174
LU2 = f2.variables['LU_INDEX'][1]


#print range(len(lon),-1,-1)#, range(len(lon[1]))
#exit()

#31 = low density, 32 = high density, 33 = commercial

for i in range(len(lon)-1,-1,-1):
    for j in range(len(lon[1])):
       print lat2[i][j], lon2[i][j], int(LU2[i][j])

exit()

for i in range(len(lon)-1,-1,-1):
    for j in range(len(lon[1])):
       print lat1[i][j], lon1[i][j], int(LU1[i][j])

for i in range(len(lon)-1,-1,-1):
    for j in range(len(lon[1])):
       print lat[i][j], lon[i][j], int(LU[i][j])

