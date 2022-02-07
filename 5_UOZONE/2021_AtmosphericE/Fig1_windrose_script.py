# Import the required packages
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from math import pi
from windrose import WindroseAxes
from datetime import datetime, timedelta

# Uncomment the following line in case you are missing those packages
# !pip install windrose openpyxl WARNING: The script sample is installed in '/home/heidit/.local/bin' which is not on PATH.
#   Consider adding this directory to PATH

M_GE = "/windata/DATA/obs_point/met/ZAMG/Jahrbuch/ZAMG_Jahrbuch2020_Monatsauswertung_GroßEnzersdorf.csv"
M_IS = "/windata/DATA/obs_point/met/ZAMG/Jahrbuch/ZAMG_Jahrbuch2020_Monatsauswertung_InnereStadt.csv"
M_HW = "/windata/DATA/obs_point/met/ZAMG/Jahrbuch/ZAMG_Jahrbuch2019_Monatsauswertung_HoheWarte.csv"
T_HW = "/windata/DATA/obs_point/met/ZAMG/Jahrbuch/ZAMG_Jahrbuch2019_Tagesauswertung_HW.csv"
synop = "/windata/DATA/obs_point/met/ZAMG/DataHub/synop_UOZONE.csv"

"""Hourly Values from ZAMG Data Hub - synop
dd   Windrichtung
ff   Windgeschwindigkeit
Tmax Maximum der Lufttemperatur
T    Lufttemperatur
N    Gesamtbedeckung des Himmels mit Wolken
Ir   Niederschlagsindikator
Pg   Luftdruck
RRR  Niederschlagsmenge im Beobachtungszeitraum tr
VV   Sichtweite
h    Höhe der tiefsten Wolken
tr   Beobachtungszeitrum für Niederschlag
"""
stations = {"11037":"Großenzersdorf", "11090":"Donaufeld", "11034":"Innere Stadt", "11035":"Hohe Warte", "11040":"Unterlaa" }
stations1 = {"5917":"Unterlaa", "5935":"Gross-Enzersdorf","5925":"Wien Innere Stadt"} #not used: 5802 - Wien Jubliaeumswrte, 5901-Wien Hohe Warte, 5935-Donaufeld
parameter = {"dd":"wind dir", "ff":"wind speed","Tmax":"tmax","T":"T","N":"cloud cover","Ir":"precipitation indic.",
             "Pg":"air pressure","RRR":"precip", "VV":"view", "h":"height of lowerst clouds","tr":"observe time for precip." }

df = pd.read_csv(synop, sep=",", skiprows=1) #47
df.columns = ['station', 'time', 'dd','ff','Tmax','T','N','Ir','Pg','RRR','VV','h','tr']
df = df.set_index(pd.to_datetime(df['time']))
df = df.drop(columns=['time'])

GE = df.loc[df['station'] == 11037]
DF = df.loc[df['station'] == 11090]
IS = df.loc[df['station'] == 11034]
HW = df.loc[df['station'] == 11035]
UL = df.loc[df['station'] == 11040]

start = datetime(2017, 5, 1, 00, 00) #start
DP1_s = datetime(2019, 3, 17, 00, 00) #drought period1 start
DP1_e = datetime(2019, 4, 29, 00, 00) #drought period1 end
DP2_s = datetime(2019, 6, 8, 00, 00) #drought period2 start
DP2_e = datetime(2019, 6, 30, 00, 00) #drought period2 end
DP3_s = datetime(2019, 8, 13, 00, 00) #drought period3 start
DP3_e = datetime(2019, 8, 31, 00, 00) #drought period3 end
DP4_s = datetime(2020, 3, 22, 00, 00) #drought period4 start
DP4_e = datetime(2020, 4, 11, 00, 00) #drought period4 end

data = GE[['dd','ff']][start:]
#data = data[DP4_s:DP4_e]
#print(data)
#exit()

plt.plot(data['dd'],linestyle='',marker='x')
#plt.show()
#exit()
#data = df.loc[df['dd'] != 90]

#remove_calm = lambda x: x if x == 90 else x
#data['dd'] = remove_calm(data['dd'])
print(data)

#data['dd'] = (data['dd']/10)*45
#print(data)
#exit()

nw1 = data.loc[data['dd'] >= 270]
nw = nw1.loc[nw1['dd'] <= 360]

se1 = data.loc[data['dd'] >= 90]
se = se1.loc[se1['dd'] <= 180]

windrosechart = data

ax = WindroseAxes.from_ax()
ax.bar(windrosechart.dd, windrosechart.ff, normed=True, opening=0.8, edgecolor='white', bins=np.arange(0, 8, 1))
#ax.contourf(windrosechart.dd, windrosechart.ff, nsector=36, bins=np.arange(0, 8, 1), cmap=cm.hot)
#ax.contourf(windrosechart.dd, windrosechart.ff, nsector=36, bins=np.arange(0, 8, 1), cmap=cm.hot)
##10 degree steps:
#ax.set_thetagrids(range(0,360,10),[90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 350, 340, 330, 320, 310, 300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100])
#ax.set_theta_zero_location('W', offset=-90)
#ax.set_theta_direction(-1)
ax.set_legend()
ax.set_title("GE, full period")
ax.set_xticklabels(['E', 'NE','N', 'NW', 'W', 'SW', 'S', 'SE'])
ax.set_yticks(np.arange(0, 50, step=5))
ax.set_yticklabels(np.arange(0, 50, step=5))
#ax.set_yticks(np.arange(0, 1000, step=100))
#ax.set_yticklabels(np.arange(0, 1000, step=100))
#x.set_xticklabels((90, 45, 0, 315, 270, 225, 180, 135))
plt.show()
#exit()

ax = WindroseAxes.from_ax()
ax.bar(nw.dd, nw.ff, normed=True, opening=0.8, edgecolor='white',bins=np.arange(0, 8, 1))
#ax.contourf(nw.dd, nw.ff, bins=np.arange(0, 8, 1), cmap=cm.hot)
ax.set_legend()
ax.set_title("GE, nw")
#ax.title(df['station'] + "nw")
ax.set_xticklabels(['E', 'NE','N', 'NW', 'W', 'SW', 'S', 'SE'])
ax.set_yticks(np.arange(0, 50, step=5))
ax.set_yticklabels(np.arange(0, 50, step=5))
plt.show()

ax = WindroseAxes.from_ax()
ax.bar(se.dd, se.ff, normed=True, opening=0.8, edgecolor='white',bins=np.arange(0, 8, 1))
#ax.contourf(se.dd, se.ff, bins=np.arange(0, 8, 1), cmap=cm.hot)
ax.set_legend()
#ax.title(df['station'] + "se")
ax.set_title("GE, se")
ax.set_xticklabels(['E', 'NE','N', 'NW', 'W', 'SW', 'S', 'SE'])
ax.set_yticks(np.arange(0, 50, step=5))
ax.set_yticklabels(np.arange(0, 50, step=5))
plt.show()

exit()
for (index_label, row_series) in wind[:-1].iterrows(): #all months of a year
    print(row_series.values)
    monthly = []
    for i in range(8): #8 wind directions
       for k in range(int(row_series.values[i])):
            monthly.append([float(row_series.values[-1].replace(',', '.')),int(wind.columns[i])])
    windrosechart = pd.DataFrame(monthly, columns=['VELOCIDAD', 'DIRECCION'])
    ax = WindroseAxes.from_ax()
    #ax.bar(windrosechart.DIRECCION, windrosechart.VELOCIDAD, normed=True, opening=0.8, edgecolor='white')
    ax.contourf(windrosechart.DIRECCION, windrosechart.VELOCIDAD, bins=np.arange(0, 8, 1), cmap=cm.hot)
    ax.set_xticklabels(['E', 'NE', 'N', 'NW', 'W', 'SW', 'S', 'SE'])
    ax.set_legend()
 #  ax.title(df['station'][0], index_label)
    #plt.show()
    plt.savefig("IS2020" + index_label + ".jpg")

exit()



"""Monthly values from Jahrbuch"""
"""
df = pd.read_csv(M_IS, sep=";", skiprows=5) #47
df.columns = ['station', 'LAT', 'LON','masl','position', 'position2','chapter','Parameter', 'JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC','year']  #TODO: local time!
wind = df.drop(columns=['station', 'LAT', 'LON','masl','position', 'position2'])
wind = wind.loc[wind['chapter'] == 'Wind']
wind = wind.set_index(wind['Parameter'])
wind = wind.drop(columns=['chapter','Parameter'])
wind = wind.transpose()
wind.columns = ['N', 'NE','E','SE', 'S','SW','W', 'NW','C','VELOCIDAD']  #TODO: local time!
wind.columns = ['0', '45','90','135', '180','225','270', '315','C','VELOCIDAD']  #TODO: local time!
print(wind)

#data = [[wind['VELOCIDAD'][0],45], [wind['VELOCIDAD'][0],135], [wind['VELOCIDAD'][0],90]]

data = []

for (index_label, row_series) in wind[:-1].iterrows(): #all months of a year
    print(row_series.values)
    for i in range(8): #8 wind directions
       for k in range(int(row_series.values[i])):
            data.append([float(row_series.values[-1].replace(',', '.')),int(wind.columns[i])])

print(data)

#data2 = [[1,60],[4,135],[3,90],[2,45],[3,120],[3,90]]
windrosechart = pd.DataFrame(data, columns = ['VELOCIDAD','DIRECCION'])

ax = WindroseAxes.from_ax()
ax.bar(windrosechart.DIRECCION, windrosechart.VELOCIDAD, normed=True, opening=0.8, edgecolor='white')
#ax.contourf(windrosechart.DIRECCION, windrosechart.VELOCIDAD, bins=np.arange(0, 8, 1), cmap=cm.hot)
ax.set_legend()
#ax.title(df['station'][0])
plt.show()


for (index_label, row_series) in wind[:-1].iterrows(): #all months of a year
    print(row_series.values)
    monthly = []
    for i in range(8): #8 wind directions
       for k in range(int(row_series.values[i])):
            monthly.append([float(row_series.values[-1].replace(',', '.')),int(wind.columns[i])])
    windrosechart = pd.DataFrame(monthly, columns=['VELOCIDAD', 'DIRECCION'])
    ax = WindroseAxes.from_ax()
    ax.bar(windrosechart.DIRECCION, windrosechart.VELOCIDAD, normed=True, opening=0.8, edgecolor='white')
    # ax.contourf(windrosechart.DIRECCION, windrosechart.VELOCIDAD, bins=np.arange(0, 8, 1), cmap=cm.hot)
    ax.set_legend()
 #  ax.title(df['station'][0], index_label)
    #plt.show()
    plt.savefig("IS2020" + index_label + ".jpg")
"""
exit()

wind['velocidad_x'] = wind['VELOCIDAD'] * np.sin(df['DIRECCION'] * pi / 180.0)
df['velocidad_y'] = df['VELOCIDAD'] * np.cos(df['DIRECCION'] * pi / 180.0)


fig, ax = plt.subplots(figsize=(8, 8), dpi=80)
x0, x1 = ax.get_xlim()
y0, y1 = ax.get_ylim()
ax.set_aspect('equal')

df.plot(kind='scatter', x='velocidad_x', y='velocidad_y', alpha=0.35, ax=ax)

df['VELOCIDAD'].hist(figsize=(10,6))


