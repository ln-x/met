# -*- coding: utf-8 -*-
import csv
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from pylab import *
from scipy import stats

outpath ='/media/lnx/Norskehavet/OFFLINE/plots'
#file_ref2015 = '/media/lnx/Norskehavet/OFFLINE/2015REF/dx345corr/TEB_PROGNOSTIC.OUT.nc'

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
a1,a2,b1,b2= 51,60,81,90 #50,59,80,89   #CE
#a1,a2,b1,b2=73,82,89,98   #NO
#a1,a2,b1,b2=57,66,128,137 #RU
#a1,a2,b1,b2=58,67,109,118 #SA
#a1,a2,b1,b2=37,46,99,108  #SE
#a1,a2,b1,b2=24,33,75,84   #SX
#a1,a2,b1,b2=31,40,68,77   #SI
#a1,a2,b1,b2=47,56,64,73   #VW
#a1,a2,b1,b2=62,71,73,82   #WE

'''cut for subregions'''
def collectMAX(relSIMPATH):
    out1=[]   #max
    out2=[]   #min
    file = '/media/lnx/Norskehavet/OFFLINE/'+relSIMPATH+'/TEB_PROGNOSTIC.OUT.nc'
    f = Dataset(file, mode='r')
    var_reg = f.variables['TCANYON'][126:174, a1:a2, b1:b2]
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
    print "\n", np.mean(list(filter(lambda x: x != 0, out1)))-273.15
    print np.mean(list(filter(lambda x: x != 0, out2)))-273.15
    #print "\n",relSIMPATH, "max_diff ", np.mean(list(filter(lambda x: x != 0, out1))) - 316.979321713 #NO: 315.698654144
    #print relSIMPATH, "min_diff ", np.mean(list(filter(lambda x: x != 0, out2))) -303.09471181 #NO: -300.521421144
    #print np.mean(list(filter(lambda x: x != 0, out1))) - 315.25217052
    #print np.mean(list(filter(lambda x: x != 0, out2))) - 301.33431289

    return out1,out2

"""
CE: 316.979321713 
CE: -303.09471181
NO: 315.698654144
NO: -300.521421144
RU:  315.319743096
RU:  297.338552968
SA: 315.471252648
SA: 299.001217067
SE: 315.459012572
SE: 299.693239641
SX: 315.309965916
SX: 300.65394799
SI: 315.228671502
SI: 301.461455391
VW: 315.445583858
VW: 302.411160108
WE: 315.25217052
WE: 301.33431289
"""
utci_ref2069_ce_max, utci_ref2069_ce_min = collectMAX("2069REF/dx345corr")
utci_alb2069_ce_max, utci_alb2069_ce_min = collectMAX("2069ALB")
utci_iso2069_ce_max, utci_iso2069_ce_min = collectMAX("2069ISO")
utci_den2069_ce_max, utci_den2069_ce_min = collectMAX("2069DEN")
utci_grr2069_ce_max, utci_grr2069_ce_min = collectMAX("2069GRR")
utci_pvr2069_ce_max, utci_pvr2069_ce_min = collectMAX("2069PVR")
utci_spr2069_ce_max, utci_spr2069_ce_min = collectMAX("2069SPR")
utci_opt2069_ce_max, utci_opt2069_ce_min = collectMAX("2069OPT/dx345corr")
