__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
import datetime
import csv

# ---READING DATA---
#path = "/home/lnx/0_TEB/TEB/TEB_v1_1550/output/"
directory = "/home/lnx/0_TEB/TEB/3_testdata/BOKUtest1/"
driver = "src_driver/driver.f90"
scenario = "twowalls"
path = directory+"output_"+scenario+"/"

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
           "TI_BLD.txt"]

data = []
datalabel = []
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
            #print data
#print datalabel

'''

with open(directory+driver) as d:
    reader = csv.reader(d)
    drivercontent = [row for row in reader]
    splityear = []
    splitmonth = []
    splitday = [] # splitlistcomp = [i.split() for i in data]
    splithour = []
    splitxstep = []
    splitnrtimestep = []

    splityear = [i.split() for i in drivercontent[107]] # Splitten der Listenelemente   split(":")  Seperator ":"
    splitmonth = [i.split() for i in drivercontent[108]]
    splitday = [i.split() for i in drivercontent[109]]
    splithour =[i.split() for i in drivercontent[110]]
    splitxstep = [i.split() for i in drivercontent[106]]
    splitnrtimestep = [i.split() for i in drivercontent[113]]

    year = int(splityear[0][4])
    month = int(splitmonth[0][4])
    day = int(splitday[0][4])
    hour = float(splithour[0][4])
    xstep = float(splitxstep[0][4])/10
    nrtimestep = int(splitnrtimestep[0][4])-1

    print year, month, day, hour,  xstep, nrtimestep

'''

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

def convert_celsius(list,output):
    for line in list:
        line = float(line[0])-273.15
        output.append(line)

for line in data[8]:
    line = float(line[0])-273.15
    tempcanyon.append(line)

convert_celsius(data[9],temproad1)
convert_celsius(data[10],temproof1)
convert_celsius(data[11],tempwall1)
convert_celsius(data[12],tempwall2)
convert_celsius(data[13],tempindoor)

print np.mean(tempcanyon)
print np.max(tempcanyon)


# ---PLOTTING---
fig = plt.figure()
plt.title('energy balance - town, %s' %(scenario),fontsize='large' )
plt.plot(x, data[2], linestyle='-', color = 'orange', label = datalabel[2]) #rn
plt.plot(x, data[0], linestyle='-', color = 'red', label = datalabel[0]) #h
plt.plot(x, data[1], linestyle='-', color = 'blue', label = datalabel[1]) #le
plt.xlabel("time [UTC]", fontsize='large')
plt.ylabel("energy flux [Wm-2]", fontsize='large')
plt.legend(loc=4, ncol=3, fontsize='large')
plt.show()

fig = plt.figure()
plt.title('temperature - canyon %s' %(scenario), fontsize='large')
plt.plot(x, tempcanyon, linestyle='-', color = 'black', label = datalabel[8]) #Canyon, data[8]
plt.plot(x, temproad1, linestyle='-', color = 'blue', label = datalabel[9]) #road1, data[9]
plt.plot(x, temproof1, linestyle='-', color = 'red', label = datalabel[10]) #roof1, data[10]
plt.plot(x, tempwall1, linestyle='-', color = 'orange', label = datalabel[11]) #walla1, data[11]
plt.plot(x, tempwall2, linestyle='-', color = 'yellow', label = datalabel[12]) #wallb1, data[12]
plt.plot(x, tempindoor, linestyle='-', color = 'grey', label = datalabel[13]) #ti bld, data[13]
plt.xlabel("time [UTC]", fontsize='large')
plt.ylabel("temperature [degC]", fontsize='large')
plt.legend(loc=4, ncol=3, fontsize='large')
plt.show()


fig = plt.figure()

ax = fig.add_subplot(411)
plt.title('canyon, %s' %(scenario),fontsize='large' )
plt.plot(x, data[5], linestyle='-', color = 'black', label = datalabel[8]) #wind
plt.ylabel("wind speed [m s-1]",fontsize='large' )
#plt.legend(loc=4, ncol=3, fontsize='small')

ax = fig.add_subplot(412)
plt.plot(x, data[6], linestyle='-', color = 'blue', label = datalabel[9]) #pressure
plt.ylabel("air pressure [Pa]",fontsize='large' )
#plt.legend(loc=4, ncol=3, fontsize='small')

ax = fig.add_subplot(413)
plt.plot(x, data[7], linestyle='-', color = 'red', label = datalabel[10]) #q
plt.ylabel("specific humidity [g g-2]",fontsize='large' )
#plt.legend(loc=4, ncol=3, fontsize='small')

ax = fig.add_subplot(414)
plt.plot(x, tempcanyon, linestyle='-', color = 'orange', label = datalabel[11]) #airtemp
plt.xlabel("time [UTC]",fontsize='large') #TODO:convert to days/hours
plt.ylabel("temperature [degC]",fontsize='large' )
#plt.legend(loc=4, ncol=3, fontsize='small')
plt.show()

#fig.savefig(/home/lnx/0_TEB/TEB/output_graphs/test.png)
