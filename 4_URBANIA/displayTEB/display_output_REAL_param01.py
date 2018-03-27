__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
import datetime
import csv

# ---READING DATA---
#path = "/home/lnx/0_TEB/TEB/TEB_v1_1550/output/"
directory = "/home/lnx/0_TEB/TEB/3_testdata/REALtest/"
driver = "src_driver/driver.f90"
scenario = "R03"
scenario2 = "R03_2020"
scenario3 = "R03_2020_GZ09"
#scenario2 = "R03_BF74"
#scenario3 = "R03_BH20_6"


path = directory+"output_"+scenario+"/"
path2 = directory+"output_"+scenario2+"/"
path3 = directory+"output_"+scenario3+"/"
path4 = directory+"output_"+scenario4+"/"


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
datalabel = []
datalabel2 = []
datalabel3 = []
datalabel4 = []

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

start = datetime.datetime(2016,8,4) #year: line 108, month: line 109, day line 110, hour: line 111, column37
#start = datetime.datetime(year,month,day) #year: line 108, month: line 109, day line 110, hour: line 111, column37
x = start + np.arange(3166) * datetime.timedelta(minutes=10)
#x = start + np.arange(nrtimestep) * datetime.timedelta(minutes=xstep)

#TODO: calculate threshold criteria (tropische naechte? sommertage, UTCI!)
#TODO: slice weeks of certain thresholds
#TODO: list important input settings of this simulation (H/W ratio, albedo,...)

#location of options:
# roughness length: line 600 col 15
# horizontal building area density
# fraction of Gardens
# building height
# vertical to horizontal surf ratio
# zroad_dir ...

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

convert_celsius(data[9],temproad1)
convert_celsius(data[10],temproof1)
convert_celsius(data[11],tempwall1)
convert_celsius(data[12],tempwall2)
convert_celsius(data[13],tempindoor)

#convert_celsius(data2[9],temproad1)


print (np.mean(tempcanyon))
print (np.max(tempcanyon))


# ---PLOTTING---
#fig = plt.figure()
#plt.title('energy balance - town, %s' %(scenario))
#plt.plot(x, data[2], linestyle='-', color = 'orange', label = datalabel[2]) #rn
#plt.plot(x, data[0], linestyle='-', color = 'red', label = datalabel[0]) #h
#plt.plot(x, data[1], linestyle='-', color = 'blue', label = datalabel[1]) #le
#plt.xlabel("time")
#plt.ylabel("energy flux [Wm-2]")
#plt.legend(loc=4, ncol=3, fontsize='small')
#plt.show()

fig = plt.figure()
plt.title('temperature - canyon, %s' %(scenario))
plt.plot(x, tempcanyon, linestyle='-', color = 'black', label = "status quo") #datalabel[8]) #Canyon, data[8]
#plt.plot(x, tempcanyon_2, linestyle='-', color = 'red', label = "builtfraction 0.55 > 0.74") #datalabel[8]) #Canyon, data[8]
#plt.plot(x, tempcanyon_3, linestyle='-', color = 'blue', label = "building height 14.6 > 20.6") #datalabel[8]) #Canyon, data[8]
#plt.plot(x, tempcanyon_4, linestyle='-', color = 'green', label = "unsealed fraction 0.28 > 0.00") #datalabel[8]) #Canyon, data[8]
plt.plot(x, tempcanyon_2, linestyle='-', color = 'red', label = "increased isolation") # 1.7/1.4 > 0.1") # 1520000 > 1496000")# 1.7/1.4 > 0.1
plt.plot(x, tempcanyon_3, linestyle='-', color = 'blue', label = "increased isolation + glazing") #GR 0.3 > 0.9
plt.grid(b=True, which='major', color='black', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='--')
#plt.plot(x, temproad1, linestyle='-', color = 'blue', label = datalabel[9]) #road1, data[9]
#plt.plot(x, temproof1, linestyle='-', color = 'red', label = datalabel[10]) #roof1, data[10]
#plt.plot(x, tempwall1, linestyle='-', color = 'orange', label = datalabel[11]) #walla1, data[11]
#plt.plot(x, tempwall2, linestyle='-', color = 'yellow', label = datalabel[12]) #wallb1, data[12]
#plt.plot(x, tempindoor, linestyle='-', color = 'grey', label = datalabel[13]) #ti bld, data[13]
plt.xlabel("time")
plt.ylabel("temperature [degC]")
plt.legend(loc=4, ncol=3, fontsize='small')
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