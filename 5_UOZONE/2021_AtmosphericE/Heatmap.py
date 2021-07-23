# -*- coding: utf-8 -*-
from pylab import *
__author__ = 'lnx'
import matplotlib.pyplot as plt
import matplotlib.cm as cm # matplotlib's color map library
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.interpolate import griddata
import numpy.ma as ma
from met.library import ReadinVindobona_Filter
from met.library import ReadinVindobona_Filter2019
from met.library import BOKUMet_Data
from datetime import datetime, timedelta
#WT_20a_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime')
#contour_levels = arange(10, 30, 0.5)
#X = WT_20a_2085_V100.columns.values
#Y = WT_20a_2085_V100.index.values
#Z = WT_20a_2085_V100.values
#Xi,Yi = np.meshgrid(X, Y)
#CS = plt.contourf(Yi, Xi, Z, contour_levels,
#                  alpha=0.7, cmap=plt.cm.jet, extend='both');
#plt.clabel(CS, inline=True, fmt='%1.1f', fontsize=10)
#plt.colorbar(CS)
#plt.title(u'Water temperature [° C] 2085/20a, V100, MLF')
#plt.xlabel('Time [days]')
#plt.ylabel('Distance from source [km]')
#show()

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
X = BOKUMetData_dailymax['AT'][March19:Nov19]
#print(len(X))
#print(X)
Y = rss['RSS_top_maize'][March19:Nov19]
#print(len(Y))
#print(Y)
Z = hcho19_dmax.append(hcho_dmax)
Z = Z[March19:Nov19]
#print(len(Z))
#print(Z)

# define grid.
#xi = np.linspace(0.1,1,18)
#yi = np.linspace(15,30,30)
# grid the data.
#zi = griddata((X, Y), Z, (xi[None,:], yi[:,None]), method='cubic')
#zi = griddata((X, Y), Z,(xi, yi), method='cubic')
#print(zi)

data = {'AT': X,
        'RSS': Y,
        'HCHO': Z
        }
df = pd.DataFrame(data,columns=['AT','RSS','HCHO'])
corrMatrix = df.corr()
#sns.heatmap(corrMatrix, annot=True)
#plt.show()

df = df.round({'AT':1, 'RSS':2,'HCHO':1})
#print(df.head())
#plt.plot(df['HCHO'])
#plt.show()
#exit()
Z = df.pivot_table(index='AT', columns='RSS', values='HCHO', aggfunc='mean', dropna=True, fill_value=0).T.values
X_unique = np.sort(df.AT.unique())
Y_unique = np.sort(df.RSS.unique())
X, Y = np.meshgrid(X_unique, Y_unique)
print(pd.DataFrame(Z).round(3))
#print(X_unique,Y_unique)
print(pd.DataFrame(X).round(3))
print(pd.DataFrame(Y).round(3))

levels = np.array([0,1,2,3,4,5,6,7,8,10,11,12])
#levels = np.array([0,0.5,1,1.5,2,2.5,3])


# Generate a color mapping of the levels we've specified

fig = plt.figure()
ax = fig.add_subplot(111)

# Generate a contour plot
#cpf = ax.contourf(X,Y,Z, len(levels), cmap=cm.Reds)
#line_colors = ['black' for l in cpf.levels]

#cp = ax.contour(X, Y, Z)#, levels=levels) #,
#cbar = fig.colorbar(cp)
#cbar.ax.set_ylabel('hcho')
# Add the contour line levels to the colorbar
#cbar.add_lines(cp)

#ax.clabel(cp, fontsize=10, colors=line_colors)
#plt.xticks([10,15,20,25,30,35])
#plt.yticks([0,0.2, 0.4,0.6,0.8,1])

cpf = ax.contourf(X,Y,Z, len(levels), cmap=cm.Reds)
cbar = fig.colorbar(cpf)
cbar.ax.set_ylabel('hcho')
ax.set_title('MAM JJA SO 2019')
ax.set_xlabel('tmax [degC]')
ax.set_ylabel('rss [-]')
#ax.legend(loc='upper right')
#plt.xlim([14,26])
#plt.ylim([0.3,0.6])
#proxy = [plt.Rectangle((1, 1), 2, 2, fc=pc.get_facecolor()[0]) for pc in cp.collections]
#plt.legend(proxy, ["C1", "C2", "C3"])

#plt.legend()
plt.show()


exit()
# contour the gridded data, plotting dots at the randomly spaced data points.
CS = plt.contour(xi,yi,zi,15,linewidths=0.5,colors='k')
CS = plt.contourf(xi,yi,zi,15,cmap=plt.cm.jet)
plt.colorbar() # draw colorbar
# plot data points.
plt.scatter(X,Y,marker='o',c='b',s=5)
plt.xlim(0.5,1)
plt.ylim(6,24)
#plt.title('griddata test (%d points)')
plt.show()
exit()

data = pd.DataFrame({'X': X, 'Y': Y, 'Z': Z})
data_pivoted = data.pivot("X", "Y", "Z")
ax = sns.heatmap(data_pivoted)
plt.show()

#Xi,Yi = np.meshgrid(X, Y)
#CS = plt.contourf(Yi, Xi, Z, contour_levels,
#                  alpha=0.7, cmap=plt.cm.jet, extend='both');
#plt.clabel(CS, inline=True, fmt='%1.1f', fontsize=10)
#plt.colorbar(CS)
#plt.title(u'HCHO [ppm] Axis D, MAM 2019')
#plt.xlabel('Tmax [degC]')
#plt.ylabel('RSS [-]')
#show()