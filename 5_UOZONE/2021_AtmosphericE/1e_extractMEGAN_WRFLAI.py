# -*- coding: utf-8 -*-
__author__ = 'lnx'
import netCDF4
import numpy as np

#LAI Input from MEGAN
infile = '/windata/Google Drive/MODELS/WRF_CHEM/VersionJan/MEGAN_WRF/laiv2003_30sec.nc'
lat = 4800
lon = 6000
variable_name = "LAI_for_Jul_2003_\(m2_perm2\)"
nci = netCDF4.Dataset(infile)

#find lai indices for Vienna: 48 / 16
print(nci.variables['lat'][23])
print(nci.variables['lon'][62])

