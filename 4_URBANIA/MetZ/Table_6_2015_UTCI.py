# -*- coding: utf-8 -*-
import csv
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from pylab import *
from scipy import stats

outpath ='/media/lnx/Norskehavet/OFFLINE/plots'

file_ref2015 = '/media/lnx/Norskehavet/OFFLINE/2015REF/dx345corr/TEB_DIAGNOSTICS.OUT.nc'
#dimensions(sizes): xx(174), yy(135), time(174) 1.7.2069 18h - 8.7.23h

f_ref2015 = Dataset(file_ref2015, mode='r')

var_units = f_ref2015.variables['UTCI_OUTSHAD'].units


"""
timeslices:
present 1988-2017, 15yr 5day maxima temperature extreme:
start 5.8.2015 18h
end 13.8.2015

	xx = 174 ;
	yy = 135 ;
	time = UNLIMITED ; // (198 currently)
variables:

future 2016-2065, 15yr 5day maxima temperature extreme:
start 1.7.2069 18h
end 8.7.2069

subregions:
"""

#a1,a2,b1,b2= 51,60,81,90# CE
#a1,a2,b1,b2=50,59,80,89   #CE
#a1,a2,b1,b2=73,82,89,98   #NO
#a1,a2,b1,b2=57,66,128,137 #RU
#a1,a2,b1,b2=58,67,109,118 #SA
#a1,a2,b1,b2=37,46,99,108  #SE
#a1,a2,b1,b2=24,33,75,84   #SX
#a1,a2,b1,b2=31,40,68,77   #SI
#a1,a2,b1,b2=47,56,64,73   #VW
a1,a2,b1,b2=62,71,73,82   #WE
'''cut for subregions'''
var_ref = f_ref2015.variables['UTCI_OUTSHAD']
#print len(f_ref2015.variables['UTCI_OUTSHAD'])
#print f_ref.variables['time']#[150:174]

var_ref2015_ce = f_ref2015.variables['UTCI_OUTSHAD'][150:198,a1:a2,b1:b2]
var_ref2015_ce2 = f_ref2015.variables['UTCI_OUTSHAD'][78:126,a1:a2,b1:b2]
utci_ref2015_ce_max=[]
utci_ref2015_ce_min=[]
for i in range(9):
    for j in range(9):
        val1= var_ref2015_ce[:,i,j].max()
        val2 = var_ref2015_ce2[:,i,j].max()
        add = np.maximum(val1,val2)
        if add!=nan:
          utci_ref2015_ce_max.append(add)
        else:
          pass
        val3= var_ref2015_ce[:,i,j].min()
        val4 = var_ref2015_ce2[:,i,j].min()
        add2 = np.minimum(val3,val4)
        if add2!= nan:
            utci_ref2015_ce_min.append(add2)
        else:
            pass

print np.mean(utci_ref2015_ce_max), np.mean(utci_ref2015_ce_min)
"""
def collectMAX(relSIMPATH):
    out1=[]   #max
    out2=[]   #min
    file = '/media/lnx/Norskehavet/OFFLINE/'+relSIMPATH+'/TEB_DIAGNOSTICS.OUT.nc'
    f = Dataset(file, mode='r')
    var_reg = f.variables['UTCI_OUTSHAD'][126:174, a1:a2, b1:b2]  #126:174
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
    #print "\n",relSIMPATH, "max_diff ", np.mean(list(filter(lambda x: x != 0, out1)))
    #print relSIMPATH, "min_diff ", np.mean(list(filter(lambda x: x != 0, out2)))

#REF/CE:  45.2181257379, 28.7547362824
#REF/NO:  44.414887728, 25.8023229079
#REF/RU:  43.9099997033, 22.0908064706
#REF/SA:  44.2085441936,24.4680844378
#REF/SE:  44.1944950911, 24.9311367267
#REF/SX: 43.7047302822,25.3708854952
#REF/SI:43.9763975978,26.4035453227
#REF/VW:44.0912614048,27.422063666
#REF/WE:43.9708595711,26.9300127078

    return out1,out2

utci_ref2069_ce_max, utci_ref2069_ce_min = collectMAX("2015REF/dx345corr")
#utci_opt2069_ce_max, utci_opt2069_ce_min = collectMAX("2015OPT/dx345corr")
"""
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


