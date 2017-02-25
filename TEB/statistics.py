__author__ = 'lnx'
import numpy as np
#import matplotlib.pyplot as plt
import numpy as np
#import datetime
import csv

directory = "/home/lnx/0_TEB/TEB/3_testdata/REALtest/"

scenarios = ["PV1",
             "PV2_Passivhausfenster",
             "PV3_Passivhausfenster_GZ09",
             "PV5_pvglass_C03",
             "PV5_pvglass_C004",
             "PV4_ALBW01",
             "PV5_ALBW05",
             "PV6_ALBR05",
             "PV7_ALBW01_ALBR05",
             "PV8_ALBW05_ALBR05",
             "R09",
             "PV15_BF75",
             "PV16_BH20",
             "PV17_WO11",
             "PV18_E_W",
             "PV19_N_S",
             "PV20_SW_NO",
             "PV21_NW_SO"]

files =  ["H_TOWN.txt",
          "LE_TOWN.txt",
          "RN_TOWN.txt",
           "T_CANYON.txt",
           "UTCI_OUTSHADE.txt",
           "UTCI_OUTSUN.txt"]

def getValues(directory, scenario, files):
    path = directory+"output_"+scenario+"/"
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
                name = [row for row in reader]
                data.append(name)
                param =  filename[:-4]
                print param
                param = []
                for line in data:
                  print line[0]
                  line = float(line[0])
                  param.append(line)
                  return param

print (scenarios)

for i in scenarios:
    utci_sun = getValues(directory,i,files)
    print (i)
    print ("mean", np.mean(utci_sun)- 21.0685871148) #Differenz zu PV2_Passivhausfenster
    print ("max", np.max(utci_sun) - 35.8765829905)
    print ("min", np.min(utci_sun)-  9.34972664252)
    print ("mean", np.mean(utci_sun[:288])-22.085736853344841) #Differenz zu PV2_Passivhausfenster
    print ("max", np.max(utci_sun[:288])-35.876582990453528)
    print ("min", np.min(utci_sun[:288])-13.685273443704533)
    print ('')

