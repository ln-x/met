# -*- coding: utf-8 -*-
__author__ = 'lnx'
import netCDF4
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os

def find_nearest_xy(array1, value1, array2, value2, array3):
   array1 = np.asarray(array1)
   array2 = np.asarray(array2)
   idx = (np.abs(array1 - value1)+np.abs(array2 - value2)).argmin()
   return array3[idx] #, array1[idx], array2[idx], idx

def OCO2_SIF():
    frames = []
    frames2 = []
    RUT_LAT = 48.192142
    RUT_LON = 16.624939
    CEN_LAT = 48.196613
    CEN_LON = 16.382294
    WW_LAT = 48.28
    WW_LON = 16.23

    OCO2_SIF_BASE = "/windata/DATA/remote/satellite/OCO2/sif_lite_B8100/"
    years = ['2017','2018','2019','2020'] #,'2021'] # '2018',
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    #days = np.array(range(31))
    #days.astype(str)
    days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    starttime = datetime(int(years[0]), int(months[0]), int(days[0]), 0, 00)
    OCO2_SIF_DirName = []
    timeaxis = []
    for year in years:
        for month in months:
            try:
              directory = OCO2_SIF_BASE + year + "/" + month + "/"
              for filename in sorted(os.listdir(directory)):
                  if filename.endswith("nc4"):
                      day = filename[15:17]
                      time = datetime(int(year), int(month), int(day))
                      timeaxis.append(time)
                      try:
                          infile1 = netCDF4.Dataset(directory+"/"+filename)
                          #OSIF_8100 = infile1.variables['SIF_757nm'][1]
                          OSIF_757 = find_nearest_xy(infile1.variables['latitude'], WW_LAT,
                                                     infile1.variables['longitude'],
                                                     CEN_LON, infile1.variables['SIF_757nm'])
                          OSIF_771 = find_nearest_xy(infile1.variables['latitude'], WW_LAT,
                                                     infile1.variables['longitude'],
                                                     CEN_LON, infile1.variables['SIF_771nm'])
                          frames.append(OSIF_757)
                          frames2.append(OSIF_771)

                      except:
                           pass
            except:
              pass
    frames = pd.DataFrame(frames, columns=["SIF_757nm"])
    frames2 = pd.DataFrame(frames, columns=["SIF_771nm"])
    frames = frames.set_index(pd.to_datetime(timeaxis))
    frames2 = frames2.set_index(pd.to_datetime(timeaxis))
    #print(frames)
    return frames, frames2




if __name__ == '__main__':
    OSIF_757, OSIF_771 = OCO2_SIF()
    #OSIF_757 = OCO2_SIF()
    print(OSIF_757)
    OSIF_757.to_csv("/home/heidit/Downloads/OSIF_8100_757nm.csv")
    OSIF_771.to_csv("/home/heidit/Downloads/OSIF_8100_771nm.csv")

