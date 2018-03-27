__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
import datetime
import csv

# ---READING DATA---
#path = "/home/lnx/0_TEB/TEB/TEB_v1_1550/output/"
directory = "/home/lnx/0_TEB/TEB/3_testdata/REALtest/"
driver = "src_driver/driver.f90"
scenario1 = "R03"
scenario2 = "R03_2020"
scenario3 = "R03_2020_GZ09"
scenario4 = "R03_2020_GZ09"
path1 = directory+"output_"+scenario1+"/"
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
           "TI_BLD.txt"]

data1 = []
for f in files:
    filename = f
    name = f[:-4]
    filepath = path1+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            name = [row for row in reader]
            data1.append(name)

data2 = []
for f in files:
    filename = f
    name = f[:-4]
    filepath = path2+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            name = [row for row in reader]
            data2.append(name)

data3 = []
for f in files:
    filename = f
    name = f[:-4]
    filepath = path3+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            name = [row for row in reader]
            data3.append(name)

data4 = []
for f in files:
    filename = f
    name = f[:-4]
    filepath = path4+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            name = [row for row in reader]
            data4.append(name)


#location of options:
# roughness length: line 600 col 15
# horizontal building area density
# fraction of Gardens
# building height
# vertical to horizontal surf ratio
# zroad_dir ...

#---CONVERSIONS---

tempcanyon_1 = []
tempcanyon_2 = []
tempcanyon_3 = []
tempcanyon_4 = []


def convert_celsius(list,output):
    for line in list:
        line = float(line[0])-273.15
        output.append(line)

convert_celsius(data1[8],tempcanyon_1)
convert_celsius(data2[8],tempcanyon_2)
convert_celsius(data3[8],tempcanyon_3)
convert_celsius(data4[8],tempcanyon_4)

tempcanyon_diff_g = np.mean(tempcanyon_1) - np.mean(tempcanyon_2)
tempcanyon_diff_vh1= np.mean(tempcanyon_2) - np.mean(tempcanyon_3)
tempcanyon_diff_vh2 = np.mean(tempcanyon_2) - np.mean(tempcanyon_4)

tempcanyon_diff_g_max = np.max(tempcanyon_1) - np.max(tempcanyon_2)
tempcanyon_diff_vh1_max= np.max(tempcanyon_2) - np.max(tempcanyon_3)
tempcanyon_diff_vh2_max = np.max(tempcanyon_2) - np.max(tempcanyon_4)

print "MEAN VALUES:"
print "%s - %s:" %(scenario1,scenario2), tempcanyon_diff_g
print "%s - %s:" %(scenario2,scenario3), tempcanyon_diff_vh1
print "%s - %s:" %(scenario2,scenario4), tempcanyon_diff_vh2
print "---"
print "MAX VALUES:"
print "%s - %s:" %(scenario1,scenario2),  tempcanyon_diff_g_max
print "%s - %s:" %(scenario2,scenario3), tempcanyon_diff_vh1_max
print "%s - %s:" %(scenario2,scenario4), tempcanyon_diff_vh2_max
print "---"

exit()

print np.mean(tempcanyon)
print np.max(tempcanyon)


exit()
