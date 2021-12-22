# -*- coding: utf-8 -*-
__author__ = 'lnx'
import netCDF4
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def find_nearest_xy(array1, value1, array2, value2, array3):
   array1 = np.asarray(array1)
   array2 = np.asarray(array2)
   idx = (np.abs(array1 - value1)+np.abs(array2 - value2)).argmin()
   return array3[idx] #, array1[idx], array2[idx], idx

def TROPOMI_SIF():
    TROPOMI_SIF_BASE = "/windata/DATA/remote/satellite/TROPOMI/"
    years = ['2019','2020'] #,'2021'] # '2018',
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    #days = np.array(range(31))
    #days.astype(str)
    days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    starttime = datetime(int(years[0]), int(months[0]), int(days[0]), 0, 00)
    TROPOMI_SIF_Name = []
    timeaxis = []
    for year in years:
        for month in months:
            for day in days:
                try:
                    TROPOMI_SIF_Name.append(TROPOMI_SIF_BASE + year + "/" + month + "/TROPOSIF_L2B_" + year + "-" + month + "-" + day + ".nc")
                    time = datetime(int(year), int(month), int(day))
                    timeaxis.append(time)
                    #print(TROPOMI_SIF_Name, timeaxis)
                except:
                    pass
    frames = []
    RUT_LAT =48.192142
    RUT_LON =16.624939
    CEN_LAT =48.196613
    CEN_LON =16.382294
    WW_LAT = 48.28
    WW_LON = 16.23

    for i in TROPOMI_SIF_Name:
        try:
            #print(i)
            infile1 = netCDF4.Dataset(i)
            infile1_data = infile1['/PRODUCT']
            TSIF_743 = find_nearest_xy(infile1_data.variables['latitude'], WW_LAT, infile1_data.variables['longitude'],
                                  WW_LON, infile1_data.variables['SIF_743'])
            frames.append(TSIF_743)
        except:
            pass
    frames = pd.DataFrame(frames, columns=["SIF"])
    frames = frames.set_index(pd.to_datetime(timeaxis))
    print(frames)
    return frames

if __name__ == '__main__':
    TSIF_743 = TROPOMI_SIF()
    #print(TSIF_743)
    TSIF_743.to_csv("/home/heidit/Downloads/TSIF_743_LAT48_28_LON16_23.csv")
