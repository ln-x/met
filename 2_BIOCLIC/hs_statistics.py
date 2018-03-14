from BIOCLIC import hs_loader
from pylab import *
__author__ = 'lnx'
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
filename = "/home/lnx/PycharmProjects/HS/049/outputfiles_newConv_elevcorr_incacloud_start89_masstransfer/Heat_Conv_24h.txt"
name, header, thedata = hs_loader.loadfile(filename=filename)
print 'loaded: ', name

#data = np.load(filename)

data = np.array(thedata)
#print data

#y = [i[0]for i in data] #column with datetime

#data = [i[1] for i in thedata]
#data = thedata[1:][1:]
#print data[0]#jeweils eine Zeile ohne Datum (Verlauf entlang Flusskilometer an einem Zeitpunkt)
#print data[1] #jeweils eine Zeile ohne Datum (Verlauf entlang Flusskilometer an einem Zeitpunkt)
#print len(data)

#min = [min(data[:]) for i in data]
#max = max(data)
#print 'max=', max
#print 'min=', min
#min = min(thedata[1][1:])
#min = min(i[1] for i in thedata)
#mean = np.mean(data)
#median = np.median(data)
#std = np.std(data)
#rmse = rmse(thedata)
#print 'mean=', mean
#print 'median=', median
#print 'stdev=', std
quit()

print thedata[0]

date_time = [i[0] for i in thedata] # Datum
x1 = [i[1] for i in thedata] # km 89
x2 = [i[2] for i in thedata] # km 88.5
rd = [i[41] for i in thedata] # km 69
oo = [i[49] for i in thedata] # km 65
uo = [i[54] for i in thedata] # km 62.5
uw = [i[57] for i in thedata] # km 61
j4 = [i[76] for i in thedata] # km 51.5

fig = plt.figure()
#ax = fig.add_subplot(221)
#subplot(121)
#boxplot(thedata[1][1:])
#subplot(122)
#hist(thedata[1][1:])
#fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/origC_m_Conv.png')
#show()




