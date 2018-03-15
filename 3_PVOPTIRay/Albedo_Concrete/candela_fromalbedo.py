# -*- coding: utf-8 -*-
import os, csv
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

##READING and PREPARING MEASUREMENT
directory = "D:/_URBANIA/METDATA/GerhardPeharz_Johanneum/2_raw"
mea1 = "2017_04_21_Reflexion_Betonproben.txt"   #Albedo (0-100), 300 - 2500nm, delta:10nm
mea2_diff = "2017_05_26_Betonproben_R_DIFF.txt" #Albedo (0-100) 2500 - 300, delta:5nm "diffuse"
mea2_tis = "2017_05_26_Betonproben_R_TIS.txt"   #Albedo (0-100)300 - 2500, delta:5nm "TIS = total integrated sphere"
meas1 = os.path.join(directory, mea1)
meas2_diff = os.path.join(directory, mea2_diff)
meas2_tis = os.path.join(directory, mea2_tis)
Meas1 = pd.read_csv(meas1, delimiter='\t', index_col=0)
Meas2_diff = pd.read_csv(meas2_diff, delimiter='\t', index_col=0)
Meas2_diff_d10nm = Meas2_diff.iloc[::2, :]
Meas2_diff_d10nm2 = Meas2_diff_d10nm.sort_index(ascending=True)
Meas2_tis = pd.read_csv(meas2_tis, delimiter='\t', index_col=0)
Meas2_tis_d10nm = Meas2_tis.iloc[::2, :]

Meas1 = Meas1[8:48] #visible range 380 to 770
Meas2_diff_d10nm2 = Meas2_diff_d10nm2[8:48] #visible range 380 to 770
Meas2_tis_d10nm = Meas2_tis_d10nm[8:48] #visible range 380 to 770

##READING AND PREPARING SPECTRUM
spec = "IECNorm 60904-3/82_1071e_FDIS.xlsx"  #Globalspectralirradiancel (W·m–2·nm–1)
spectrum = os.path.join(directory, spec)
Spec2 = pd.read_excel(spectrum, sheetname="Sheet1", skiprows=2)
Spec2_10nm = pd.DataFrame(index=range(280,4010,10),columns=["Wm2"])
Spec2_10nm = Spec2_10nm.fillna(0)
n = Spec2.iloc[:,0].size
m = Spec2_10nm.iloc[:,0].size

j=0
for i in range(0,n-5): #last five lines contain comments!
    if Spec2.iloc[i,0]%10 == 0:
        Spec2_10nm.iloc[j,0] = Spec2.iloc[i,1] #filter values to obtain a 10nm resolution
        j+=1
    else:
        pass
Spec2_cut = Spec2_10nm[10:50] #visible range 380 to 770

##CREATE X-AXIS in 10nm range:
wavel = range(380,780,10)
#http://www.intl-light.com/handbookthanks.html - Referenzen in "OSA Handbook of Optics"
Vlambda = [0.000039, 0.000120, 0.000396, 0.001210, 0.004000, 0.011600, 0.023000, 0.038000, 0.060000, 0.090980,
    0.139020, 0.208020, 0.323000, 0.503000, 0.710000, 0.862000, 0.954000, 0.994950, 0.995000, 0.952000, 0.870000,
    0.757000, 0.631000, 0.381000, 0.381000, 0.265000, 0.175000, 0.107000, 0.061000, 0.032000, 0.017000, 0.008210,
    0.004102, 0.002091, 0.001047, 0.000520, 0.000249, 0.000120, 0.000060, 0.000030]
lambda_day = pd.DataFrame({'Vlambda':Vlambda,'wavelength': wavel})
lambda_day.set_index('wavelength',inplace=True)


probes = [(Meas2_tis_d10nm.iloc[:,0]/100),(Meas2_tis_d10nm.iloc[:,1]/100),(Meas2_tis_d10nm.iloc[:,3]/100),
(Meas2_tis_d10nm.iloc[:,5]/100),(Meas2_tis_d10nm.iloc[:,4]/100),(Meas2_tis_d10nm.iloc[:,6]/100)]

labels = [102, 201, 301, 401, 303, 403]

lu_flu1_global = 1 * Spec2_cut.iloc[:, 0] * 683 * lambda_day.iloc[:, 0]
luminous_flux_global = np.trapz(lu_flu1_global, dx=10)  # lumen/m²
luminance_global = luminous_flux_global / (2 * np.pi)  # candela/m2
print round(luminance_global,2), "cd/m²"

for i in probes:
    #print i
    lu_flu1 = i * Spec2_cut.iloc[:, 0] * 683 * lambda_day.iloc[:, 0]
    luminous_flux = np.trapz(lu_flu1, dx=10)  # lumen/m²
    luminance = luminous_flux / (2 * np.pi)  # candela/m2
    print round(luminance,2), "cd/m²"

