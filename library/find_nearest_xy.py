# -*- coding: utf-8 -*-
__author__ = 'lnx'
import numpy as np
from netCDF4 import Dataset

def find_nearest_xy(array1, value1, array2, value2, array3):
   array1 = np.asarray(array1)
   array2 = np.asarray(array2)
   idx = (np.abs(array1 - value1)+np.abs(array2 - value2)).argmin()
   return array3[idx] #, array1[idx], array2[idx], idx


if __name__ == '__main__':
   infilename = "/windata/DATA/models/boku/EMEP/output/UOZONE/uozone_hourInst.nc"
   RUT_LAT = 48.192142
   RUT_LON = 16.624939
   CEN_LAT = 48.196613
   CEN_LON = 16.382294
   WW_LAT = 48.28
   WW_LON = 16.23
   infile = Dataset(infilename)
   print(infile.variables['lat'][:])
   #exit()
   CSCHMIDT_GRID_i = find_nearest_xy(infile.variables['lat'], WW_LAT,
                                                   infile.variables['lon'],
                                                   WW_LON, infile.variables['SURF_ppb_O3'])
   print(CSCHMIDT_GRID_i)