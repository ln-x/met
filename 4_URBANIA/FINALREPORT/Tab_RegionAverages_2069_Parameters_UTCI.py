# -*- coding: utf-8 -*-
import csv
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset

file_ref = '/media/lnx/Norskehavet/OFFLINE/2069REF/dx345corr/TEB_DIAGNOSTICS.OUT.nc'
file_alb = '/media/lnx/Norskehavet/OFFLINE/2069ALB/TEB_DIAGNOSTICS.OUT.nc'
file_iso = '/media/lnx/Norskehavet/OFFLINE/2069ISO/TEB_DIAGNOSTICS.OUT.nc'
file_grr = '/media/lnx/Norskehavet/OFFLINE/2069GRR/TEB_DIAGNOSTICS.OUT.nc'
file_den = '/media/lnx/Norskehavet/OFFLINE/2069DEN/TEB_DIAGNOSTICS.OUT.nc'
file_pvr = '/media/lnx/Norskehavet/OFFLINE/2069PVR/TEB_DIAGNOSTICS.OUT.nc'
file_spr = '/media/lnx/Norskehavet/OFFLINE/2069SPR/TEB_DIAGNOSTICS.OUT.nc'
file_opt = '/media/lnx/Norskehavet/OFFLINE/2069OPT/dx345corr/TEB_DIAGNOSTICS.OUT.nc'
#dimensions(sizes): xx(174), yy(135), time(174) 1.7.2069 18h - 8.7.23h
#CE, NO, SA, RU, SE, SX, SI, VW, WE = [],[],[],[],[],[],[],[],[]
CE_ref,CE_alb,CE_iso,CE_grr,CE_den,CE_pvr,CE_spr,CE_opt =[],[],[],[],[],[],[],[]

#for i in range(0,36,1):
i = 140 #7.7. 15h
j = 155 #8.7. 6h

f_ref = Dataset(file_ref, mode='r')
f_alb = Dataset(file_alb, mode='r')
f_iso = Dataset(file_iso, mode='r')
f_grr = Dataset(file_grr, mode='r')
f_den = Dataset(file_den, mode='r')
f_pvr = Dataset(file_pvr, mode='r')
f_spr = Dataset(file_spr, mode='r')
f_opt = Dataset(file_opt, mode='r')
var_units = f_ref.variables['UTCI_OUTSHAD'].units
var_ref = f_ref.variables['UTCI_OUTSHAD'][i],f_ref.variables['UTCI_OUTSHAD'][j]
var_alb = f_alb.variables['UTCI_OUTSHAD'][i],f_alb.variables['UTCI_OUTSHAD'][j]
var_iso = f_iso.variables['UTCI_OUTSHAD'][i],f_iso.variables['UTCI_OUTSHAD'][j]
var_den = f_den.variables['UTCI_OUTSHAD'][i],f_den.variables['UTCI_OUTSHAD'][j]
var_grr = f_grr.variables['UTCI_OUTSHAD'][i],f_grr.variables['UTCI_OUTSHAD'][j]
var_pvr = f_pvr.variables['UTCI_OUTSHAD'][i],f_pvr.variables['UTCI_OUTSHAD'][j]
var_spr = f_spr.variables['UTCI_OUTSHAD'][i],f_spr.variables['UTCI_OUTSHAD'][j]
var_opt = f_opt.variables['UTCI_OUTSHAD'][i],f_opt.variables['UTCI_OUTSHAD'][j]
 #print np.average(var[50:58][:, 80:85].flatten())
 #print np.hstack(var2[50:58][:, 80:85])
 #print np.average(np.hstack(var[50:58][:, 80:85]))
 #print np.average(np.hstack(var2[50:58][:, 80:85]))

f_ref.close()
f_alb.close()
f_iso.close()
f_den.close()
f_grr.close()
f_pvr.close()
f_spr.close()
f_opt.close()
#print tair[50:59].shape

var_ref_15h_ce = np.mean(var_ref[0][50:59][:,80:89].flatten())
var_ref_15h_si = np.mean(var_ref[0][31:40][:,68:77].flatten())
var_alb_15h_ce = np.mean(var_alb[0][50:59][:,80:89].flatten())
var_iso_15h_ce = np.mean(var_iso[0][50:59][:,80:89].flatten())
var_den_15h_ce = np.mean(var_den[0][50:59][:,80:89].flatten())
#var_den_15h_se = np.mean(var_den[0][37:46][:,99:108].flatten())
#var_den_15h_no = np.mean(var_den[0][73:82][:,89:98].flatten())
var_den_15h_si = np.mean(var_den[0][31:40][:,68:77].flatten())
var_grr_15h_ce = np.mean(var_grr[0][50:59][:,80:89].flatten())
var_pvr_15h_ce = np.mean(var_pvr[0][50:59][:,80:89].flatten())
var_spr_15h_ce = np.mean(var_spr[0][50:59][:,80:89].flatten())
var_opt_15h_ce = np.mean(var_opt[0][50:59][:,80:89].flatten())

var_ref_6h_ce = np.mean(var_ref[1][50:59][:,80:89].flatten())
var_ref_6h_si = np.mean(var_ref[1][31:40][:,68:77].flatten())
var_alb_6h_ce = np.mean(var_alb[1][50:59][:,80:89].flatten())
var_iso_6h_ce = np.mean(var_iso[1][50:59][:,80:89].flatten())
var_den_6h_ce = np.mean(var_den[1][50:59][:,80:89].flatten())
#var_den_6h_no = np.mean(var_den[1][73:82][:,89:98].flatten())
#var_den_6h_se = np.mean(var_den[1][37:46][:,99:108].flatten())
var_den_6h_si = np.mean(var_den[1][31:40][:,68:77].flatten())
var_grr_6h_ce = np.mean(var_grr[1][50:59][:,80:89].flatten())
var_pvr_6h_ce = np.mean(var_pvr[1][50:59][:,80:89].flatten())
var_spr_6h_ce = np.mean(var_spr[1][50:59][:,80:89].flatten())
var_opt_6h_ce = np.mean(var_opt[1][50:59][:,80:89].flatten())

print "UTCI Shade"
print "Scenario 7.7.2069,15UTC  8.7.2069,6UTC"
print "REF_CE", round(var_ref_15h_ce,2), round(var_ref_6h_ce,2)
print "ALB_CE", round(var_alb_15h_ce - var_ref_15h_ce,2), round(var_alb_6h_ce -var_ref_6h_ce,2)
print "ISO_CE", round(var_iso_15h_ce - var_ref_15h_ce,2), round( var_iso_6h_ce-var_ref_6h_ce,2)
print "GRR_CE", round(var_grr_15h_ce - var_ref_15h_ce,2), round( var_grr_6h_ce-var_ref_6h_ce,2)
print "PVR_CE", round(var_pvr_15h_ce - var_ref_15h_ce,2), round( var_pvr_6h_ce-var_ref_6h_ce,2)
print "SPR_CE", round(var_spr_15h_ce - var_ref_15h_ce,2), round( var_spr_6h_ce-var_ref_6h_ce,2)
print "OPT_CE", round(var_opt_15h_ce - var_ref_15h_ce,2), round( var_opt_6h_ce-var_ref_6h_ce,2)
print "DEN_CE", round(var_den_15h_ce - var_ref_15h_ce,2), round(var_den_6h_ce-var_ref_6h_ce,2)
#print "DEN_NO", var_den_15h_no - var_ref_15h_ce, var_den_6h_no-var_ref_6h_ce
#print "DEN_SE", var_den_15h_se - var_ref_15h_ce, var_den_6h_se-var_ref_6h_ce
print "DEN_SI", round(var_den_15h_si - var_ref_15h_si,2), round(var_den_6h_si-var_ref_6h_si,2)

exit()

print "REF", var_ref[0][50][80], var_ref[1][50][80]
print "ALB", var_alb[0][50][80]-44.8954890335,var_alb[1][50][80]-31.4353743191
print "ISO", var_iso[0][50][80]-44.8954890335,var_iso[1][50][80]-31.4353743191
print "DEN", var_den[0][50][80]-44.8954890335,var_den[1][50][80]-31.4353743191
print "GRR", var_grr[0][50][80]-44.8954890335,var_grr[1][50][80]-31.4353743191
print "PVR", var_pvr[0][50][80]-44.8954890335,var_pvr[1][50][80]-31.4353743191
print "SPR", var_spr[0][50][80]-44.8954890335,var_spr[1][50][80]-31.4353743191
print "OPT", var_opt[0][50][80]-44.8954890335,var_opt[1][50][80]-31.4353743191



exit()

#NO1 = tair1_max[89:98][:,73:82]
#CE1 = tair1_max[80:89][:,50:59]
#RU1 = tair1_max[128:137][:,56:66]
#SA1 = tair1_max[109:118][:,58:67]
#SE1 = tair1_max[99:108][:,37:46]
#SX1 = tair1_max[75:84][:,24:33]
#SI1 = tair1_max[68:77][:,31:40]
#VW1 = tair1_max[64:73][:,47:56]
#WE1 = tair1_max[73:82][:,62:71]
exit()
CE_ref.append(np.average(np.hstack(var_ref[50:59][:, 80:89])))

#RU.append(np.average(np.hstack(var_ref[57:66][:, 128:137])))
#SA.append(np.average(np.hstack(var_ref[58:67][:, 109:118])))
CE_alb.append(np.average(np.hstack(var_alb[50:59][:, 80:89])))
CE_iso.append(np.average(np.hstack(var_iso[50:59][:, 80:89])))
CE_den.append(np.average(np.hstack(var_den[50:59][:, 80:89])))
CE_grr.append(np.average(np.hstack(var_grr[50:59][:, 80:89])))
CE_pvr.append(np.average(np.hstack(var_pvr[50:59][:, 80:89])))
CE_spr.append(np.average(np.hstack(var_spr[50:59][:, 80:89])))
CE_opt.append(np.average(np.hstack(var_opt[50:59][:, 80:89])))

#print CE_ref[0]-273.15, CE_alb[0]-CE_ref[0], CE_iso[0]-CE_ref[0], CE_den[0]-CE_ref[0], CE_grr[0]-CE_ref[0], CE_pvr[0]-CE_ref[0], CE_spr[0]-CE_ref[0], CE_opt[0]-CE_ref[0]

exit()
def difference(x,y):
 diff = []
 for i in range(len(x)):
    diff.append(x[i] - y[i])
 return diff

CEdiff_1 = difference(CE1,CE)
CEdiff_2 = difference(CE2,CE)
CEdiff_3 = difference(CE3,CE)
RUdiff_1 = difference(RU1,RU)
RUdiff_2 = difference(RU2,RU)
RUdiff_3 = difference(RU3,RU)
SAdiff_1 = difference(SA1,SA)
SAdiff_2 = difference(SA2,SA)
SAdiff_3 = difference(SA3,SA)

print len(CE), len(CE2)
exit()

time = range(0,36,1)
#"""
fig_tair = plt.figure()
major_ticks = np.arange(0, 36, 6)
minor_ticks = np.arange(0, 36, 3)
plt.xticks(major_ticks)

#plt.xticks(minor_ticks)
#plt.plot(time,ISdiff_DenseIso, color="black", label="Dense-Iso")
plt.plot(time,CEdiff_1, color="red", label="Center, DE2-Ref")
plt.plot(time,CEdiff_2, color="red", label="Center, ISO-Ref", linestyle="--")
plt.plot(time,CEdiff_3, color="red", label="Center, ALB-Ref", linestyle=":")
plt.plot(time,RUdiff_1, color="green", label="Rural, DE2-Ref")
plt.plot(time,RUdiff_2, color="green", label="Rural, ISO-Ref", linestyle="--")
plt.plot(time,RUdiff_3, color="green", label="Rural, ALB-Ref", linestyle=":")
plt.plot(time,SAdiff_1, color="blue", label="Seestadt, DE2-Ref")
plt.plot(time,SAdiff_2, color="blue", label="Seestadt, ISO-Ref", linestyle="--")
plt.plot(time,SAdiff_3, color="blue", label="Seestadt, ALB-Ref", linestyle=":")
plt.axhline(y=0.000, color="black")#, xmin=0, xmax=1, hold=None, linewidth=2)
plt.axvline(x=10.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=17.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=25.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=34.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
#plt.axvline(x=41.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
#plt.axvline(x=65.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
#plt.axvline(x=89.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
#plt.axvline(x=113.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
#plt.axvline(x=137.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)

plt.ylabel(r"$\delta UTCI$"u'[°C]')
plt.legend(loc='lower left')
plt.show()