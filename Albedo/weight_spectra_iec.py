# -*- coding: utf-8 -*-
import os, csv
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
#import plotly.plotly as py  # tools to communicate with Plotly's server

directory = "D:/_URBANIA/METDATA/GerhardPeharz_Johanneum/2_raw"
#http://rredc.nrel.gov/solar/spectra/am1.5/astmg173/astmg173.html
#0 Wvlgth nm
#1 Etr W*m-2*nm-1  Extraterrestrial Radiation (solar spectrum at TOA) at mean Earth Sun distance
#2 Global tilt  W*m-2*nm-1  Spectral radiation from solar disk plus sky diffuse and diffuse reflected from ground on south facing surface tilted 37deg from horizontal
#3 Direct+circumsolar W*m-2*nm-1  Direct=Direct Normal Irradiance Nearly parallel (0.5 deg divergent cone) radiation on surface with surface normal tracking (pointing to) the sun, excluding scattered sky and reflected ground radiation
#Circumsolar=Spectral irradiance within +/- 2.5 degree (5 degree diameter) field of view centered on the 0.5 deg diameter solar disk, but excluding the radiation from the disk
#
#
#spec = "ASTMG173_2.csv"
spec = "IECNorm 60904-3/82_1071e_FDIS.xlsx"

mea1 = "2017_04_21_Reflexion_Betonproben.txt"
mea2_diff = "2017_05_26_Betonproben_R_DIFF.txt"
mea2_tis = "2017_05_26_Betonproben_R_TIS.txt" #TIS = total integrated sphere
meas1 = os.path.join(directory, mea1)
meas2_diff = os.path.join(directory, mea2_diff)
meas2_tis = os.path.join(directory, mea2_tis)

spectrum = os.path.join(directory, spec)
#Spec1 = pd.read_csv(spectrum, skiprows=1,index_col=0) #delta 0.5 nm

Spec2 = pd.read_excel(spectrum, sheetname="Sheet1", skiprows=2)#, header=2, skip_footer=0, index_col=None, names=None, parse_cols=None, parse_dates=False, date_parser=None, na_values=None, thousands=None, convert_float=True, has_index_names=None, converters=None, dtype=None, true_values=None, false_values=None, engine=None, squeeze=False, **kwds)[source]
#print Spec2.ix[1] #first row
#print Spec2.iloc[:, 0] #nanometer
#print Spec2.iloc[:, 1] #global spectral irradiance

#print 280%10
#print 280.5%10
#print Spec2.iloc[:,1].size #2007

Spec2_10nm = pd.DataFrame(index=range(280,4010,10),columns=["Wm2"])
Spec2_10nm = Spec2_10nm.fillna(0)
#print Spec2_10nm
n = Spec2.iloc[:,0].size
m = Spec2_10nm.iloc[:,0].size
#print n,m
#print Spec2_10nm.iloc[:,0].head()

#print 2002, Spec2.iloc[2002,0], Spec2.iloc[2002,1] #"yes"

j=0
for i in range(0,n-5): #last five lines contain comments!
    if Spec2.iloc[i,0]%10 == 0:
        #print i, Spec2.iloc[i,0], Spec2.iloc[i,1] #"yes"
        #j = Spec2.iloc[i,0]
        Spec2_10nm.iloc[j,0] = Spec2.iloc[i,1]
        j+=1
    else:
        pass #print "no"
    #print j

Spec2_cut = Spec2_10nm[2:223] #measurements only available from 300 to 2500 nanometer, therefore cut spectrum
#print Spec2_cut

#print Spec2_10nm.head()
#print Spec2_10nm.iloc[:,0].size

Meas1 = pd.read_csv(meas1, delimiter='\t', index_col=0) #delta 10nm
#print Meas1 #MV4_03 [%]  MV4_02 [%]  MV4_01 [%]  MV3_03 [%]  MV3_02 [%]
                   # MV3_01 [%]  MV2_02 [%]  MV2_01 [%]  MV1_02 [%]  MV1_01 [%]
Meas2_diff = pd.read_csv(meas2_diff, delimiter='\t', index_col=0) #delta 5nm
Meas2_diff_d10nm = Meas2_diff.iloc[::2, :]
Meas2_diff_d10nm2 = Meas2_diff_d10nm.sort_index(ascending=True)#)
#print Meas2_diff_d10nm2
 #MV1_02_Oberseite DIFF  MV2_01_Oberseite DIFF  MV2_02_Oberseite DIFF
 #MV3_01_Oberseite DIFF  MV3_03_Oberseite DIFF  MV4_01_Oberseite DIFF
 #MV4_03_Oberseite DIFF
Meas2_tis = pd.read_csv(meas2_tis, delimiter='\t', index_col=0) #delta 5nm
Meas2_tis_d10nm = Meas2_tis.iloc[::2, :]
Meas2_tis_d10nm2 = Meas2_tis_d10nm.sort_index(ascending=True)#)

#print Meas2_diff_d10nm2
#Meas1_w = Meas1[:,:] * Spec1.iloc[:,2]
#print Meas1.head()
#print Meas1.iloc[:,1].head() #MV4_02 (2te Spate)
#print Spec1.head()
#print Spec1.iloc[:,2].head() #dircirc

#print Meas1.head()

#exit()
#print Meas2_tis_d10nm.head()

wavel = range(300,2510,10)
#print len(wavel)
#print len(Spec1)
#print len(Meas2_tis_d10nm)

"""
fig = plt.figure()
plt.title("ASTM G-173 Reference")
plt.plot(wavel,Spec1.iloc[:,0],label="extraterr")
plt.plot(wavel,Spec1.iloc[:,1],label="globaltilt")
plt.plot(wavel,Spec1.iloc[:,2],label="direct+circum")
plt.ylabel(u" Spectral Irradiance [W/m²/nm]")
plt.xlabel("wavelength [nm]")
plt.legend()
plt.show()


fig = plt.figure()

major_ticks = np.arange(300, 2500, 100)
minor_ticks = np.arange(300, 2500, 50)

ax1 = fig.add_subplot(511)
ax1.set_title("Gehwege, TIS")
ax1.plot(wavel,Meas2_tis_d10nm.iloc[:,0],label="MV1_2 2 Normalbeton, Besenstrich")
ax1.plot(wavel,Meas2_tis_d10nm.iloc[:,1],label="MV2_1 2 Normalbeton hell, Besenstrich")
ax1.set_xticks(major_ticks)
ax1.set_xticks(minor_ticks, minor=True)
ax1.grid(which='both', color='black', linestyle=':')
ax1.get_xaxis().set_ticklabels([])
ax1.set_ylim(0,100)
ax1.legend()

#Meas2_tis.iloc[:,0].plot()
ax2 = fig.add_subplot(512, sharex=ax1)
ax2.set_title(u"nicht befahrbare Betonfläche, TIS")
ax2.plot(wavel,Meas1.iloc[:,9],label="MVI_01_1 Normalbeton, glatt abgezogen")
ax2.plot(wavel,Meas1.iloc[:,4],label=u"MV3_02_1 Straßenbeton, glatt abgezogen")
ax2.set_xticks(major_ticks)
ax2.set_xticks(minor_ticks, minor=True)
ax2.grid(which='both', color='black', linestyle=':')
ax2.get_xaxis().set_ticklabels([])
ax2.set_ylim(0,100)
ax2.legend()

ax3 = fig.add_subplot(513, sharex=ax1)
ax3.set_title("Sichtbetonmauer, TIS")
ax3.plot(wavel,Meas1.iloc[:,8],label=u"MV1_02_1 Normalbeton Schalfläche")
ax3.plot(wavel,Meas1.iloc[:,7],label=u"MV2_01_1 Normalbeton hell Schalfläche")
ax3.plot(wavel,Meas1.iloc[:,6],label=u"MV2_02_1 Normalbeton hell Schalfläche")
ax3.set_xticks(major_ticks)
ax3.set_xticks(minor_ticks, minor=True)
ax3.grid(which='both', color='black', linestyle=':')
ax3.get_xaxis().set_ticklabels([])
ax3.set_ylabel(u"albedo [%]")
ax3.set_ylim(0,100)
ax3.legend()

ax4 = fig.add_subplot(514, sharex=ax1)
ax4.set_title("Stasse niederangig, TIS")
ax4.plot(wavel,Meas2_tis_d10nm.iloc[:,3],label=u"MV3_01_2 Straßenbeton, Besenstrich")
ax4.plot(wavel,Meas2_tis_d10nm.iloc[:,5],label=u"MV4_01_2 Straßenbeton hell, Besenstrich")
ax4.set_xticks(major_ticks)
ax4.set_xticks(minor_ticks, minor=True)
ax4.grid(which='both', color='black', linestyle=':')
ax4.get_xaxis().set_ticklabels([])
ax4.set_ylim(0,100)
ax4.legend()

ax5 = fig.add_subplot(515)
ax5.set_title("Stasse hochrangig, TIS")
ax5.plot(wavel,Meas2_tis_d10nm.iloc[:,4],label=u"MV3_03_2 Straßenbeton, Waschbetonstruktur")
ax5.plot(wavel,Meas2_tis_d10nm.iloc[:,6],label=u"MV4_03_2 Straßenbeton, hell, Waschbetonstruktur")
ax5.set_xlabel("wavelength [nm]")
ax5.legend()
ax5.set_ylim(0,100)
ax5.set_xticks(major_ticks)
ax5.set_xticks(minor_ticks, minor=True)
ax5.grid(which='both', color='black', linestyle=':')
#ax5.get_xaxis().set_ticklabels()#ax5.grid(b=True, which='minor', color='r', linestyle=':')

plt.setp(ax1.get_xticklabels(), visible=True)
plt.show()
"""
#exit()

Meas1.loc[:,'302_w'] = (Meas1.iloc[:,4]/100) * Spec2_cut.iloc[:,0]
Meas1.loc[:,'202_w'] = (Meas1.iloc[:,6]/100) * Spec2_cut.iloc[:,0]
Meas1.loc[:,'201_w'] = (Meas1.iloc[:,7]/100) * Spec2_cut.iloc[:,0]
Meas1.loc[:,'102_w'] = (Meas1.iloc[:,8]/100) * Spec2_cut.iloc[:,0]
Meas1.loc[:,'101_w'] = (Meas1.iloc[:,9]/100) * Spec2_cut.iloc[:,0]

Meas2_tis_d10nm2.loc[:,'102_w'] = (Meas2_tis_d10nm2.iloc[:,0]/100) * Spec2_cut.iloc[:,0]
Meas2_tis_d10nm2.loc[:,'201_w'] = (Meas2_tis_d10nm2.iloc[:,1]/100) * Spec2_cut.iloc[:,0]
Meas2_tis_d10nm2.loc[:,'301_w'] = (Meas2_tis_d10nm2.iloc[:,3]/100) * Spec2_cut.iloc[:,0]
Meas2_tis_d10nm2.loc[:,'401_w'] = (Meas2_tis_d10nm2.iloc[:,5]/100) * Spec2_cut.iloc[:,0]
Meas2_tis_d10nm2.loc[:,'303_w'] = (Meas2_tis_d10nm2.iloc[:,4]/100) * Spec2_cut.iloc[:,0]
Meas2_tis_d10nm2.loc[:,'403_w'] = (Meas2_tis_d10nm2.iloc[:,6]/100) * Spec2_cut.iloc[:,0]

w102 = np.array(Meas2_tis_d10nm2.loc[:,'102_w'])
w201 = np.array(Meas2_tis_d10nm2.loc[:,'201_w'])
w301 = np.array(Meas2_tis_d10nm2.loc[:,'301_w'])
w401 = np.array(Meas2_tis_d10nm2.loc[:,'401_w'])
w303 = np.array(Meas2_tis_d10nm2.loc[:,'303_w'])
w403 = np.array(Meas2_tis_d10nm2.loc[:,'403_w'])

#INTERPOLATE
def Interpolate_10to1nm(a):
    interpolated_x = np.arange(300,2501,1)
    data_x = np.arange(300,2510,10)
    interp_1nm = np.interp(interpolated_x, data_x, a)
    return interp_1nm

a102_1nm = Interpolate_10to1nm(Meas2_tis_d10nm2.iloc[:,0]/100) #'102_w'
w102_1nm = Interpolate_10to1nm(w102) #'102_w'
total_irrad = Interpolate_10to1nm(Spec2_cut.iloc[:,0])
#print Meas2_tis_d10nm2.iloc[:,0]/100
#print w102_1nm

#INTEGRATED ALBEDO, IRRADIANCE
def IntegratedAlbedo(a):
    total_irrad_1nm = Interpolate_10to1nm(Spec2_cut.iloc[:,0])
    total_irrad_integrated = np.trapz(total_irrad_1nm)
    weighted_irrad_1nm = Interpolate_10to1nm(a)
    weighted_irrad_integrated = np.trapz(weighted_irrad_1nm)
    integratedalbedo = weighted_irrad_integrated/total_irrad_integrated
    return integratedalbedo

"""
#Version1
#for i in weighted:
#    print IntegratedAlbedo(i)

weight_label = {(u"Gehwege",u"Normalbeton, Besenstrich") : "Meas2_tis_d10nm2['102_w']",
                (u"Gehwege",u"Normalbeton hell, Besenstrich") : "Meas2_tis_d10nm2['201_w']",
                (u"nicht befahrbare Betonfäche",u"Normalbeton, glatt abgezogen"): "Meas1['101_w']",
                (u"nicht befahrbare Betonfäche",u"Straßenbeton, glatt abgezogen"): "Meas1['302_w']",
                (u"Sichtbetonmauer",u"Normalbeton Schalfläche, glatt abgezogen"): "Meas1['102_w']",
                (u"Sichtbetonmauer",u"Normalbeton hell, Schalfläche"): "Meas1['201_w']",
                (u"Sichtbetonmauer",u"Normalbeton hell, Schalfläche2"): "Meas1['202_w']",
                (u"Stasse niederangig",u"Straßenbeton, Besenstrich"): "Meas2_tis_d10nm2['301_w']",
                (u"Stasse niederangig",u"Straßenbeton hell, Besenstrich"): "Meas2_tis_d10nm2['401_w']",
                (u"Stasse hochrangig",u"Straßenbeton , Waschbetonstruktur"): "Meas2_tis_d10nm2['303_w']",
                (u"Stasse hochrangig",u"Straßenbeton hell, Waschbetonstruktur"): "Meas2_tis_d10nm2['403_w']"}
#Version2
#for i in weight_label.keys():
#    print len(weight_label[i]),i
"""

#Version3
weight_tuples = [((u"Gehwege",u"Normalbeton, Besenstrich"), Meas2_tis_d10nm2['102_w'],Meas2_tis_d10nm2.iloc[:,0]/100),
                ((u"Gehwege",u"Normalbeton hell, Besenstrich"), Meas2_tis_d10nm2['201_w'],Meas2_tis_d10nm2.iloc[:,1]/100),
                ((u"nicht befahrbare Betonfäche",u"Normalbeton, glatt abgezogen"), Meas1['101_w'],Meas1.iloc[:,9]/100),
                ((u"nicht befahrbare Betonfäche",u"Straßenbeton, glatt abgezogen"), Meas1['302_w'],Meas1.iloc[:,4]/100),
                ((u"Sichtbetonmauer",u"Normalbeton Schalfläche, glatt abgezogen"), Meas1['102_w'],Meas1.iloc[:,8]/100),
                ((u"Sichtbetonmauer",u"Normalbeton hell, Schalfläche"), Meas1['201_w'],Meas1.iloc[:,7]/100),
                ((u"Sichtbetonmauer",u"Normalbeton hell, Schalfläche2"), Meas1['202_w'],Meas1.iloc[:,6]/100),
                ((u"Stasse niederangig",u"Straßenbeton, Besenstrich"), Meas2_tis_d10nm2['301_w'], Meas2_tis_d10nm2.iloc[:,3]/100),
                ((u"Stasse niederangig",u"Straßenbeton hell, Besenstrich"), Meas2_tis_d10nm2['401_w'], Meas2_tis_d10nm2.iloc[:,5]/100),
                ((u"Stasse hochrangig",u"Straßenbeton , Waschbetonstruktur"), Meas2_tis_d10nm2['303_w'],Meas2_tis_d10nm2.iloc[:,4]/100),
                ((u"Stasse hochrangig",u"Straßenbeton hell, Waschbetonstruktur"), Meas2_tis_d10nm2['403_w'],Meas2_tis_d10nm2.iloc[:,6]/100)]


for i in weight_tuples:
    #print len(weight_label[i]),i
    print "integrated_albedo=",IntegratedAlbedo(i[1]), "mean_albedo=",np.mean(i[2]), i[0]

#http://www.intl-light.com/handbookthanks.html - Referenzen in "OSA Handbook of Optics"
lambda_day = [(380,0.000039), (390, 0.000120), (400, 0.000396), (410, 0.001210),(420, 0.004000),
    (430,     0.011600),    (440,     0.023000),    (450,     0.038000),    (460,     0.060000),
    (470,     0.090980),    (480,     0.139020),    (490,     0.208020),    (500,     0.323000),
    (507,     0.444310),    (510,     0.503000),    (520,     0.710000),    (530,     0.862000),
    (540,     0.954000),    (550,     0.994950),    (555,     1.000000),    (560,     0.995000),
    (570,     0.952000),    (580,     0.870000),    (590,     0.757000),    (600,     0.631000),
    (620,     0.381000),    (630,     0.265000),    (640,     0.175000),    (650,     0.107000),
    (660,     0.061000),    (670,     0.032000),    (680,     0.017000),    (690,     0.008210),
    (700,     0.004102),    (710,    0.002091),    (720,     0.001047),    (730,     0.000520),
    (740,    0.000249),    (750,     0.000120),    (760,    0.000060),    (770,     0.000030)]



def Eye_response(a):
    Spec3_cut = Spec2_10nm[10:50] #measurements only available from 380 to 770 nanometer, therefore cut spectrum
    data_x2 = np.arange(380,780,10)
    #print Spec3_cut, data_x2
    #a = Meas2_tis_d10nm2.iloc[:,0]/100
    a_cut = a[8:48]
    #print a_cut
    response = lambda_day ...
    return response



"""
print 'mean albedo: 102_w', np.mean(a102_1nm)
#print '102_w', np.mean(Meas2_tis_d10nm2.iloc[:,0]/100)
print 'integrated albedo: 102_w', np.trapz(a102_1nm)
print 'integrated irradiance: 102_w', np.trapz(w102_1nm)
print 'integrated irradiance: total', np.trapz(total_irrad)
print 'integrated albedo?: 102,w ',  np.trapz(w102_1nm)/np.trapz(total_irrad)
"""


exit()

print "w102","w201","w301","w401","w303","w403"
print np.sum(w102),np.sum(w201),np.sum(w301),np.sum(w401),np.sum(w303),np.sum(w403)
#35.3003391714 51.711945565 42.0302815228 53.4509034006 25.1831214938 34.3731590275
print np.sum(w102[8:46])*10,np.sum(w201[8:46])*10,np.sum(w301[8:46])*10,np.sum(w401[8:46])*10,np.sum(w303[8:46])*10,np.sum(w403[8:46])*10 #visible: 380-750nm
print np.sum(w102[8:15])*10,np.sum(w201[8:15])*10,np.sum(w301[8:15])*10,np.sum(w401[8:15])*10,np.sum(w303[8:15])*10,np.sum(w403[8:15])*10 #violet: 380 - 450nm
print np.sum(w102[15:19])*10,np.sum(w201[15:19])*10,np.sum(w301[15:19])*10,np.sum(w401[15:19])*10,np.sum(w303[15:19])*10,np.sum(w403[15:19])*10 #blue: 450 - 495nm
print np.sum(w102[20:27])*10,np.sum(w201[20:27])*10,np.sum(w301[20:27])*10,np.sum(w401[20:27])*10,np.sum(w303[20:27])*10,np.sum(w403[20:27])*10 #green: 495 - 570nm
print np.sum(w102[27:29])*10,np.sum(w201[27:29])*10*10,np.sum(w301[27:29])*10,np.sum(w401[27:29])*10,np.sum(w303[27:29])*10,np.sum(w403[27:29])*10 #yellow: 570 - 590nm
print np.sum(w102[29:32])*10,np.sum(w201[29:32])*10,np.sum(w301[29:32])*10,np.sum(w401[29:32])*10,np.sum(w303[29:32])*10,np.sum(w403[29:32])*10 #orange: 590 - 620nm
print np.sum(w102[32:46])*10,np.sum(w201[32:46])*10,np.sum(w301[32:46])*10,np.sum(w401[32:46])*10,np.sum(w303[32:46])*10,np.sum(w403[32:46])*10 #red: 620 - 750nm
print np.sum(w102[46:111])*10,np.sum(w201[46:111])*10,np.sum(w301[46:111])*10,np.sum(w401[46:111])*10,np.sum(w303[46:111])*10,np.sum(w403[46:111])*10 #NIR - A: 750 - 1400nm
print np.sum(w102[111:])*10,np.sum(w201[111:])*10,np.sum(w301[111:])*10,np.sum(w401[111:])*10,np.sum(w303[111:])*10,np.sum(w403[111:]*10) #NIR - B: 1400 - 3000nm

vis=[np.sum(w102[8:46])*10,np.sum(w201[8:46])*10,np.sum(w301[8:46])*10,np.sum(w401[8:46])*10,np.sum(w303[8:46])*10,np.sum(w403[8:46])*10] #visible: 380-750nm
violet=[np.sum(w102[8:15])*10,np.sum(w201[8:15])*10,np.sum(w301[8:15])*10,np.sum(w401[8:15])*10,np.sum(w303[8:15])*10,np.sum(w403[8:15])*10] #violet: 380 - 450nm
blue=[np.sum(w102[15:19])*10,np.sum(w201[15:19])*10,np.sum(w301[15:19])*10,np.sum(w401[15:19])*10,np.sum(w303[15:19])*10,np.sum(w403[15:19])*10] #blue: 450 - 495nm
#print np.sum(w102[20:27])*10,np.sum(w201[20:27])*10,np.sum(w301[20:27])*10,np.sum(w401[20:27])*10,np.sum(w303[20:27])*10,np.sum(w403[20:27])*10] #green: 495 - 570nm
#print np.sum(w102[27:29])*10,np.sum(w201[27:29])*10*10,np.sum(w301[27:29])*10,np.sum(w401[27:29])*10,np.sum(w303[27:29])*10,np.sum(w403[27:29])*10] #yellow: 570 - 590nm
#print np.sum(w102[29:32])*10,np.sum(w201[29:32])*10,np.sum(w301[29:32])*10,np.sum(w401[29:32])*10,np.sum(w303[29:32])*10,np.sum(w403[29:32])*10] #orange: 590 - 620nm
#print np.sum(w102[32:46])*10,np.sum(w201[32:46])*10,np.sum(w301[32:46])*10,np.sum(w401[32:46])*10,np.sum(w303[32:46])*10,np.sum(w403[32:46])*10] #red: 620 - 750nm
#print np.sum(w102[46:111])*10,np.sum(w201[46:111])*10,np.sum(w301[46:111])*10,np.sum(w401[46:111])*10,np.sum(w303[46:111])*10,np.sum(w403[46:111])*10] #NIR - A: 750 - 1400nm
#print np.sum(w102[111:])*10,np.sum(w201[111:])*10,np.sum(w301[111:])*10,np.sum(w401[111:])*10,np.sum(w303[111:])*10,np.sum(w403[111:]*10)] #NIR - B: 1400 - 3000nm

#bins = np.linspace(-10, 10, 100)
#pyplot.hist(vis, bins, alpha=0.5)
#pyplot.hist(violet, bins, alpha=0.5)

#plt.hist([1, 2, 1], bins=[0, 1, 2, 3])

#from scipy.integrate import quad
#df['C'] = df.apply(lambda x: quad(lambda x: x, x[0], x[1])[0], axis=1)



fig = plt.figure()

major_ticks = np.arange(300, 2500, 100)
minor_ticks = np.arange(300, 2500, 50)

ax1 = fig.add_subplot(511)
ax1.set_title("Gehwege, TIS")
ax1.plot(wavel,Meas2_tis_d10nm2['102_w'],label="MV1_2 2 Normalbeton, Besenstrich")
ax1.plot(wavel,Meas2_tis_d10nm2['201_w'],label="MV2_1 2 Normalbeton hell, Besenstrich")
ax1.set_xticks(major_ticks)
ax1.set_xticks(minor_ticks, minor=True)
ax1.grid(which='both')#, color='black', linestyle=':')
ax1.get_xaxis().set_ticklabels([])
ax1.set_ylim(0,1)
ax1.legend()

#Meas2_tis.iloc[:,0].plot()
ax2 = fig.add_subplot(512, sharex=ax1)
ax2.set_title(u"nicht befahrbare Betonfläche, TIS")
ax2.plot(wavel,Meas1['101_w'],label="MVI_01_1 Normalbeton, glatt abgezogen")
ax2.plot(wavel,Meas1['302_w'],label=u"MV3_02_1 Straßenbeton, glatt abgezogen")
ax2.set_xticks(major_ticks)
ax2.set_xticks(minor_ticks, minor=True)
ax2.grid(b=True, which='major', color='black', linestyle=':')
ax2.grid(b=True, which='minor', color='black', linestyle=':')
ax2.get_xaxis().set_ticklabels([])
ax2.set_ylim(0,1)
ax2.legend()

ax3 = fig.add_subplot(513, sharex=ax1)
ax3.set_title("Sichtbetonmauer, TIS")
ax3.plot(wavel,Meas1['102_w'], label=u"MV1_02_1 Normalbeton Schalfläche")
ax3.plot(wavel,Meas1['201_w'], label=u"MV2_01_1 Normalbeton hell Schalfläche")
ax3.plot(wavel,Meas1['202_w'],label=u"MV2_02_1 Normalbeton hell Schalfläche")
ax3.set_xticks(major_ticks)
ax3.set_xticks(minor_ticks, minor=True)
ax3.grid(b=True, which='major', color='black', linestyle=':')
ax3.grid(b=True, which='minor', color='black', linestyle=':')
ax3.get_xaxis().set_ticklabels([])
ax3.set_ylabel(u"Reflected Spectral Irradiance[W/m²/nm]")
ax3.set_ylim(0,1)
ax3.legend()

ax4 = fig.add_subplot(514, sharex=ax1)
ax4.set_title("Stasse niederangig, TIS")
ax4.plot(wavel,Meas2_tis_d10nm2['301_w'],label=u"MV3_01_2 Straßenbeton, Besenstrich")
ax4.plot(wavel,Meas2_tis_d10nm2['401_w'],label=u"MV4_01_2 Straßenbeton hell, Besenstrich")
ax4.set_xticks(major_ticks)
ax4.set_xticks(minor_ticks, minor=True)
ax4.grid(b=True, which='major', color='black', linestyle=':')
ax4.grid(b=True, which='minor', color='black', linestyle=':')
#ax4.get_xaxis().set_ticklabels([])
ax4.set_ylim(0,1)
ax4.legend()

ax5 = fig.add_subplot(515)
ax5.set_title("Stasse hochrangig, TIS")
ax5.plot(wavel,Meas2_tis_d10nm2['303_w'],label=u"MV3_03_2 Straßenbeton, Waschbetonstruktur")
ax5.plot(wavel,Meas2_tis_d10nm2['403_w'],label=u"MV4_03_2 Straßenbeton, hell, Waschbetonstruktur")
ax5.set_xlabel("wavelength [nm]")
ax5.set_xticks(major_ticks)
ax5.set_xticks(minor_ticks, minor=True)
ax5.grid(b=True, which='major', color='black', linestyle=':')
ax5.grid(b=True, which='minor', color='black', linestyle=':')
#ax5.grid(b=True, which='minor', color='r', linestyle=':')
ax5.set_ylim(0,1)
ax5.legend()

#plt.setp(ax1.get_xticklabels(), visible=False)
plt.show()



#Spec1_d10nm = Spec1.iloc[::20, :] #extract every 20th row, starting from 1st row   until 400nm
                                  #400 - 1700: d1nm
                                  #1702
                                  #1705 - 4000:d5nm
#print Spec1
#Spec1_d10nm = Spec1.iloc[0] > 285.0
#test = Spec1.loc[Spec1["Wvlgth nm"] == "300.0"]
#df.loc[df['A'] == 'foo']
#print Spec1.iloc[:,2]
#print Spec1_d10nm.iloc[:]
#print Spec1_d10nm.iloc[:,2]
