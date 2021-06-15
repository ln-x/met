# Import the required packages
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from math import pi
from windrose import WindroseAxes

# Uncomment the following line in case you are missing those packages
# !pip install windrose openpyxl WARNING: The script sample is installed in '/home/heidit/.local/bin' which is not on PATH.
#   Consider adding this directory to PATH

M_GE = "/windata/DATA/obs_point/met/ZAMG/Jahrbuch/ZAMG_Jahrbuch2020_Monatsauswertung_GroßEnzersdorf.csv"
M_IS = "/windata/DATA/obs_point/met/ZAMG/Jahrbuch/ZAMG_Jahrbuch2020_Monatsauswertung_InnereStadt.csv"
M_HW = "/windata/DATA/obs_point/met/ZAMG/Jahrbuch/ZAMG_Jahrbuch2019_Monatsauswertung_HoheWarte.csv"
T_HW = "/windata/DATA/obs_point/met/ZAMG/Jahrbuch/ZAMG_Jahrbuch2019_Tagesauswertung_HW.csv"

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

exit()

wind['velocidad_x'] = wind['VELOCIDAD'] * np.sin(df['DIRECCION'] * pi / 180.0)
df['velocidad_y'] = df['VELOCIDAD'] * np.cos(df['DIRECCION'] * pi / 180.0)


fig, ax = plt.subplots(figsize=(8, 8), dpi=80)
x0, x1 = ax.get_xlim()
y0, y1 = ax.get_ylim()
ax.set_aspect('equal')

df.plot(kind='scatter', x='velocidad_x', y='velocidad_y', alpha=0.35, ax=ax)

df['VELOCIDAD'].hist(figsize=(10,6))


