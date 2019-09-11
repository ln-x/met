# -*- coding: utf-8 -*-
import csv
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from pylab import *
from scipy import stats

outpath ='/media/lnx/Norskehavet/OFFLINE/plots'
file_ref2015 = '/media/lnx/Norskehavet/OFFLINE/2015REF/dx345corr/TEB_PROGNOSTIC.OUT.nc'

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
#a1,a2,b1,b2= 51,60,81,90 #50,59,80,89   #CE
#a1,a2,b1,b2=73,82,89,98   #NO
#a1,a2,b1,b2=57,66,128,137 #RU
#a1,a2,b1,b2=58,67,109,118 #SA
#a1,a2,b1,b2=37,46,99,108  #SE
#a1,a2,b1,b2=24,33,75,84   #SX
a1,a2,b1,b2=31,40,68,77   #SI
#a1,a2,b1,b2=47,56,64,73   #VW
#a1,a2,b1,b2=62,71,73,82   #WE

'''cut for subregions'''
def collectMAX(relSIMPATH):
    out1=[]   #max
    out2=[]   #min
    out3=[]   #max
    out4=[]   #min
    file = '/media/lnx/Norskehavet/OFFLINE/'+relSIMPATH+'/TEB_DIAGNOSTICS.OUT.nc'
    f = Dataset(file, mode='r')
    var_reg = f.variables['TRAD_SHADE'][126:174, a1:a2, b1:b2]
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
    var_regSUN = f.variables['TRAD_SUN'][126:174, a1:a2, b1:b2]
    for i in range(9):
        for j in range(9):
           add = (var_regSUN[:,i,j].max())
           if add!=nan:
             out3.append(add)
           else:
             out3.append(0)
           add2 = var_regSUN[:, i, j].min()
           if add2 != nan:
             out4.append(add2)
           else:
             out4.append(0)
    f.close()
    #print "\n", np.mean(list(filter(lambda x: x != 0, out1)))
    #print np.mean(list(filter(lambda x: x != 0, out2)))
    #print np.mean(list(filter(lambda x: x != 0, out3)))
    #print np.mean(list(filter(lambda x: x != 0, out4)))
    #print "\n",relSIMPATH, "max_diff ", np.mean(list(filter(lambda x: x != 0, out1))) - 316.979321713 #NO: 315.698654144
    #print relSIMPATH, "min_diff ", np.mean(list(filter(lambda x: x != 0, out2))) -303.09471181 #NO: -300.521421144
    print np.mean(list(filter(lambda x: x != 0, out1))) - 328.568820869
    print np.mean(list(filter(lambda x: x != 0, out2))) - 298.993857664
    print np.mean(list(filter(lambda x: x != 0, out3))) - 354.88244882
    #print np.mean(list(filter(lambda x: x != 0, out4))) - 304.066382408

    return out1,out2

"""
CE: 327.549008568
CE: 304.066382408
CE: 353.916730274

NO: 329.793281233
NO: 299.031403442
NO: 355.507313789

RU: 327.29513726
RU: 294.294684728
RU: 353.711671846 

SA:
330.219940816
298.313922866
355.877615999 

SE: 
329.178492267
297.365672546
354.99890576

SX: 
328.217894746
297.791312533
354.542310259

SI: 
328.568820869
298.993857664
354.88244882

VW: 
328.941890918
300.45128785
355.084371173

WE: 
329.239776258
300.581189454
355.20443619
"""
utci_ref2069_ce_max, utci_ref2069_ce_min = collectMAX("2069REF/dx345corr")
utci_alb2069_ce_max, utci_alb2069_ce_min = collectMAX("2069ALB")
utci_iso2069_ce_max, utci_iso2069_ce_min = collectMAX("2069ISO")
utci_den2069_ce_max, utci_den2069_ce_min = collectMAX("2069DEN")
utci_grr2069_ce_max, utci_grr2069_ce_min = collectMAX("2069GRR")
utci_pvr2069_ce_max, utci_pvr2069_ce_min = collectMAX("2069PVR")
utci_spr2069_ce_max, utci_spr2069_ce_min = collectMAX("2069SPR")
utci_opt2069_ce_max, utci_opt2069_ce_min = collectMAX("2069OPT/dx345corr")

exit()
tstatistics_alb, pvalue_alb = stats.ttest_rel(utci_ref2069_ce_min,utci_alb2069_ce_min)
tstatistics_iso, pvalue_iso = stats.ttest_rel(utci_ref2069_ce_min,utci_iso2069_ce_min)
tstatistics_grr, pvalue_grr = stats.ttest_rel(utci_ref2069_ce_min,utci_grr2069_ce_min)
tstatistics_den, pvalue_den = stats.ttest_rel(utci_ref2069_ce_min,utci_den2069_ce_min)
tstatistics_pvr, pvalue_pvr = stats.ttest_rel(utci_ref2069_ce_min,utci_pvr2069_ce_min)
tstatistics_spr, pvalue_spr = stats.ttest_rel(utci_ref2069_ce_min,utci_spr2069_ce_min)
tstatistics_opt, pvalue_opt = stats.ttest_rel(utci_ref2069_ce_min,utci_opt2069_ce_min)

print pvalue_alb, pvalue_iso, pvalue_grr, pvalue_den, pvalue_pvr, pvalue_spr, pvalue_opt
#result for _rel (CE): MAX 3.40749250069e-27 1.33137198503e-40 1.61454789167e-33 0.0123816209679 5.20325709417e-36 0.304196932476 2.93936246538e-08
                #(CE): MIN 2.04798764991e-42 1.05187491487e-46 7.72763708206e-44 0.00734892392589 2.27389712924e-44 0.122820513359 5.40872192165e-38
#result for _ind (CE): MAX 0.907478854148 0.462138768485 0.931008810796 0.999259777872 0.908740388788 0.691739621648 0.931843086897

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


