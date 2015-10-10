from Hs_scripts import hs_loader

__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
#import matplotlib as mpl

filename1 = "/home/lnx/PycharmProjects/HS/049/outputfiles_origConv_elevcorr_incacloud_start89_masstransfer_2/Temp_H2O.txt"
name, header, thedata = hs_loader.loadfile(filename=filename1)
data = np.array(thedata)
studyregion = [i[31:76] for i in data]        #cuts km 74 - 51.5  (for start from km 89)
OMI = studyregion[777:944]     #cuts 2.8.2013 0h - 9.8.2013 2013h (for start from 1.7.2013 0h)
WTmin = min(min(i) for i in OMI)
WTmax = max(max(j) for j in OMI)
WTstd = np.std(OMI)
listedOMI = []
for i in OMI:
    for j in i:
        listedOMI.append(j)
WTmean = np.average(listedOMI)
print "WTmin(OMI)=", WTmin, "WTmax(OMI)=", WTmax, "WTmean(OMI)=", WTmean, "WTstd(OMI)=", WTstd

filename1 = "/home/lnx/PycharmProjects/HS/049/outputfiles_origConv_elevcorr_incacloud_start89_masstransfer_2/Heat_Conv.txt"
name, header, thedata = hs_loader.loadfile(filename=filename1)
data = np.array(thedata)
studyregion = [i[31:76] for i in data]        #cuts km 74 - 51.5  (for start from km 89)
OMI = studyregion[777:944]     #cuts 2.8.2013 0h - 9.8.2013 2013h (for start from 1.7.2013 0h)
Cvmin = min(min(i) for i in OMI)
Cvmax = max(max(j) for j in OMI)
Cvstd = np.std(OMI)
listedOMI = []
for i in OMI:
    for j in i:
        listedOMI.append(j)
Cvmean = np.average(listedOMI)
print "Cvmin(OMI)=", Cvmin, "Cvmax(OMI)=", Cvmax, "Cvmean(OMI)=", Cvmean, "Cvstd(OMI)=", Cvstd

filename1 = "/home/lnx/PycharmProjects/HS/049/outputfiles_origConv_elevcorr_incacloud_start89_masstransfer_2/Heat_Cond.txt"
name, header, thedata = hs_loader.loadfile(filename=filename1)
data = np.array(thedata)
studyregion = [i[31:76] for i in data]        #cuts km 74 - 51.5  (for start from km 89)
OMI = studyregion[777:944]     #cuts 2.8.2013 0h - 9.8.2013 2013h (for start from 1.7.2013 0h)
Cdmin = min(min(i) for i in OMI)
Cdmax = max(max(j) for j in OMI)
Cdstd = np.std(OMI)
listedOMI = []
for i in OMI:
    for j in i:
        listedOMI.append(j)
Cdmean = np.average(listedOMI)
print "Cdmin(OMI)=", Cdmin, "Cdmax(OMI)=", Cdmax, "Cdmean(OMI)=", Cdmean, "Cdstd(OMI)=", Cdstd

filename1 = "/home/lnx/PycharmProjects/HS/049/outputfiles_origConv_elevcorr_incacloud_start89_masstransfer_2/Heat_Evap.txt"
name, header, thedata = hs_loader.loadfile(filename=filename1)
data = np.array(thedata)
studyregion = [i[31:76] for i in data]        #cuts km 74 - 51.5  (for start from km 89)
OMI = studyregion[777:944]     #cuts 2.8.2013 0h - 9.8.2013 2013h (for start from 1.7.2013 0h)
Evmin = min(min(i) for i in OMI)
Evmax = max(max(j) for j in OMI)
Evstd = np.std(OMI)
listedOMI = []
for i in OMI:
    for j in i:
        listedOMI.append(j)
Evmean = np.average(listedOMI)
print "Evmin(OMI)=", Evmin, "Evmax(OMI)=", Evmax, "Evmean(OMI)=", Evmean, "Evstd(OMI)=", Evstd

filename1 = "/home/lnx/PycharmProjects/HS/049/outputfiles_origConv_elevcorr_incacloud_start89_masstransfer_2/Heat_TR.txt"
name, header, thedata = hs_loader.loadfile(filename=filename1)
data = np.array(thedata)
studyregion= [i[31:76] for i in data]        #cuts km 74 - 51.5  (for start from km 89)
OMI = studyregion[777:944]     #cuts 2.8.2013 0h - 9.8.2013 2013h (for start from 1.7.2013 0h)
Lwmin = min(min(i) for i in OMI)
Lwmax = max(max(j) for j in OMI)
Lwstd = np.std(OMI)
listedOMI = []
for i in OMI:
    for j in i:
        listedOMI.append(j)
Lwmean = np.average(listedOMI)
print "Lwmin(OMI)=", Lwmin, "Lwmax(OMI)=", Lwmax, "Lwmean(OMI)=", Lwmean, "Lwstd(OMI)=", Lwstd

filename1 = "/home/lnx/PycharmProjects/HS/049/outputfiles_origConv_elevcorr_incacloud_start89_masstransfer_2/Heat_SR6.txt"
name, header, thedata = hs_loader.loadfile(filename=filename1)
data = np.array(thedata)
studyregion = [i[31:76] for i in data]        #cuts km 74 - 51.5  (for start from km 89)
OMI = studyregion[777:944]     #cuts 2.8.2013 0h - 9.8.2013 2013h (for start from 1.7.2013 0h)
SR6min = min(min(i) for i in OMI)
SR6max = max(max(j) for j in OMI)
SR6std = np.std(OMI)
listedOMI = []
for i in OMI:
    for j in i:
        listedOMI.append(j)
SR6mean = np.average(listedOMI)
print "SR6min(OMI)=", SR6min, "SR6max(OMI)=", SR6max, "SR6mean(OMI)=", SR6mean, "SR6std(OMI)=", SR6std


filename1 = "/home/lnx/PycharmProjects/HS/049/outputfiles_origConv_elevcorr_incacloud_start89_penman_2/Heat_Conv.txt"
name, header, thedata = hs_loader.loadfile(filename=filename1)
data = np.array(thedata)
studyregion = [i[31:76] for i in data]        #cuts km 74 - 51.5  (for start from km 89)
OMI = studyregion[777:944]     #cuts 2.8.2013 0h - 9.8.2013 2013h (for start from 1.7.2013 0h)
Cvmin_p2 = min(min(i) for i in OMI)
Cvmax_p2 = max(max(j) for j in OMI)
Cvstd_p2 = np.std(OMI)
listedOMI = []
for i in OMI:
    for j in i:
        listedOMI.append(j)
Cvmean_p2 = np.average(listedOMI)
print "Cvmin_p2(OMI)=", Cvmin_p2, "Cvmax_p2(OMI)=", Cvmax_p2, "Cvmean_p2(OMI)=", Cvmean_p2, "Cvstd_p2(OMI)=", Cvstd_p2

filename1 = "/home/lnx/PycharmProjects/HS/049/outputfiles_origConv_elevcorr_incacloud_start89_penman_2/Heat_Cond.txt"
name, header, thedata = hs_loader.loadfile(filename=filename1)
data = np.array(thedata)
studyregion = [i[31:76] for i in data]        #cuts km 74 - 51.5  (for start from km 89)
OMI = studyregion[777:944]     #cuts 2.8.2013 0h - 9.8.2013 2013h (for start from 1.7.2013 0h)
Cdmin_p2 = min(min(i) for i in OMI)
Cdmax_p2 = max(max(j) for j in OMI)
Cdstd_p2 = np.std(OMI)
listedOMI = []
for i in OMI:
    for j in i:
        listedOMI.append(j)
Cdmean_p2 = np.average(listedOMI)
print "Cdmin_p2(OMI)=", Cdmin_p2, "Cdmax_p2(OMI)=", Cdmax_p2, "Cdmean(OMI)=", Cdmean_p2, "Cdstd(OMI)=", Cdstd_p2

filename1 = "/home/lnx/PycharmProjects/HS/049/outputfiles_origConv_elevcorr_incacloud_start89_penman_2/Heat_Evap.txt"
name, header, thedata = hs_loader.loadfile(filename=filename1)
data = np.array(thedata)
studyregion = [i[31:76] for i in data]        #cuts km 74 - 51.5  (for start from km 89)
OMI = studyregion[777:944]     #cuts 2.8.2013 0h - 9.8.2013 2013h (for start from 1.7.2013 0h)
Evmin_p2 = min(min(i) for i in OMI)
Evmax_p2 = max(max(j) for j in OMI)
Evstd_p2 = np.std(OMI)
listedOMI = []
for i in OMI:
    for j in i:
        listedOMI.append(j)
Evmean_p2 = np.average(listedOMI)
print "P2 Evmin(OMI)=", Evmin_p2, "Evmax(OMI)=", Evmax_p2, "Evmean(OMI)=", Evmean_p2, "Evstd(OMI)=", Evstd_p2

filename1 = "/home/lnx/PycharmProjects/HS/049/outputfiles_origConv_elevcorr_incacloud_start89_penman_2/Heat_TR.txt"
name, header, thedata = hs_loader.loadfile(filename=filename1)
data = np.array(thedata)
studyregion= [i[31:76] for i in data]        #cuts km 74 - 51.5  (for start from km 89)
OMI = studyregion[777:944]     #cuts 2.8.2013 0h - 9.8.2013 2013h (for start from 1.7.2013 0h)
Lwmin_p2 = min(min(i) for i in OMI)
Lwmax_p2 = max(max(j) for j in OMI)
Lwstd_p2 = np.std(OMI)
listedOMI = []
for i in OMI:
    for j in i:
        listedOMI.append(j)
Lwmean_p2 = np.average(listedOMI)
print "P2 Lwmin(OMI)=", Lwmin_p2, "Lwmax(OMI)=", Lwmax_p2, "Lwmean(OMI)=", Lwmean_p2, "Lwstd(OMI)=", Lwstd_p2

filename1 = "/home/lnx/PycharmProjects/HS/049/outputfiles_origConv_elevcorr_incacloud_start89_penman_2/Heat_SR6.txt"
name, header, thedata = hs_loader.loadfile(filename=filename1)
data = np.array(thedata)
studyregion = [i[31:76] for i in data]        #cuts km 74 - 51.5  (for start from km 89)
OMI = studyregion[777:944]     #cuts 2.8.2013 0h - 9.8.2013 2013h (for start from 1.7.2013 0h)
SR6min_p2 = min(min(i) for i in OMI)
SR6max_p2 = max(max(j) for j in OMI)
SR6std_p2 = np.std(OMI)
listedOMI = []
for i in OMI:
    for j in i:
        listedOMI.append(j)
SR6mean_p2 = np.average(listedOMI)
print "P2 SR6min(OMI)=", SR6min_p2, "SR6max(OMI)=", SR6max_p2, "SR6mean(OMI)=", SR6mean_p2, "SR6std(OMI)=", SR6std_p2

filename1 = "/home/lnx/PycharmProjects/HS/049_P500_hourlyinflowdata_alongAusleitung_evapPenman/outputfiles/Heat_Conv.txt"
name, header, thedata = hs_loader.loadfile(filename=filename1)
data = np.array(thedata)
studyregion = [i[31:76] for i in data]        #cuts km 74 - 51.5  (for start from km 89)
OMI = studyregion[777:944]     #cuts 2.8.2013 0h - 9.8.2013 2013h (for start from 1.7.2013 0h)
Cvmin_p = min(min(i) for i in OMI)
Cvmax_p = max(max(j) for j in OMI)
Cvstd_p = np.std(OMI)
listedOMI = []
for i in OMI:
    for j in i:
        listedOMI.append(j)
Cvmean_p = np.average(listedOMI)
print "submitted: Cvmin(OMI)=", Cvmin_p, "Cvmax(OMI)=", Cvmax_p, "Cvmean(OMI)=", Cvmean_p, "Cvstd(OMI)=", Cvstd_p

filename1 = "/home/lnx/PycharmProjects/HS/049_P500_hourlyinflowdata_alongAusleitung_evapPenman/outputfiles/Heat_Cond.txt"
name, header, thedata = hs_loader.loadfile(filename=filename1)
data = np.array(thedata)
studyregion = [i[31:76] for i in data]        #cuts km 74 - 51.5  (for start from km 89)
OMI = studyregion[777:944]     #cuts 2.8.2013 0h - 9.8.2013 2013h (for start from 1.7.2013 0h)
Cdmin_p = min(min(i) for i in OMI)
Cdmax_p = max(max(j) for j in OMI)
Cdstd_p = np.std(OMI)
listedOMI = []
for i in OMI:
    for j in i:
        listedOMI.append(j)
Cdmean_p = np.average(listedOMI)
print "Submitted: Cdmin(OMI)=", Cdmin_p, "Cdmax(OMI)=", Cdmax_p, "Cdmean(OMI)=", Cdmean_p, "Cdstd(OMI)=", Cdstd_p

filename1 = "/home/lnx/PycharmProjects/HS/049_P500_hourlyinflowdata_alongAusleitung_evapPenman/outputfiles/Heat_Evap.txt"
name, header, thedata = hs_loader.loadfile(filename=filename1)
data = np.array(thedata)
studyregion = [i[31:76] for i in data]        #cuts km 74 - 51.5  (for start from km 89)
OMI = studyregion[777:944]     #cuts 2.8.2013 0h - 9.8.2013 2013h (for start from 1.7.2013 0h)
Evmin_p = min(min(i) for i in OMI)
Evmax_p = max(max(j) for j in OMI)
Evstd_p = np.std(OMI)
listedOMI = []
for i in OMI:
    for j in i:
        listedOMI.append(j)
Evmean_p = np.average(listedOMI)
print "Submitted Evmin(OMI)=", Evmin_p, "Evmax(OMI)=", Evmax_p, "Evmean(OMI)=", Evmean_p, "Evstd(OMI)=", Evstd_p

filename1 = "/home/lnx/PycharmProjects/HS/049_P500_hourlyinflowdata_alongAusleitung_evapPenman/outputfiles/Heat_TR.txt"
name, header, thedata = hs_loader.loadfile(filename=filename1)
data = np.array(thedata)
studyregion= [i[31:76] for i in data]        #cuts km 74 - 51.5  (for start from km 89)
OMI = studyregion[777:944]     #cuts 2.8.2013 0h - 9.8.2013 2013h (for start from 1.7.2013 0h)
Lwmin_p = min(min(i) for i in OMI)
Lwmax_p = max(max(j) for j in OMI)
Lwstd_p = np.std(OMI)
listedOMI = []
for i in OMI:
    for j in i:
        listedOMI.append(j)
Lwmean_p = np.average(listedOMI)
print "Submitted Lwmin(OMI)=", Lwmin_p, "Lwmax(OMI)=", Lwmax_p, "Lwmean(OMI)=", Lwmean_p, "Lwstd(OMI)=", Lwstd_p

filename1 = "/home/lnx/PycharmProjects/HS/049_P500_hourlyinflowdata_alongAusleitung_evapPenman/outputfiles/Heat_SR6.txt"
name, header, thedata = hs_loader.loadfile(filename=filename1)
data = np.array(thedata)
studyregion = [i[31:76] for i in data]        #cuts km 74 - 51.5  (for start from km 89)
OMI = studyregion[777:944]     #cuts 2.8.2013 0h - 9.8.2013 2013h (for start from 1.7.2013 0h)
SR6min_p = min(min(i) for i in OMI)
SR6max_p = max(max(j) for j in OMI)
SR6std_p = np.std(OMI)
listedOMI = []
for i in OMI:
    for j in i:
        listedOMI.append(j)
SR6mean_p = np.average(listedOMI)
print "Submitted SR6min(OMI)=", SR6min_p, "SR6max(OMI)=", SR6max_p, "SR6mean(OMI)=", SR6mean_p, "SR6std(OMI)=", SR6std_p

x_mt_new = [1,2,3,4,5]
y_mt_new = [Cdmean, Cvmean, Evmean, Lwmean, SR6mean]
y_p_new = [Cdmean_p2, Cvmean_p2, Evmean_p2, Lwmean_p2, SR6mean_p2]
y_p_submit = [Cdmean_p, Cvmean_p, Evmean_p, Lwmean_p, SR6mean_p]

#pm_orig =
#pm_new =

fig = plt.figure()

plt.bar(x_mt_new, y_mt_new, color='red', lw=0.5, label='mt_new')
plt.title('Cv,Cd,Ev,Lw,SR6, OMI, Pinka,(origConv,masstransfer)')
fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/Chart_Heatfluxes_Masstransfer_new.png')

fig = plt.figure()

plt.bar(x_mt_new, y_p_new, color='green', lw=0.5, label='p_new')
plt.title('Cv,Cd,Ev,Lw,SR6, OMI, Pinka,(origConv,penman 2)')
fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/Chart_Heatfluxes_Penman_new.png')


fig = plt.figure()

plt.bar(x_mt_new, y_p_submit, color='blue', lw=0.5, label='p_submitted')
plt.title('Cv,Cd,Ev,Lw,SR6, OMI, Pinka,(origConv,penman submitted)')
fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/Chart_Heatfluxes_Submitted_p.png')

#plt.xlabel('time[h]')
#plt.xlabel('min','max','mean','std')
#plt.legend()

plt.show()