from Hs_scripts import hs_loader

__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import math
import csv

def loadfile2(filename):
    with open(filename,"r") as f:    #Einlesen des Files in eine Liste
        alldata = f.readlines()

    name = alldata[1]
    header = alldata[7] #Liste mit Flusskilometern - Distance from Mouth
    data = alldata[7:]  #Liste ab 8.Zeile der alten Liste - Beginn der Rohdaten

    splitdata = []       #splitlistcomp = [i.split() for i in data]
    for i in data:
        splitdata.append(i.split())  #Splitten der Listenelemente   split(":")  Seperator ":"

    return name, header, splitdata

#filename1 = "/home/lnx/PycharmProjects/HS/049/outputfiles_origConv_elevcorr_incacloud_start89_masstransfer_2/Temp_H2O.txt" #incacloud, sed 0.1m
#filename1 = "/home/lnx/PycharmProjects/HS/300_P500_STQ_2013_m/outputfiles/Temp_H2O.txt" # incacloud, sed5m
#filename1 = "/home/lnx/PycharmProjects/HS/299_P500_STQ_2013_m/outputfiles/Temp_H2O.txt" # incacloud, sed 5m allivium temp 10.5
#filename1 = "/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_m/outputfiles_fricvelEQwind/Temp_H2O.txt" # cloud const, sed5m
#filename1 = "/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_m/outputfiles_fricvelorig_sed1m/Temp_H2O.txt" # cloud const, sed5m
filename1 = "/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_m/outputfiles_fricvelWindVTS_sed1m/Temp_H2O.txt" # cloud const, sed5m

simname = []
simname = filename1[29:]


name, header, thedata = hs_loader.loadfile(filename=filename1)

date_time = [i[0] for i in thedata] # Datum
hbs = [i[1] for i in thedata] # km 89
tbs = [i[10] for i in thedata] # km 84.5
sds = [i[19] for i in thedata] # km 80
rds = [i[41] for i in thedata] # km 69
oos = [i[49] for i in thedata] # km 65
uos = [i[54] for i in thedata] # km 62.5
uws = [i[57] for i in thedata] # km 61
j1s = [i[68] for i in thedata] # km 55.5
j2s = [i[69] for i in thedata] # km 55
j3s = [i[70] for i in thedata] # km 54.5
j4s = [i[76] for i in thedata] # km 51.5
z1s = [i[85] for i in thedata] # km 47
z2s = [i[86] for i in thedata] # km 46.5
bds = [i[89] for i in thedata] # km 45
wds = [i[97] for i in thedata] # km 41
bgs = [i[103] for i in thedata] # km 38

#filename2 = "/home/lnx/2_Documents/_BioClic/_Simulationen/Measurements_1.csv" #1 July 2013 - 29 August 2013
filename2 = "/home/lnx/2_Documents/_BioClic/_Simulationen/Measurements_20130725_0809_corr.csv"
name2, header2, thedata2 = loadfile2(filename=filename2)

hb = [float(i[1]) for i in thedata2] # km 89
tb = [float(i[2]) for i in thedata2] # km 84.5
sd = [float(i[3]) for i in thedata2] # km 80
rd = [float(i[4]) for i in thedata2] # km 69
oo = [float(i[5]) for i in thedata2] # km 65
uo = [float(i[6]) for i in thedata2] # km 62.5
uw = [float(i[7]) for i in thedata2] # km 61
j1 = [float(i[8]) for i in thedata2] # km 55.5
j2 = [float(i[9]) for i in thedata2] # km 55
j3 = [float(i[10]) for i in thedata2] # km 54.5
j4 = [float(i[11]) for i in thedata2] # km 51.5
z1 = [float(i[12]) for i in thedata2] # km 47
z2 = [float(i[13]) for i in thedata2] # km 46.5
bd = [float(i[14]) for i in thedata2] # km 45
wd = [float(i[15]) for i in thedata2] # km 41
bg = [float(i[16]) for i in thedata2] # km 38

#list of tuples with all 16 stations:
stations_all = [(hb,hbs),(tb,tbs),(sd,sds),(rd,rds),(oo,oos),(uo,uos),(uw,uws),(j1,j1s),(j2,j2s),(j3,j3s),(j4,j4s),(z1,z1s),(z2,z2s),(bd,bds),(wd,wds),(bg,bgs)]
stations = [(hb,hbs),(tb,tbs),(sd,sds),(rd,rds),(oo,oos),(uo,uos),(uw,uws),(j3,j3s),(j4,j4s),(z2,z2s),(wd,wds),(bg,bgs)]#stations with missing data removed

stations_names_all = ['hb','tb','sd','rd','oo','uo','uw','j1','j2','j3','j4','z1','z2','bd','wd','bg']
stations_names = ['hb','tb','sd','rd','oo','uo','uw','j3','j4','z2','wd','bg']


x = np.arange(0,len(date_time),1)
y = np.arange(0,len(stations),1)

f = open("/home/lnx/2_Documents/_BioClic/_Simulationen/Output_298_sed1m_fricvWindVTS.txt",'w')
f.write(filename1)

for i in y:

    rmse = []
    for j in x:
        rmse.append(((stations[i][0][j]-stations[i][1][j])**2)**0.5)
        #print 'i=', i, 'j=', j, 'rmse=', rmse
    rmse_m = 0
    for j in x:
        rmse_m = rmse_m + rmse[j]
    rmse_m = rmse_m/(len(rmse))
    print stations_names[i]
    print 'rmse:', rmse_m
    f.write('\n')
    f.write(str(stations_names[i]))
    f.write('\nrmse:')
    f.write(str(rmse_m))

    slope, intercept, r_value, p_value, std_err = linregress(stations[i][0],stations[i][1])
    print 'r_value:', r_value       # correlation coefficient
    print 'r-squared:', r_value**2  #coefficient of determination
    f.write('\nr_value:')
    f.write(str(r_value))       # correlation coefficient
    f.write('\nr-squared:')
    f.write(str(r_value**2))  #coefficient of determination
    f.write('\n')

    #min/max/amplitude/mean of whole period
    min_m = min(stations[i][0])
    min_s = min(stations[i][1])
    max_m = max(stations[i][0])
    max_s = max(stations[i][0])
    amp_m = max_m - min_m
    amp_s = max_s - min_s
    mean_m = np.mean(stations[i][0])
    mean_s = np.mean(stations[i][1])

    #if abs(amp_m - amp_s) > 1: print "amplitudes m, s:", amp_m, amp_s
    if abs(min_m - min_s) > 1: print "min m, s:", min_m, min_s
    if abs(max_m - max_s) > 1: print "max m, s:", max_m, max_s
    if abs(mean_m - mean_s) > 1: print "mean m, s:", mean_m, mean_s
    print "\n"

    #"gleitendes" min/max?
    for j in x:
        min_m = min(stations[i][0][j:j+23])
        print min_m

    #daily mean

    # x ...number of hours, d = x/24 ... days

    d = np.arange(0,len(date_time)/24,1)

    for j in x:
        for k in d:
            min_m = min(stations[i][0][k])



# slope, intercept, r_value, p_value, std_err = linregress(uws,uw)
# print 'r_value:', r_value       # correlation coefficient
# print "r-squared:", r_value**2  #coefficient of determination

#slope : float   - slope of the regression line
#intercept : float - intercept of the regression line
#r-value : float -correlation coefficient
#p-value : float -two-sided p-value for a hypothesis test whose null hypothesis is that the slope is zero
#stderr : float -Standard error of the estimate

fig = plt.figure()
plt.title(simname)
plt.plot(date_time, uos, color='red', lw=0.5, label='uo_s')
plt.plot(date_time, uo, color='blue', lw=0.5, label='uo_m')
#plt.plot(date_time, rmse_uw, color='black', lw=0.5, label='rmse_uw')


fig.autofmt_xdate()
plt.xlabel('time[h]')
plt.ylabel('water temperature [degC]')
plt.legend()

fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/UO_Validation_OrigConv_m_298_sed1m_FricvelWindVTS.png')
plt.show()