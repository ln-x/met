# -*- coding: utf-8 -*-
__author__ = 'lnx'

import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime
import netCDF4
from met.library import ReadinVindobona_Filter_fullperiod
from scipy import stats
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
from dateutil import rrule

"""READ IN MGNOUT CAMS"""
foldername_ol = "/data1/models/nilu/SEEDS/MEGAN/2019/ol/ISOP/"  #MGNOUT_CAMS_BIG_ISOP_20190102.nc
foldername_as = "/data1/models/nilu/SEEDS/MEGAN/2019/assim_LAI/ISOP/"

#The isoprene emissions are in units of mole m-2 s-1.
# bottom-up isoprene emissions for 2019 using the MEGAN-SURFEX coupling at NILU has been completed.
# This includes the correction to PAR, and the emission totals are now much more consistent with existing datasets,
# e.g., CAMS-GLOBAL-BIOGENIC. For instance, for 2019, using the SURFEX data from the assimilation of LAI,
# we get an annual total of 5.15 Tg yr-1 (see attached) compared to approx. 4.95 Tg yr-1 from CAMS-GLOBAL-BIO v3.1 and
# 4.65 Tg yr-1 from CAMS-GLOBAL-BIO v3.0.

def EmisSEEDS(foldername):
    files = os.listdir(foldername)
    files = sorted(files)
    dateaxis=[]
    Emis_max=[]
    Emis_noontime=[]
    Emis_noon=[]
    index_lat = 202  #LAT 48.25°N
    index_lon = 422 #LON 16.25°E (city rim to Wienerwald) or 421: LON 16.15°E (middle Wienerwald)
    for i in range(len(files)):
        day = str(files[i][-5:-3])  # splitlistcomp[3:4]
        month = str(files[i][-7:-5])  # splitlistcomp[2:3]
        year = "20" + str(files[i][-9:-7])  # splitlistcomp[:2]
        #print(day,month,year)
        date = datetime.datetime(year=int(year), month=int(month), day=int(day))
        #print(date)
        dateaxis.append(date)
        path = foldername+files[i]
        infile = netCDF4.Dataset(path)  #path.decode('UTF-8')  #OSError: [Errno -51] NetCDF: Unknown file format: b'/windata/DATA/models/nilu/MEGAN3_SURFEX_SEEDS/MEGAN/ol/MGNOUT_CAMS_BIG_20190803.nc'
        Emis_hourlyvalue = infile.variables['Emiss'][:, index_lat, index_lon, 0]  #TODO: only first emission layer (ISO) read in
        Emis_max.append(Emis_hourlyvalue.max())
        #print(Emis_hourlyvalue)
        #Emis_hourly.append(Emis_hourlyvalue)
        Emis_noon = np.average(Emis_hourlyvalue[8:14])
        Emis_noontime.append(Emis_noon)
    Emis_max = pd.DataFrame({'datetime': dateaxis, 'ISO': Emis_max})
    Emis_max['datetime'] = pd.to_datetime(Emis_max['datetime'])
    Emis_max = Emis_max.set_index(['datetime'])
    Emis_noontime = pd.DataFrame({'datetime': dateaxis, 'ISO': Emis_noontime})
    Emis_noontime['datetime'] = pd.to_datetime(Emis_noontime['datetime'])
    Emis_noontime = Emis_noontime.set_index(['datetime'])
    return Emis_max, Emis_noontime

Emis_ol, Emis_ol_noontime = EmisSEEDS(foldername_ol)
Emis_assim, Emis_assim_noontime = EmisSEEDS(foldername_as)

"read in SAFAEs MEGAN2.1-SURFEX results"
file_ol = "/data1/models/cnrm/201906/ISBA_DIAGNOSTICS.OUT.nc"
file_ol2 = "/data1/models/cnrm/201907/ISBA_DIAGNOSTICS.OUT.nc"

#file_ol_2 = "/data1/models/cnrm/201907/ISBA_DIAGNOSTICS.OUT_lat202lon422.nc"
# Isoprene data are available in the ISBA_DIAGNOSTICS.OUT.nc file
# with a description of the activity_factor, soil moisture activity factor (gamma_sm),
# leaf age activity factor (gamma_age). You can find the 16 PFTs distribution and data of PPFD calculated by megan.
#unit= kg/m2/s::  Molar mass of C5H8, Isoprene is 68.11702 g/mol  -> 1 mol = 1 kg * (1/68*1000)

f_ol_201906 = netCDF4.Dataset(file_ol, mode='r')
f_ol_201907 = netCDF4.Dataset(file_ol2, mode='r')
f_ol_units = f_ol_201907.variables['ISOPRENE'].units
ISO_201906 = f_ol_201906.variables['ISOPRENE'][:,202,422]
ISO_201907 = f_ol_201907.variables['ISOPRENE'][:,202,422]
ISO_201906_mol = ISO_201906*14.7058824 #(1/0.06811702)
ISO_201907_mol = ISO_201907*14.7058824 #(1/0.06811702)
#f_ol_201907.close
start = datetime.datetime(2019,6,1,0,0) #hours since 2019-07-01 00:00:00
stop = datetime.datetime(2019,8,1,0,0)
dts = list(rrule.rrule(rrule.HOURLY,count=1464,dtstart=start))
ISO_20190607_mol = np.ma.append(ISO_201906_mol, ISO_201907_mol)
Emis_ol2 = pd.DataFrame({'datetime': dts, 'ISO': ISO_20190607_mol})

Emis_ol2 = Emis_ol2.set_index(['datetime'])
Emis_ol2_noontime = Emis_ol2.loc[(Emis_ol2.index.hour >=9)&(Emis_ol2.index.hour <=15)] #FILTER for hours around zenith
Emis_ol2_noontime = Emis_ol2_noontime.resample("D").mean()
Emis_ol2 = Emis_ol2.resample("D").max()

"""
fig, ax = plt.subplots()
ax.plot_date(dates, ISO_201907_mol)
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
ax.set_ylabel("mol/m²/s")
plt.show()
"""
#Emis_assim_noontime.plot()
#plt.show()

"read in VINDOBONA"
foldername_D = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D",begin = datetime.datetime(2017, 5, 1, 0, 0, 0))
hcho_w = hcho_dmax.resample("W").mean()

"""
fig = plt.figure()
#plt.suptitle(f"OBS {start} - {end}")
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()
ax1.plot(Emis_ol,linewidth="1", color='darkgreen', label="MOD: MGN3,ol ISO,dmax", linestyle=":")
ax1.plot(Emis_assim,linewidth="1", color='darkblue', label="MOD: MGN3,assim ISO,dmax", linestyle=":")
ax2.plot(hcho_dmax[:],linewidth="2", color='black', label="OBS: HCHO,dmax", linestyle=":")
ax1.plot(Emis_ol2,linewidth="1", color='darkred', label="MOD: MGN2.1,ol ISO,dmax", linestyle=":")

ax1.plot(Emis_ol_noontime,linewidth="1", color='green', label="MOD: MGN3,ol ISO,9-15", linestyle="solid")
ax1.plot(Emis_assim_noontime,linewidth="1", color='blue', label="MOD: MGN3,assim ISO,9-15", linestyle="solid")
ax2.plot(hcho_d[:],linewidth="2", color='grey', label="OBS: HCHO,9-15", linestyle="solid")
ax1.plot(Emis_ol2_noontime,linewidth="1", color='red', label="MOD: MGN2.1,ol ISO,9-15", linestyle="solid")
ax1.set_xlabel("days")
#ax1.set_xlim(start,end)
ax1.set_ylabel("[mol s-1 m-2]", size="medium")
ax2.set_ylabel("[ppb]", size="medium")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()
"""


def Plot6var(df1, df2, Emis_ol2, df3, title):
    #print(df2.ISO,df3)
    Emis_052019_as = df2.ISO[datetime.datetime(2019, 5, 1, 00, 00): datetime.datetime(2019, 5, 31, 00, 00)]
    hcho_052019 = df3[datetime.datetime(2019, 5, 1, 00, 00): datetime.datetime(2019, 5, 31, 00, 00)].values.flatten()
    Emis_062019_as = df2[datetime.datetime(2019, 6, 1, 00, 00): datetime.datetime(2019, 6, 30, 00, 00)].values.flatten()
    hcho_062019 = df3[datetime.datetime(2019, 6, 1, 00, 00): datetime.datetime(2019, 6, 30, 00, 00)].values.flatten()
    Emis_072019_as = df2[datetime.datetime(2019, 7, 1, 00, 00): datetime.datetime(2019, 7, 31, 00, 00)].values.flatten()
    hcho_072019 = df3[datetime.datetime(2019, 7, 1, 00, 00): datetime.datetime(2019, 7, 31, 00, 00)].values.flatten()
    Emis_082019_as = df2[datetime.datetime(2019, 8, 1, 00, 00): datetime.datetime(2019, 8, 31, 00, 00)].values.flatten()
    hcho_082019 = df3[datetime.datetime(2019, 8, 1, 00, 00): datetime.datetime(2019, 8, 31, 00, 00)].values.flatten()
    idx_as = np.isfinite(Emis_052019_as) & np.isfinite(hcho_052019)
    SRho05, Sp05 = (stats.spearmanr(Emis_052019_as[idx_as], hcho_052019[idx_as]))
    #m5_as, b5_as = np.polyfit(Emis_JJA2019_as[idx_as], hcho_JJA2019[idx_as], 1)
    #y_est_as = m5_as * Emis_JJA2019_as + b5_as
    color1= "palegreen"
    color2= "mediumseagreen"
    color3= "thistle"
    color4= "mediumpurple"
    a = 0
    fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(8, 3), sharey=True, dpi=100)
    #fig.suptitle(title, fontsize="small")
    axs[0].set_title('(a) May 19 \n SRho={:.2f} \n p={:.2f}'.format(SRho05, Sp05), fontsize='small')
    axs[0].scatter(Emis_052019_as, hcho_052019, color=color1, s=10)#, label="S-M3_assim")
    axs[1].set_title('(b) Jun 19')# \n SRho{:.2f} \n p={:.2f}'.format(SRho05, Sp05), fontsize='small')
    axs[1].scatter(Emis_062019_as, hcho_062019, color=color1, s=10)#, label="S-M3_assim")
    axs[2].set_title('(c) Jul 19')# \n SRho{:.2f} \n p={:.2f}'.format(SRho05, Sp05), fontsize='small')
    axs[2].scatter(Emis_072019_as, hcho_072019, color=color1, s=10)#, label="S-M3_ol")
    axs[3].set_title('(d) Aug 19')# \n SRho{:.2f} \n p={:.2f}'.format(SRho05, Sp05), fontsize='small')
    axs[3].scatter(Emis_082019_as, hcho_082019, color=color1, s=10)#, label="S-M2_ol"
    #plt.plot(Emis_JJA2019_as, y_est_as, color=color1)
    # ax0.fill_between(x5, y_est - y_err_AT, y_est + y_err_AT, alpha=0.2)
    plt.ylabel("HCHO [ppb]", size="small")
    plt.xlabel("ISOP [mol s-1 m-2]", size="small")
    #plt.ylim(0, ylimit)
    #plt.legend()
    fig.tight_layout()
    plt.show()

#Plot6var(Emis_ol, Emis_assim, Emis_ol2, hcho_dmax,"daily max", ylimit=8)
Plot6var(Emis_ol_noontime, Emis_assim_noontime, Emis_ol2_noontime, hcho_d,"noon time mean (9-15)")

exit()
def Plot6var(df1, df2, Emis_ol2, df3, title):
    #TODO: define drought/non-drought periods
    #Emis_MAM2018 = df1[datetime(2018, 3, 1, 00, 00): datetime(2018, 5, 31, 00, 00)]
    #Emis_MAM2020 = df1[datetime(2020, 3, 1, 00, 00): datetime(2020, 5, 31, 00, 00)]
    #hcho_dmaxMAM2018 = df1[datetime(2018, 3, 1, 00, 00): datetime(2018, 5, 31, 00, 00)]
    #hcho_dmaxMAM2020 = df1[datetime(2020, 3, 1, 00, 00): datetime(2020, 5, 31, 00, 00)]
    Emis_JJA2019_as = df1[datetime.datetime(2019, 6, 1, 00, 00): datetime.datetime(2019, 7, 31, 00, 00)].values.flatten()
    Emis_JJA2019_ol3 = df2[datetime.datetime(2019, 6, 1, 00, 00): datetime.datetime(2019, 7, 31, 00, 00)].values.flatten()
    hcho_JJA2019 = df3[datetime.datetime(2019, 6, 1, 00, 00): datetime.datetime(2019, 7, 31, 00, 00)].values.flatten()
    #print(Emis_JJA2019_ol3)
    #exit()

    print("Spearman Test/Significance of Linear Regression:")
    #var = [np.var(x, ddof=1) for x in [hcho_JJA2019]]
    """
    x5 = df1 #y5 = df1['hcho'].values.flatten()
    y5 = df2
    print(x5)
    idx = np.isfinite(x5) & np.isfinite(y5)
    print(idx)
    SRho, Sp = (stats.spearmanr(x5[idx], y5[idx]))
    m5, b5 = np.polyfit(x5[idx], y5[id], 1)
    """
    idx_as = np.isfinite(Emis_JJA2019_as) & np.isfinite(hcho_JJA2019)
    SRho_as, Sp_as = (stats.spearmanr(Emis_JJA2019_as[idx_as], hcho_JJA2019[idx_as]))
    m5_as, b5_as = np.polyfit(Emis_JJA2019_as[idx_as], hcho_JJA2019[idx_as], 1)
    y_est_as = m5_as * Emis_JJA2019_as + b5_as

    idx_ol3 = np.isfinite(Emis_JJA2019_ol3) & np.isfinite(hcho_JJA2019)
    SRho_ol3, Sp_ol3 = (stats.spearmanr(Emis_JJA2019_ol3[idx_ol3], hcho_JJA2019[idx_ol3]))
    m5_ol3, b5_ol3 = np.polyfit(Emis_JJA2019_ol3[idx_ol3], hcho_JJA2019[idx_ol3], 1)
    y_est_ol3 = m5_ol3 * Emis_JJA2019_ol3 + b5_ol3

    Emis_olnp = Emis_ol2.to_numpy().flatten()
    idx2 = np.isfinite(Emis_olnp) & np.isfinite(hcho_JJA2019)
    SRho2, Sp2 = (stats.spearmanr(Emis_olnp[idx2], hcho_JJA2019[idx2]))
    m52, b52 = np.polyfit(Emis_olnp[idx2], hcho_JJA2019[idx2], 1)
    y_est2 = m52 * Emis_olnp + b52

    color1= "palegreen"
    color2= "mediumseagreen"
    color3= "thistle"
    color4= "mediumpurple"
    a = 0
    fig, axs = plt.subplots(1, 1, figsize=(8, 6), dpi=100)
    fig.suptitle(title, fontsize="small")
    plt.scatter(Emis_JJA2019_as, hcho_JJA2019, color=color1, s=10, label="S-M3_assim")
    plt.scatter(Emis_JJA2019_ol3, hcho_JJA2019, color=color2, s=10, label="S-M3_ol")
    plt.scatter(Emis_olnp, hcho_JJA2019, color=color4, s=10, label="S-M2_ol")

    plt.plot(Emis_JJA2019_as, y_est_as, color=color1)
    plt.plot(Emis_JJA2019_ol3, y_est_ol3, color=color2)
    plt.plot(Emis_olnp, y_est2, color=color4)
    #axs[0, 0].set_title('(a) \n p_lowO3={:.2f} \n p_highO3={:.2f}'.format(Sp_AT, Sp_AT_2), fontsize='small')
    plt.title('JJ2019 \n'
              'S-M2_ol SRho={:.2f}, p={:.2f} \n'
              'S-M3_ol SRho={:.2f}, p={:.2f} \n'
              'S-M3_as SRho={:.2f}, p={:.2f}'.format(SRho2, Sp2, SRho_ol3, Sp_ol3, SRho_as, Sp_as), fontsize='small')

    # ax0.fill_between(x5, y_est - y_err_AT, y_est + y_err_AT, alpha=0.2)
    plt.ylabel("HCHO [ppb]", size="small")
    plt.xlabel("ISOP [mol s-1 m-2]", size="small")
    #plt.ylim(0, ylimit)
    plt.legend()
    fig.tight_layout()
    plt.show()
    #plt.savefig("/home/heidit/Downloads/" + title + ".jpg")

    fig, axs = plt.subplots(1, 1, figsize=(8, 6), dpi=100)
    fig.suptitle(title, fontsize="small")
    plt.scatter(Emis_JJA2019_as, hcho_JJA2019, color=color1, s=10, label="S-M3_assim")
    plt.scatter(Emis_JJA2019_ol3, hcho_JJA2019, color=color2, s=10, label="S-M3_ol")
    plt.scatter(Emis_olnp, hcho_JJA2019, color=color4, s=10, label="S-M2_ol")

    plt.plot(Emis_JJA2019_as, y_est_as, color=color1)
    plt.plot(Emis_JJA2019_ol3, y_est_ol3, color=color2)
    plt.plot(Emis_olnp, y_est2, color=color4)
    #axs[0, 0].set_title('(a) \n p_lowO3={:.2f} \n p_highO3={:.2f}'.format(Sp_AT, Sp_AT_2), fontsize='small')
    plt.title('JJ2019 \n'
              'S-M2_ol SRho={:.2f}, p={:.2f} \n'
              'S-M3_ol SRho={:.2f}, p={:.2f} \n'
              'S-M3_as SRho={:.2f}, p={:.2f}'.format(SRho2, Sp2, SRho_ol3, Sp_ol3, SRho_as, Sp_as), fontsize='small')

    # ax0.fill_between(x5, y_est - y_err_AT, y_est + y_err_AT, alpha=0.2)
    plt.ylabel("HCHO [ppb]", size="small")
    plt.xlabel("ISOP [mol s-1 m-2]", size="small")
    #plt.ylim(0, ylimit)
    plt.legend()
    fig.tight_layout()

    plt.show()


    fig, axs = plt.subplots(3, 1, figsize=(8, 6), dpi=100)
    #fig.suptitle(title, fontsize="small")
    axs[0].scatter(Emis_JJA2019_as, hcho_JJA2019, color=color1, s=10, label="S-M3_assim")
    axs[1].scatter(Emis_JJA2019_ol3, hcho_JJA2019, color=color2, s=10, label="S-M3_ol")
    axs[2].scatter(Emis_olnp, hcho_JJA2019, color=color4, s=10, label="S-M2_ol")
    axs[0].plot(Emis_JJA2019_as, y_est_as, color=color1)
    axs[1].plot(Emis_JJA2019_ol3, y_est_ol3, color=color2)
    axs[2].plot(Emis_olnp, y_est2, color=color4)
    #axs[0, 0].set_title('(a) \n p_lowO3={:.2f} \n p_highO3={:.2f}'.format(Sp_AT, Sp_AT_2), fontsize='small')
    plt.title('JJ2019 \n'
              'S-M2_ol SRho={:.2f}, p={:.2f} \n'
              'S-M3_ol SRho={:.2f}, p={:.2f} \n'
              'S-M3_as SRho={:.2f}, p={:.2f}'.format(SRho2, Sp2, SRho_ol3, Sp_ol3, SRho_as, Sp_as), fontsize='small')

    # ax0.fill_between(x5, y_est - y_err_AT, y_est + y_err_AT, alpha=0.2)
    plt.ylabel("HCHO [ppb]", size="small")
    plt.xlabel("ISOP [mol s-1 m-2]", size="small")
    axs[0].legend()
    axs[1].legend()
    axs[2].legend()
    #plt.xlim(0, 4.5)
    fig.tight_layout()
    plt.show()

#Plot6var(Emis_ol, Emis_assim, Emis_ol2, hcho_dmax,"daily max", ylimit=8)
Plot6var(Emis_ol_noontime, Emis_assim_noontime, Emis_ol2_noontime, hcho_d,"noon time mean (9-15)")