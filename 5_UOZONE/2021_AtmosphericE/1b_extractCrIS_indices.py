# -*- coding: utf-8 -*-
__author__ = 'lnx'
import netCDF4
import numpy as np

infile2 = '/windata/Google Drive/DATA/remote/satellite/SuomiNNP_CrIS/201310_CrIS_Isoprene.nc'

#global isoprene data: find Vienna
nci = netCDF4.Dataset(infile2)
print(nci.variables['lat'][69]) #48LAT
print(nci.variables['lon'][78]) #15LON
print(nci.variables['Isop'][69,78])
#for 2013_01: 843505200000000.0 [molec/cm²] CrIS retrieved isoprene column density
#for 2013_04: 581560250000000.0
#for 2013_07: 247324400000000.0
#for 2013_10: 319617700000000.0
exit()
