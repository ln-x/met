# -*- coding: utf-8 -*-
import csv
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt

file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S12_FORC_WRF_333_STQ_2DURBPARAM_long_corr/SURF_ATM_DIAGNOSTICS.OUT.nc'
#file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S15_XUNIF/SURF_ATM_DIAGNOSTICS.OUT.nc'
file1 = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S14/SURF_ATM_DIAGNOSTICS.OUT.nc'
file2 = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S17_XUNIF/SURF_ATM_DIAGNOSTICS.OUT.nc'

A,F,C,W,N,E,S = [],[],[],[],[],[],[]
CS1,WS1,NS1,ES1,SS1 = [],[],[],[],[]
CS2,WS2,NS2,ES2,SS2 = [],[],[],[],[]


Urban_agric = []
Urban_forest = []
Urban_agric2 = []
Urban_forest2 = []

CdiffS1,WdiffS1,NdiffS1,EdiffS1,SdiffS1 = [],[],[],[],[]
CdiffS2,WdiffS2,NdiffS2,EdiffS2,SdiffS2 = [],[],[],[],[]

for i in range(55,79,1):   #55:0 UTC
#timeslice = 57
 print i
 f = nc.Dataset(file)
 tair = f.variables['T2M'][i] #55: 0UTC, ...73:13UTC
 lon = f.variables['xx'][:]
 lat = f.variables['yy'][:]
 #print lat 333.333 666.666 ...
 #print len(tair[0]) #174 width, 135 length

 """other try"""
 tair_regionC = tair[40:50][:,90:100]
 tair_regionW = tair[80:90][:,10:20]
 tair_regionN = tair[120:130][:,40:50]
 tair_regionE = tair[80:90][:,130:140]
 tair_regionS = tair[10:20][:,90:100]
 tair_regionFo = tair[3:13][:,3:13]
 tair_regionAg = tair[122:132][:,3:13]

 f = nc.Dataset(file1)
 tair1 = f.variables['T2M'][i]
 tair_regionC1 = tair1[40:50][:,90:100]
 tair_regionW1 = tair1[80:90][:,10:20]
 tair_regionN1 = tair1[120:130][:,40:50]
 tair_regionE1 = tair1[80:90][:,130:140]
 tair_regionS1 = tair1[10:20][:,90:100]
 tair_regionFo1 = tair1[3:13][:,3:13]
 tair_regionAg1 = tair1[122:132][:,3:13]

 f = nc.Dataset(file2)
 tair2 = f.variables['T2M'][i]
 tair_regionC2 = tair2[40:50][:,90:100]
 tair_regionW2 = tair2[80:90][:,10:20]
 tair_regionN2 = tair2[120:130][:,40:50]
 tair_regionE2 = tair2[80:90][:,130:140]
 tair_regionS2 = tair2[10:20][:,90:100]
 tair_regionFo2 = tair2[3:13][:,3:13]
 tair_regionAg2 = tair2[122:132][:,3:13]

 #tair_regionC = tair[80:90][:,50:60]
 #tair_regionW = tair[20:30][:,80:90]
 #tair_regionN = tair[40:50][:,120:130]
 #tair_regionE = tair[130:140][:,80:90]
 #tair_regionS = tair[90:100][:,10:20]
 #print type(tair_regionC)
 #print len(tair_regionC)

 #print "C", np.average(np.hstack(tair_regionC2))- np.average(np.hstack(tair_regionC))
 #print "W", np.average(np.hstack(tair_regionW2))- np.average(np.hstack(tair_regionW))
 #print "N", np.average(np.hstack(tair_regionN2))- np.average(np.hstack(tair_regionN))
 #print "E", np.average(np.hstack(tair_regionE2))- np.average(np.hstack(tair_regionE))
 #print "S", np.average(np.hstack(tair_regionS2))- np.average(np.hstack(tair_regionS))
 a = np.average(np.hstack(tair_regionAg))
 f = np.average(np.hstack(tair_regionFo))
 c = np.average(np.hstack(tair_regionC))
 w = np.average(np.hstack(tair_regionW))
 n = np.average(np.hstack(tair_regionN))
 e = np.average(np.hstack(tair_regionE))
 s = np.average(np.hstack(tair_regionS))
 c1 = np.average(np.hstack(tair_regionC1))
 w1 = np.average(np.hstack(tair_regionW1))
 n1 = np.average(np.hstack(tair_regionN1))
 e1 = np.average(np.hstack(tair_regionE1))
 s1 = np.average(np.hstack(tair_regionS1))
 c2 = np.average(np.hstack(tair_regionC2))
 w2 = np.average(np.hstack(tair_regionW2))
 n2 = np.average(np.hstack(tair_regionN2))
 e2 = np.average(np.hstack(tair_regionE2))
 s2 = np.average(np.hstack(tair_regionS2))
 cdiff1 = np.average(np.hstack(tair_regionC1)) - np.average(np.hstack(tair_regionC))
 wdiff1 = np.average(np.hstack(tair_regionW1)) - np.average(np.hstack(tair_regionW))
 ndiff1 = np.average(np.hstack(tair_regionN1)) - np.average(np.hstack(tair_regionN))
 ediff1 = np.average(np.hstack(tair_regionE1)) - np.average(np.hstack(tair_regionE))
 sdiff1 = np.average(np.hstack(tair_regionS1)) - np.average(np.hstack(tair_regionS))
 cdiff2 = np.average(np.hstack(tair_regionC2)) - np.average(np.hstack(tair_regionC))
 wdiff2 = np.average(np.hstack(tair_regionW2)) - np.average(np.hstack(tair_regionW))
 ndiff2 = np.average(np.hstack(tair_regionN2)) - np.average(np.hstack(tair_regionN))
 ediff2 = np.average(np.hstack(tair_regionE2)) - np.average(np.hstack(tair_regionE))
 sdiff2 = np.average(np.hstack(tair_regionS2)) - np.average(np.hstack(tair_regionS))
 print "urban-rural"
 c_a = np.average(np.hstack(tair_regionC))- np.average(np.hstack(tair_regionAg))
 c_f = np.average(np.hstack(tair_regionC))- np.average(np.hstack(tair_regionFo))
 c2_a2 = np.average(np.hstack(tair_regionC2))- np.average(np.hstack(tair_regionAg2))
 c2_f2 = np.average(np.hstack(tair_regionC2))- np.average(np.hstack(tair_regionFo2))
 print (np.average(np.hstack(tair_regionC2))- np.average(np.hstack(tair_regionAg2)))-(np.average(np.hstack(tair_regionC))- np.average(np.hstack(tair_regionAg)))
 print (np.average(np.hstack(tair_regionC2))- np.average(np.hstack(tair_regionFo2)))-(np.average(np.hstack(tair_regionC))- np.average(np.hstack(tair_regionFo)))
 Urban_agric.append(c_a)
 Urban_forest.append(c_f)
 Urban_agric2.append(c2_a2)
 Urban_forest2.append(c2_f2)
 A.append(a)
 F.append(f)
 C.append(c)
 E.append(e)
 N.append(n)
 W.append(w)
 S.append(s)
 CS1.append(c1)
 ES1.append(e1)
 NS1.append(n1)
 WS1.append(w1)
 SS1.append(s1)
 CS2.append(c2)
 ES2.append(e2)
 NS2.append(n2)
 WS2.append(w2)
 SS2.append(s2)
 CdiffS1.append(cdiff1)
 EdiffS1.append(ediff1)
 NdiffS1.append(ndiff1)
 WdiffS1.append(wdiff1)
 SdiffS1.append(sdiff1)
 CdiffS2.append(cdiff2)
 EdiffS2.append(ediff2)
 NdiffS2.append(ndiff2)
 WdiffS2.append(wdiff2)
 SdiffS2.append(sdiff2)

time =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23] #UTC

#Urban_agric = [3.64,3.62]
#Urban_forest = [4.30,4.20]
#Urban_agric2 = [3.87,3.83]
#Urban_forest2 = [4.52,4.41]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

major_ticks = np.arange(0, 23, 6)
minor_ticks = np.arange(0, 23, 3)
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.plot(time,A, color="green", label="Agriculture")
ax.plot(time,F, color="blue", label="Wienerwald")
ax.plot(time,C, color="violet", label="Center_Ref")
ax.plot(time,E, color="yellow", label="East_Ref")
#ax.plot(time,N, color="grey", label="North_Ref")
ax.plot(time,W, color="orange", label="West_Ref")
ax.plot(time,S, color="red", label="South_Ref")
#ax.plot(time,CS1, color="violet", linestyle="dashed")
#ax.plot(time,ES1, color="yellow", linestyle="dashed")
#ax.plot(time,NS1, color="grey", linestyle="dashed")
#ax.plot(time,WS1, color="orange", linestyle="dashed")
#ax.plot(time,SS1, color="red", linestyle="dashed")
ax.plot(time,CS2, color="violet", linestyle=":")
ax.plot(time,ES2, color="yellow", linestyle=":")
ax.plot(time,NS2, color="grey", linestyle=":")
ax.plot(time,WS2, color="orange", linestyle=":")
ax.plot(time,SS2, color="red", linestyle=":")
ax.set_xlabel("hours [UTC]")
ax.set_ylabel(r"$T_{air_2m}$"u'[°C]')
ax.legend(loc='upper center')
#ax.set_xlim(0, 23)
plt.show()


fig = plt.figure()
ax = fig.add_subplot(121)


major_ticks = np.arange(0, 23, 6)
minor_ticks = np.arange(0, 23, 3)
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.plot(time,Urban_agric, color="green", label="Center-Agric., STQ")
ax.plot(time,Urban_agric2, color="green", linestyle=":",label="Center-Agric., S3")
ax.plot(time,Urban_forest, color="blue", label="Center-Wienerwald, STQ")
ax.plot(time,Urban_forest2, color="blue", linestyle=":", label="Center-Wienerwald, S3")
ax.set_xlabel("hours [UTC]")
ax.set_ylabel(r"$T_{air_2m}$"u'[°C]')
ax.legend(loc='upper left')
#ax.set_xlim(0, 23)
plt.show()
exit()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

major_ticks = np.arange(0, 23, 6)
minor_ticks = np.arange(0, 23, 3)
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.plot(time,CdiffS2, color="violet", label="Center")
ax.plot(time,EdiffS2, color="green", label="East")
ax.plot(time,NdiffS2, color="blue", label="North")
ax.plot(time,WdiffS2, color="orange", label="West")
ax.plot(time,SdiffS2, color="red", label="South")
ax.plot(time,CdiffS1, color="violet", label="Center", linestyle=":")
ax.plot(time,EdiffS1, color="green", label="East", linestyle=":")
ax.plot(time,NdiffS1, color="blue", label="North", linestyle=":")
ax.plot(time,WdiffS1, color="orange", label="West", linestyle=":")
ax.plot(time,SdiffS1, color="red", label="South", linestyle=":")
ax.set_xlabel("hours [UTC]")
ax.set_ylabel(r"$T_{air_2m}$"u'[°C]')
ax.legend(loc='upper left')
#ax.set_xlim(0, 23)
plt.show()





# select two regions
latidx1 = (lat >= (80.*333.333)) & (lat <= (100.*333.333))
lonidx1 = (lon >= (60.*333.333)) & (lon <= (40.*333.333))

# these basically listing the values in an array (2 in this case)
tairX = tair[:]
tair1 = tairX[:, latidx1][..., lonidx1]
tair_1 = tair1

# time to get the mean values
print np.mean(tair_1)
print "............."
#print np.mean(tair_2)
print "............."