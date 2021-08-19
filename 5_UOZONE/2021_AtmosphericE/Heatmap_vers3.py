# -*- coding: utf-8 -*-
__author__ = 'lnx'
import matplotlib.pyplot as plt
import matplotlib.cm as cm # matplotlib's color map library
import pandas as pd
import numpy as np
from scipy.interpolate import griddata

from met.library import ReadinVindobona_Filter
from met.library import ReadinVindobona_Filter2019
from met.library import BOKUMet_Data
from datetime import datetime, timedelta

#HCHO
foldername = "/windata/DATA/remote/ground/maxdoas/MAXDOAS2020/DQ/"
foldername2019 = "/windata/DATA/remote/ground/maxdoas/MAXDOAS2019/"
hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter.loadfileALL(foldername)
hcho19_d, hcho19_dmax, hcho19_m = ReadinVindobona_Filter2019.loadfileALL(foldername2019)

#SM
file_rss_rutz = "/windata/DATA/obs_point/land/Bodenfeuchte_Rutzendorf/2008_2020_Rutzendorf_ARIS_results_sepp.xlsx"
rss = pd.read_excel(file_rss_rutz, sheet_name="RSS_top", usecols="A,B,C,D,E,F", skiprows=11)#, converters={'A': pd.to_datetime})
rss.columns = ['datetime', 'RSS_top_maize', 'RSS_top_sBarley','RSS_top_sugBeet','RSS_top_wWheat', 'RSS_top_grass']  #TODO: local time!
rss = rss.set_index(pd.to_datetime(rss['datetime']))
rss = rss.drop(columns=['datetime'])

#AT
BOKUMetData = BOKUMet_Data.BOKUMet()
BOKUMetData_hourlymean = BOKUMetData.resample('H').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
#DAILY MAX
BOKUMetData_dailymax = BOKUMetData_hourlymean.resample('D').agg({'DT': np.max, 'AT': np.max, 'RH': np.max, 'GR': np.max, 'WS': np.max,
                                                      'WD': np.max, 'WSG': np.max, 'PC': np.sum, 'AP': np.max})
'''TIMESLICES'''
March19 = datetime(2019, 3, 1, 00, 00) #JD 2020=92
April19 = datetime(2019, 4, 1, 00, 00) #JD 2020=92
May19 = datetime(2019, 5, 1, 00, 00) #JD 2020=92
June19 = datetime(2019, 6, 1, 00, 00)  #JD 2020=183
Jul19 = datetime(2019, 7, 1, 00, 00)  #JD 2020=183
Aug19 = datetime(2019, 8, 1, 00, 00) #JD 2020=92
Sept19 = datetime(2019, 9, 1, 00, 00)  #JD 2020=183
Nov19 = datetime(2019, 11, 1, 00, 00)  #JD 2020=183
Dec19 = datetime(2019, 12, 1, 00, 00)  #JD 2020=183
March20 = datetime(2020, 3, 1, 00, 00) #JD 2020=92
June20 = datetime(2020, 6, 1, 00, 00)  #JD 2020=183
Aug20 = datetime(2020, 8, 1, 00, 00)  #JD 2020=183
Sept20 = datetime(2020, 9, 1, 00, 00)  #JD 2020=183
#contour_levels = arange(1, 2, 5)
X = BOKUMetData_dailymax['AT'][June19:Sept19]
Y = rss['RSS_top_maize'][June19:Sept19]
Z = hcho19_dmax.append(hcho_dmax)
Z = Z[June19:Sept19]


Z = Z.fillna(Z.mean())
#Z = Z.fillna(value=0)


# define grid.

#xi = np.linspace(X.min(), X.max(), 10)
#yi = np.linspace(Y.min(), Y.max(), 10)
xi = np.linspace(5,38,30)
yi = np.linspace(0.05,1,18)

# grid the data.
z_grid = griddata((X,Y),Z,(xi[None,:],yi[:,None]),method='cubic',fill_value=0)

#contourplot
fig = plt.figure()
levels = np.array([0,1,2,3,4,5,6,7,8,10,11,12])
cpl = plt.contourf(xi,yi,z_grid,len(levels),cmap=cm.Reds)
cbar = fig.colorbar(cpl)
cbar.ax.set_ylabel('hcho [ppb]')
plt.scatter(X,Y,marker='o',c='b',s=5)
plt.xlabel('daily max air temperature [degC]')
plt.ylabel('rss [-]')
#plt.title('March19:Nov19, linear interpolation')
plt.title('1June19:1Sep19, cubic interpolation')
plt.show()

#cpf = ax.contourf(X,Y,Z, len(levels), cmap=cm.Reds)


exit()
