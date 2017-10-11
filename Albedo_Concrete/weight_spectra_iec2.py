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
Spec2_cut = Spec2_10nm[2:223] #measurements only available from 300 to 2500 nanometer, therefore cut spectrum

##CREATE X-AXIS in 10nm range:
wavel = range(300,2510,10)

"""
##PLOT ALBEDO for each useage-type
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
plt.setp(ax1.get_xticklabels(), visible=True)
plt.show()
"""

##WEIGHT MEASURED ALBEDO WITH SPECTRUM
#divide Albedovalues per 100 (0-100) -> (0-1)
#multiply with Globalspectralirradiance (W·m–2·nm–1)

Meas_probes = [(Meas2_tis_d10nm.iloc[:,0]/100),
               (Meas2_tis_d10nm.iloc[:,1]/100),
               (Meas2_tis_d10nm.iloc[:,3]/100),
               (Meas2_tis_d10nm.iloc[:,5]/100),
               (Meas2_tis_d10nm.iloc[:,4]/100),
               (Meas2_tis_d10nm.iloc[:,6]/100)]

for i in Meas_probes:
    #print "shortwave: 300-2500nm;", round(np.trapz(i[:]),2)
    print "shortwave: 300-2500nm;", round(np.mean(i[:]),2)
    print "visible: 380-750nm;", round(np.mean(i[8:46]),2)
    #print np.sum(i[8:46])
    print "violet: 380 - 450nm;", round(np.mean(i[8:15]),2)
    print "blue: 450 - 495nm;", round(np.mean(i[15:19]),2)
    print "green: 495 - 570nm;", round(np.mean(i[20:27]),2)
    print "yellow: 570 - 590nm;", round(np.mean(i[27:29]),2)
    print "orange: 590 - 620nm;", round(np.mean(i[29:32]),2)
    print "red: 620 - 750nm;", round(np.mean(i[32:46]),2)
    print "NIR - A: 750 - 1400nm;", round(np.mean(i[46:111]),2)
    print "NIR - B: 1400 - 3000nm;", round(np.mean(i[111:]),2)

Meas1.loc[:,'302_w'] = (Meas1.iloc[:,4]/100) * Spec2_cut.iloc[:,0] #Add new column at end of Meas1
Meas1.loc[:,'202_w'] = (Meas1.iloc[:,6]/100) * Spec2_cut.iloc[:,0] #Add new column at end of Meas1
Meas1.loc[:,'201_w'] = (Meas1.iloc[:,7]/100) * Spec2_cut.iloc[:,0] #Add new column at end of Meas1
Meas1.loc[:,'102_w'] = (Meas1.iloc[:,8]/100) * Spec2_cut.iloc[:,0] #Add new column at end of Meas1
Meas1.loc[:,'101_w'] = (Meas1.iloc[:,9]/100) * Spec2_cut.iloc[:,0] #Add new column at end of Meas1

Meas2_tis_d10nm.loc[:,'102_w'] = (Meas2_tis_d10nm.iloc[:,0]/100) * Spec2_cut.iloc[:,0] #Add new column at end of Meas2_tis_d10nm
Meas2_tis_d10nm.loc[:,'201_w'] = (Meas2_tis_d10nm.iloc[:,1]/100) * Spec2_cut.iloc[:,0] #Add new column at end of Meas2_tis_d10nm
Meas2_tis_d10nm.loc[:,'301_w'] = (Meas2_tis_d10nm.iloc[:,3]/100) * Spec2_cut.iloc[:,0] #Add new column at end of Meas2_tis_d10nm
Meas2_tis_d10nm.loc[:,'401_w'] = (Meas2_tis_d10nm.iloc[:,5]/100) * Spec2_cut.iloc[:,0] #Add new column at end of Meas2_tis_d10nm
Meas2_tis_d10nm.loc[:,'303_w'] = (Meas2_tis_d10nm.iloc[:,4]/100) * Spec2_cut.iloc[:,0] #Add new column at end of Meas2_tis_d10nm
Meas2_tis_d10nm.loc[:,'403_w'] = (Meas2_tis_d10nm.iloc[:,6]/100) * Spec2_cut.iloc[:,0] #Add new column at end of Meas2_tis_d10nm

w102 = np.array(Meas2_tis_d10nm.loc[:,'102_w']) #export values to a numpy array
w201 = np.array(Meas2_tis_d10nm.loc[:,'201_w'])
w301 = np.array(Meas2_tis_d10nm.loc[:,'301_w'])
w401 = np.array(Meas2_tis_d10nm.loc[:,'401_w'])
w303 = np.array(Meas2_tis_d10nm.loc[:,'303_w'])
w403 = np.array(Meas2_tis_d10nm.loc[:,'403_w'])

weight_tuples = [((u"Gehwege,Normalbeton, Besenstrich"), Meas2_tis_d10nm['102_w'],Meas2_tis_d10nm.iloc[:,0]/100),
                ((u"Gehwege,Normalbeton hell, Besenstrich"), Meas2_tis_d10nm['201_w'],Meas2_tis_d10nm.iloc[:,1]/100),
                ((u"nicht befahrbare Betonfäche,Normalbeton, glatt abgezogen"), Meas1['101_w'],Meas1.iloc[:,9]/100),
                ((u"nicht befahrbare Betonfäche,Straßenbeton, glatt abgezogen"), Meas1['302_w'],Meas1.iloc[:,4]/100),
                ((u"Sichtbetonmauer,Normalbeton Schalfläche, glatt abgezogen"), Meas1['102_w'],Meas1.iloc[:,8]/100),
                ((u"Sichtbetonmauer,Normalbeton hell, Schalfläche"), Meas1['201_w'],Meas1.iloc[:,7]/100),
                ((u"Sichtbetonmauer,Normalbeton hell, Schalfläche2"), Meas1['202_w'],Meas1.iloc[:,6]/100),
                ((u"Stasse niederangig,Straßenbeton, Besenstrich"), Meas2_tis_d10nm['301_w'], Meas2_tis_d10nm.iloc[:,3]/100),
                ((u"Stasse niederangig,Straßenbeton hell, Besenstrich"), Meas2_tis_d10nm['401_w'], Meas2_tis_d10nm.iloc[:,5]/100),
                ((u"Stasse hochrangig,Straßenbeton , Waschbetonstruktur"), Meas2_tis_d10nm['303_w'],Meas2_tis_d10nm.iloc[:,4]/100),
                ((u"Stasse hochrangig,Straßenbeton hell, Waschbetonstruktur"), Meas2_tis_d10nm['403_w'],Meas2_tis_d10nm.iloc[:,6]/100)]

#http://www.intl-light.com/handbookthanks.html - Referenzen in "OSA Handbook of Optics"
lambda_day = [(380,0.000039), (390, 0.000120), (400, 0.000396), (410, 0.001210),(420, 0.004000),
    (430,     0.011600),    (440,     0.023000),    (450,     0.038000),    (460,     0.060000),
    (470,     0.090980),    (480,     0.139020),    (490,     0.208020),    (500,     0.323000),
    (507,     0.444310),    (510,     0.503000),    (520,     0.710000),    (530,     0.862000),
    (540,     0.954000),    (550,     0.994950),    (555,     1.000000),    (560,     0.995000),
    (570,     0.952000),    (580,     0.870000),    (590,     0.757000),    (600,     0.631000),
    (620,     0.381000),    (630,     0.265000),    (640,     0.175000),    (650,     0.107000),
    (660,     0.061000),    (670,     0.032000),    (680,     0.017000),    (690,     0.008210),
    (700,     0.004102),    (710,     0.002091),    (720,     0.001047),    (730,     0.000520),
    (740,     0.000249),    (750,     0.000120),    (760,     0.000060),    (770,     0.000030)]

##FUNCTIONS
def Interpolate_10to1nm(a):
    interpolated_x = np.arange(300,2501,1)
    data_x = np.arange(300,2510,10)
    interp_1nm = np.interp(interpolated_x, data_x, a)
    return interp_1nm

def WeightedIrradiance(a):
    weighted_irrad_1nm = Interpolate_10to1nm(a)
    weighted_irrad_integrated = np.trapz(weighted_irrad_1nm)
    return round(weighted_irrad_integrated,2)

def IntegratedAlbedo(a):
    integratedalbedo = WeightedIrradiance(a)/total_irrad_integrated
    return round(integratedalbedo,2)

def Eye_response(a):
    #weighted irradiance
    weighted_irrad_1nm = Interpolate_10to1nm(a)
    weighted_irrad_1nm_vis = weighted_irrad_1nm[80:471]
    weighted_irrad_1nm_integrated = np.trapz(weighted_irrad_1nm_vis)
    #eye responsiveness
    a_cut = a[8:48]
    a_interp_1nm = np.interp(interpolated_x2, data_x2, a_cut)
    a_1nm_eye_weighted = a_interp_1nm * weighted_irrad_1nm_vis
    weighted_irrad_1nm_integrated = np.trapz(a_1nm_eye_weighted)
    return round(weighted_irrad_1nm_integrated,2)

#Eye_response((u"Gehwege",u"Normalbeton, Besenstrich"), Meas2_tis_d10nm['102_w'],Meas2_tis_d10nm.iloc[:,0]/100)

eye_r = []
total_ir = []
weight_i =[]
##TOTAL IRRADIANCE
total_irrad_1nm = Interpolate_10to1nm(Spec2_cut.iloc[:,0])
total_irrad_integrated = np.trapz(total_irrad_1nm) #983.698608609 W/m2
total_irrad_1nm_vis = total_irrad_1nm[80:471]  # measurements only available from 380 to 770 nanometer, therefore cut spectrum from 300 to 2500
total_irrad_1nm_vis_integrated = np.trapz(total_irrad_1nm_vis) #513.7355

data_x2 = np.arange(380, 780, 10)
interpolated_x2 = np.arange(380, 771, 1)

a= Meas2_tis_d10nm.iloc[:,0]/100

#test = np.array([2.0,4.0])
#testmean = np.mean(test)
#testinteg = np.trapz(test, dx=0.0001)
#testsum = np.sum(test/10000)
#print testmean, testinteg, testsum
#print w102
#exit()


for i in weight_tuples:
    #print ("mean_albedo=",round(np.mean(i[2]),2),"%",\
    #       "eye weighted irrad.=",Eye_response(i[1]), "W/m2", \
    #      "weighted irrad.=",WeightedIrradiance(i[1]), "W/m2", \
    #       i[0]) #,/
          #"integr.albedo=", IntegratedAlbedo(i[1]), "%"
    eye_r.append(Eye_response(i[1]))
    weight_i.append(WeightedIrradiance(i[1]))

#x = total_ir
y = np.arange(11)
#print eye_r

fig, ax = plt.subplots()
width = 0.4
labels = ['G,NB,B','G,NBh,B','nbB,NB,g','nbB,SB,g','SB,NBS,g','SB,NBh,S1','SB,NBh,S2','Sn,SB,B','Sn,SBh,B','Sn,SB,W','Sn,SBh,W' ]
colors = ['green','lightgreen','blue','lightblue','beige','yellow','yellow','red','orange','violet','pink']
plt.barh(y, eye_r, color=colors, label=labels)
plt.barh(y + width, weight_i, label=labels)
plt.xlabel(u"irradiance [W/m²]")
plt.ylabel("probes")
#plt.legend(prop={'size': 10})
ax.set_yticks(y)
ax.set_yticklabels(labels)
plt.show()


fig, ax = plt.subplots()
#labels = ['G,NB,B', 'G,NBh,B', 'nbB,NB,g','nbB,SB,g', 'SB,NBS,g', 'SB,NBh,S1','SB,NBh,S2', 'Sn,SB,B', 'Sn,SBh,B','Sn,SB,W', 'Sn,SBh,W' ]
labels = ['G1', 'G2', 'nbB1','nbB2', 'SB1', 'SB2','SB3', 'S1', 'S2','S3', 'S4' ]
colors = ['green','lightgreen','blue','lightblue','brown','yellow','lightyellow','red','orange','violet','pink']
plt.bar(y, eye_r, color=colors, label=labels)
plt.xlabel("probes")
plt.ylabel(u"irradiance [W/m²]")
#plt.legend(prop={'size': 10})
ax.set_xticks(y)
ax.set_xticklabels(labels, rotation=0, rotation_mode="anchor")
#plt.set_title('bars with legend')
plt.show()

#fig = plt.gcf()


"""
print 'mean albedo: 102_w', np.mean(a102_1nm)
#print '102_w', np.mean(Meas2_tis_d10nm2.iloc[:,0]/100)
print 'integrated albedo: 102_w', np.trapz(a102_1nm)
print 'integrated irradiance: 102_w', np.trapz(w102_1nm)
print 'integrated irradiance: total', np.trapz(total_irrad)
print 'integrated albedo?: 102,w ',  np.trapz(w102_1nm)/np.trapz(total_irrad)
"""
spec = (Spec2_cut.iloc[:,0])
print np.trapz(spec)
probes = [w102,w201,w301,w401,w303,w403, spec]



for i in probes:
    #print "shortwave: 300-2500nm;", round(np.trapz(i[:])*10,2)
    #print "visible: 380-750nm;", round(np.trapz(i[8:46])*10,2)
    #print np.sum(i[8:46])
    #print "violet: 380 - 450nm;", round(np.trapz(i[8:15])*10,2)
    #print "blue: 450 - 495nm;", round(np.trapz(i[15:19])*10,2)
    #print "green: 495 - 570nm;", round(np.trapz(i[20:27])*10,2)
    #print "yellow: 570 - 590nm;", round(np.trapz(i[27:29])*10,2)
    #print "orange: 590 - 620nm;", round(np.trapz(i[29:32])*10,2)
    #print "red: 620 - 750nm;", round(np.trapz(i[32:46])*10,2)
    #print "NIR - A: 750 - 1400nm;", round(np.trapz(i[46:111])*10,2)
    #print "NIR - B: 1400 - 3000nm;", round(np.trapz(i[111:])*10,2)
    print "555nm", i[25]

#lux[lx] <— > watt / centimeter² (at 555 nm) [W / cm² (at555nm)] lux[lx] = 1.46412884333821E-07
# watt / centimeter² (at 555nm) [W / cm² (at555nm)]

fig = plt.figure()

major_ticks = np.arange(300, 2500, 100)
minor_ticks = np.arange(300, 2500, 50)

ax1 = fig.add_subplot(511)
ax1.set_title("Gehwege, TIS")
ax1.plot(wavel,Meas2_tis_d10nm['102_w'],label="MV1_2 2 Normalbeton, Besenstrich")
ax1.plot(wavel,Meas2_tis_d10nm['201_w'],label="MV2_1 2 Normalbeton hell, Besenstrich")
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
ax3.set_ylabel(u"IECNorm Weighted, Spectral reflected irradiance [W/m²/nm]")
ax3.set_ylim(0,1)
ax3.legend()

ax4 = fig.add_subplot(514, sharex=ax1)
ax4.set_title("Stasse niederangig, TIS")
ax4.plot(wavel,Meas2_tis_d10nm['301_w'],label=u"MV3_01_2 Straßenbeton, Besenstrich")
ax4.plot(wavel,Meas2_tis_d10nm['401_w'],label=u"MV4_01_2 Straßenbeton hell, Besenstrich")
ax4.set_xticks(major_ticks)
ax4.set_xticks(minor_ticks, minor=True)
ax4.grid(b=True, which='major', color='black', linestyle=':')
ax4.grid(b=True, which='minor', color='black', linestyle=':')
#ax4.get_xaxis().set_ticklabels([])
ax4.set_ylim(0,1)
ax4.legend()

ax5 = fig.add_subplot(515)
ax5.set_title("Stasse hochrangig, TIS")
ax5.plot(wavel,Meas2_tis_d10nm['303_w'],label=u"MV3_03_2 Straßenbeton, Waschbetonstruktur")
ax5.plot(wavel,Meas2_tis_d10nm['403_w'],label=u"MV4_03_2 Straßenbeton, hell, Waschbetonstruktur")
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
