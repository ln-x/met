# -*- coding: utf-8 -*-
__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
import datetime
import csv
from matplotlib.offsetbox import AnchoredOffsetbox, AuxTransformBox, VPacker,\
    TextArea, DrawingArea
import matplotlib.ticker as ticker


class AnchoredText(AnchoredOffsetbox):
    def __init__(self, s, loc, pad=0.4, borderpad=0.5, prop=None, frameon=True):
        self.txt = TextArea(s,
                            minimumdescent=False)
        super(AnchoredText, self).__init__(loc, pad=pad, borderpad=borderpad,
                                           child=self.txt,
                                           prop=prop,
                                           frameon=frameon)


# ---READING DATA---
#path = "/home/lnx/0_TEB/TEB/TEB_v1_1550/output/"
directory = "/home/lnx/MODELS/TEB/3_testdata/LCZtest/"
driver = "src_driver/driver.f90"
scenario1 = "LCZ9"
scenario2 = "LCZ6"
scenario3 = "LCZ2"
scenario4 = "LCZ5"
scenario5 = "LCZ2" #dummy
scenario6 = "LCZ2" #dummy
scenario7 = "LCZ4"
scenario8 = "LCZ2" #dummy
scenario9 = "LCZ8"

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


print (np.mean(tempcanyon))
print (np.max(tempcanyon))


n = len(tempcanyon)
t1 = n - 71 - 18 #midnight - 5:50min - 3h = 9h
t2 = n - 71 + 18 + 3  #midnight - 5:50min + 3h + 0.5h = 15h
#t3 = n - 71 - 54 #midnight - 5:50min - 9h = 3h
#t4 = n - 71 - 18 + 3 #midnight - 5:50min - 3h + 0.5h = 9h
t3 = n - 71 - 54 - 12 #midnight - 5:50min - 9h = 3h
t4 = n - 71 - 18 + 3 -12 #midnight - 5:50min - 3h + 0.5h = 9h

def my_formatter(x,p):
    #return "%1.2f" %x
    return time.strftime("%H:%M") %x
#time.strftime("%Y-%m-%d %H:%M")

fig = plt.figure()#sharex= True, sharey= True)

ax1 = fig.add_subplot(421)
at = AnchoredText("a",loc=2, frameon=True)
ax1.add_artist(at)
ax1.plot(x[:120], tempcanyon_3[:120], linestyle='-', color = 'red', label='LCZ2 compact mid-rise')#3dichtes Wohn(misch)gebiet
ax1.plot(x[:120], tempcanyon_7[:120], linestyle='-', color = 'brown', label='LCZ4 open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
ax1.plot(x[:120], tempcanyon_4[:120], linestyle='-', color = 'orange', label='LCZ5 open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
ax1.plot(x[:120], tempcanyon_2[:120], linestyle='-', color = 'yellow', label='LCZ6 open low-rise')#2 Gartenstadt
ax1.plot(x[:120], tempcanyon_9[:120], linestyle='-', color = 'blue', label='LCZ8 large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
ax1.plot(x[:120], tempcanyon[:120], linestyle='-', color = 'green', label='LCZ9 sparsely built') #1 locker bebautes Wohn(misch)gebiet
for label in ax1.get_xticklabels()[::2]:
    label.set_visible(False)
#ax1.get_xaxis().set_major_formatter(ticker.FuncFormatter(my_formatter))
#plt.gcf().autofmt_xdate()
ax1.grid(b=True, which='major', color='grey', linestyle=':')
ax1.set_ylabel(u'T_air[°C]', fontsize='large')

ax1 = fig.add_subplot(422)
ax1.plot(x[t1:t2], tempcanyon_3[t1:t2], linestyle='-', color = 'red', label='LCZ2 compact mid-rise')#3dichtes Wohn(misch)gebiet
ax1.plot(x[t1:t2],tempcanyon_7[t1:t2], linestyle='-', color = 'brown', label='LCZ4 open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
ax1.plot(x[t1:t2],tempcanyon_4[t1:t2], linestyle='-', color = 'orange', label='LCZ5 open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
ax1.plot(x[t1:t2],tempcanyon_2[t1:t2], linestyle='-', color = 'yellow', label='LCZ6 open low-rise')#2 Gartenstadt
ax1.plot(x[t1:t2],tempcanyon_9[t1:t2], linestyle='-', color = 'blue', label='LCZ8 large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
ax1.plot(x[t1:t2],tempcanyon[t1:t2], linestyle='-', color = 'green', label='LCZ9 sparsely built') #1 locker bebautes Wohn(misch)gebiet
for label in ax1.get_xticklabels()[::2]:
    label.set_visible(False)
ax1.grid(b=True, which='major', color='grey', linestyle=':')
#ax1.set_ylabel(u'air temperature [°C]', fontsize='large')

"""
ax1 = fig.add_subplot(333)
ax1.plot(x[t3:t4],tempcanyon_3[t3:t4], linestyle='-', color = 'red', label='LCZ2 compact mid-rise')#3dichtes Wohn(misch)gebiet
ax1.plot(x[t3:t4],tempcanyon_7[t3:t4], linestyle='-', color = 'brown', label='LCZ4 open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
ax1.plot(x[t3:t4],tempcanyon_4[t3:t4], linestyle='-', color = 'orange', label='LCZ5 open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
ax1.plot(x[t3:t4],tempcanyon_2[t3:t4], linestyle='-', color = 'yellow', label='LCZ6 open low-rise')#2 Gartenstadt
ax1.plot(x[t3:t4],tempcanyon_9[t3:t4], linestyle='-', color = 'blue', label='LCZ8 large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
ax1.plot(x[t3:t4],tempcanyon[t3:t4], linestyle='-', color = 'green', label='LCZ9 sparsely built') #1 locker bebautes Wohn(misch)gebiet
for label in ax1.get_xticklabels()[::2]:
    label.set_visible(False)
ax1.grid(b=True, which='major', color='grey', linestyle=':')
ax1.set_ylabel(u'air temperature [°C]', fontsize='large')
"""
ax2 = fig.add_subplot(425)
at = AnchoredText("c",loc=2, frameon=True)
ax2.add_artist(at)
ax2.plot(x[:120], data3[1][:120], linestyle='-', color = 'red', label='LCZ2 compact mid-rise')#3dichtes Wohn(misch)gebiet
ax2.plot(x[:120],data7[1][:120], linestyle='-', color = 'brown', label='LCZ4 open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
ax2.plot(x[:120],data4[1][:120], linestyle='-', color = 'orange', label='LCZ5 open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
ax2.plot(x[:120],data2[1][:120], linestyle='-', color = 'yellow', label='LCZ6 open low-rise')#2 Gartenstadt
ax2.plot(x[:120],data9[1][:120], linestyle='-', color = 'blue', label='LCZ8 large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
ax2.plot(x[:120],data[1][:120], linestyle='-', color = 'green', label='LCZ9 sparsely built') #1 locker bebautes Wohn(misch)gebiet
for label in ax2.get_xticklabels()[::2]:
    label.set_visible(False)
ax2.grid(b=True, which='major', color='grey', linestyle=':')
ax2.set_ylabel(u'L.E.[W/m²]', fontsize='large')

ax2 = fig.add_subplot(426)
ax2.plot(x[t1:t2],data3[1][t1:t2], linestyle='-', color = 'red', label='LCZ2 compact mid-rise')#3dichtes Wohn(misch)gebiet
ax2.plot(x[t1:t2],data7[1][t1:t2], linestyle='-', color = 'brown', label='LCZ4 open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
ax2.plot(x[t1:t2],data4[1][t1:t2], linestyle='-', color = 'orange', label='LCZ5 open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
ax2.plot(x[t1:t2],data2[1][t1:t2], linestyle='-', color = 'yellow', label='LCZ6 open low-rise')#2 Gartenstadt
ax2.plot(x[t1:t2],data9[1][t1:t2], linestyle='-', color = 'blue', label='LCZ8 large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
ax2.plot(x[t1:t2],data[1][t1:t2], linestyle='-', color = 'green', label='LCZ9 sparsely built') #1 locker bebautes Wohn(misch)gebiet
for label in ax2.get_xticklabels()[::2]:
    label.set_visible(False)
ax2.grid(b=True, which='major', color='grey', linestyle=':')
#ax2.set_ylabel(u'latent heat flux [W/m²]', fontsize='large')
ax2.set_ylim([0,610])
"""
ax2 = fig.add_subplot(339)
ax2.plot(x[t3:t4],data3[1][t3:t4], linestyle='-', color = 'red', label='LCZ2 compact mid-rise')#3dichtes Wohn(misch)gebiet
ax2.plot(x[t3:t4],data7[1][t3:t4], linestyle='-', color = 'brown', label='LCZ4 open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
ax2.plot(x[t3:t4],data4[1][t3:t4], linestyle='-', color = 'orange', label='LCZ5 open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
ax2.plot(x[t3:t4],data2[1][t3:t4], linestyle='-', color = 'yellow', label='LCZ6 open low-rise')#2 Gartenstadt
ax2.plot(x[t3:t4],data9[1][t3:t4], linestyle='-', color = 'blue', label='LCZ8 large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
ax2.plot(x[t3:t4],data[1][t3:t4], linestyle='-', color = 'green', label='LCZ9 sparsely built') #1 locker bebautes Wohn(misch)gebiet
for label in ax2.get_xticklabels()[::2]:
    label.set_visible(False)
ax2.grid(b=True, which='major', color='grey', linestyle=':')
ax2.set_ylabel(u'latent heat flux [W/m²]', fontsize='large')
#plt.setp(ax3.get_xticklabels(), visible=False)
ax2.set_ylim([-200,350])
"""
ax3 = fig.add_subplot(423)
at = AnchoredText("b",loc=2, frameon=True)
ax3.add_artist(at)
ax3.plot(x[:120],data3[2][:120], linestyle='-', color = 'red', label='LCZ2 compact mid-rise')#3dichtes Wohn(misch)gebiet
ax3.plot(x[:120],data7[2][:120], linestyle='-', color = 'brown', label='LCZ4 open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
ax3.plot(x[:120],data4[2][:120], linestyle='-', color = 'orange', label='LCZ5 open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
ax3.plot(x[:120],data2[2][:120], linestyle='-', color = 'yellow', label='LCZ6 open low-rise')#2 Gartenstadt
ax3.plot(x[:120],data9[2][:120], linestyle='-', color = 'blue', label='LCZ8 large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
ax3.plot(x[:120],data[2][:120], linestyle='-', color = 'green', label='LCZ9 sparsely built') #1 locker bebautes Wohn(misch)gebiet
#ax.set_ylim([-50,50])
#ax.set_xlim([0.0,23.0])
for label in ax3.get_xticklabels()[::2]:
    label.set_visible(False)
ax3.grid(b=True, which='major', color='grey', linestyle=':')
ax3.set_ylabel(u'Q* [W/m²]', fontsize='large')
#ax3.set_xlabel('time [UTC]', fontsize='large')

ax3 = fig.add_subplot(424)
ax3.plot(x[t1:t2],data3[2][t1:t2], linestyle='-', color = 'red', label='LCZ2 compact mid-rise')#3dichtes Wohn(misch)gebiet
ax3.plot(x[t1:t2],data7[2][t1:t2], linestyle='-', color = 'brown', label='LCZ4 open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
ax3.plot(x[t1:t2],data4[2][t1:t2], linestyle='-', color = 'orange', label='LCZ5 open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
ax3.plot(x[t1:t2],data2[2][t1:t2], linestyle='-', color = 'yellow', label='LCZ6 open low-rise')#2 Gartenstadt
ax3.plot(x[t1:t2],data9[2][t1:t2], linestyle='-', color = 'blue', label='LCZ8 large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
ax3.plot(x[t1:t2],data[2][t1:t2], linestyle='-', color = 'green', label='LCZ9 sparsely built') #1 locker bebautes Wohn(misch)gebiet
#plt.setp(ax3.get_xticklabels(), visible=False)
ax3.set_ylim([0,610])
#ax3.set_xlim([0.0,23.0])
for label in ax3.get_xticklabels()[::2]:
    label.set_visible(False)
ax3.grid(b=True, which='major', color='grey', linestyle=':')
#ax3.set_ylabel(u'radiation balance [W/m²]', fontsize='large')
#ax3.set_xlabel('time [UTC]', fontsize='large')
"""
ax3 = fig.add_subplot(336)
ax3.plot(x[t3:t4],data3[2][t3:t4], linestyle='-', color = 'red', label='LCZ2 compact mid-rise')#3dichtes Wohn(misch)gebiet
ax3.plot(x[t3:t4],data7[2][t3:t4], linestyle='-', color = 'brown', label='LCZ4 open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
ax3.plot(x[t3:t4],data4[2][t3:t4], linestyle='-', color = 'orange', label='LCZ5 open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
ax3.plot(x[t3:t4],data2[2][t3:t4], linestyle='-', color = 'yellow', label='LCZ6 open low-rise')#2 Gartenstadt
ax3.plot(x[t3:t4],data9[2][t3:t4], linestyle='-', color = 'blue', label='LCZ8 large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
ax3.plot(x[t3:t4],data[2][t3:t4], linestyle='-', color = 'green', label='LCZ9 sparsely built') #1 locker bebautes Wohn(misch)gebiet
#plt.setp(ax3.get_xticklabels(), visible=False)
ax3.set_ylim([-200,350])
#ax.set_xlim([0.0,23.0])
for label in ax3.get_xticklabels()[::2]:
    label.set_visible(False)
ax3.grid(b=True, which='major', color='grey', linestyle=':')
ax3.set_ylabel(u'radiation balance [W/m²]', fontsize='large')
ax3.set_xlabel('time [UTC]', fontsize='large')
"""
ax4 = fig.add_subplot(427)
at = AnchoredText("d",loc=2, frameon=True)
ax4.add_artist(at)
ax4.plot(x[:120],data3[0][:120], linestyle='-', color = 'red', label='LCZ2 compact mid-rise')#3dichtes Wohn(misch)gebiet
ax4.plot(x[:120],data7[0][:120], linestyle='-', color = 'brown', label='LCZ4 open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
ax4.plot(x[:120],data4[0][:120], linestyle='-', color = 'orange', label='LCZ5 open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
ax4.plot(x[:120],data2[0][:120], linestyle='-', color = 'yellow', label='LCZ6 open low-rise')#2 Gartenstadt
ax4.plot(x[:120],data9[0][:120], linestyle='-', color = 'blue', label='LCZ8 large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
ax4.plot(x[:120],data[0][:120], linestyle='-', color = 'green', label='LCZ9 sparsely built') #1 locker bebautes Wohn(misch)gebiet
#ax.set_ylim([-50,50])
#ax.set_xlim([0.0,23.0])
for label in ax4.get_xticklabels()[::2]:
    label.set_visible(False)
ax4.grid(b=True, which='major', color='grey', linestyle=':')
ax4.set_ylabel(u'H [W/m²]', fontsize='large')
ax4.set_xlabel('time [UTC]', fontsize='large')

ax4 = fig.add_subplot(428)
ax4.plot(x[t1:t2],data3[0][t1:t2], linestyle='-', color = 'red', label='LCZ2 - compact mid-rise')#3dichtes Wohn(misch)gebiet
ax4.plot(x[t1:t2],data7[0][t1:t2], linestyle='-', color = 'brown', label='LCZ4 open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
ax4.plot(x[t1:t2],data4[0][t1:t2], linestyle='-', color = 'orange', label='LCZ5 open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
ax4.plot(x[t1:t2],data2[0][t1:t2], linestyle='-', color = 'yellow', label='LCZ6 - open low-rise')#2 Gartenstadt
ax4.plot(x[t1:t2],data9[0][t1:t2], linestyle='-', color = 'blue', label='LCZ8 - large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
ax4.plot(x[t1:t2],data[0][t1:t2], linestyle='-', color = 'green', label='LCZ9 - sparsely built') #1 locker bebautes Wohn(misch)gebiet
#plt.setp(ax3.get_xticklabels(), visible=False)
ax4.set_ylim([0,610])
#ax4.set_xlim([0.0,23.0])
for label in ax4.get_xticklabels()[::2]:
    label.set_visible(False)
ax4.grid(b=True, which='major', color='grey', linestyle=':')
#ax4.set_ylabel(u'sensible heat flux [W/m²]', fontsize='large')
ax4.set_xlabel('time [UTC]', fontsize='large')
"""
ax4 = fig.add_subplot()
ax4.plot(x[t3:t4],data3[0][t3:t4], linestyle='-', color = 'red', label='LCZ2 - compact mid-rise')#3dichtes Wohn(misch)gebiet
ax4.plot(x[t3:t4],data7[0][t3:t4], linestyle='-', color = 'brown', label='LCZ4 open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
ax4.plot(x[t3:t4],data4[0][t3:t4], linestyle='-', color = 'orange', label='LCZ5 open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
ax4.plot(x[t3:t4],data2[0][t3:t4], linestyle='-', color = 'yellow', label='LCZ6 - open low-rise')#2 Gartenstadt
ax4.plot(x[t3:t4],data9[0][t3:t4], linestyle='-', color = 'blue', label='LCZ8 - large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
ax4.plot(x[t3:t4],data[0][t3:t4], linestyle='-', color = 'green', label='LCZ9 - sparsely built') #1 locker bebautes Wohn(misch)gebiet
#plt.setp(ax3.get_xticklabels(), visible=False)
ax4.set_ylim([-200,350])
#ax.set_xlim([0.0,23.0])
for label in ax4.get_xticklabels()[::2]:
    label.set_visible(False)
ax4.grid(b=True, which='major', color='grey', linestyle=':')
ax4.set_ylabel(u'sensible heat flux [W/m²]', fontsize='large')
ax4.set_xlabel('time [UTC]', fontsize='large')
"""
plt.show()

exit()

fig = plt.figure()
plt.plot(x[t1:t2],data3[0][t1:t2], linestyle='-', color = 'red', label='compact mid-rise')#3dichtes Wohn(misch)gebiet
plt.plot(x[t1:t2],data7[0][t1:t2], linestyle='-', color = 'brown', label='open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
plt.plot(x[t1:t2],data4[0][t1:t2], linestyle='-', color = 'orange', label='open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
plt.plot(x[t1:t2],data2[0][t1:t2], linestyle='-', color = 'yellow', label='open low-rise')#2 Gartenstadt
plt.plot(x[t1:t2],data9[0][t1:t2], linestyle='-', color = 'blue', label='large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
plt.plot(x[t1:t2],data[0][t1:t2], linestyle='-', color = 'green', label='sparsely built') #1 locker bebautes Wohn(misch)gebiet
plt.legend(bbox_to_anchor=(0., 1.01, 1., .102), loc='lower center',
           ncol=3, mode="expand", borderaxespad=0.)
plt.show()

exit()


fig = plt.figure()#sharex= True, sharey= True)

ax = fig.add_subplot(221)
#plt.setp(ax.get_xticklabels(), visible=False)
ax.plot(tempcanyon_3[:120], linestyle='-', color = 'blue', label='LCZ2 compact mid-rise')#3dichtes Wohn(misch)gebiet
ax.plot(tempcanyon_7[:120], linestyle='-', color = 'red', label='LCZ4 open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
ax.plot(tempcanyon_4[:120], linestyle='-', color = 'green', label='LCZ5 open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
ax.plot(tempcanyon_2[:120], linestyle='-', color = 'black', label='LCZ6 open low-rise')#2 Gartenstadt
ax.plot(tempcanyon_9[:120], linestyle='-', color = 'orange', label='LCZ8 large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
ax.plot(tempcanyon[:120], linestyle='-', color = 'red', label='LCZ9 sparsely built') #1 locker bebautes Wohn(misch)gebiet
ax.set_ylabel(u'air temperature [°C]', fontsize='large')
#ax.set_xlim([0.0,23.0])

ax = fig.add_subplot(222)
ax.plot(data3[1][:120], linestyle='-', color = 'blue', label='LCZ2 compact mid-rise')#3dichtes Wohn(misch)gebiet
ax.plot(data7[1][:120], linestyle='-', color = 'red', label='LCZ4 open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
ax.plot(data4[1][:120], linestyle='-', color = 'green', label='LCZ5 open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
ax.plot(data2[1][:120], linestyle='-', color = 'black', label='LCZ6 open low-rise')#2 Gartenstadt
ax.plot(data9[1][:120], linestyle='-', color = 'orange', label='LCZ8 large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
ax.plot(data[1][:120], linestyle='-', color = 'red', label='LCZ9 sparsely built') #1 locker bebautes Wohn(misch)gebiet
plt.setp(ax.get_xticklabels(), visible=False)
ax.set_ylabel(u'latent heat flux [W/m²]', fontsize='large')
#ax.set_ylim([-100,0])
#ax.set_xlim([0.0,23.0])

ax = fig.add_subplot(223)
ax.plot(data3[2][:120], linestyle='-', color = 'blue', label='LCZ2 compact mid-rise')#3dichtes Wohn(misch)gebiet
ax.plot(data7[2][:120], linestyle='-', color = 'red', label='LCZ4 open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
ax.plot(data4[2][:120], linestyle='-', color = 'green', label='LCZ5 open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
ax.plot(data2[2][:120], linestyle='-', color = 'black', label='LCZ6 open low-rise')#2 Gartenstadt
ax.plot(data9[2][:120], linestyle='-', color = 'orange', label='LCZ8 large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
ax.plot(data[2][:120], linestyle='-', color = 'red', label='LCZ9 sparsely built') #1 locker bebautes Wohn(misch)gebiet
#ax.set_ylim([-50,50])
#ax.set_xlim([0.0,23.0])
ax.set_ylabel(u'radiation balance [W/m²]', fontsize='large')
ax.set_xlabel('time [h]', fontsize='large')

ax = fig.add_subplot(224)
ax.plot(data3[0][:120], linestyle='-', color = 'blue', label='LCZ2 - compact mid-rise')#3dichtes Wohn(misch)gebiet
ax.plot(data7[0][:120], linestyle='-', color = 'red', label='LCZ4 open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
ax.plot(data4[0][:120], linestyle='-', color = 'green', label='LCZ5 open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
ax.plot(data2[0][:120], linestyle='-', color = 'black', label='LCZ6 - open low-rise')#2 Gartenstadt
ax.plot(data9[0][:120], linestyle='-', color = 'orange', label='LCZ8 - large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
ax.plot(data[0][:120], linestyle='-', color = 'red', label='LCZ9 - sparsely built') #1 locker bebautes Wohn(misch)gebiet
#ax.set_ylim([-50,50])
#ax.set_xlim([0.0,23.0])
ax.set_ylabel(u'sensible heat flux [W/m²]', fontsize='large')
ax.set_xlabel('time [h]', fontsize='large')

plt.show()


exit()



fig = plt.figure()
plt.plot(x[t1:t2], tempcanyon_3[t1:t2], linestyle='-', color = 'darkred', label='LCZ2 compact mid-rise')#3dichtes Wohn(misch)gebiet
plt.plot(x[t1:t2], tempcanyon_7[t1:t2], linestyle='-', color = 'red', label='LCZ4 open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
plt.plot(x[t1:t2], tempcanyon_4[t1:t2], linestyle='-', color = 'orange', label='LCZ5 open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
plt.plot(x[t1:t2], tempcanyon_2[t1:t2], linestyle='-', color = '#ffa07a', label='LCZ6 open low-rise')#2 Gartenstadt #Light Salmon ffa07a
plt.plot(x[t1:t2], tempcanyon_9[t1:t2], linestyle='-', color = 'grey', label='LCZ8 large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
plt.plot(x[t1:t2], tempcanyon[t1:t2], linestyle='-', color = '#ffdab9', label='LCZ9 sparsely built') #1 locker bebautes Wohn(misch)gebiet ffdab9 Peach Puff
plt.grid(b=True, which='major', color='grey', linestyle=':')
#plt.grid(b=True, which='minor', color='r', linestyle='--')
plt.xlabel("time [h] ")
plt.ylabel(u"canyon temperature [°C]")
plt.legend(loc=4, ncol=3, fontsize='small')
plt.show()

exit()

fig = plt.figure()
plt.plot(x[t1:t2],data7[1][t1:t2], linestyle='-', color = 'darkred', label='LCZ4 open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
plt.plot(x[t1:t2],data3[1][t1:t2], linestyle='-', color = 'red', label='LCZ2 compact mid-rise')#3dichtes Wohn(misch)gebiet
plt.plot(x[t1:t2],data4[1][t1:t2], linestyle='-', color = 'orange', label='LCZ5 open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
plt.plot(x[t1:t2],data2[1][t1:t2], linestyle='-', color = '#ffa07a', label='LCZ6 open low-rise')#2 Gartenstadt
plt.plot(x[t1:t2],data9[1][t1:t2], linestyle='-', color = 'grey', label='LCZ8 large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
plt.plot(x[t1:t2],data[1][t1:t2], linestyle='-', color = '#ffdab9', label='LCZ9 sparsely built') #1 locker bebautes Wohn(misch)gebiet
plt.grid(b=True, which='major', color='grey', linestyle=':')
plt.grid(b=True, which='minor', color='r', linestyle=':')
plt.xlabel("time")
plt.ylabel(u'latent heat flux [W/m²]')
plt.legend(loc=4, ncol=3, fontsize='small')
plt.show()

fig = plt.figure()
plt.plot(x[t1:t2],data7[2][t1:t2], linestyle='-', color = 'darkred', label='LCZ4 open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
plt.plot(x[t1:t2],data3[2][t1:t2], linestyle='-', color = 'red', label='LCZ2 compact mid-rise')#3dichtes Wohn(misch)gebiet
plt.plot(x[t1:t2],data4[2][t1:t2], linestyle='-', color = 'orange', label='LCZ5 open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
plt.plot(x[t1:t2],data2[2][t1:t2], linestyle='-', color = '#ffa07a', label='LCZ6 open low-rise')#2 Gartenstadt
plt.plot(x[t1:t2],data9[2][t1:t2], linestyle='-', color = 'grey', label='LCZ8 large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
plt.plot(x[t1:t2],data[2][t1:t2], linestyle='-', color = '#ffdab9', label='LCZ9 sparsely built') #1 locker bebautes Wohn(misch)gebiet
plt.grid(b=True, which='major', color='black', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='--')
plt.xlabel("time")
plt.ylabel(u'radiation balance [W/m²]')
plt.legend(loc=4, ncol=3, fontsize='small')
plt.show()



fig = plt.figure()
plt.plot(x[t1:t2],data7[0][t1:t2], linestyle='-', color = 'darkred', label='LCZ4 open high-rise')#7 Geschaefts-Kern-u.Mischgebiet
plt.plot(x[t1:t2],data3[0][t1:t2], linestyle='-', color = 'red', label='LCZ2 compact mid-rise')#3dichtes Wohn(misch)gebiet
plt.plot(x[t1:t2],data4[0][t1:t2], linestyle='-', color = 'orange', label='LCZ5 open mid-rise')#4großvolumiger solitaerer Wohn(misch)bau
plt.plot(x[t1:t2],data2[0][t1:t2], linestyle='-', color = '#ffa07a', label='LCZ6 open low-rise')#2 Gartenstadt
plt.plot(x[t1:t2],data9[0][t1:t2], linestyle='-', color = 'grey', label='LCZ8 large low-rise')#9Industrie prod Gewerbe, Grosshandel inkl. Lager
plt.plot(x[t1:t2],data[0][t1:t2], linestyle='-', color = '#ffdab9', label='LCZ9 sparsely built') #1 locker bebautes Wohn(misch)gebiet
plt.grid(b=True, which='major', color='black', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='--')
plt.xlabel("time")
plt.ylabel(u'sensible heat flux [W/m²]')
plt.legend(loc=4, ncol=3, fontsize='small')
plt.show()