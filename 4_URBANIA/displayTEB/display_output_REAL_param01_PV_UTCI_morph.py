__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
import datetime
import csv

# ---READING DATA---
#path = "/home/lnx/0_TEB/TEB/TEB_v1_1550/output/"
directory = "/home/lnx/0_TEB/TEB/3_testdata/REALtest/"
driver = "src_driver/driver.f90"
scenario1 = "PV1"
scenario2 = "PV2_Passivhausfenster"
scenario3 = "PV15_BF75"
scenario4 = "PV16_BF75_BH20"
scenario5 = "PV17_BF75_BH20_WO11"
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
            name = [row for row in reader]
            data9.append(name)

start = datetime.datetime(2016,8,4) #year: line 108, month: line 109, day line 110, hour: line 111, column37
x = start + np.arange(3166) * datetime.timedelta(minutes=10)

x = x[-288:]

fig = plt.figure()
plt.title('UTCI Sonne (-), Schatten (--)')
#plt.plot(x, data[14], linestyle='-', color = 'yellow', label = "STQ")
plt.plot(x, data2[14][-288:], linestyle='-', color = 'black', label = "STQ")
plt.plot(x, data2[15][-288:], linestyle='--', color = 'black')#,
plt.plot(x, data3[14][-288:], linestyle='-', color = 'red', label = "Bebauung +0.25")#"Hoehe/Breite 2 -> 4")
plt.plot(x, data3[15][-288:], linestyle='--', color = 'red')#,
plt.plot(x, data4[14][-288:], linestyle='-', color = 'blue', label = "Bauhoehe +5m")
plt.plot(x, data4[15][-288:], linestyle='--', color = 'blue')#,
plt.plot(x, data5[14][-288:], linestyle='-', color = 'green', label = "vertikal/horiz.Flaeche 2.1 -> 1.1") #offenere Bauweise
plt.plot(x, data5[15][-288:], linestyle='--', color = 'green')#,

#plt.plot(x, data3[14][-288:], linestyle='-', color = 'turquoise', label = "BF 0.55 -> 0.75")
#plt.plot(x, data3[15][-288:], linestyle='--', color = 'turquoise')#, label = "BF 0.55 -> 0.75")
#plt.plot(x, data4[14][-288:], linestyle='-', color = 'blue', label = "BF 0.75 + BH 14.6 -> 20.")
#plt.plot(x, data4[15][-288:], linestyle='--', color = 'blue')#, label = "BF 0.75 + BH 14.6 -> 20.")
#plt.plot(x, data5[14][-288:], linestyle='-', color = 'violet', label = "BF 0.75 + BH 20 + WI 2.1 -> 1.1")
#plt.plot(x, data5[15][-288:], linestyle='--', color = 'violet')#, label = "BF 0.75 + BH 20 + WI 2.1 -> 1.1")

plt.grid(b=True, which='major', color='black', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='--')
plt.xlabel("Zeit [UTC]", fontsize='large')
plt.ylabel("UTCI [gradC]", fontsize='large')
plt.legend(loc=4, ncol=2, fontsize='large')
plt.show()