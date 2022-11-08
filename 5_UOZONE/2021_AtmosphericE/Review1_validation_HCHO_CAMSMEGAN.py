# -*- coding: utf-8 -*-
__author__ = 'lnx'

import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime
import netCDF4
from met.library import ReadinVindobona_Filter_fullperiod
from scipy import stats

"""READ IN MGNOUT CAMS"""
foldername_ol = "/data1/models/nilu/MEGAN3_SURFEX_SEEDS/MEGAN/2019/ol/ISOP/"  #MGNOUT_CAMS_BIG_ISOP_20190102.nc
foldername_as = "/data1/models/nilu/MEGAN3_SURFEX_SEEDS/MEGAN/2019/assim_LAI/ISOP/"

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
    Emis=[]
    index_lat = 202  #LAT 48.25°N
    index_lon = 422 #LON 16.25°E (city rim to Wienerwald) or 421: LON 16.15°E (middle Wienerwald)
    for i in range(len(files)):
        day = str(files[i][-5:-3])  # splitlistcomp[3:4]
        month = str(files[i][-7:-5])  # splitlistcomp[2:3]
        year = "20" + str(files[i][-9:-7])  # splitlistcomp[:2]
        #print(day,month,year)
        date = datetime(year=int(year), month=int(month), day=int(day))
        #print(date)
        dateaxis.append(date)
        path = foldername+files[i]
        infile = netCDF4.Dataset(path)  #path.decode('UTF-8')  #OSError: [Errno -51] NetCDF: Unknown file format: b'/windata/DATA/models/nilu/MEGAN3_SURFEX_SEEDS/MEGAN/ol/MGNOUT_CAMS_BIG_20190803.nc'
        Emis_dailyvalue = infile.variables['Emiss'][:, index_lat, index_lon, 0]  #TODO: only first emission layer (ISO) read in
        Emis.append(Emis_dailyvalue.max())
    Emis = pd.DataFrame({'datetime': dateaxis, 'ISO': Emis})
    Emis['datetime'] = pd.to_datetime(Emis['datetime'])
    Emis = Emis.set_index(['datetime'])
    #print(Emis)

    return Emis

Emis_ol = EmisSEEDS(foldername_ol)
Emis_assim = EmisSEEDS(foldername_as)


"read in SAFAEs MEGAN2.1-SURFEX results"
foldername_ol_2 = "/data1/models/cnrm/201906/ISBA_
#Isoprene data are available in the ISBA_DIAGNOSTICS.OUT.nc file
# with a description of the activity_factor, soil moisture activity factor (gamma_sm),
# leaf age activity factor (gamma_age). You can find the 16 PFTs distribution and data of PPFD calculated by megan.
"""
file_ref_pro = '/media/lnx/Norskehavet/OFFLINE/2069REF/dx345corr/TEB_PROGNOSTIC.OUT.nc'
f_ref = netCDF4.Dataset(file_ref_pro, mode='r')
#cut for subregions
TSURFACE_units = f_ref.variables['TROOF1'].units
TROOF1_ref_ce = f_ref.variables['TROOF1'][:,50:59,80:89]
f_ref.close()
TROOF1_ref_ce = TROOF1_ref_ce.reshape(174,81)
TROOF1_ref_ce_ts = TROOF1_ref_ce.mean(axis=1) - 273.15
start = datetime.datetime(2069,7,1,19,0)  #1...174
stop = datetime.datetime(2069,7,9,0,0)
delta = datetime.timedelta(hours=1)
dates = mpl.dates.drange(start,stop,delta)
date_format = mpl.dates.DateFormatter('      %H') #Meteorol. Z. Format:  %H%M UTC %d %B %Y

fig = plt.figure()
plt.title("ROOF")
plt.plot(dates, TROOF1_ref_ce_ts, color='black', label=u"REF")
plt.xlabel("Time [UTC]")
plt.ylabel(u"Surface temperature [°C]", size="large")
plt.legend(loc='lower right', ncol=3)
plt.ylim(0, 100)
#plt.ylim(-5, 10)
"""

"read in VINDOBONA"
foldername_D = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D", begin= datetime(2017, 5, 1, 0, 0, 0))
hcho_w = hcho_dmax.resample("W").mean()

"""
fig = plt.figure()
#plt.suptitle(f"OBS {start} - {end}")
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()
ax1.plot(Emis_ol,linewidth="1", color='black', label="MOD: MGNOUT,ol ISO,dmax", linestyle="solid")
ax1.plot(Emis_assim,linewidth="1", color='red', label="MOD: MGNOUT,assim ISO,dmax", linestyle="solid")
ax2.plot(hcho_dmax[:],linewidth="1", color='violet', label="OBS: HCHO,dmax", linestyle=":")
ax1.set_xlabel("days")
#ax1.set_xlim(start,end)
ax1.set_ylabel("[mol s-1 m-2]", size="medium")
ax2.set_ylabel("[ppb]", size="medium")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()
"""

def Plot6var(df1, df2, title, ylimit):
    #TODO: define drought/non-drought periods
    #Emis_MAM2018 = df1[datetime(2018, 3, 1, 00, 00): datetime(2018, 5, 31, 00, 00)]
    #Emis_MAM2020 = df1[datetime(2020, 3, 1, 00, 00): datetime(2020, 5, 31, 00, 00)]
    #hcho_dmaxMAM2018 = df1[datetime(2018, 3, 1, 00, 00): datetime(2018, 5, 31, 00, 00)]
    #hcho_dmaxMAM2020 = df1[datetime(2020, 3, 1, 00, 00): datetime(2020, 5, 31, 00, 00)]
    Emis_JJA2019 = df1[datetime(2019, 6, 1, 00, 00): datetime(2019, 8, 31, 00, 00)].values.flatten()
    hcho_JJA2019 = df2[datetime(2019, 6, 1, 00, 00): datetime(2019, 8, 31, 00, 00)].values.flatten()
    """
    x5 = df1 #y5 = df1['hcho'].values.flatten()
    y5 = df2
    print(x5)
    idx = np.isfinite(x5) & np.isfinite(y5)
    print(idx)
    SRho, Sp = (stats.spearmanr(x5[idx], y5[idx]))
    m5, b5 = np.polyfit(x5[idx], y5[id], 1)
    """
    idx = np.isfinite(Emis_JJA2019) & np.isfinite(hcho_JJA2019)
    print(idx)
    SRho, Sp = (stats.spearmanr(Emis_JJA2019[idx], hcho_JJA2019[idx]))
    m5, b5 = np.polyfit(Emis_JJA2019[idx], hcho_JJA2019[idx], 1)
    y_est = m5 * Emis_JJA2019 + b5
    #print(Emis_JJA2019[idx], hcho_JJA2019[idx])
    print(y_est)
    print(m5,b5)
    #exit()
    print("Spearman Test/Significance of Linear Regression:")
    print("ISOP", SRho, Sp)
    #x5_MAM2020 = Emis_MAM2012 #df2['AT'].values.flatten()
    #y5_MAM2020 = Emis_MAM2012 #df2['hcho'].values.flatten()
    #idx_2 = np.isfinite(x5_2) & np.isfinite(y5_2)
    #SRho_2, Sp_2 = (stats.spearmanr(x5_2[idx_2], y5_2[idx_2]))
    #print("Variance")
    #var = [np.var(x, ddof=1) for x in [hcho_JJA2019]]
    #print(var)
    #print([np.var(x, ddof=1) for x in [hcho_JJA2019]])
    #print("ISOP", Sp_2)
    #m5_2, b5_2 = np.polyfit(x5_2[idxAT_2], y5_2[idxAT_2], 1)

    color1= "palegreen"
    color2= "mediumseagreen"
    color3= "thistle"
    color4= "mediumpurple"
    a = 0
    fig, axs = plt.subplots(1, 1, figsize=(8, 6), dpi=100)
    #fig.suptitle(title, fontsize="small")
    plt.scatter(Emis_JJA2019, hcho_JJA2019, color=color2, s=10, label="S-M3_assim")
    plt.plot(Emis_JJA2019, y_est, color="black")
    #axs[0, 0].set_title('(a) \n p_lowO3={:.2f} \n p_highO3={:.2f}'.format(Sp_AT, Sp_AT_2), fontsize='small')
    plt.title('JJA2019: SRho={:.2f} \n p={:.2f}'.format(SRho, Sp), fontsize='small')
    #axs[0, 0].scatter(x5_2[a:], y5_2[a:], color=color3, s=5)
    #y_est_2 = m5_2 * x5_2 + b5_2
    #axs[0, 0].plot(x5_2, y_est_2, color=color4)
    # ax0.fill_between(x5, y_est - y_err_AT, y_est + y_err_AT, alpha=0.2)
    plt.ylabel("HCHO [ppb]", size="small")
    plt.xlabel("ISOP [mol s-1 m-2]", size="small")
    plt.ylim(0, ylimit)
    plt.legend()
    fig.tight_layout()
    plt.show()
    #plt.savefig("/home/heidit/Downloads/" + title + ".jpg")

Plot6var(Emis_ol,hcho_dmax," ", ylimit=8)