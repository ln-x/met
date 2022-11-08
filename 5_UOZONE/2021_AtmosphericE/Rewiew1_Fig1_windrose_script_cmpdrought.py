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
stations = {"11037":"Großenzersdorf", "11090":"Donaufeld", "11034":"Innere Stadt", "11035":"Hohe Warte", "11040":"Unterlaa", "5802":"Wien Jubliaeumswarte"}
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
JW = df.loc[df['station'] == 5802]

dataMAM18 = IS[['dd','ff']][datetime(2018, 5, 1, 00, 00):datetime(2018, 5, 31, 00, 00)]
dataMAM20 = IS[['dd','ff']][datetime(2020, 5, 1, 00, 00):datetime(2020, 5, 31, 00, 00)]

dataMAM18JW = JW[['dd','ff']][datetime(2018, 3, 1, 00, 00):datetime(2018, 5, 31, 00, 00)]
dataMAM20JW = JW[['dd','ff']][datetime(2020, 3, 1, 00, 00):datetime(2020, 5, 31, 00, 00)]

ax = WindroseAxes.from_ax()
ax.bar(dataMAM20.dd, dataMAM20.ff, normed=True, opening=0.8, edgecolor='white', bins=np.arange(0, 8, 1))
ax.set_legend()
ax.set_title("IS, M20")
ax.set_xticklabels(['E', 'NE','N', 'NW', 'W', 'SW', 'S', 'SE'])
ax.set_yticks(np.arange(0, 50, step=5))
ax.set_yticklabels(np.arange(0, 50, step=5))
plt.show()

ax = WindroseAxes.from_ax()
ax.bar(dataMAM18.dd, dataMAM18.ff, normed=True, opening=0.8, edgecolor='white', bins=np.arange(0, 8, 1))
#ax.contourf(windrosechart.dd, windrosechart.ff, nsector=36, bins=np.arange(0, 8, 1), cmap=cm.hot)
#ax.contourf(windrosechart.dd, windrosechart.ff, nsector=36, bins=np.arange(0, 8, 1), cmap=cm.hot)
##10 degree steps:
#ax.set_thetagrids(range(0,360,10),[90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 350, 340, 330, 320, 310, 300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100])
#ax.set_theta_zero_location('W', offset=-90)
#ax.set_theta_direction(-1)
ax.set_legend()
ax.set_title("IS, M18")
ax.set_xticklabels(['E', 'NE','N', 'NW', 'W', 'SW', 'S', 'SE'])
ax.set_yticks(np.arange(0, 50, step=5))
ax.set_yticklabels(np.arange(0, 50, step=5))
#ax.set_yticks(np.arange(0, 1000, step=100))
#ax.set_yticklabels(np.arange(0, 1000, step=100))
#x.set_xticklabels((90, 45, 0, 315, 270, 225, 180, 135))
plt.show()

exit()


