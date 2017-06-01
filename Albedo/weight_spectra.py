# -*- coding: utf-8 -*-
import os, csv
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

directory = "D:/_URBANIA/METDATA/GerhardPeharz_Johanneum/2_raw"

#http://rredc.nrel.gov/solar/spectra/am1.5/astmg173/astmg173.html
#0 Wvlgth nm
#1 Etr W*m-2*nm-1  Extraterrestrial Radiation (solar spectrum at TOA) at mean Earth Sun distance
#2 Global tilt  W*m-2*nm-1  Spectral radiation from solar disk plus sky diffuse and diffuse reflected from ground on south facing surface tilted 37deg from horizontal
#3 Direct+circumsolar W*m-2*nm-1  Direct=Direct Normal Irradiance Nearly parallel (0.5 deg divergent cone) radiation on surface with surface normal tracking (pointing to) the sun, excluding scattered sky and reflected ground radiation
#Circumsolar=Spectral irradiance within +/- 2.5 degree (5 degree diameter) field of view centered on the 0.5 deg diameter solar disk, but excluding the radiation from the disk

spec = "ASTMG173.csv"
mea1 = "2017_04_21_Reflexion_Betonproben.txt"
mea2_diff = "2017_05_26_Betonproben_R_DIFF.txt"
mea2_tis = "2017_05_26_Betonproben_R_TIS.txt" #TIS = total integrated sphere
spectrum = os.path.join(directory, spec)
meas1 = os.path.join(directory, mea1)
meas2_diff = os.path.join(directory, mea2_diff)
meas2_tis = os.path.join(directory, mea2_tis)

Spec1 = pd.read_csv(spectrum, skiprows=1,index_col=0) #delta 0.5 nm
#Spec1_d10nm = Spec1.iloc[::20, :] #extract every 20th row, starting from 1st row   until 400nm
                                  #400 - 1700: d1nm
                                  #1702
                                  #1705 - 4000:d5nm

Spec1_d10nm = Spec1.iloc[0] > 285.0
#print Spec1.iloc[:,2]
print Spec1_d10nm.iloc[:]
#print Spec1_d10nm.iloc[:,2]

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
#print Meas2_tis_d10nm.head()

wavel = range(300,2500,10)
#print len(wavel)
#print len(Spec1_d10nm)
#GEHWEGE:
#MV1_02_2 Normalbeton, Besenstrich
#print Meas2_tis.iloc[:,2] #2 "MV2_2_Oberseite TIS"
#MV2_01_2 Normalbeton hell, Besenstrich
#print Meas2_tis.iloc[:,0] #0 "MV1_2_Oberseite TIS"

fig = plt.figure()
#plt.plot(wavel,Spec1_d10nm.iloc[:,2],label="globaltilt")
#plt.plot(wavel,Spec1_d10nm.iloc[:,3],label="direct+circum")
#plt.legend()
#plt.show()

#Meas2_tis.iloc[:,0].plot()

#NICHT BEFAHRBAHRE BETONFLAECHEN:
#MVI_01_1 Normalbeton, glatt abgezogen

#SICHTBETONMAUER
#MV1_02_1 Normalbeton Schalfläche
#MV2_01_1 Normalbeton hell Schalfläche
#MV2_02_1 Normalbeton hell Schalfläche

#STRASSEN IM NIEDERRANGIGEN NETZ
#MV3_01_2 Straßenbeton, Besenstrich
#MV4_01_2 Straßenbeton hell, Besenstrich

#STRASSEN IM HOCHRANGINGEN NETZ
#MV3_03_2 Straßenbeton, Waschbetonstruktur
#MV4_03_2 Straßenbeton, hell, Waschbetonstruktur

#NICHT BEFAHRBARE BETONFLÄCHEN
#MV3_02_1 Straßenbeton, glatt abgezogen