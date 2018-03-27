__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
import datetime
import csv

# ---READING DATA---
#path = "/home/lnx/0_TEB/TEB/TEB_v1_1550/output/"
directory = "/home/lnx/0_TEB/TEB/3_testdata/REALtest/"
driver = "src_driver/driver.f90"
scenario = "PV2_copy"
scenario2 = "PV5_pvglass_C03"

path = directory+"output_"+scenario+"/"
path2 = directory+"output_"+scenario2+"/"

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
datalabel = []
datalabel2 = []

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

start = datetime.datetime(2016,8,4) #year: line 108, month: line 109, day line 110, hour: line 111, column37
#start = datetime.datetime(year,month,day) #year: line 108, month: line 109, day line 110, hour: line 111, column37
x = start + np.arange(3166) * datetime.timedelta(minutes=10)
#x = start + np.arange(nrtimestep) * datetime.timedelta(minutes=xstep)

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

convert_celsius(data[9],temproad1)
convert_celsius(data[10],temproof1)
convert_celsius(data[11],tempwall1)
convert_celsius(data[12],tempwall2)
convert_celsius(data[13],tempindoor)

#convert_celsius(data2[9],temproad1)

print (np.mean(tempcanyon))
print (np.max(tempcanyon))
x = x[-288:]


# ---PLOTTING---
fig = plt.figure()
plt.title('Energiebilanz - Stadt, STQ (-), PV(--)',  fontsize='large')#%s' %(scenario))
plt.plot(x, data[2][-288:], linestyle='-', color = 'orange', label="Strahlungsbilanz") #label = datalabel[2]) #rn
plt.plot(x, data2[2][-288:], linestyle='--', color = 'orange')#, label = datalabel[2]) #rn
plt.plot(x, data[0][-288:], linestyle='-', color = 'red', label="sensible Waerme" )#label = datalabel[0]) #h
plt.plot(x, data2[0][-288:], linestyle='--', color = 'red')#, label = datalabel[0]) #h
plt.plot(x, data[1][-288:], linestyle='-', color = 'blue', label="latente Waerme")#label = datalabel[1]) #le
plt.plot(x, data2[1][-288:], linestyle='--', color = 'blue')#, label = datalabel[1]) #le
plt.xlabel("Zeit [UTC]")
plt.ylabel("Energie fluss [Wm-2]")
plt.legend(loc="best", ncol=1, fontsize='large')
plt.show()

fig = plt.figure()
plt.title('temperature - canyon', fontsize='large')#, %s' %(scenario))
plt.plot(x, tempcanyon, linestyle='-', color = 'black', label = "status quo") #datalabel[8]) #Canyon, data[8]
plt.plot(x, tempcanyon, linestyle='-', color = 'blue', label = "PV Fassade")# thermal conductiv. 0.3
plt.grid(b=True, which='major', color='black', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='--')
plt.ylabel("temperature [degC]")
plt.legend(loc=4, ncol=2, fontsize='large')
plt.show()

"""

fig = plt.figure()

ax = fig.add_subplot(411)
plt.title('canyon, %s' %(scenario))
plt.plot(x, data[5], linestyle='-', color = 'black', label = datalabel[8]) #wind
plt.ylabel("wind speed [m s-1]")
#plt.legend(loc=4, ncol=3, fontsize='small')

ax = fig.add_subplot(412)
plt.plot(x, data[6], linestyle='-', color = 'blue', label = datalabel[9]) #pressure
plt.ylabel("air pressure [Pa]")
#plt.legend(loc=4, ncol=3, fontsize='small')

ax = fig.add_subplot(413)
plt.plot(x, data[7], linestyle='-', color = 'red', label = datalabel[10]) #q
plt.ylabel("specific humidity [g g-2]")
#plt.legend(loc=4, ncol=3, fontsize='small')

ax = fig.add_subplot(414)
plt.plot(x, tempcanyon, linestyle='-', color = 'orange', label = datalabel[11]) #airtemp
plt.xlabel("time") #TODO:convert to days/hours
plt.ylabel("temperature [degC]")
#plt.legend(loc=4, ncol=3, fontsize='small')
plt.show()

#fig.savefig(/home/lnx/0_TEB/TEB/output_graphs/test.png)

"""