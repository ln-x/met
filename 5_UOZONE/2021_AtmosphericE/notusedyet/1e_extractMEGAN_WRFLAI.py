# -*- coding: utf-8 -*-
__author__ = 'lnx'
import netCDF4
import numpy as np

#LAI Input from MEGAN
#totallat = 4800
#totallon = 6000

lat_vie = 2184
lon_vie = 3164

months = ["01","02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
months_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
for i in range(12):
    infile = '/windata/Google Drive/MODELS/WRF_CHEM/VersionJan/MEGAN_WRF/laiv2003' + months[i] + '_30sec.nc'
    variable_name = "LAI_for_" + months_names[i] + "_2003_(m2_per_m2)"
    nci = netCDF4.Dataset(infile)
    print(months_names[i], nci.variables[variable_name][lat_vie, lon_vie])

#Vienna/Coordinates
#48.2082° N, 16.3738° E
#find lai indices for Vienna: 48 / 16

#print(nci.variables['lat'][2184])
#print(nci.variables['lon'][3164])

#print(nci.variables[variable_name][lat_vie,lon_vie])

