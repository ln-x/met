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

folders = ['BMon_RSS_2019', 'BMon_RSS_2020','BMon_RSS_2021']
cultivars = ['grass', 'maize', 'wWheat']
#filebase = 'BMON_MO_AGROGL--:500m_' + year ...

#def find_nearest_xy(array1, value1, array2, value2, array3):
#   array1 = np.asarray(array1)
#   array2 = np.asarray(array2)
#   idx = (np.abs(array1 - value1)+np.abs(array2 - value2)).argmin()
#   return array3[idx], array1[idx], array2[idx], idx

def ARIS():
    frames = []
    timeaxis = []
    RUT_LAT = 48.192142
    RUT_LON = 16.624939
    #CEN_LAT = 48.196613
    #CEN_LON = 16.382294
    CEN_LAT = 539
    CEN_LON = 1242
    for folder in folders:
        #for cultivar in cultivars:
              directory = ARISfolder + folder + "/" + "wWheat" + "/"
              #lst = os.listdir(directory)
              #lst = lst.sort()
              #print(lst)
              for filename in sorted(os.listdir(directory)):
                  #if filename.endswith("nc"):
                      #print(filename)
                      #timeaxis.append(time)
                      #try:
                          infile1 = netCDF4.Dataset(directory+"/"+filename)
                          #print(infile1.__dict__['product_spatial_sampling'])
                          #for dim in infile1.dimensions.values():
                          #    print(dim) #x=1402, y=802
                          #for var in infile1.variables.values():
                          #    print(var)
                          #print(infile1['RSS_SUB'][CEN_LAT,CEN_LON])
                          a = infile1['RSS_SUB'][520:540,1230:1250].mean()  #530:540,1230:1240

                          #a,b,c,d = find_nearest_xy(infile1.variables['y'], CEN_LAT,
                          #                           infile1.variables['x'],
                          #                           CEN_LON, infile1.variables['RSS_TOP'])
                          #print(a,b,c,d)
                          frames.append(a)
                          year = filename[22:26]
                          month = filename[26:28]
                          day = filename[28:30]
                          time = datetime.datetime(int(year), int(month), int(day), hour=00)
                          timeaxis.append(time)
                      #except:
                      #     pass

    frames = pd.DataFrame(frames, columns=["RSS"])
    frames = frames.set_index(pd.to_datetime(timeaxis))
    frames.index.name = "date"
    #return timeaxis
    return frames
if __name__ == '__main__':
    frames = ARIS()
    #print(frames)
    frames.to_csv("/windata/DATA/models/boku/ARIS/ARIS_x1230-40y530-40mean_wWheat.csv")