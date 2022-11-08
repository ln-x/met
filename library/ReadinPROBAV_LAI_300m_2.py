# -*- coding: utf-8 -*-
__author__ = 'lnx'
import netCDF4
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os

def find_nearest_xy(array1, value1, array2, value2, array3):
   array1 = np.asarray(array1)
   array2 = np.asarray(array2)
   idx = (np.abs(array1 - value1)+np.abs(array2 - value2)).argmin()
   return array3[idx] #, array1[idx], array2[idx], idx

#import PROBA V LAI using Jupyter notebook code (https://notebooks.terrascope.be/user/htrimmel/lab/workspaces/auto-1/tree/notebook-samples/datasets/CopernicusGlobalLand/cgls-openEO_uozone.ipynb)
"""
import openeo
session = openeo.connect("https://openeo-dev.vito.be").authenticate_oidc("egi")
session.describe_collection("CGLS_LAI300_V1_GLOBAL")
LAI300 = session.load_collection("CGLS_LAI300_V1_GLOBAL")
%time LAI300.filter_temporal("2018-01-01","2020-12-31").filter_bbox([15.8,47.8,16.6,48.5]).download("LAI.nc",format="NetCDF")
%time LAI300.filter_temporal("2018-01-01","2020-12-31").filter_bbox([16.1,48.22,16.26,48.32]).download("LAI_2.nc",format="NetCDF")
"""
#TODO select another bbox?

newdate_ts = []
def LAI():
    frames = []
    RUT_LAT = 48.192142
    RUT_LON = 16.624939
    CEN_LAT = 48.196613
    CEN_LON = 16.382294
    WW_LAT = 48.28
    WW_LON = 16.23

    LAI_BASE = "/windata/DATA/remote/satellite/PROBAV_LAI300m/raw/"
    infile1 = netCDF4.Dataset(LAI_BASE + "LAI_2.nc")  #LAI_2.nc: only close to Vienna (108x256x512), LAI.nc: stadtregion+
    LAI = infile1.variables['lai'][:][:][:]   #print(len(LAI),len(LAI[1]),len(LAI[1][1])) #t=108 y=768 x=512
    #print(LAI[107])  #108 value -> 10d period for 3 yr
    print(len(LAI))
    LAI.data[LAI == 255] = 0      #TODO 1 filter 255 values! np.nan
    LAI = LAI/30  #scalar factor applied
    LAI_amean = LAI.mean(axis=(1, 2)) #make area mean of whole domain
    t = infile1.variables['t'][:]  #days since 1990 - 01 - 01
    t = np.array(t[:])
    start = datetime(1990, 1, 1)
    #delta = timedelta(int(t[1]))
    #newdate = start + delta
    delta_ts = list(map(lambda a: timedelta(int(a)), t))
    newdate_ts = list(map(lambda a: start + a, delta_ts))

    #print(len(LAI_amean),len(newdate_ts))
    LAI_df = pd.DataFrame({"time":newdate_ts,"LAI":LAI_amean})
    LAI_df = LAI_df.set_index(pd.to_datetime(LAI_df['time']))
    LAI_df = LAI_df.drop(columns=['time'])

    return LAI_df


if __name__ == '__main__':
    LAI_df = LAI()
    plt.plot(LAI_df)
    #plt.plot(timeline, LAI)
    plt.xlabel("time [10d]")
    plt.ylabel("LAI [-]")
    plt.show()
    #LAI.to_csv("/home/heidit/Downloads/LAI.csv")
