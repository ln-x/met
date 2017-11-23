__author__ = 'lnx'
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import datetime
import csv

from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

# ---READING DATA---
#path = "/home/lnx/0_TEB/TEB/TEB_v1_1550/output/"
directory = "/home/lnx/0_TEB/TEB/3_testdata/REALtest/"
driver = "src_driver/driver.f90"
scenario1 = "PV1"
scenario2 = "PV2_Passivhausfenster"
scenario3 = "PV15_BF75"
scenario4 = "PV16_BH20"
scenario5 = "PV17_WO11"
scenario6 = "PV18_E_W"
scenario7 = "PV19_N_S"
scenario8 = "PV20_SW_NO"
scenario9 = "PV21_NW_SO"

path = directory+"output_"+scenario1+"/"
path2 = directory+"output_"+scenario2+"/"
path3 = directory+"output_"+scenario3+"/"
path4 = directory+"output_"+scenario4+"/"
path5 = directory+"output_"+scenario5+"/"
path6 = directory+"output_"+scenario6+"/"
path7 = directory+"output_"+scenario7+"/"
path8 = directory+"output_"+scenario8+"/"
path9 = directory+"output_"+scenario9+"/"


files =  ["H_TOWN.txt",
          "LE_TOWN.txt",
          "RN_TOWN.txt",
           "HVAC_COOL.txt",
          "HVAC_HEAT.txt",
           "U_CANYON.txt",
           "P_CANYON.txt",
           "Q_CANYON.txt",
           "T_CANYON.txt",
           "T_ROAD1.txt",
           "T_ROOF1.txt",
           "T_WALLA1.txt",
           "T_WALLB1.txt",
           "TI_BLD.txt",
           "UTCI_OUTSHADE.txt",
           "UTCI_OUTSUN.txt"]

data = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
data7 = []
data8 = []
data9 = []
datalabel = []
datalabel2 = []
datalabel3 = []
datalabel4 = []
datalabel5 = []
datalabel6 = []
datalabel7 = []
datalabel8 = []
datalabel9 = []

for f in files:
    filename = f
    name = f[:-4]
    filepath = path+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel.append(str(name))
            #print datalabel
            name = [row for row in reader]
            data.append(name)
    filepath = path2+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel2.append(str(name))
            #print datalabel
            name = [row for row in reader]
            data2.append(name)
    filepath = path3+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel3.append(str(name))
            #print datalabel
            name = [row for row in reader]
            data3.append(name)
    filepath = path4+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel4.append(str(name))
            #print datalabel
            name = [row for row in reader]
            data4.append(name)
    filepath = path5+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel5.append(str(name))
            #print datalabel
            name = [row for row in reader]
            data5.append(name)

    filepath = path6+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel6.append(str(name))
            #print datalabel
            name = [row for row in reader]
            data6.append(name)
    filepath = path7+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel7.append(str(name))
            #print datalabel
            name = [row for row in reader]
            data7.append(name)

    filepath = path8+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel8.append(str(name))
            #print datalabel
            name = [row for row in reader]
            data8.append(name)

    filepath = path9+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel9.append(str(name))
            #print datalabel
            name = [row for row in reader]
            data9.append(name)

start = datetime.datetime(2016,8,4) #year: line 108, month: line 109, day line 110, hour: line 111, column37
#start = datetime.datetime(year,month,day) #year: line 108, month: line 109, day line 110, hour: line 111, column37
x = start + np.arange(3166) * datetime.timedelta(minutes=10)
#x = start + np.arange(nrtimestep) * datetime.timedelta(minutes=xstep)

#TODO: calculate threshold criteria (tropische naechte? sommertage, UTCI!)
#TODO: slice weeks of certain thresholds
#TODO: list important input settings of this simulation (H/W ratio, albedo,...)


#---CONVERSIONS---

tempcanyon = []
temproad1 = []
temproof1 = []
tempwall1 = []
tempwall2 = []
tempindoor = []

tempcanyon_2 = []
temproad1_2 = []
temproof1_2 = []
tempwall1_2 = []
tempwall2_2 = []
tempindoor_2 = []

tempcanyon_3 = []
temproad1_3 = []
temproof1_3 = []
tempwall1_3 = []
tempwall2_3 = []
tempindoor_3 = []

tempcanyon_4 = []
temproad1_4 = []
temproof1_4 = []
tempwall1_4 = []
tempwall2_4 = []
tempindoor_4 = []

tempcanyon_5 = []
tempcanyon_6 = []
tempcanyon_7 = []
tempcanyon_8 = []
tempcanyon_9 = []



def convert_celsius(list,output):
    for line in list:
        line = float(line[0])-273.15
        output.append(line)

for line in data[8]:
    line = float(line[0])-273.15
    tempcanyon.append(line)

for line in data2[8]:
    line = float(line[0])-273.15
    tempcanyon_2.append(line)

for line in data3[8]:
    line = float(line[0])-273.15
    tempcanyon_3.append(line)

for line in data4[8]:
    line = float(line[0])-273.15
    tempcanyon_4.append(line)


for line in data5[8]:
    line = float(line[0])-273.15
    tempcanyon_5.append(line)


for line in data6[8]:
    line = float(line[0])-273.15
    tempcanyon_6.append(line)


for line in data7[8]:
    line = float(line[0])-273.15
    tempcanyon_7.append(line)

for line in data8[8]:
    line = float(line[0])-273.15
    tempcanyon_8.append(line)

for line in data9[8]:
    line = float(line[0])-273.15
    tempcanyon_9.append(line)

convert_celsius(data[9],temproad1)
convert_celsius(data[10],temproof1)
convert_celsius(data[11],tempwall1)
convert_celsius(data[12],tempwall2)
convert_celsius(data[13],tempindoor)

#convert_celsius(data2[9],temproad1)

"""
print (np.mean(tempcanyon_2))
print (np.max(tempcanyon_2[-288:]))
print (np.min(tempcanyon_2[-288:]))
print (np.mean(tempcanyon_3))
print (np.max(tempcanyon_3[-288:]))
print (np.min(tempcanyon_3[-288:]))
print (np.mean(tempcanyon_4))
print (np.max(tempcanyon_4[-288:]))
print (np.min(tempcanyon_4[-288:]))
print (np.mean(tempcanyon_5))
print (np.max(tempcanyon_5[-288:]))
print (np.min(tempcanyon_5[-288:]))
"""

x = x[-288:]

print (np.mean(tempcanyon_2))
print (np.mean(tempcanyon_3))
print (np.mean(tempcanyon_4))
print (np.mean(tempcanyon_5))

exit()


fig = plt.figure()
#plt.title('Albedo' )

#fig.set_size_inches(3.39,2.54)
#axisrange = [220,270,15,40]
#plt.axis(axisrange)
plt.ylim(14, 28)

plt.plot(x, tempcanyon_2[-144:], linestyle='-', color = 'black', label = "STQ")
plt.plot(x, tempcanyon_3[-144:], linestyle='-', color = 'red', label = "Bebauung +0.25")
plt.plot(x, tempcanyon_4[-144:], linestyle='-', color = 'blue', label = "Bauhoehe +5m")
plt.plot(x, tempcanyon_5[-144:], linestyle='-', color = 'green', label = "vertikal/horiz.Flaeche 2.1 -> 1.1")

plt.grid(b=True, which='major', color='black', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='--')
plt.xlabel("Zeit [UTC] ",  fontsize='large')
plt.ylabel("Lufttemperatur im Canyon [gradC]", fontsize='large')
plt.legend(loc=4, ncol=2, fontsize='large')

#inset_axes = inset_axes(parent_axes,
#                        width="30%", # width = 30% of parent_bbox
#                        height=1., # height : 1 inch
#                        loc=3)

#inset_axes = zoomed_inset_axes(gca(),
#                               0.5, # zoom = 0.5
#                               loc=1)

plt.show()