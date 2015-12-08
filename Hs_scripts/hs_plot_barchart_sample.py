from Hs_scripts import hs_loader

__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
#import matplotlib as mpl

filename1 = "/home/lnx/PycharmProjects/HS/049/outputfiles_origConv_elevcorr_incacloud_start89_masstransfer_2/Temp_H2O.txt"
name, header, thedata = hs_loader.loadfile(filename=filename1)

data = np.array(thedata)
#print data[0]

#extract data of study time and region
#studyregion = [i[39:84] for i in data]       #cuts km 74 - 51.5  (for start from km 93)
studyregion = [i[31:76] for i in data]        #cuts km 74 - 51.5  (for start from km 89)
print studyregion[0]
print studyregion[777]
#OMI = studyregion[177:344]     #cuts 2.8.2013 0h - 9.8.2013 2013h (for start from 26.7.2013 0h)
OMI = studyregion[777:944]     #cuts 2.8.2013 0h - 9.8.2013 2013h (for start from 1.7.2013 0h)
#print OMI[0]
min = min(min(i) for i in OMI)
max = max(max(j) for j in OMI)
std = np.std(OMI)
listedOMI = []       #splitlistcomp = [i.split() for i in data]
for i in OMI:
    for j in i:
        listedOMI.append(j)
print listedOMI
print type(listedOMI)
mean = np.average(listedOMI)
print "min(OMI)=", min, "max(OMI)=", max, "mean(OMI)=", mean, "std(OMI)=", std
print "time steps (len(OMI)):", len(OMI) #should be 167
print "longitudinal steps (len(OMI[0])):", len(OMI[0]) #should be 45
print "number of data entries (len(listedOMI)):",len(listedOMI) #should be 7515

x_mt_new = [1,2,3,4]
y_mt_new = [min,max,mean,std]
#pm_orig =
#pm_new =

fig = plt.figure()

plt.bar(x_mt_new, y_mt_new, color='red', lw=0.5, label='mt_new')

#plt.xlabel('time[h]')
plt.xlabel('min','max','mean','std')
plt.legend()

#fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/UW_Validation_OrigConv_m.png')
plt.show()

