# -*- coding: utf-8 -*-
__author__ = 'lnx'
import datetime
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import netCDF4

#simulated with DDSAT https://dssat.net/
#EPSG:31287, MGI / Austria Lambert -> deprecated! Replaced by ETRS89 / Austria Lambert (CRS code 3416).
x=1402 #lon
y=802  #lat
#fillvalue = -9999.f

#TOP:0-10cm, SUB:10-40, Combined:0-40cm
ARISfolder = "/windata/DATA/models/boku/ARIS/"

FCTOP = netCDF4.Dataset(ARISfolder + "BMon_netCDF_Basisdata/FCTOP.nc")   #field capacity of top soil 0-10 cm
FCSUB = ARISfolder + "BMon_netCDF_Basisdata/FCSUB.nc"  #field capacity of lower soil  10-40 cm
AFCTOP = ARISfolder + "BMon_netCDF_Basisdata/AFCTOP.nc"  #accessible or available field capacity
AFCSUB = ARISfolder + "BMon_netCDF_Basisdata/AFCSUB.nc"
##  VWC = FCTOP - (1-RSS)*AFCTOP

years = ['BMon_RSS_2019', 'BMon_RSS_2020','BMon_RSS_2021']
cultivars = ['grass', 'maize', 'wWheat']
#filebase = 'BMON_MO_AGROGL--:500m_' + year ...


def ARIS():
    frames = []
    frames2 = []
    RUT_LAT = 48.192142
    RUT_LON = 16.624939
    CEN_LAT = 48.196613
    CEN_LON = 16.382294
    timeaxis = []
    for year in years:
        for cultivar in cultivars:
              directory = ARISfolder + year + "/" + cultivar + "/"
              for filename in os.listdir(directory):
                  if filename.endswith("nc"):
                      year= filename[22:26]
                      month = filename[26:28]
                      day = filename[28:30]
                      time = datetime.datetime(int(year), int(month), int(day), hour=12)
                      timeaxis.append(time)
                      print(time)
                      try:
                          infile1 = netCDF4.Dataset(directory+"/"+filename)
                          #OSIF_8100 = infile1.variables['SIF_757nm'][1]
                          #ARIS = find_nearest_xy(infile1.variables['latitude'], CEN_LAT,
                          #                           infile1.variables['longitude'],
                          #                           CEN_LON, infile1.variables['SIF_757nm'])
                          frames.append(ARIS)
                      except:
                           pass

    frames = pd.DataFrame(frames, columns=["SIF_757nm"])
    return timeaxis
if __name__ == '__main__':
    time = ARIS()
    print(time)