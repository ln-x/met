import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from scipy import stats
import met.library.BOKUMet_Data
from met.library.Datetime_recipies import datestdtojd
from met.library.conversions import *
from met.library import ReadinVindobona_Filter_fullperiod
from met.library import ReadinVindobona_Glyoxal
import matplotlib.gridspec as gridspec

from mpl_toolkits.axes_grid1 import host_subplot
from mpl_toolkits import axisartist
import matplotlib.pyplot as plt

yM_m = [0,1,2,3,4,5,6,7,8,9,10,11]
yM = [15,46,74,105,135,166,196,227,258,288,319,349]
yM_ticks = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
yM18 = [15,46,74,105,135,166,196,227,258,288,319]
yM19 = [15,46,74,105,135,166,196,227,258,288]
yM20 = [15,46,74,105,135,166,196,227,258,288,319]
yM21 = [15,46,74,105,135,166,196,227]
start2017 = datetime(2017, 5, 1, 00, 00)
start2018 = datetime(2018, 1, 1, 00, 00)
start2019 = datetime(2019, 1, 1, 00, 00)
start2020 = datetime(2020, 1, 1, 00, 00)
end2020 = datetime(2020, 12, 31, 00, 00)
start2021 = datetime(2021, 1, 1, 00, 00)
end2021 = datetime(2021, 9, 1, 00, 00)

'''READ IN BOKU Metdata'''
BOKUMetData = met.library.BOKUMet_Data.BOKUMet() #10min values
BOKUMetData_hourlymean = BOKUMetData.resample('H').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean, 'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_dailysum = BOKUMetData_hourlymean.resample('D').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.sum, 'WS': np.mean, 'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_dailymax = BOKUMetData_hourlymean.resample('D').agg({'DT': np.max, 'AT': np.max, 'RH': np.max, 'GR': np.max, 'WS': np.max,'WD': np.max, 'WSG': np.max, 'PC': np.sum, 'AP': np.max})
#JULIAN DAY
BOKUMetData_dailysum['JD'] = (BOKUMetData_dailysum.index)
f = lambda x: datestdtojd(str(x)[:-9])
BOKUMetData_dailysum['JD'] = BOKUMetData_dailysum['JD'].apply(f)

"read in VINDOBONA"

foldername_D = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D", begin= datetime(2017, 5, 1, 0, 0, 0))

nw = pd.concat([hcho_dmax,BOKUMetData_dailysum["WD"][datetime(2017,5,1):datetime(2021,8,31)]],axis=1)
nw.columns =['hcho', 'WD']
nw.index.name = 'datetime'
nw =nw.loc[(nw['WD'] >=270) & (nw['WD'] <=359)]

#hcho_dmax_m = hcho_dmax.resample('M').mean()
#hcho_d_m = hcho_d.resample('M').mean()   #TODO switch between all data and nw only
hcho_dmax_nw = nw['hcho']
#hcho_d_m = nw['hcho'].resample('M').mean()

hcho_dmax17 = hcho_dmax[datetime(2017,5,1,0,0):datetime(2017,12,31,0,0)]
hcho_17fill = np.full(shape=120,fill_value=np.NaN)
hcho_dmax17_a = np.append(hcho_17fill, hcho_dmax17)
hcho_dmax18 = hcho_dmax[start2018:datetime(2018,12,31,0,0)]
hcho_dmax19 = hcho_dmax[start2019:datetime(2019,12,31,0,0)]
hcho_dmax20 = hcho_dmax[start2020:datetime(2020,12,31,0,0)]
hcho_dmax21 = hcho_dmax[start2021:end2021]

#print(hcho_dmax17_a,hcho_dmax18,hcho_dmax19,hcho_dmax20,hcho_dmax21)

#hcho_dmax17_m = hcho_dmax17.ffill()
#hcho_dmax17_m= hcho_dmax17_m.resample('W').mean()
#hcho_17fill_m = np.full(shape=4,fill_value=np.NaN)
#hcho_dmax17_a_m = np.append(hcho_17fill_m, hcho_dmax17_m)
hcho_dmax18 = hcho_dmax18.ffill()
hcho_dmax18_m = hcho_dmax18.resample('M').mean()
hcho_dmax19 = hcho_dmax19.ffill()
hcho_dmax19_m = hcho_dmax19.resample('M').mean()
hcho_dmax20 = hcho_dmax20.ffill()
hcho_dmax20_m = hcho_dmax20.resample('M').mean()
hcho_dmax21 = hcho_dmax21.ffill()
hcho_dmax21_m = hcho_dmax21.resample('M').mean()
#print(hcho_dmax17_m, hcho_dmax18_m,hcho_dmax19_m,hcho_dmax20_m,hcho_dmax21_m)

#print(hcho_dmax17, hcho_dmax18_m, hcho_dmax19_m, hcho_dmax20_m)


""" FIGURE 10c """

print(hcho_dmax18, hcho_dmax19, hcho_dmax20)

figure = plt.figure
#plt.plot(range(len(hcho_dmax17_a_m)),hcho_dmax18_m, color='purple', linestyle="-", marker="x", label="2017")
plt.plot(range(len(hcho_dmax18_m)),hcho_dmax18_m, color='blue', linestyle="-", marker="x", label="2018")
plt.plot(range(len(hcho_dmax19_m)),hcho_dmax19_m, color='green', linestyle="-", marker="x",label="2019")
plt.plot(range(len(hcho_dmax20_m)),hcho_dmax20_m, color='orange', linestyle="-", marker="x",label="2020")#
#plt.plot(yM21,hcho_dmax21_m, color='red', linewidth=1, marker="x",label="2021")
plt.title("NW days")
plt.grid(True)
plt.xticks(yM_m, yM_ticks)
plt.xlabel("months")
plt.ylabel("hcho [ppb]")
plt.legend()
plt.show()
