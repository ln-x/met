# -*- coding: utf-8 -*-
__author__ = 'lnx'
import matplotlib.pyplot as plt
import matplotlib.cm as cm # matplotlib's color map library
import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.interpolate import griddata
from skgstat.models import spherical
from scipy.linalg import solve

from met.library import ReadinVindobona_Filter_fullperiod
#from met.library import ReadinVindobona_Filter2019
from met.library import BOKUMet_Data
from datetime import datetime

#HCHO
foldername_D = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D", begin= datetime(2017, 5, 1, 0, 0, 0))
#hcho19_d, hcho19_dmax, hcho19_m = ReadinVindobona_Filter2019.loadfileALL(foldername2019)

#SM
file_rss_rutz = "/windata/DATA/obs_point/land/Bodenfeuchte_Rutzendorf/2008_2020_Rutzendorf_ARIS_results_sepp.xlsx"
rss = pd.read_excel(file_rss_rutz, sheet_name="RSS_sub", usecols="A,B,C,D,E,F", skiprows=11)#, converters={'A': pd.to_datetime})
rss.columns = ['datetime', 'RSS_sub_maize', 'RSS_sub_sBarley','RSS_sub_sugBeet','RSS_sub_wWheat', 'RSS_sub_grass']  #TODO: local time!
#rss = pd.read_excel(file_rss_rutz, sheet_name="RSS_top", usecols="A,B,C,D,E,F", skiprows=11)#, converters={'A': pd.to_datetime})
#rss.columns = ['datetime', 'RSS_top_maize', 'RSS_top_sBarley','RSS_top_sugBeet','RSS_top_wWheat', 'RSS_top_grass']  #TODO: local time!
rss = rss.set_index(pd.to_datetime(rss['datetime']))
rss = rss.drop(columns=['datetime'])

rss_ARIS = pd.read_csv("/windata/DATA/models/boku/ARIS/ARIS_x1230-40y530-40mean_wWheat.csv", sep=",")
rss_ARIS_x = rss_ARIS.set_index(pd.to_datetime(rss_ARIS['date']))
rss_ARIS = rss_ARIS_x.drop(columns=['date'])

#AT
BOKUMetData = BOKUMet_Data.BOKUMet()
BOKUMetData_hourlymean = BOKUMetData.resample('H').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
#DAILY MAX
BOKUMetData_dailymax = BOKUMetData_hourlymean.resample('D').agg({'DT': np.max, 'AT': np.max, 'RH': np.max, 'GR': np.max, 'WS': np.max,
                                                      'WD': np.max, 'WSG': np.max, 'PC': np.sum, 'AP': np.max})

#DAILY SUM
BOKUMetData_dailysum = BOKUMetData_hourlymean.resample('D').agg({'DT': np.max, 'AT': np.mean, 'RH': np.max, 'GR': np.sum, 'WS': np.max,
                                                      'WD': np.max, 'WSG': np.max, 'PC': np.sum, 'AP': np.max})


vp_sat = 0.611 * np.exp((17.3 * BOKUMetData_hourlymean["AT"])/(BOKUMetData_hourlymean["AT"]+237.3))  #kPa sh. Dingman
vp_air = 0.611 * np.exp((17.3 * BOKUMetData_hourlymean["AT"])/(BOKUMetData_hourlymean["AT"]+237.3)) * (BOKUMetData_hourlymean["RH"]/100)
vpd = vp_sat - vp_air
#print(vp_sat,vp_air, vpd)
#vpd.plot()
#plt.show()
vpd_d = vpd.resample('D').mean()
vpd_dmax = vpd.resample('D').max()
vpd_dmax_w = vpd_dmax.resample('W').max()

'''TIMESLICES'''
March19 = datetime(2019, 3, 1, 00, 00) #JD 2020=92
April19 = datetime(2019, 4, 1, 00, 00) #JD 2020=92
May17 = datetime(2017, 5, 1, 00, 00) #JD 2020=92
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

##start insert 20200820
#f2 = lambda x: (((1.25e-12)*(x**5)+ (7.38e-9)*(x**4) - (5.365e-6)*(x**3) + 0.000926*(x**2) - 0.00036*x + 1.08)*0.9*1000)
#BOKUMetData_dailysum["GRthres"] = BOKUMetData_dailysum['JD'].apply(f2)
#print(BOKUMetData_dailysum.shape)
#isHighGR = BOKUMetData_dailysum["GR"] > BOKUMetData_dailysum["GRthres"]
#X_filter = BOKUMetData_dailymax[isHighGR]
##end insert 20200820

start = May17
end = Sept20

'''READ IN Vinzenz's classification'''
metclass_r = pd.read_csv("/windata/DATA/metclass_vienna.csv", sep=";")
metclass_x = metclass_r.set_index(pd.to_datetime(metclass_r['time']))
metclass = metclass_x.drop(columns=['time'])

metclass_cut = metclass[start:end]
X = BOKUMetData_dailysum['AT'][start:end]
#Y = rss['RSS_sub_wWheat'][March19:Nov19]
#Y = rss['RSS_sub_wWheat'][March19:Nov19]
Y = rss_ARIS['RSS'][start:end]
#Y = Y.fillna(value=0)
Z = hcho_dmax
Z = Z[start:end]

Z = Z.fillna(Z.mean())
#Z = Z.fillna(value=0)
df = pd.concat([X,Y,hcho_dmax[start:end],metclass_cut,BOKUMetData_dailysum["GR"][start:end],vpd_dmax[start:end]], axis=1, keys=["AT","2","3","metclass","GR","VDP"])
#print(df)
#df = df.dropna()
df.columns = df.columns.droplevel(-1)
#df = df.drop(df[df.metclass == "C"].index)
df_clear = df.loc[df["GR"] >= 4500]
df_clear = df_clear.dropna()
print(df_clear)

X = df_clear["AT"]
#Y = df_clear["2"]
Y = df_clear["VDP"]
Z = df_clear["3"]

#"""
s0 = [2., 2.]
distance_matrix = pdist([s0] + list(zip(X,Y)))
#print(squareform(distance_matrix))
# range= 7. sill = 2. nugget = 0.
#model = lambda h: spherical(h, 7.0, 2.0, 0.0)
model = lambda h: spherical(h, 5.0, 3., 0.0)

##!!!CHECK len(M) below first! Then adapt distance_matrix and variances!!!!###
variances = model(distance_matrix[:250]) #MAM: 93, MAM only A days: 18, 1MAR - 1Nov: 246, only A days: 54
assert len(variances) == 250 #5
#print(variances)
#print(len(X),len(Y),len(Z))
#exit()
dists = pdist(list(zip(X,Y)))
M = squareform(model(dists))
print(len(M))  #<<<<<<---- CHECK here!!!!### and enter

# solve for a
a = solve(M, variances)
#print(a)

# calculate estimation
#print(Z.dot(a))
#print(np.sum(a))

#print(Z)
Z = Z * a
#print(Z)
#"""

# define grid.
#xi = np.linspace(X.min(), X.max(), 10)
#yi = np.linspace(Y.min(), Y.max(), 10)
#xi = np.linspace(5,38,30)
xi = np.linspace(0,38,30)
#yi = np.linspace(0,3,18)
yi = np.linspace(0,8,20)

# grid the data.
z_grid = griddata((X,Y),Z,(xi[None,:],yi[:,None]),method='linear',fill_value=0)

#contourplot
fig = plt.figure()
levels = np.array([0,1,2,3,4,5,6,7,8,10,11,12,13,14,15])
cpl = plt.contourf(xi,yi,z_grid,len(levels),cmap=cm.Reds)
cbar = fig.colorbar(cpl)
cbar.ax.set_ylabel('hcho [ppb]')
#plt.scatter(X,Y,marker='o',c='b',s=5)
#plt.scatter(X,Y,marker='o',c=Z,cmap=cm.coolwarm,s=25)
plt.xlabel('daily mean air temperature [degC]')
#plt.ylabel('rss wWheat ARIS [-]')
plt.ylabel('vpd [hpa]')

plt.legend()
#plt.title(f'{start} -{end}, kriging , "A" days')
plt.title(f'{start} -{end}, "A" days')
plt.show()

#cpf = ax.contourf(X,Y,Z, len(levels), cmap=cm.Reds)


exit()
