# -*- coding: utf-8 -*-
import csv
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from pylab import *

outpath ='/media/lnx/Norskehavet/OFFLINE/plots'
file_ref = '/media/lnx/Norskehavet/OFFLINE/2069REF/dx345corr/TEB_DIAGNOSTICS.OUT.nc'
file_alb = '/media/lnx/Norskehavet/OFFLINE/2069ALB/TEB_DIAGNOSTICS.OUT.nc'
file_iso = '/media/lnx/Norskehavet/OFFLINE/2069ISO/TEB_DIAGNOSTICS.OUT.nc'
file_grr = '/media/lnx/Norskehavet/OFFLINE/2069GRR/TEB_DIAGNOSTICS.OUT.nc'
file_den = '/media/lnx/Norskehavet/OFFLINE/2069DEN/TEB_DIAGNOSTICS.OUT.nc'
file_pvr = '/media/lnx/Norskehavet/OFFLINE/2069PVR/TEB_DIAGNOSTICS.OUT.nc'
file_spr = '/media/lnx/Norskehavet/OFFLINE/2069SPR/TEB_DIAGNOSTICS.OUT.nc'
file_opt = '/media/lnx/Norskehavet/OFFLINE/2069OPT/dx345corr/TEB_DIAGNOSTICS.OUT.nc'
#dimensions(sizes): xx(174), yy(135), time(174) 1.7.2069 18h - 8.7.23h

f_ref = Dataset(file_ref, mode='r')
f_alb = Dataset(file_alb, mode='r')
f_iso = Dataset(file_iso, mode='r')
f_grr = Dataset(file_grr, mode='r')
f_den = Dataset(file_den, mode='r')
f_pvr = Dataset(file_pvr, mode='r')
f_spr = Dataset(file_spr, mode='r')
f_opt = Dataset(file_opt, mode='r')
var_units = f_ref.variables['UTCI_OUTSHAD'].units

'''cut for subregions'''
var_ref = f_ref.variables['UTCI_OUTSHAD']

var_ref_ce = f_ref.variables['UTCI_OUTSUN'][:,50:59,80:89]
var_alb_ce = f_alb.variables['UTCI_OUTSUN'][:,50:59,80:89]
var_iso_ce = f_iso.variables['UTCI_OUTSUN'][:,50:59,80:89]
var_den_ce = f_den.variables['UTCI_OUTSUN'][:,50:59,80:89]
var_grr_ce = f_grr.variables['UTCI_OUTSUN'][:,50:59,80:89]
var_pvr_ce = f_pvr.variables['UTCI_OUTSUN'][:,50:59,80:89]
var_spr_ce = f_spr.variables['UTCI_OUTSUN'][:,50:59,80:89]
var_opt_ce = f_opt.variables['UTCI_OUTSUN'][:,50:59,80:89]
print var_ref_ce.shape

utci_ref_ce_max=[]
utci_ref_ce_min=[]
for i in range(9):
    for j in range(9):
        add1 = var_ref_ce[126:149,i,j].max()
        add2 = var_ref_ce[150:174,i,j].max()
        if add1!=nan: utci_ref_ce_max.append(add1)
        else: utci_ref_ce_max.append(0)
        if add2!=nan: utci_ref_ce_max.append(add2)
        else: utci_ref_ce_max.append(0)
        add3 = var_ref_ce[126:149, i, j].min()
        add4 = var_ref_ce[150:174, i, j].min()
        if add3 != nan: utci_ref_ce_min.append(add3)
        else: utci_ref_ce_min.append(0)
        if add4 != nan: utci_ref_ce_min.append(add4)
        else: utci_ref_ce_min.append(0)

utci_alb_ce_max=[]
utci_alb_ce_min=[]
for i in range(9):
    for j in range(9):
        add1 = var_alb_ce[126:149,i,j].max()
        add2 = var_alb_ce[150:174,i,j].max()
        if add1!=nan: utci_alb_ce_max.append(add1)
        else: utci_alb_ce_max.append(0)
        if add2!=nan: utci_alb_ce_max.append(add2)
        else: utci_alb_ce_max.append(0)
        add3 = var_alb_ce[126:149, i, j].min()
        add4 = var_alb_ce[150:174, i, j].min()
        if add3 != nan: utci_alb_ce_min.append(add3)
        else: utci_alb_ce_min.append(0)
        if add4 != nan: utci_alb_ce_min.append(add4)
        else: utci_alb_ce_min.append(0)

utci_iso_ce_max=[]
utci_iso_ce_min=[]
for i in range(9):
    for j in range(9):
        add1 = var_iso_ce[126:149,i,j].max()
        add2 = var_iso_ce[150:174,i,j].max()
        if add1!=nan: utci_iso_ce_max.append(add1)
        else: utci_iso_ce_max.append(0)
        if add2!=nan: utci_iso_ce_max.append(add2)
        else: utci_iso_ce_max.append(0)
        add3 = var_iso_ce[126:149, i, j].min()
        add4 = var_iso_ce[150:174, i, j].min()
        if add3 != nan: utci_iso_ce_min.append(add3)
        else: utci_iso_ce_min.append(0)
        if add4 != nan: utci_iso_ce_min.append(add4)
        else: utci_iso_ce_min.append(0)

utci_den_ce_max=[]
utci_den_ce_min=[]
for i in range(9):
    for j in range(9):
        add1 = var_den_ce[126:149,i,j].max()
        add2 = var_den_ce[150:174,i,j].max()
        if add1!=nan: utci_den_ce_max.append(add1)
        else: utci_den_ce_max.append(0)
        if add2!=nan: utci_den_ce_max.append(add2)
        else: utci_den_ce_max.append(0)
        add3 = var_den_ce[126:149, i, j].min()
        add4 = var_den_ce[150:174, i, j].min()
        if add3 != nan: utci_den_ce_min.append(add3)
        else: utci_den_ce_min.append(0)
        if add4 != nan: utci_den_ce_min.append(add4)
        else: utci_den_ce_min.append(0)

utci_grr_ce_max=[]
utci_grr_ce_min=[]
for i in range(9):
    for j in range(9):
        add1 = var_grr_ce[126:149,i,j].max()
        add2 = var_grr_ce[150:174,i,j].max()
        if add1!=nan: utci_grr_ce_max.append(add1)
        else: utci_grr_ce_max.append(0)
        if add2!=nan: utci_grr_ce_max.append(add2)
        else: utci_grr_ce_max.append(0)
        add3 = var_grr_ce[126:149, i, j].min()
        add4 = var_grr_ce[150:174, i, j].min()
        if add3 != nan: utci_grr_ce_min.append(add3)
        else: utci_grr_ce_min.append(0)
        if add4 != nan: utci_grr_ce_min.append(add4)
        else: utci_grr_ce_min.append(0)

utci_pvr_ce_max=[]
utci_pvr_ce_min=[]
for i in range(9):
    for j in range(9):
        add1 = var_pvr_ce[126:149,i,j].max()
        add2 = var_pvr_ce[150:174,i,j].max()
        if add1!=nan: utci_pvr_ce_max.append(add1)
        else: utci_pvr_ce_max.append(0)
        if add2!=nan: utci_pvr_ce_max.append(add2)
        else: utci_pvr_ce_max.append(0)
        add3 = var_pvr_ce[126:149, i, j].min()
        add4 = var_pvr_ce[150:174, i, j].min()
        if add3 != nan: utci_pvr_ce_min.append(add3)
        else: utci_pvr_ce_min.append(0)
        if add4 != nan: utci_pvr_ce_min.append(add4)
        else: utci_pvr_ce_min.append(0)

f_ref.close()
f_alb.close()
f_iso.close()
f_den.close()
f_grr.close()
f_pvr.close()
f_spr.close()
f_opt.close()

UTCI_CE_max= transpose([utci_ref_ce_max,utci_alb_ce_max,
utci_iso_ce_max,utci_den_ce_max,utci_grr_ce_max, utci_pvr_ce_max])

UTCI_CE_min = transpose([utci_ref_ce_min,utci_alb_ce_min,
utci_iso_ce_min, utci_den_ce_min, utci_grr_ce_min, utci_pvr_ce_min])

#TairCE_filtered = TairCE[~np.isnan(TairCE)]
labels = ["REF","ALB","ISO","DEN","GRR","PVR"]
#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.boxplot.html
#The box extends from the lower (Q1) to the upper (Q3) quartile values of data, with a line at the median
#The whiskers extend from the box to show the range of data, default=1.5 ->   Q1-whis*IQR, Q3+whis*IQR (interquartiles range)
#whis=[5,95]  Set whiskers to percentiles

fig2, axs = plt.subplots(nrows=1, ncols=2)#, figsize=(9, 4))
#fig2.suptitle("daily maxima and minima, averaged over center for 8 Jul 2069")
axs[0].boxplot(UTCI_CE_max, notch=True, labels=labels, showfliers=False)#, whis=[5,95])
axs[0].set_ylabel(r"$UTCI Sun$"u'[°C]')
axs[0].set_xlabel("MAX")
axs[0].set_ylim([42,55])

#axs[1].boxplot(UTCI_CE_min,  notch=True, labels=labels, showfliers=True,  whis=[5,95])
axs[1].boxplot(UTCI_CE_min,  notch=True, labels=labels, showfliers=False)#True,  whis=[5,95])
axs[1].set_xlabel("MIN")
axs[1].set_ylim([25,37])
#axs[1].set_yticklabels([])

plt.rcParams["axes.grid"]=True
plt.show()


