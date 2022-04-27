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
p1, = host.plot(spi['SPI-3'][datetime(2018,2,1):datetime(2018,10,31)], color="orange", linewidth="2", label="SPI-3")
#p1, = host.plot(spi['SPI-6'][datetime(2018,4,1):datetime(2018,10,31)], color="red", linewidth="2",label="SPI-6")
p2, = par1.plot(hcho_d_m[datetime(2018,2,1):datetime(2018,10,31)], color="black", label="HCHO")
p3, = par2.plot(o3_1990_2020_m[datetime(2018,2,1):datetime(2018,10,31)],color="violet", label="O3")

p1, = host.plot(spi['SPI-3'][datetime(2019,2,1):datetime(2019,10,31)], color="orange", linewidth="2")
#p1, = host.plot(spi['SPI-6'][datetime(2019,4,1):datetime(2019,10,31)], color="red", linewidth="2")
p2, = par1.plot(hcho_d_m[datetime(2019,2,1):datetime(2019,10,31)], color="black")
p3, = par2.plot(o3_1990_2020_m[datetime(2019,2,1):datetime(2019,10,31)],color="violet")

p1, = host.plot(spi['SPI-3'][datetime(2020,2,1):datetime(2020,10,31)], color="orange", linewidth="2")
#p1, = host.plot(spi['SPI-6'][datetime(2020,4,1):datetime(2020,10,31)], color="red", linewidth="2")
p2, = par1.plot(hcho_d_m[datetime(2020,2,1):datetime(2020,10,31)], color="black")
p3, = par2.plot(o3_1990_2020_m[datetime(2020,2,1):datetime(2020,10,31)],color="violet")

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
