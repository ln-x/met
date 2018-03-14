# coding=utf-8
from BIOCLIC import hs9_loader
from BIOCLIC import hs_cdataloader

__author__ = 'lnx'
import matplotlib.pyplot as plt

filename = "C:\heatsource900b5_339\win32\Test\outputfiles\Temp_H2O.txt"
thedata = hs9_loader.loadfile(filename=filename)
#print 'loaded: ', thedata

#TODO: for i[0] until i[154] find MIN  -> write to list
#TODO: for i[0] until i[154] find MAX

date_time = [i[0] for i in thedata]

thedata_withouttime = [i[1:] for i in thedata]
print thedata_withouttime

Tmin = []
Tmax = []

#for x in range(len(thedata)):
for x in thedata_withouttime:
#print [x for b in thedata for x in b]
    #xx = [i[1] for i in thedata]
    Tmin0, idx = min((Tmin0, idx) for (idx,Tmin0) in enumerate (x))
    Tmin.append(Tmin0)
    #print Tmin0, Tmin, idx
    Tmax0, idx = max((Tmax0, idx) for (idx, Tmax0) in enumerate (x))
    Tmax.append(Tmax0)
    #print Tmax0, Tmax, idx

print Tmin, Tmax
print len(date_time), len(Tmin), len(Tmax)
fig = plt.figure()

plt.title('Tmin, Tmax')
plt.plot(date_time, Tmin,color='blue', lw=0.5)
plt.plot(date_time, Tmax,color='red', lw =0.5)

plt.ylabel('water temperature[degC]')
plt.xlabel('river distance from mouth?[km]')
fig.autofmt_xdate()

plt.show()