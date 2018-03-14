from BIOCLIC import hs_loader
from pylab import *
__author__ = 'lnx'
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from mpl_toolkits.axes_grid.anchored_artists import AnchoredText

#1)load file
#filename = "/home/lnx/PycharmProjects/HS/049/outputfiles_newConv_elevcorr_incacloud_start89_masstransfer/Heat_Conv_24h.txt"
#filename = "/home/lnx/PycharmProjects/HS/049/outputfiles_origConv_elevcorr_incacloud_start89_masstransfer/Hyd_Vel.txt"
#filename = "/home/lnx/PycharmProjects/HS/049/outputfiles_origConv_elevcorr_incacloud_start89_masstransfer/Temp_H2O.txt"
filename = "/home/lnx/PycharmProjects/HS/049/outputfiles_origConv_elevcorr_incacloud_start89_masstransfer/Hyd_DA.txt"

name, header, thedata = hs_loader.loadfile(filename=filename)
#name =  name.strip()                                                 #ev. fuer in den Titel laden
print 'loaded: ', name

data = np.array(thedata)

#2)prepare y axis
#y = [i[ 0]for i in data]                                             #extract column with datetime from data
#y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24] #1 day
y = [i for i in range(1, 1441, 1)]                                     #1440 hours from 1 July 0h - 29 August 2013 23h
#print y

#3)prepare x axis
#splitheader = []
#for i in header:
#        splitheader.append(i.split())                                #Splitten der Listenelemente   split(":")  Seperator ":"
#print splitheader
#x = splitheader[1:]
#x = [i for i in range(164, 0, 1)]                                    #TODO: Wie macht  man das fuer floats?
#x = [89,88.5,88,87.5,87,86.5,86,85.5,85,84.5,84,83.5,83,82.5,82,81.5,81,80.5,80,79.5,79,78.5,78,77.5,77,76.5,76,75.5,
#     75,74.5,74,73.5,73,72.5,72,71.5,71,70.5,70,69.5,69,68.5,68,67.5,67,66.5,66,65.5,65,64.5,64,63.5,63,62.5,62,61.5,
#     61,60.5,60,59.5,59,58.5,58,57.5,57,56.5,56,55.5,55,54.5,54,53.5,53,52.5,52,51.5,51,50.5,50,49.5,49,48.5,48,47.5,
#     47,46.5,46,45.5,45,44.5,44,43.5,43,42.5,42,41.5,41,40.5,40,39.5,39,38.5,38,37.5,37,36.5,36,35.5,35,34.5,34,33.5,
#     33,32.5,32,31.5,31,30.5,30,29.5,29,28.5,28,27.5,27,26.5,26,25.5,25,24.5,24,23.5,23,22.5,22,21.5,21,20.5,20,19.5,
#     19,18.5,18,17.5,17,16.5,16,15.5,15,14.5,14,13.5,13,12.5,12,11.5,11,10.5,10,9.5,9,8.5,8,7.5]
x = np.arange(89,7.5,0.5)

X, Y = np.meshgrid(x,y)

#4)prepare z axis
puredata = [i[1:] for i in data]                                      #schneidet bei jeder Zeile jeweils 1.Wert (Datum) ab
print puredata[0]                                                    #jeweils eine Zeile inkl Datum (Verlauf entlang Flusskilometer an einem Zeitpunkt)
Z = puredata

#5)statistics
min = min(min(i) for i in Z)
max = max(max(j) for j in Z)
delta = (max-min)/15
print "min(Z)=", min, "max(Z)=", max, "delta=(min-max)/15=", delta

std = np.std(Z)
print "std(Z)=", std

V = np.arange(min,max,delta)
#N = np.arange(-1, 1, 0.5)

listeddata = []       #splitlistcomp = [i.split() for i in data]
for i in Z:
    for j in i:
        listeddata.append(j)
#print listeddata
#print type(listeddata)

mean = average(listeddata)

print "time steps (len(Z)):", len(Z)
print "longitudinal steps (len(Z[0])):", len(Z[0])
print "number of data entries (len(listeddata)):",len(listeddata)

#listeddata = np.array(listeddata)

#print all(listeddata > 0)          #TODO Example:   all(item[2] == 0 for item in items)
#print any(listeddata[i] == 1000 for i in listeddata) #TODO

#min2 = min(listeddata)
#print min2

fig = plt.figure()

ax = fig.add_subplot(221)
subplot(121)
boxplot(listeddata)

#annotate("max=33") #, (10,10), xycoords='data', xytext=(1,10))

#col_labels = ['value']
#row_labels = ['min','max','stdv']
#table_vals = [-1, 5, 3]
#my_table = plt.table(cellText=table_vals, colWidths=[0.1]*3,rowLabels=row_labels, colLabels=col_labels, loc='upper right')

subplot(122)
hist(listeddata)
#plt.title('Flow velocity[m/s], 1Jul-29Aug2013, Pinka,(origConv,masstransfer)')
#plt.title('water temperature[degC], 1Jul-29Aug2013, Pinka,(origConv,masstransfer)')
plt.title('average depth[m], 1Jul-29Aug2013, Pinka,(origConv,masstransfer)')

plt.text(70,110000, 'min=',fontsize=12)
plt.text(100,110000, min,fontsize=12)
plt.text(70,100000, 'max=',fontsize=12)
plt.text(100,100000, max,fontsize=12)
plt.text(70,90000, 'mean=',fontsize=12)
plt.text(100,90000, mean,fontsize=12)
plt.text(70,80000, 'std=',fontsize=12)
plt.text(100,80000, std,fontsize=12)

fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/origC_m_DA_statistics.png')

#show()

#6)contour

fig = plt.figure()
CS = plt.contour(Z, V, cmap=mpl.cm.jet)                               #oder N?
plt.clabel(CS, inline=True, fmt='%1.1f', fontsize=10)
plt.colorbar(CS)
#plt.title('Convection [ ' $W/m2$ ' ], 1 July 2013, Pinka, %s', name)     #TODO: $$ und %s geht leider nicht
#plt.title('flow velocity [m/s], 1 Jul  - 29 Aug 2013, Pinka, (origConv, masstransfer)')
#plt.title('water temperature[degC], 1Jul-29Aug2013, Pinka,(origConv,masstransfer)')
plt.title('average depth[m], 1Jul-29Aug2013, Pinka,(origConv,masstransfer)')
plt.xlabel('distance from upstream model boundary [km*2]')
plt.ylabel('time[h]')
#plt.legend()
fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/origC_m_DA.png')


show()
