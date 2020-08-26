# -*- coding: utf-8 -*-
import csv
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from pylab import *

outpath ='/media/lnx/Norskehavet/OFFLINE/plots'
"""
timeslices:
present 1988-2017, 15yr 5day maxima temperature extreme:
start 5.8.2015 18h
end 13.8.2015

future 2016-2065, 15yr 5day maxima temperature extreme:
start 1.7.2069 18h
end 8.7.2069

subregions:

"""
a1,a2,b1,b2= 51,60,81,90#50,59,80,89   #CE
#a1,a2,b1,b2=73,82,89,98   #NO
#a1,a2,b1,b2=57,66,128,137 #RU
#a1,a2,b1,b2=58,67,109,118 #SA
#a1,a2,b1,b2=37,46,99,108  #SE
#a1,a2,b1,b2=24,33,75,84   #SX
#a1,a2,b1,b2=31,40,68,77   #SI
#a1,a2,b1,b2=47,56,64,73   #VW
#a1,a2,b1,b2=62,71,73,82   #WE

def collectMAX(relSIMPATH, startindex, endindex):
    out1=[]   #max
    out2=[]   #min
    file = '/media/lnx/Norskehavet/OFFLINE/'+relSIMPATH+'/TEB_DIAGNOSTICS.OUT.nc'
    f = Dataset(file, mode='r')
    var_reg = f.variables['UTCI_OUTSHAD'][startindex:endindex, a1:a2, b1:b2]
    for i in range(9):
        for j in range(9):
           add = (var_reg[:,i,j].max())
           if add!=nan:
             out1.append(add)
           else:
             out1.append(0)
           add2 = var_reg[:, i, j].min()
           if add2 != nan:
             out2.append(add2)
           else:
             out2.append(0)
    f.close()
    print "\n",relSIMPATH, "max ", np.mean(list(filter(lambda x: x != 0, out1)))
    print relSIMPATH, "min ", np.mean(list(filter(lambda x: x != 0, out2)))
    return out1,out2

#2015: 150:198
#2069: 126:174
utci_ref2069_ce_max, utci_ref2069_ce_min = collectMAX("2069REF/dx345corr",126,174)
utci_spr2069_ce_max, utci_spr2069_ce_min = collectMAX("2069SPR",126,174)
utci_opt2069_ce_max, utci_opt2069_ce_min = collectMAX("2069OPT/dx345corr",126,174)
utci_ref2069_ce_max, utci_ref2015_ce_min = collectMAX("2015REF/dx345corr",150,198)
utci_opt2069_ce_max, utci_opt2015_ce_min = collectMAX("2015OPT/dx345corr",150,198)
#exit()

UTCI_CE_max= transpose([utci_ref2069_ce_max,utci_alb2069_ce_max,
utci_iso2069_ce_max,utci_den2069_ce_max,utci_grr2069_ce_max, utci_pvr2069_ce_max])

UTCI_CE_min = transpose([utci_ref2069_ce_min,utci_alb2069_ce_min,
utci_iso2069_ce_min, utci_den2069_ce_min, utci_grr2069_ce_min, utci_pvr2069_ce_min])

#TairCE_filtered = TairCE[~np.isnan(TairCE)]
labels = ["REF","ALB","ISO","DEN","GRR","PVR"]
#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.boxplot.html
#The box extends from the lower (Q1) to the upper (Q3) quartile values of data, with a line at the median
#The whiskers extend from the box to show the range of data, default=1.5 ->   Q1-whis*IQR, Q3+whis*IQR (interquartiles range)
#whis=[5,95]  Set whiskers to percentiles

fig2, axs = plt.subplots(nrows=1, ncols=2)#, figsize=(9, 4))
#fig2.suptitle("daily maxima and minima, averaged over center for 8 Jul 2069")
axs[0].boxplot(UTCI_CE_max, notch=True, labels=labels, showfliers=False)
axs[0].set_ylabel(r"$UTCI Shade$"u'[°C]')
axs[0].set_xlabel("MAX")
#axs[0].set_ylim([42,55])
axs[0].set_ylim([44,48])

#axs[1].boxplot(UTCI_CE_min,  notch=True, labels=labels, showfliers=True,  whis=[5,95])
axs[1].boxplot(UTCI_CE_min,  notch=True, labels=labels, showfliers=False)
axs[1].set_xlabel("MIN")
#axs[1].set_ylim([25,37])
axs[1].set_ylim([27,31])
#axs[1].set_yticklabels([])

plt.show()


