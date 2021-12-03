# -*- coding: utf-8 -*-
__author__ = 'lnx'
import netCDF4
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os

RUT_LAT = 48.192142
RUT_LON = 16.624939
CEN_LAT = 48.196613
CEN_LON = 16.382294

def find_nearest_xy(array1, value1, array2, value2, array3):
   array1 = np.asarray(array1)
   array2 = np.asarray(array2)
   idx = (np.abs(array1 - value1)+np.abs(array2 - value2)).argmin()
   return array3[idx]

def TROPOMI_SIF():
    TROPOMI_SIF_BASE = "/windata/DATA/remote/satellite/TROPOMI/"
    years = ['2018','2019','2020','2021']
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    timeaxis = []
    frames = []
    for year in years:
        for month in months:
          try:
            foldername = TROPOMI_SIF_BASE + year + "/" + month
            files = os.listdir(foldername)
            for i in files:
                    try:
                        #print(str(i[21:23]))
                        filename = foldername + "/" + i
                        #print(filename)
                        daydt = str(i[21:23])
                        monthdt = str(i[18:20])
                        yeardt = str(i[13:17])
                        print(daydt,monthdt,yeardt)
                        troposif_date = datetime(year=int(yeardt), month=int(monthdt), day=int(daydt))
                        print(troposif_date)
                        timeaxis.append(troposif_date)

                        infile1 = netCDF4.Dataset(filename)
                        infile1_data = infile1['/PRODUCT']
                        TSIF_743 = find_nearest_xy(infile1_data.variables['latitude'], CEN_LAT,
                                                   infile1_data.variables['longitude'],
                                                   CEN_LON, infile1_data.variables['SIF_743'])
                        frames.append(TSIF_743)

                    except:
                        pass
          except:
            print(year, month, " can not be found")
            pass

    frames = pd.DataFrame(frames, columns=["SIF"])
    print(timeaxis)
    frames = frames.set_index(pd.to_datetime(timeaxis))
    print(frames)
    return frames

if __name__ == '__main__':
    TSIF_743 = TROPOMI_SIF()
    #print(TSIF_743)
    TSIF_743.to_csv("/home/heidit/Downloads/TSIF_743.csv")

#TODO solve error:
#File "/home/heidit/PycharmProjects/met/library/ReadinTROPOMISIF_743.py", line 51, in TROPOMI_SIF
#  frames = frames.set_index(pd.to_datetime(timeaxis))
#File "/usr/local/lib/python3.8/dist-packages/pandas/core/frame.py", line 4767, in set_index
#   raise ValueError(
#ValueError: Length mismatch: Expected 976 rows, received array of length 1096
