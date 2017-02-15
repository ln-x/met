__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
import datetime
import csv

# ---READING DATA---
#path = "/home/lnx/0_TEB/TEB/TEB_v1_1550/output/"
directory = "/home/lnx/0_TEB/TEB/3_testdata/REALtest/"
driver = "src_driver/driver.f90"
scenario2 = "PV2_Passivhausfenster"
scenario3 = "PV10_HVAC1"
scenario4 = "PV10_HVAC2"
scenario5 = "PV10_HVAC3"

#scenario5 = "PV12_PVF1"
scenario6 = "PV13_GRF1"
scenario7 = "PV14_GF045" #garden fraction full

path2 = directory+"output_"+scenario2+"/"
path3 = directory+"output_"+scenario3+"/"
path4 = directory+"output_"+scenario4+"/"
path5 = directory+"output_"+scenario5+"/"
path6 = directory+"output_"+scenario6+"/"
path7 = directory+"output_"+scenario7+"/"

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

data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
data7 = []
datalabel2 = []
datalabel3 = []
datalabel4 = []
datalabel5 = []
datalabel6 = []
datalabel7 = []

for f in files:
    filename = f
    name = f[:-4]
    filepath = path2+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel2.append(str(name))
            name = [row for row in reader]
            data2.append(name)
    filepath = path3+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel3.append(str(name))
            name = [row for row in reader]
            data3.append(name)
    filepath = path4+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel4.append(str(name))
            name = [row for row in reader]
            data4.append(name)
    filepath = path5+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel5.append(str(name))
            name = [row for row in reader]
            data5.append(name)

    filepath = path6+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel6.append(str(name))
            name = [row for row in reader]
            data6.append(name)
    filepath = path7+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel7.append(str(name))
            name = [row for row in reader]
            data7.append(name)

start = datetime.datetime(2016,8,4) #year: line 108, month: line 109, day line 110, hour: line 111, column37
x = start + np.arange(3166) * datetime.timedelta(minutes=10)

x = x[-288:]

fig = plt.figure()
plt.title('24.-25.8.2016, dichtes Wohn(misch)gebiet, Passivhausstandard')
plt.plot(x, data2[14][-288:], linestyle='-', color = 'black', label = "STQ")
plt.plot(x, data2[15][-288:], linestyle='--', color = 'black')#, label = "STQ")
#plt.plot(x, data3[14], linestyle='-', color = 'orange', label = "HVAC1 evaporation frac. for condensers: 0") #no change visible
#plt.plot(x, data3[15], linestyle='--', color = 'orange')#, label = "HVAC1")#no change visible
#plt.plot(x, data4[14], linestyle='-', color = 'red', label = "HVAC2 evaporation frac. for condenser: 1")
#plt.plot(x, data4[15], linestyle='--', color = 'red')#, label = "HVACmax")
#plt.plot(x, data5[14], linestyle='-', color = 'blue', label = "HVAC3")
#plt.plot(x, data5[15], linestyle='--', color = 'blue', label = "HVAC3")

#plt.plot(x, data5[14], linestyle='-', color = 'violet', label = "Solar panels on roof")#no change visible
#plt.plot(x, data5[15], linestyle='--', color = 'violet')#, label = "Solar panels on roof")#no change visible
#plt.plot(x, data6[14], linestyle='-', color = 'green', label = "Green roofs")#no change visible
#plt.plot(x, data6[15], linestyle='--', color = 'green')#, label = "Green roofs")#no change visible
plt.plot(x, data7[14][-288:], linestyle='-', color = 'blue', label = "All unbuilt unsealed")
plt.plot(x, data7[15][-288:], linestyle='--', color = 'blue')#, label = "All unbuilt unsealed")

plt.grid(b=True, which='major', color='black', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='--')
plt.xlabel("time")
plt.ylabel("UTCI sun(-), shade(- -)")
plt.legend(loc=4, ncol=3, fontsize='small')
plt.show()