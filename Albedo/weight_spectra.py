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
spec = "ASTMG173_2.csv"
mea1 = "2017_04_21_Reflexion_Betonproben.txt"
mea2_diff = "2017_05_26_Betonproben_R_DIFF.txt"
mea2_tis = "2017_05_26_Betonproben_R_TIS.txt" #TIS = total integrated sphere
spectrum = os.path.join(directory, spec)
meas1 = os.path.join(directory, mea1)
meas2_diff = os.path.join(directory, mea2_diff)
meas2_tis = os.path.join(directory, mea2_tis)

Spec1 = pd.read_csv(spectrum, skiprows=1,index_col=0) #delta 0.5 nm
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

Meas1.loc[:,'302_w'] = (Meas1.iloc[:,4]/100) * Spec1.iloc[:,2]
Meas1.loc[:,'202_w'] = (Meas1.iloc[:,6]/100) * Spec1.iloc[:,2]
Meas1.loc[:,'201_w'] = (Meas1.iloc[:,7]/100) * Spec1.iloc[:,2]
Meas1.loc[:,'102_w'] = (Meas1.iloc[:,8]/100) * Spec1.iloc[:,2]
Meas1.loc[:,'101_w'] = (Meas1.iloc[:,9]/100) * Spec1.iloc[:,2]

Meas2_tis_d10nm2.loc[:,'102_w'] = (Meas2_tis_d10nm2.iloc[:,0]/100) * Spec1.iloc[:,2]
Meas2_tis_d10nm2.loc[:,'201_w'] = (Meas2_tis_d10nm2.iloc[:,1]/100) * Spec1.iloc[:,2]
Meas2_tis_d10nm2.loc[:,'301_w'] = (Meas2_tis_d10nm2.iloc[:,3]/100) * Spec1.iloc[:,2]
Meas2_tis_d10nm2.loc[:,'401_w'] = (Meas2_tis_d10nm2.iloc[:,5]/100) * Spec1.iloc[:,2]
Meas2_tis_d10nm2.loc[:,'303_w'] = (Meas2_tis_d10nm2.iloc[:,4]/100) * Spec1.iloc[:,2]
Meas2_tis_d10nm2.loc[:,'403_w'] = (Meas2_tis_d10nm2.iloc[:,6]/100) * Spec1.iloc[:,2]

w102 = np.array(Meas2_tis_d10nm2.loc[:,'102_w'])
w201 = np.array(Meas2_tis_d10nm2.loc[:,'201_w'])
w301 = np.array(Meas2_tis_d10nm2.loc[:,'301_w'])
w401 = np.array(Meas2_tis_d10nm2.loc[:,'401_w'])
w303 = np.array(Meas2_tis_d10nm2.loc[:,'303_w'])
w403 = np.array(Meas2_tis_d10nm2.loc[:,'403_w'])

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

exit()

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
