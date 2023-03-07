import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from scipy import stats
import met.library.BOKUMet_Data
from met.library.Datetime_recipies import datestdtojd
import matplotlib.gridspec as gridspec

"read in EDO - SPI data"
#spi = pd.read_csv("/windata/DATA/obs_point/land/EDO/SPI_16_48.2017to2021.20211206100030.txt", delimiter="|",skiprows=2,header=0)
spi = pd.read_csv("/windata/DATA/obs_point/land/EDO/spi.16_48.1990to2021.20211217121607.txt", delimiter="|",skiprows=2,header=0) #spi1.16_48.1990to2021.20211217120417.txt
spi = spi.set_index(pd.to_datetime(spi['Date'])) #utc=True
spi = spi.drop(columns=['Date'])
spi = spi[:-12]

'''READ IN EEA air pollution data'''
pathbase2 = "/windata/DATA/obs_point/chem/EEA/"
o3_1990_2019_mda1 = pd.read_csv(pathbase2 + "o3_mda1_1990-2019_AT_mug.csv")
o3_1990_2019_mda1 = o3_1990_2019_mda1.set_index(pd.to_datetime(o3_1990_2019_mda1['date']))
o3_1990_2019_mda1 = o3_1990_2019_mda1.drop(columns=['date'])
o3_1990_2019_mda8 = pd.read_csv(pathbase2 + "o3_mda8_1990-2019_AT_mug.csv")
o3_1990_2019_mda8 = o3_1990_2019_mda8.set_index(pd.to_datetime(o3_1990_2019_mda8['date']))
o3_1990_2019_mda8 = o3_1990_2019_mda8.drop(columns=['date'])
o3_2020_mda1 = pd.read_csv(pathbase2 + "AT_O3_2020.csv")                        #TODO! replace mda1 with mda8!
o3_2020_mda1 = o3_2020_mda1.set_index(pd.to_datetime(o3_2020_mda1['date']))
o3_2020_mda1 = o3_2020_mda1.drop(columns=['date'])
o3_2020_mda8 = o3_2020_mda1.resample('8H', label='right').mean()
o3_2020_mda8 = o3_2020_mda8.resample('D').mean()
o3_1990_2020_mda8 = pd.concat([o3_1990_2019_mda8, o3_2020_mda8], axis=0)
o3_1990_2020_mda8 = o3_1990_2020_mda8["AT9STEF"]#*ugm3toppb_o3 #MUG->PPB
o3_1990_2020_m = o3_1990_2020_mda8[datetime(1990,1,1):datetime(2021,12,30)].resample('M').mean()
o3_1990_2020_m = o3_1990_2020_m[:-1]
#print(spi,o3_1990_2020_m)

o3_1990_2020_m_spring = o3_1990_2020_m.loc[(o3_1990_2020_m.index.month >= 3) & (o3_1990_2020_m.index.month <= 5)]
spi3_d_m_spring = spi.loc[(spi.index.month>=3)&(spi.index.month<=5)]
o3_1990_2020_m_summer = o3_1990_2020_m.loc[(o3_1990_2020_m.index.month>=6)&(o3_1990_2020_m.index.month<=8)]
spi3_d_m_summer = spi.loc[(spi.index.month>=6)&(spi.index.month<=8)]
spi3_d_m_spring = spi3_d_m_spring.resample("M").mean()
spring_dry = pd.concat([spi3_d_m_spring, o3_1990_2020_m_spring], axis=1)
#spring_dry = spring_dry.loc[(spring_dry['SPI-6'] <= 0 )]
#spring_dry = spring_dry[datetime(1990,1,1):datetime(1999,12,31)].dropna()
spring_dry = spring_dry[datetime(2010,1,1):datetime(2019,12,31)].dropna()

spi3_d_m_summer = spi3_d_m_summer.resample("M").mean()
summer_dry = pd.concat([spi3_d_m_summer, o3_1990_2020_m_summer], axis=1)
#summer_dry = summer_dry.loc[(summer_dry['SPI-6'] <= 0 )]
#summer_dry = summer_dry[datetime(1990,1,1):datetime(1999,12,31)].dropna()
summer_dry = summer_dry[datetime(2010,1,1):datetime(2019,12,31)].dropna()

"""Regresssion seasons"""
y5_mam = spring_dry['AT9STEF'].values.flatten()
y5_jja = summer_dry['AT9STEF'].values.flatten()

x5_SPI3_mam = spring_dry['SPI-3'].values.flatten()  #TODO: decide - keep dry or not dry?
x5_SPI3_jja = summer_dry['SPI-3'].values.flatten()
idx_SPI3_mam = np.isfinite(x5_SPI3_mam) & np.isfinite(y5_mam)
idx_SPI3_jja = np.isfinite(x5_SPI3_jja) & np.isfinite(y5_jja)
m5_SPI3_mam, b5_SPI3_mam = np.polyfit(x5_SPI3_mam[idx_SPI3_mam], y5_mam[idx_SPI3_mam], 1)
m5_SPI3_jja, b5_SPI3_jja = np.polyfit(x5_SPI3_jja[idx_SPI3_jja], y5_jja[idx_SPI3_jja], 1)
SRho_SPI3_mam, Sp_SPI3_mam = (stats.spearmanr(x5_SPI3_mam, y5_mam))
SRho_SPI3_jja, Sp_SPI3_jja = (stats.spearmanr(x5_SPI3_jja, y5_jja))

"""Stastics"""
print("Shapiro/Normality")
print("MAM", stats.shapiro(x5_SPI3_mam).pvalue, "JJA", stats.shapiro(x5_SPI3_jja).pvalue, "HCHO_mam",
                            stats.shapiro(y5_mam).pvalue,"HCHO_jja", stats.shapiro(y5_jja).pvalue)
print("Variance")
var = [np.var(x, ddof=1) for x in [x5_SPI3_mam, y5_mam, x5_SPI3_jja, x5_SPI3_jja]]
print(var)
#print("Levene Test/Homoscedasticity")
#print("AT", Lp_AT, "GR", Lp_GR, "VPD", Lp_VPD, "SM", Lp_SM, "SIF", Lp_SIF, "O3", Lp_O3)
#print("AT", Lp_AT_2, "GR", Lp_GR_2, "VPD", Lp_VPD_2, "SM", Lp_SM_2, "SIF", Lp_SIF_2, "O3", Lp_O3_2)

"""Plotting"""
fig = plt.figure
plt.title('p_mam={:.2f} \n p_jja={:.2f}'.format(Sp_SPI3_mam, Sp_SPI3_jja), fontsize='small')
plt.scatter(x5_SPI3_mam, y5_mam, color='green', label="MAM", s=5)
plt.scatter(x5_SPI3_jja, y5_jja, color='red', label="JJA", s=5)
plt.plot(x5_SPI3_mam, m5_SPI3_mam * x5_SPI3_mam + b5_SPI3_mam, color='green')
plt.plot(x5_SPI3_jja, m5_SPI3_jja * x5_SPI3_jja + b5_SPI3_jja, color='red')
plt.ylabel("O3 [μg/m³]", size="small")
plt.xlabel("SPI 3 [-]", size="small")
plt.legend(loc="lower right")
#plt.xlim([-3, 0])
plt.xlim([-3, 3])
#plt.title("full year")
#plt.title('r={:.2f} \n p={:.2f} \n n=52'.format(SRho_SPI, Sp_SPI), fontsize='small')
plt.show()

exit()

"""Timeserie HCHO_SPI"""
figure = plt.figure
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(spi['SPI-3'], color="orange", label="SPI-3")
ax1.plot(spi['SPI-6'], color="red", label="SPI-6")
ax2.plot(o3_1990_2020_m, label= "O3 STEF")
ax1.legend(loc="upper left")
ax2.legend()
plt.show()


#exit()
"""Regression SPI-HCHO"""
y5 = o3_1990_2020_m.values.flatten()  #Mai 17 - Aug 2021
x5_SPI1 = spi['SPI-1'].values.flatten()
x5_SPI3 = spi['SPI-3'].values.flatten()
x5_SPI6 = spi['SPI-6'].values.flatten()
x5_SPI9 = spi['SPI-9'].values.flatten()
x5_SPI12 = spi['SPI-12'].values.flatten()
idxSPI = np.isfinite(x5_SPI1) & np.isfinite(y5)
m5_SPI1, b5_SPI1 = np.polyfit(x5_SPI1[idxSPI], y5[idxSPI], 1)
m5_SPI3, b5_SPI3 = np.polyfit(x5_SPI3[idxSPI], y5[idxSPI], 1)
m5_SPI6, b5_SPI6 = np.polyfit(x5_SPI6[idxSPI], y5[idxSPI], 1)
m5_SPI9, b5_SPI9 = np.polyfit(x5_SPI9[idxSPI], y5[idxSPI], 1)
m5_SPI12, b5_SPI12 = np.polyfit(x5_SPI12[idxSPI], y5[idxSPI], 1)

SRho_SPI1, Sp_SPI1 = (stats.spearmanr(x5_SPI1[idxSPI], y5[idxSPI]))
SRho_SPI3, Sp_SPI3 = (stats.spearmanr(x5_SPI3[idxSPI], y5[idxSPI]))
SRho_SPI6, Sp_SPI6 = (stats.spearmanr(x5_SPI6[idxSPI], y5[idxSPI]))
SRho_SPI9, Sp_SPI9 = (stats.spearmanr(x5_SPI9[idxSPI], y5[idxSPI]))
SRho_SPI12, Sp_SPI12 = (stats.spearmanr(x5_SPI12[idxSPI], y5[idxSPI]))

fig = plt.figure
plt.scatter(x5_SPI1, y5, color='yellow', label="SPI-1", s=5)
plt.scatter(x5_SPI3, y5, color='orange', label="SPI-3", s=5)
plt.scatter(x5_SPI6, y5, color='red', label="SPI-6", s=5)
plt.scatter(x5_SPI9, y5, color='violet', label="SPI-9", s=5)
plt.scatter(x5_SPI12, y5, color='blue', label="SPI-12", s=5)
plt.plot(x5_SPI1, m5_SPI1 * x5_SPI1 + b5_SPI1, color='yellow')
plt.plot(x5_SPI3, m5_SPI3 * x5_SPI3 + b5_SPI3, color='orange')
plt.plot(x5_SPI6, m5_SPI6 * x5_SPI6 + b5_SPI6, color='red')
plt.plot(x5_SPI9, m5_SPI9 * x5_SPI9 + b5_SPI9, color='violet')
plt.plot(x5_SPI12, m5_SPI12 * x5_SPI12 + b5_SPI12, color='blue')
plt.ylabel("O3 [ppb]", size="small")
plt.xlabel("SPI [-]", size="small")
plt.legend()
plt.title("full year")
#plt.title('r={:.2f} \n p={:.2f} \n n=52'.format(SRho_SPI, Sp_SPI), fontsize='small')
plt.show()
