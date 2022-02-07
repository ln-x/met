import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from scipy import stats
import met.library.BOKUMet_Data
from met.library.Datetime_recipies import datestdtojd
from met.library.conversions import *
from met.library import ReadinVindobona_Filter_fullperiod
from met.library import ReadinVindobona_Glyoxal
import matplotlib.gridspec as gridspec

from mpl_toolkits.axes_grid1 import host_subplot
from mpl_toolkits import axisartist
import matplotlib.pyplot as plt

yM = [15,46,74,105,135,166,196,227,258,288,319,349]
yM_ticks = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
yM18 = [15,46,74,105,135,166,196,227,258,288,319]
yM19 = [15,46,74,105,135,166,196,227,258,288]
yM20 = [15,46,74,105,135,166,196,227,258,288,319]
yM21 = [15,46,74,105,135,166,196,227]
start2017 = datetime(2017, 5, 1, 00, 00)
start2018 = datetime(2018, 1, 1, 00, 00)
start2019 = datetime(2019, 1, 1, 00, 00)
start2020 = datetime(2020, 1, 1, 00, 00)
end2020 = datetime(2020, 12, 31, 00, 00)
start2021 = datetime(2021, 1, 1, 00, 00)
end2021 = datetime(2021, 9, 1, 00, 00)

'''READ IN BOKU Metdata'''
BOKUMetData = met.library.BOKUMet_Data.BOKUMet() #10min values
BOKUMetData_hourlymean = BOKUMetData.resample('H').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean, 'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_dailysum = BOKUMetData_hourlymean.resample('D').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.sum, 'WS': np.mean, 'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_dailymax = BOKUMetData_hourlymean.resample('D').agg({'DT': np.max, 'AT': np.max, 'RH': np.max, 'GR': np.max, 'WS': np.max,'WD': np.max, 'WSG': np.max, 'PC': np.sum, 'AP': np.max})

#print(BOKUMetData_hourlymean['RH'])
vp_sat = 0.611 * np.exp((17.3 * BOKUMetData_hourlymean["AT"])/(BOKUMetData_hourlymean["AT"]+237.3))  #kPa sh. Dingman
vp_air = 0.611 * np.exp((17.3 * BOKUMetData_hourlymean["AT"])/(BOKUMetData_hourlymean["AT"]+237.3)) * (BOKUMetData_hourlymean["RH"]/100)
vpd = vp_sat - vp_air
#print(vp_sat,vp_air, vpd)

#vpd.plot()
#plt.show()

vpd_d = vpd.resample('D').mean()
vpd_dmax = vpd.resample('D').max()
vpd_dmax_w = vpd_dmax.resample('W').mean()
vpd_dmax_sigma = vpd_dmax.std()

BOKUMetData_dailysum['JD'] = (BOKUMetData_dailysum.index) #JULIAN DAY
f = lambda x: datestdtojd(str(x)[:-9])
BOKUMetData_dailysum['JD'] = BOKUMetData_dailysum['JD'].apply(f)

#FILTER - GLOBAL RADIATION
juliandays = range(365)
thres_glob = []
#APOLIS in kWh/m2 (Tagessumme Globalstrahlung) ! thres_glob = ((1.25e-12)*(x**5)+ (7.38e-9)*(x**4) - (5.365e-6)*(x**3) + 0.000926*(x**2) - 0.00036*x + 1.08)*0.9
for x in juliandays:
    thres_glob.append(((1.25e-12)*(x**5)+ (7.38e-9)*(x**4) - (5.365e-6)*(x**3) + 0.000926*(x**2) - 0.00036*x + 1.08)*0.9*1000)  #in Wh/m2 Tagessumme

f2 = lambda x: (((1.25e-12)*(x**5)+ (7.38e-9)*(x**4) - (5.365e-6)*(x**3) + 0.000926*(x**2) - 0.00036*x + 1.08)*0.9*1000)
BOKUMetData_dailysum["GRthres"] = BOKUMetData_dailysum['JD'].apply(f2)

isHighGR = BOKUMetData_dailysum["GR"] > BOKUMetData_dailysum["GRthres"]
HighGRdays = BOKUMetData_dailysum[isHighGR]
#print(HighGRdays)

BOKUMetData_monthly = BOKUMetData.resample('M').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})

BOKUMetData_dailymax_m = BOKUMetData_dailymax.resample('M').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})

BOKUMetData_dailymax_w = BOKUMetData_dailymax.resample('W').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})

AT_dmax_sigma= BOKUMetData_dailymax["AT"].std()


"read in EDO - SPI data"
spi = pd.read_csv("/windata/DATA/obs_point/land/EDO/SPI_16_48.2017to2021.20211206100030.txt", delimiter="|",skiprows=2,header=0)
spi = spi.set_index(pd.to_datetime(spi['Date'])) #utc=True
spi = spi.drop(columns=['Date'])
spi = spi[4:-4]
#print(spi)
#exit()


"read in VINDOBONA"

foldername_D = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
foldername_K = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_KQ"
foldername_glyoxal = "/windata/DATA/remote/ground/maxdoas/chocho2020"

hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D", begin= datetime(2017, 5, 1, 0, 0, 0))
hchoK_d, hchoK_dmax, hchoK_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_K,"K", begin= datetime(2020, 1, 1, 0, 0, 0))
#hchoK_d, hchoK_dmax, hchoK_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_K,"K", begin= datetime.datetime(2020, 1, 1, 0, 0, 0)))
#print(len(hchoK_dmax))
#print(len(hcho_dmax))
chochoD_dmax, chochoK_dmax = ReadinVindobona_Glyoxal.loadfileALL(foldername_glyoxal)

nw = pd.concat([hcho_d,BOKUMetData_dailymax_w["WD"][datetime(2017,5,1):datetime(2021,8,31)]],axis=1)
nw.columns =['hcho', 'WD']
nw.index.name = 'datetime'
nw =nw.loc[(nw['WD'] >=270) & (nw['WD'] <=359)]

hcho_dmax_m = hcho_dmax.resample('M').mean()
#hcho_d_m = hcho_d.resample('M').mean()   #TODO switch between all data and nw only
hcho_d_m = nw['hcho'].resample('M').mean()
#print(hcho_d_m)

hcho_d_m_spring = hcho_d_m.loc[(hcho_d_m.index.month>=3)&(hcho_d_m.index.month<=5)]
spi3_d_m_spring = spi.loc[(spi.index.month>=3)&(spi.index.month<=5)]
hcho_d_m_winter = hcho_d_m.loc[(hcho_d_m.index.month<=2)|(hcho_d_m.index.month>=12)]
spi3_d_m_winter = spi.loc[(spi.index.month<=2)|(spi.index.month>=12)]
hcho_d_m_summer = hcho_d_m.loc[(hcho_d_m.index.month>=6)&(hcho_d_m.index.month<=8)]
spi3_d_m_summer = spi.loc[(spi.index.month>=6)&(spi.index.month<=8)]
hcho_d_m_autumn = hcho_d_m.loc[(hcho_d_m.index.month>=9)&(hcho_d_m.index.month<=11)]
spi3_d_m_autumn = spi.loc[(spi.index.month>=9)&(spi.index.month<=11)]

hcho_d_m_jfm = hcho_d_m.loc[(hcho_d_m.index.month>=1)&(hcho_d_m.index.month<=3)]
spi3_d_m_jfm = spi.loc[(spi.index.month>=1)&(spi.index.month<=3)]
hcho_d_m_fma = hcho_d_m.loc[(hcho_d_m.index.month>=2)&(hcho_d_m.index.month<=4)]
spi3_d_m_fma = spi.loc[(spi.index.month>=2)&(spi.index.month<=4)]

hcho_dmax_w = hcho_dmax.resample('W').mean()
hcho_dmax_sigma = hcho_dmax.std()#(axis=1)

print(hcho_dmax_sigma)
#exit()

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
#print(o3_1990_2019_mda1)
o3_2020_mda8 = o3_2020_mda1.resample('8H', label='right').mean()
o3_2020_mda8 = o3_2020_mda8.resample('D').mean()

o3_1990_2020_mda8 = pd.concat([o3_1990_2019_mda8, o3_2020_mda8], axis=0)
o3_1990_2020_mda8 = o3_1990_2020_mda8["AT9STEF"]#*ugm3toppb_o3 #MUG->PPB
o3_1990_2020_m = o3_1990_2020_mda8[datetime(1990,1,1):datetime(2021,12,30)].resample('M').mean()
o3_1990_2020_m = o3_1990_2020_m[:-1]


"""Timeserie HCHO_SPI"""

#figure = plt.figure
#ax1 = plt.gca()
#ax2 = ax1.twinx()
#ax3 = ax1.twinx()
#ax1.plot(spi['SPI-3'][datetime(2018,1,1):datetime(2020,12,31)], color="orange", label="SPI-3")
#ax1.plot(spi['SPI-6'][datetime(2018,1,1):datetime(2020,12,31)], color="red", label="SPI-6")
#ax2.plot(hcho_d_m[datetime(2018,1,1):datetime(2020,12,31)],color="black", label= "HCHO")
#ax3.plot(o3_1990_2020_m[datetime(2018,1,1):datetime(2020,12,31)],color="violet", label= "O3")
#ax1.legend(loc="upper left")
#ax2.legend(loc="upper right")
#ax3.legend(loc="lower right")
#ax1.set_ylabel("[-]")
#ax2.set_ylabel("[ppb]")
#ax3.set_ylabel("[ug m-3]")
#plt.show()

host = host_subplot(111, axes_class=axisartist.Axes)
plt.subplots_adjust(right=0.75)
par1 = host.twinx()
par2 = host.twinx()
par2.axis["right"] = par2.new_fixed_axis(loc="right", offset=(60, 0))
par1.axis["right"].toggle(all=True)
par2.axis["right"].toggle(all=True)
p1, = host.plot(spi['SPI-3'][datetime(2018,4,1):datetime(2018,10,31)], color="orange", linewidth="2", label="SPI-3")
p1, = host.plot(spi['SPI-6'][datetime(2018,4,1):datetime(2018,10,31)], color="red", linewidth="2",label="SPI-6")
p2, = par1.plot(hcho_d_m[datetime(2018,4,1):datetime(2018,10,31)], color="black", label="HCHO")
p3, = par2.plot(o3_1990_2020_m[datetime(2018,4,1):datetime(2018,10,31)],color="violet", label="O3")

p1, = host.plot(spi['SPI-3'][datetime(2019,4,1):datetime(2019,10,31)], color="orange", linewidth="2")
p1, = host.plot(spi['SPI-6'][datetime(2019,4,1):datetime(2019,10,31)], color="red", linewidth="2")
p2, = par1.plot(hcho_d_m[datetime(2019,4,1):datetime(2019,10,31)], color="black")
p3, = par2.plot(o3_1990_2020_m[datetime(2019,4,1):datetime(2019,10,31)],color="violet")

p1, = host.plot(spi['SPI-3'][datetime(2020,4,1):datetime(2020,10,31)], color="orange", linewidth="2")
p1, = host.plot(spi['SPI-6'][datetime(2020,4,1):datetime(2020,10,31)], color="red", linewidth="2")
p2, = par1.plot(hcho_d_m[datetime(2020,4,1):datetime(2020,10,31)], color="black")
p3, = par2.plot(o3_1990_2020_m[datetime(2020,4,1):datetime(2020,10,31)],color="violet")

#host.set_xlim(0, 2)
#host.set_ylim(0, 2)
#par1.set_ylim(0, 4)
#par2.set_ylim(1, 65)
host.set_xlabel("time [months]")
host.set_ylabel("SPI [-]")
par1.set_ylabel("HCHO [ppb]")
par2.set_ylabel("O3 [ug/m-3]")

host.legend(loc="lower left")

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(p3.get_color())

plt.show()


exit()

#Regresssion seasons
"""
y5_djf = hcho_d_m_winter.values.flatten()
y5_mam = hcho_d_m_spring.values.flatten()
y5_jja = hcho_d_m_summer.values.flatten()
y5_son = hcho_d_m_autumn.values.flatten()
y5_jfm = hcho_d_m_jfm.values.flatten()
y5_fma = hcho_d_m_fma.values.flatten()

x5_SPI3_djf = spi3_d_m_winter['SPI-1'].values.flatten()
x5_SPI3_mam = spi3_d_m_spring['SPI-1'].values.flatten()
x5_SPI3_jja = spi3_d_m_summer['SPI-1'].values.flatten()
x5_SPI3_son = spi3_d_m_autumn['SPI-1'].values.flatten()
x5_SPI3_jfm = spi3_d_m_jfm['SPI-1'].values.flatten()
x5_SPI3_fma = spi3_d_m_fma['SPI-1'].values.flatten()

m5_SPI3_djf, b5_SPI3_djf = np.polyfit(x5_SPI3_djf, y5_djf, 1)
m5_SPI3_mam, b5_SPI3_mam = np.polyfit(x5_SPI3_mam, y5_mam, 1)
m5_SPI3_jja, b5_SPI3_jja = np.polyfit(x5_SPI3_jja, y5_jja, 1)
m5_SPI3_son, b5_SPI3_son = np.polyfit(x5_SPI3_son, y5_son, 1)
m5_SPI3_jfm, b5_SPI3_jfm = np.polyfit(x5_SPI3_jfm, y5_jfm, 1)
m5_SPI3_fma, b5_SPI3_fma = np.polyfit(x5_SPI3_fma, y5_fma, 1)

SRho_SPI3_djf, Sp_SPI3_djf = (stats.spearmanr(x5_SPI3_djf, y5_djf))
SRho_SPI3_mam, Sp_SPI3_mam = (stats.spearmanr(x5_SPI3_mam, y5_mam))
SRho_SPI3_jja, Sp_SPI3_jja = (stats.spearmanr(x5_SPI3_jja, y5_jja))
fig = plt.figure
plt.scatter(x5_SPI3_djf, y5_djf, color='black', label="SPI-1 winter (DJF)", s=5)
plt.scatter(x5_SPI3_jfm, y5_jfm, color='blue', label="SPI-1 JFM", s=5)
plt.scatter(x5_SPI3_fma, y5_fma, color='turquoise', label="SPI-1 FMA", s=5)
plt.scatter(x5_SPI3_mam, y5_mam, color='green', label="SPI-1 spring (MAM)", s=5)
plt.scatter(x5_SPI3_jja, y5_jja, color='red', label="SPI-1 summer (JJA)", s=5)
plt.scatter(x5_SPI3_son, y5_son, color='brown', label="SPI-1 autumn (SON)", s=5)

plt.plot(x5_SPI3_djf, m5_SPI3_djf * x5_SPI3_djf + b5_SPI3_djf, color='black')
plt.plot(x5_SPI3_jfm, m5_SPI3_jfm * x5_SPI3_jfm + b5_SPI3_jfm, color='blue')
plt.plot(x5_SPI3_fma, m5_SPI3_fma * x5_SPI3_fma + b5_SPI3_fma, color='turquoise')
plt.plot(x5_SPI3_mam, m5_SPI3_mam * x5_SPI3_mam + b5_SPI3_mam, color='green')
plt.plot(x5_SPI3_jja, m5_SPI3_jja * x5_SPI3_jja + b5_SPI3_jja, color='red')
plt.plot(x5_SPI3_son, m5_SPI3_son * x5_SPI3_son + b5_SPI3_son, color='brown')
plt.ylabel("HCHO [ppb]", size="small")
plt.xlabel("SPI [-]", size="small")
plt.legend(loc="upper right")
#plt.title("full year")
#plt.title('r={:.2f} \n p={:.2f} \n n=52'.format(SRho_SPI, Sp_SPI), fontsize='small')
plt.show()

"""
#Regression SPI-HCHO
"""
y5 = hcho_d_m.values.flatten()  #Mai 17 - Aug 2021
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
plt.ylabel("HCHO [ppb]", size="small")
plt.xlabel("SPI [-]", size="small")
plt.legend()
plt.title("full year")
#plt.title('r={:.2f} \n p={:.2f} \n n=52'.format(SRho_SPI, Sp_SPI), fontsize='small')
plt.show()
"""
pff = pd.concat([hcho_dmax, BOKUMetData_dailymax["AT"],HighGRdays["GR"],HighGRdays["WD"]],axis=1)
pff.columns =['hcho', 'AT', 'GR', 'WD']
#pff = pff.dropna()
pffNW = pff.loc[(pff['WD'] >=270) & (pff['WD'] <=359)]
pffNW = pffNW.dropna()
pffSE = pff.loc[(pff['WD'] >=90) & (pff['WD'] <=180)]
pffSE = pffSE.dropna()
pffK = pd.concat([hchoK_dmax, BOKUMetData_dailymax["AT"],HighGRdays["GR"],HighGRdays["WD"]],axis=1)
pffKNW = pffK.loc[(pff['WD'] >=270) & (pffK['WD'] <=359)]
pffKNW = pffKNW.dropna()
pffKSE = pffK.loc[(pff['WD'] >=90) & (pffK['WD'] <=180)]
pffKSE = pffKSE.dropna()
pffCHOCHO = pd.concat([chochoD_dmax, BOKUMetData_dailymax["AT"],HighGRdays["GR"],HighGRdays["WD"]],axis=1)
pff.columns =['chocho', 'AT', 'GR', 'WD']
pff = pff.dropna()
pffNWcho = pffCHOCHO.loc[(pff['WD'] >=270) & (pffCHOCHO['WD'] <=359)]
pffNWcho = pffNWcho.dropna()
pffSEcho = pffCHOCHO.loc[(pff['WD'] >=90) & (pffCHOCHO['WD'] <=180)]
pffSEcho = pffSEcho.dropna()

hcho_dmax = pffNW['hcho']  #TODO: keep changes for ONLY NW or delete this line to go back to not filtered version

hcho_dmax17 = hcho_dmax[datetime(2017,5,1,0,0):datetime(2017,12,31,0,0)]
hcho_17fill = np.full(shape=120,fill_value=np.NaN)
hcho_dmax17_a = np.append(hcho_17fill, hcho_dmax17)
hcho_dmax18 = hcho_dmax[start2018:datetime(2018,12,31,0,0)]
hcho_dmax19 = hcho_dmax[start2019:datetime(2019,12,31,0,0)]
hcho_dmax20 = hcho_dmax[start2020:datetime(2020,12,31,0,0)]
hcho_dmax21 = hcho_dmax[start2021:end2021]

#print(hcho_dmax17_a,hcho_dmax18,hcho_dmax19,hcho_dmax20,hcho_dmax21)


hcho_dmax17_m = hcho_dmax17.resample('W').mean()
hcho_17fill_m = np.full(shape=4,fill_value=np.NaN)
hcho_dmax17_a_m = np.append(hcho_17fill_m, hcho_dmax17_m)
hcho_dmax18_m = hcho_dmax18.resample('W').mean()
hcho_dmax19_m = hcho_dmax19.resample('W').mean()
hcho_dmax20_m = hcho_dmax20.resample('W').mean()
hcho_dmax21_m = hcho_dmax21.resample('W').mean()
#print(hcho_dmax17_m, hcho_dmax18_m,hcho_dmax19_m,hcho_dmax20_m,hcho_dmax21_m)

#print(hcho_dmax17, hcho_dmax18_m, hcho_dmax19_m, hcho_dmax20_m)

"""
#read in soil moisture data
"""
file_rss_rutz = "/windata/DATA/obs_point/land/Bodenfeuchte_Rutzendorf/2008_2020_Rutzendorf_ARIS_results_sepp.xlsx"
rss = pd.read_excel(file_rss_rutz, sheet_name="RSS_top", usecols="A,B,C,D,E,F", skiprows=11)#, converters={'A': pd.to_datetime})
rss.columns = ['datetime', 'RSS_top_maize', 'RSS_top_sBarley','RSS_top_sugBeet','RSS_top_wWheat', 'RSS_top_grass']  #TODO: local time!
rss = rss.set_index(pd.to_datetime(rss['datetime']))
rss = rss.drop(columns=['datetime'])

rss_sub = pd.read_excel(file_rss_rutz, sheet_name="RSS_sub", usecols="A,B,C,D,E,F", skiprows=11)#, converters={'A': pd.to_datetime})
rss_sub.columns = ['datetime', 'RSS_sub_maize', 'RSS_sub_sBarley','RSS_sub_sugBeet','RSS_sub_wWheat', 'RSS_sub_grass']  #TODO: local time!
rss_sub = rss_sub.set_index(pd.to_datetime(rss_sub['datetime']))
rss_sub = rss_sub.drop(columns=['datetime'])

#RSS climatological mean difference
mean12yr_d = rss_sub.groupby([rss_sub.index.month, rss_sub.index.day]).mean()
mean12yr_d["new_index"] = mean12yr_d.index.map(lambda x:datetime(2000, x[0], x[1]))
mean12yr_d = mean12yr_d.set_index("new_index")
#print(mean12yr_d['RSS_sub_wWheat'])
mean12yr_d_noleap = mean12yr_d.drop(pd.date_range('2000-02-29','2000-2-29'), errors='ignore') #remove 29.Feb
#print(mean12yr_d['2000-02-28':'2000-03-2'])

rss_sub17_diff_w = rss_sub['RSS_sub_wWheat'][datetime(2017,5,1):datetime(2017,12,31)].sub(mean12yr_d_noleap['RSS_sub_wWheat'][datetime(2000,5,1):].values)
rss_sub18_diff_w = rss_sub['RSS_sub_wWheat'][datetime(2018,1,1):datetime(2018,12,31)].sub(mean12yr_d_noleap['RSS_sub_wWheat'].values)
rss_sub19_diff_w = rss_sub['RSS_sub_wWheat'][datetime(2019,1,1):datetime(2019,12,31)].sub(mean12yr_d_noleap['RSS_sub_wWheat'].values)
rss_sub20_diff_w = rss_sub['RSS_sub_wWheat'][datetime(2020,1,1):datetime(2020,12,31)].sub(mean12yr_d['RSS_sub_wWheat'].values)
rss_sub_diff_w = pd.concat([rss_sub17_diff_w,rss_sub18_diff_w,rss_sub19_diff_w,rss_sub20_diff_w])
#print(rss_sub_diff_w)
""" FIGURE 8 """

print(hcho_dmax18_m, hcho_dmax19_m, hcho_dmax20_m)

figure = plt.figure
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
#plt.title("")
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax1.plot(range(len(hcho_dmax18_m)),hcho_dmax18_m, color='blue', linestyle="", marker="x", label="2018")
ax1.plot(range(len(hcho_dmax19_m)),hcho_dmax19_m, color='green', linestyle="", marker="x",label="2019")
ax1.plot(range(len(hcho_dmax20_m)),hcho_dmax20_m, color='orange', linestyle="", marker="x",label="2020")
#plt.plot(yM21,hcho_dmax21_m, color='red', linewidth=1, marker="x",label="2021")
plt.title("NW days")
ax1.grid(True)
ax2.grid(True)
plt.xticks(yM, yM_ticks)
#ax2.plot(range(len(hcho_dmax20_m)),hcho_dmax20_m["hcho"]-hcho_dmax19_m["hcho"], color='green', linewidth=1, marker="x",label="2020-19")
#ax2.plot(range(len(hcho_dmax20_m)),hcho_dmax20_m-hcho_dmax18_m, color='blue', linewidth=1, marker="x",label="2020-18")
plt.xlabel("days")
plt.ylabel("hcho [ppb]")
plt.legend()
plt.show()

figure = plt.figure
ax1 = plt.gca()
ax2 = ax1.twinx()
#ax1.plot(pffNW['AT'],color='powderblue',label="NW AT_max", linewidth=2)
#ax1.plot(pffSE['AT'],color='peachpuff',label="SE AT_max", linewidth=2)
#ax1.plot(pffKNW['AT'],color='lightblue',label="NW AT_max", linestyle="-", linewidth=2)
#ax1.plot(pffKSE['AT'],color='lightred',label="SE AT_max",  linestyle="-", linewidth=2)
#ax1.plot(BOKUMetData_dailymax['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=0.5)
#ax1.plot(BOKUMetData_dailymax_m['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=1)
#ax1.plot(BOKUMetData_dailymax_w['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=2)
ax2.plot(pffNW['hcho'], color='blue', label="NW hcho_max D", marker="x", linestyle="-", linewidth=0.5)
ax2.plot(pffSE['hcho'], color='red', label="SE hcho_max D", marker="x", linestyle="-", linewidth=0.5)
ax2.plot(pffKNW['hcho'], color='turquoise', label="NW hcho_max K", marker="x", linestyle="-", linewidth=0.5)
ax2.plot(pffKSE['hcho'], color='orange', label="SE hcho_max K", marker="x", linestyle="-", linewidth=0.5)
ax1.plot(pffNWcho['chocho'], color='brown', label="NW chocho D", linestyle="-", linewidth=1)
ax1.plot(pffSEcho['chocho'], color='violet', label="SE chocho D", linestyle="-", linewidth=1)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
#plt.xticks(yM, yM_ticks)
plt.xlabel("time [days]")
ax2.set_ylabel("VMR hcho [ppb]")
ax1.set_ylabel("DSC [Molek / cmý]")
#ax1.set_ylabel("air temperature [°C]")
#ax1.set_ylim(-5, 80)
#ax2.set_ylim(0, 6)
plt.legend()
plt.show()

N=7 #days
atmaxSE_5daymean = np.convolve(pffSE['AT'], np.ones(N)/N, mode='valid')
atmaxNW_5daymean = np.convolve(pffNW['AT'], np.ones(N)/N, mode='valid')
hchomaxSE_5daymean = np.convolve(pffSE['hcho'], np.ones(N)/N, mode='valid')
hchomaxNW_5daymean = np.convolve(pffNW['hcho'], np.ones(N)/N, mode='valid')

Runningmean_5daysSE = pffSE[6:]
Runningmean_5daysSE.insert(1,'AT5d', atmaxSE_5daymean.tolist())
Runningmean_5daysSE.insert(1,'hcho5d', hchomaxSE_5daymean.tolist())
#print(Runningmean_5daysSE['AT5d'])
Runningmean_5daysNW = pffNW[6:]
Runningmean_5daysNW.insert(1,'AT5d', atmaxNW_5daymean.tolist())
Runningmean_5daysNW.insert(1,'hcho5d', hchomaxNW_5daymean.tolist())
#print(Runningmean_5daysNW['AT5d'])

pffSE_veg = pffSE.loc[(pffSE.index.month>=4)&(pffSE.index.month<=10)]
pffSE_noveg = pffSE.loc[(pffSE.index.month>=11)|(pffSE.index.month<=3)]
pffNW_veg = pffNW.loc[(pffNW.index.month>=4)&(pffNW.index.month<=10)]
pffNW_noveg = pffNW.loc[(pffNW.index.month>=11)|(pffNW.index.month<=3)]

print("all: \n ")
print(pffSE,pffNW)
print("AT SE:", pffSE['AT'].mean()," AT NW:", pffNW['AT'].mean()," hcho SE:", pffSE['hcho'].mean(), " hcho NW:", pffNW['hcho'].mean())
print("veg: \n ")
print(pffSE_veg, pffNW_veg)
print("AT SE:", pffSE_veg['AT'].mean()," AT NW:", pffNW_veg['AT'].mean()," hcho SE:", pffSE_veg['hcho'].mean(), " hcho NW:", pffNW_veg['hcho'].mean())
print("noveg: \n ")
print(pffSE_noveg, pffNW_noveg)
print("AT SE:", pffSE_noveg['AT'].mean()," AT NW:", pffNW_noveg['AT'].mean()," hcho SE:", pffSE_noveg['hcho'].mean(), " hcho NW:", pffNW_noveg['hcho'].mean())



""" FIGURE 5 """
commonstart = datetime(2017,6,14)
commonend = datetime(2021,8,12)

figure = plt.figure
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
ax1 = plt.subplot(gs[0])
ax1 = plt.gca()
#ax2 = ax1.twinx()
ax3 = plt.subplot(gs[1])
ax3 = plt.gca()
#ax4 = ax3.twinx()
ax1.plot(Runningmean_5daysSE['AT5d'],color='red',label="SE", linewidth=2,linestyle="",marker="o",markersize=5) #pffNW['AT']
ax1.plot(Runningmean_5daysNW['AT5d'],color='blue',label="NW", linewidth=2,linestyle="",marker="o",markersize=5) #pffSE['AT']
#ax1.plot(pffKNW['AT'],color='lightblue',label="NW AT_max", linestyle="-", linewidth=2)
#ax1.plot(pffKSE['AT'],color='lightred',label="SE AT_max",  linestyle="-", linewidth=2)
#ax1.plot(BOKUMetData_dailymax['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=0.5)
#ax1.plot(BOKUMetData_dailymax_m['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=1)
#ax1.plot(BOKUMetData_dailymax_w['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=2)
#ax2.plot(pffNW['hcho'], color='blue', label="NW hcho_max D", marker="x", linestyle="-", linewidth=0.5)
#ax2.plot(pffSE['hcho'], color='red', label="SE hcho_max D", marker="x", linestyle="-", linewidth=0.5)
#ax2.plot(pffKNW['hcho'], color='turquoise', label="NW hcho_max K", marker="x", linestyle="-", linewidth=0.5)
#ax2.plot(pffKSE['hcho'], color='orange', label="SE hcho_max K", marker="x", linestyle="-", linewidth=0.5)
#plt.xticks(yM, yM_ticks)
ax1.set_ylabel("AT [°C]")
#ax1.set_ylim(-5, 80)
ax3.plot(Runningmean_5daysSE['hcho'],color='red',label="SE AT_max", linewidth=2,linestyle="",marker="o",markersize=5) #pffNW['AT']
ax3.plot(Runningmean_5daysNW['hcho'],color='blue',label="NW AT_max", linewidth=2,linestyle="",marker="o",markersize=5) #pffSE['AT']
ax3.set_ylabel("HCHO [ppb]")
#ax3.plot(Runningmean_5daysSE['AT5d'][commonstart:commonend] - Runningmean_5daysNW['AT5d'][commonstart:commonend], color='black',label="SE - NW AT_dmax 5 day gliding mean", linewidth=2)
#ax3.plot(pffNW['AT'].resample("2W").mean(),color='black',label="NW AT_dmax weekly", linewidth=2)
#ax3.plot(pffSE['AT'].resample("2W").mean() - pffNW['AT'].resample("2W").mean(),color='black',label="SE - NW AT_dmax weekly", linewidth=2)
#ax4.plot(Runningmean_5daysSE['hcho5d'][commonstart:commonend] - Runningmean_5daysNW['hcho5d'][commonstart:commonend], color='blue', label="SE - NW hcho dmax 5 day gliding mean", linewidth=2)
#ax3.set_ylabel(r"$\Delta$ air temperature [°C]")
#ax4.set_ylabel(r"$\Delta$ VMR hcho [ppb]")
#ax2.set_ylim(0, 6)
ax1.legend(loc='lower left')
#ax2.legend(loc='upper right')
#ax3.legend(loc='upper left')
#ax4.legend(loc='upper right')
plt.xlabel("time [days]")
plt.show()

""" FIGURE 1 """
figure = plt.figure
gs = gridspec.GridSpec(3, 1,height_ratios=[1,1,1])
#plt.title("wWheat, 40-100 cm")
ax1 = plt.subplot(gs[0])
#ax1 = plt.gca()
#ax2 = ax1.twinx()
#ax3 = ax1.twinx()
ax2 = plt.subplot(gs[1])
ax3 = plt.subplot(gs[2])

#ax2.plot(hcho_dmax, color='black', label="HCHO dmean", linewidth=0.1)
#ax2.plot(hcho_dmax17, color='violet', label="2017", linewidth=0.1)
#ax2.plot(hcho_dmax18, color='blue', label="2018", linewidth=0.1)
#ax2.plot(hcho_dmax19, color='green', label="2019", linewidth=0.1)
#ax2.plot(hcho_dmax20, color='orange', label="2020", linewidth=0.1)
#ax2.plot(hcho_dmax21, color='violet', label="2021", linewidth=0.1)
AT = BOKUMetData_dailymax_m[start2017:end2021]['AT']
print(AT)
#ax1.plot(BOKUMetData_dailymax['AT'][start2017:end2021],color='grey',label="AT dmax", linewidth=0.1)
ax1.fill_between(AT.index, AT+AT_dmax_sigma,AT - AT_dmax_sigma, facecolor='grey', alpha=0.2)
#ax1.plot(AT,color='grey',label="AT dmax monthly", linewidth=1)
ax1.plot(BOKUMetData_dailymax_w['AT'][start2017:end2021],color='grey',label="AT dmax weekly", linewidth=2)

#interestingdates = [datetime(2017,9,30),datetime(2017,10,22),datetime(2018,8,5),datetime(2021,5,30)]
#ax1.axvline(x=interestingdates)
#ax1.axvline(x=datetime(2017,9,30))
#ax1.axvline(x=datetime(2017,10,22))
#ax1.axvline(x=datetime(2018,8,5))
#ax1.axvline(x=datetime(2021,5,30))
#ax2.axvline(x=datetime(2017,9,30))
#ax2.axvline(x=datetime(2017,10,22))
#ax2.axvline(x=datetime(2018,8,5))
#ax2.axvline(x=datetime(2021,5,30))
#ax3.axvline(x=datetime(2017,9,30))
#ax3.axvline(x=datetime(2017,10,22))
#ax3.axvline(x=datetime(2018,8,5))
#ax3.axvline(x=datetime(2021,5,30))

#ax1.axvline(x=datetime(2020,9,6))
#ax2.axvline(x=datetime(2020,9,6))
#ax3.axvline(x=datetime(2020,9,6))

#ax1.axvline(x=datetime(2019,10,6))
#ax2.axvline(x=datetime(2019,10,6))
#ax3.axvline(x=datetime(2019,10,6))


ax2.fill_between(hcho_dmax_m[start2017:end2021].index, hcho_dmax_m[start2017:end2021]+hcho_dmax_sigma, hcho_dmax_m[start2017:end2021] - hcho_dmax_sigma, facecolor='purple', alpha=0.2)
#ax2.plot(hcho_dmax_m[start2017:end2021], color="purple",label="HCHO dmax monthly",linewidth=1)
ax2.plot(hcho_dmax_w[start2017:end2021], color="purple",label="HCHO dax weekly",linewidth=2)
#ax2.set_title(r'hcho observation $\mu$ and $\pm \sigma$ interval')

ax3.plot(vpd_dmax_w[start2017:end2021], color="blue", label="vpd_dmax weekly", linewidth=2)
ax3.fill_between(vpd_dmax_w[start2017:end2021].index,vpd_dmax_w[start2017:end2021]+vpd_dmax_sigma, vpd_dmax_w[start2017:end2021]-vpd_dmax_sigma, facecolor="blue", alpha=0.2)
#ax3.plot(vpd_dmax[start2017:end2021], color="blue", label="vpd_dmax weekly", linewidth=0.1)
#ax3.plot(rss_sub_diff_w,color="black", label="rss_diff")
#ax3.axhline(y=0,color='black')
#upper = 0.0
#supper = np.ma.masked_where(rss_sub_diff_w > upper, rss_sub_diff_w)
#slower = np.ma.masked_where(rss_sub_diff_w < upper, rss_sub_diff_w)
#ax.plot(t, slower, t, supper)
#ax2.legend(loc="lower right")
#ax1.legend(loc="lower right")
#ax3.legend(loc="lower right")
#plt.xticks(yM, yM_ticks)
plt.xlabel("time [days]")
ax3.set_ylabel("VPD [kPa]")
ax2.set_ylabel("HCHO [ppb]")
ax1.set_ylabel("AT [°C]")
#ax1.set_ylim(-5, 80)
#ax2.set_ylim(0, 6)
plt.show()
