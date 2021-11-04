# -*- coding: utf-8 -*-
__author__ = 'lnx'
import netCDF4
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def find_nearest_xy(array1, value1, array2, value2, array3):
   array1 = np.asarray(array1)
   array2 = np.asarray(array2)
   idx = (np.abs(array1 - value1)+np.abs(array2 - value2)).argmin()
   return array3[idx] #, array1[idx], array2[idx], idx

def CAMXin_MEGANout():
    CAMXin_MEGANout_BASE = "/windata/DATA/models/boku/CAMX/BOKU2020/3_CAMXinput_MEGANout/"
    years = ['2020'] #2015
    months = ['01','02','03','04']#,'05','06','07','08','09','10','11','12']
    #days = np.array(range(31))
    #days.astype(str)
    days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    MEGANout_Name = []
    timeaxis = []
    for year in years:
        for month in months:
            for day in days:
                try:
                    MEGANout_Name.append(CAMXin_MEGANout_BASE + "BOKU3/megan_out_CB05_BOKU3_" + year + month + day + ".nc")
                    #time = datetime(int(year), int(month), int(day))
                    #timeaxis.append(time)
                    #print(timeaxis)
                except:
                    pass
    frames = []

    starttime = datetime(int(years[0]), int(months[0]), int(days[0]))
    time = starttime
    for i in MEGANout_Name:
        try:
            infile1 = netCDF4.Dataset(i)
            ISOP = infile1['ISOP'][:, 0, 76, 181]
            ISOP = ISOP.mean(axis=0)
            frames.append(ISOP)
            timeaxis.append(time)
            time = time + timedelta(days=1)
        except:
            pass
    frames = pd.DataFrame(frames, columns=["ISOP"]) #TERP
    frames = frames.set_index(pd.to_datetime(timeaxis))
    print(frames)
    return frames

if __name__ == '__main__':
    MEGANout = CAMXin_MEGANout()
    #print(TSIF_743)
    figure = plt.figure
    plt.plot(MEGANout["ISOP"],linestyle="-",label="ISOP")
    plt.ylabel("biogenic VOC emission [mol/s]")
    plt.xlabel("time [h]")
    plt.legend(loc='upper left')
    plt.show()
    #MEGANout.to_csv("/home/heidit/Downloads/MEGANout.csv")
