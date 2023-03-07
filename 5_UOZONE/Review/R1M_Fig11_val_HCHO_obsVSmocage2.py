# -*- coding: utf-8 -*-
__author__ = 'lnx'

import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime
import netCDF4
import ReadinVindobona_Filter_fullperiod
from scipy import stats
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
from dateutil import rrule
import BOKUMet_Data
"""
# Set the minimum and maximum size for the dots in the plot
min_size = 10
max_size = 100
# Calculate the range of the third variable (z)
z_min = 3
z_max = 16
z_range = 13
# Scale the size of the dots according to the range of the third variable
#scaled_WSsizes = [(size - z_min) / z_range * (max_size - min_size) + min_size for size in ws19]
#s+3.641666666666667)*(12.906250000000002*(100+10))-10)
s = (21 - z_min)/z_range*(max_size-min_size) + min_size
print(s) 
s_inv = ((s-min_size)/(max_size-min_size)*z_range + z_min)  
print(s_inv)
"""
'''READ IN BOKU Metdata'''
BOKUMetData = BOKUMet_Data.BOKUMet()
#print(BOKUMetData) #10min values
#DAILY MEANS
BOKUMetData_hourlymean = BOKUMetData.resample('H').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_dailysum = BOKUMetData_hourlymean.resample('D').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.sum, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
#DAILY MAX
'''READ IN EEA air pollution data'''
pathbase2 = "/Users/lnx/DATA/obs_point/chem/EEA/"
o3_1990_2019_mda1 = pd.read_csv(pathbase2 + "o3_mda1_1990-2019_AT_mug.csv")
o3_1990_2019_mda1 = o3_1990_2019_mda1.set_index((pd.to_datetime(o3_1990_2019_mda1['date'])))
o3_1990_2019_mda1 = o3_1990_2019_mda1.drop(columns=['date'])
o3_1990_2019_mda8 = pd.read_csv(pathbase2 + "o3_mda8_1990-2019_AT_mug.csv")
o3_1990_2019_mda8 = o3_1990_2019_mda8.set_index(pd.to_datetime(o3_1990_2019_mda8['date']))
o3_1990_2019_mda8 = o3_1990_2019_mda8.drop(columns=['date'])
o3_2020_mda1 = pd.read_csv(pathbase2 + "AT_O3_2020.csv")
o3_2020_mda1 = o3_2020_mda1.set_index(pd.to_datetime(o3_2020_mda1['date']))
o3_2020_mda1 = o3_2020_mda1.drop(columns=['date'])
o3_1990_2020_mda1 = pd.concat([o3_1990_2019_mda1, o3_2020_mda1], axis=0)
o3_2020_mda8 = o3_2020_mda1.resample('8H', label='right').mean()
o3_2020_mda8 = o3_2020_mda8.resample('D').mean()
o3_1990_2020_mda8 = pd.concat([o3_1990_2019_mda8, o3_2020_mda8], axis=0)
o3_1990_2020_mda8 = o3_1990_2020_mda8#*ugm3toppb_o3 #MUG->PPB
o3_1990_2020_da = o3_1990_2020_mda8.resample('D').mean()
o3_1990_2020_m = o3_1990_2020_mda8.resample('M').mean()
o3_1990_2020_mda1_w = o3_1990_2020_mda1.resample('W').mean()
o3_1990_2020_mda8_w = o3_1990_2020_mda8.resample('W').mean()

"""READ IN MGNOUT CAMS"""
#foldername_ol = "/data1/models/nilu/SEEDS/MEGAN/2019/ol/ISOP/"  #MGNOUT_CAMS_BIG_ISOP_20190102.nc
#foldername_as = "/data1/models/nilu/SEEDS/MEGAN/2019/assim_LAI/ISOP/"

"read in VINDOBONA"
foldername_D = "/Users/lnx/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
hcho_f, hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D",begin = datetime.datetime(2017, 5, 1, 0, 0, 0))
hcho_w = hcho_dmax.resample("W").mean()

"""READ IN MGNOUT CAMS"""
#foldername_ol = "/data1/models/nilu/SEEDS/MEGAN/2019/ol/ISOP/"  #MGNOUT_CAMS_BIG_ISOP_20190102.nc
#foldername_as = "/data1/models/nilu/SEEDS/MEGAN/2019/assim_LAI/ISOP/"
foldername_as = "/Users/lnx/DATA/models/NILU/MEGAN/ISO_JJA19/"

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

#Emis_ol, Emis_ol_noontime = EmisSEEDS(foldername_ol)
Emis_assim, Emis_assim_noontime = EmisSEEDS(foldername_as)

wd = BOKUMetData_dailysum["WD"] #TODO WD= daily mean-> maybe there is a better way to aggregate winddir?
wd0619 = wd[datetime.datetime(2019, 6, 1, 00, 00): datetime.datetime(2019, 6, 30, 00, 00)]
wd0719 = wd[datetime.datetime(2019, 7, 1, 00, 00): datetime.datetime(2019, 7, 31, 00, 00)]
wd0819 = wd[datetime.datetime(2019, 8, 1, 00, 00): datetime.datetime(2019, 8, 31, 00, 00)]

ws = BOKUMetData_dailysum["WS"]
ws19 = ws[datetime.datetime(2019, 6, 1, 00, 00): datetime.datetime(2019, 8, 31, 00, 00)]
ws0619 = ws[datetime.datetime(2019, 6, 1, 00, 00): datetime.datetime(2019, 6, 30, 00, 00)]
ws0719 = ws[datetime.datetime(2019, 7, 1, 00, 00): datetime.datetime(2019, 7, 31, 00, 00)]
ws0819 = ws[datetime.datetime(2019, 8, 1, 00, 00): datetime.datetime(2019, 8, 31, 00, 00)]

# Set the minimum and maximum size for the dots in the plot
min_size = 10
max_size = 100

# Calculate the range of the third variable (z)
z_min = min(ws19)
z_max = max(ws19)
z_range = z_max - z_min
print("zmin", z_min, "zmax", z_max, "zrange",z_range)

# Scale the size of the dots according to the range of the third variable
scaled_WSsizes = [(size - z_min) / z_range * (max_size - min_size) + min_size for size in ws19]
print(scaled_WSsizes)

print(len(scaled_WSsizes[:30]),len(scaled_WSsizes[30:-31]),len(scaled_WSsizes[-31:]))

hcho_062019 = hcho_d[datetime.datetime(2019, 6, 1, 00, 00): datetime.datetime(2019, 6, 30, 00, 00)].values.flatten()
hcho_072019 = hcho_d[datetime.datetime(2019, 7, 1, 00, 00): datetime.datetime(2019, 7, 31, 00, 00)].values.flatten()
hcho_082019 = hcho_d[datetime.datetime(2019, 8, 1, 00, 00): datetime.datetime(2019, 8, 31, 00, 00)].values.flatten()

def Plot6var():
    ISO_0619 = Emis_assim_noontime.ISO[datetime.datetime(2019, 6, 1, 00, 00): datetime.datetime(2019, 6, 30, 00, 00)]
    ISO_0719 = Emis_assim_noontime.ISO[datetime.datetime(2019, 7, 1, 00, 00): datetime.datetime(2019, 7, 31, 00, 00)]
    ISO_0819 = Emis_assim_noontime.ISO[datetime.datetime(2019, 8, 1, 00, 00): datetime.datetime(2019, 8, 31, 00, 00)]
    color1= "black"
    a = 0
    fig, axs = plt.subplots(nrows=1, ncols=3, sharey=True, dpi=100) #ERROR: , aspect='equal'
    ax = axs.flatten()
    #ax[0].set_aspect('equal', 'box')
    #ax[0].axis('equal')
    
    ax[0].set_title('(d) Jun 19')# \n SRho{:.2f} \n p={:.2f}'.format(SRho05, Sp05), fontsize='small')
    plt1 = ax[0].scatter(hcho_062019, ISO_0619, s=scaled_WSsizes[:30], c=wd0619,cmap="rainbow_r")  #9-15mean!  color=color1,
    ax[1].set_title('(e) Jul 19')# \n SRho{:.2f} \n p={:.2f}'.format(SRho05, Sp05), fontsize='small')
    plt2 = ax[1].scatter(hcho_072019, ISO_0719, s=scaled_WSsizes[30:-31], c=wd0719,cmap="rainbow_r")
    ax[2].set_title('(f) Aug 19')  # \n SRho{:.2f} \n p={:.2f}'.format(SRho05, Sp05), fontsize='small')
    plt3 = ax[2].scatter(hcho_082019, ISO_0819, s=scaled_WSsizes[-31:], c=wd0819,cmap="rainbow_r")
    ax[0].set_ylabel("ISO_mod [mol s-1 m-2]", size="small")
    ax[0].set_xlabel("HCHO_obs [ppb] ", size="small")
    ax[1].set_ylabel("ISO_mod [mol s-1 m-2]", size="small")
    ax[1].set_xlabel("HCHO_obs [ppb]", size="small")
    ax[2].set_ylabel("ISO_mod [mol s-1 m-2]", size="small")
    ax[2].set_xlabel("HCHO_obs [ppb]", size="small")
    fig.tight_layout()

    # produce a legend with the unique colors from the scatter
    legend1 = ax[0].legend(*plt1.legend_elements(), loc="upper left", title="WD [°]") #limit number of classes: *plt1.legend_elements(num=4)
    legend1a = ax[1].legend(*plt2.legend_elements(), loc="upper left", title="WD [°]")
    legend1b = ax[2].legend(*plt3.legend_elements(), loc="upper left", title="WD [°]")
    ax[0].add_artist(legend1)
    ax[1].add_artist(legend1a)
    ax[2].add_artist(legend1b)
    # produce a legend with a cross section of sizes from the scatter
    #plt.legend(["5","10","14"],[5,10,14])
    kw = dict(prop="sizes", num=4, color="grey", fmt="{x}",
              func=lambda s:((s - min_size) / (max_size - min_size) * z_range + z_min)) #inverse function of scaling function.
    legend2 = ax[0].legend(*plt1.legend_elements(**kw), loc="upper right", title="WS [m/s]")
    legend2a = ax[1].legend(*plt2.legend_elements(**kw), loc="upper right", title="WS [m/s]")
    legend2b = ax[2].legend(*plt3.legend_elements(**kw), loc="upper right", title="WS [m/s]")
    for ax in fig.get_axes():
        ax.set_xlim(0, 6)
        ax.set_ylim(0, 6E-8)
    # plt.colorbar(plt1, label="WD [°]")
    plt.show()

Plot6var()



foldername_as_moc = "/Volumes/Expansion/data1/models/mocage/assim/"  #hmmacc01+Jun-2019.nc, hmmacc01+Jul-2019.nc
filename_as_moc_jun = "/Volumes/Expansion/data1/models/mocage/assim/hmmacc01+Jun-2019.nc"
filename_as_moc_jul = "/Volumes/Expansion/data1/models/mocage/assim/hmmacc01+Jul-2019.nc"
filename_as_moc_aug = "/Volumes/Expansion/data1/models/mocage/assim/hmmacc01+Aug-2019.nc"

def ReadinMocage(path, starttime):
#def ReadinMocage(foldername):
    #files = os.listdir(foldername)
    #files = sorted(files)
    #print(files) #['hmmacc01+Jul-2019.nc', 'hmmacc01+Jun-2019.nc']
    time_moc = []
    HCHO_moc = []
    ISO_moc = []
    O3_moc = []
    index_lat = 201 #city:201 ww:202 #CAMS European grid
    index_lon = 424 #city:424 ww:422 #CAMS European grid
    #for i in range(len(files)):
    #    path = foldername + files[i]
    #    infile = netCDF4.Dataset(path)  # path.decode('UTF-8')  #OSError: [Errno -51] NetCDF: Unknown file format: b'/windata/DATA/models/nilu/MEGAN3_SURFEX_SEEDS/MEGAN/ol/MGNOUT_CAMS_BIG_20190803.nc'
    #    HCHO_hourlyvalue = infile.variables['HCHO_47'][:, index_lat, index_lon]
    #    ISO_hourlyvalue = infile.variables['ISO_47'][:, index_lat, index_lon]
    #    O_x_hourlyvalue = infile.variables['O_x_47'][:, index_lat, index_lon]
    #    time = infile.variables['time'][:]
    #    time_moc.append(time)
    #    HCHO_moc.append(HCHO_hourlyvalue)
    #    ISO_moc.append(ISO_hourlyvalue)
    #    O3_moc.append(O_x_hourlyvalue)
    #    print(HCHO_moc, ISO_moc, O3_moc, time_moc)
    #path = foldername + 'hmmacc01+Jul-2019.nc'
    infile = netCDF4.Dataset(path)
    HCHO_moc = infile.variables['HCHO_47'][:, index_lat, index_lon]
    ISO_moc = infile.variables['ISO_47'][:, index_lat, index_lon]
    O3_moc = infile.variables['O_x_47'][:, index_lat, index_lon]
    #starttime = datetime.datetime(2019,7,1,0,0) #2019-06-01 00:00:00
    time = infile.variables['time'][:]
    timeaxis = pd.date_range(starttime, periods=len(time), freq="H")
    #print(len(timeaxis), len(ISO_moc))
    MOC_out = pd.DataFrame({'datetime': timeaxis, 'ISO': ISO_moc, 'HCHO': HCHO_moc,'O3': O3_moc})
    MOC_out['datetime'] = pd.to_datetime(MOC_out['datetime'])
    MOC_out = MOC_out.set_index(['datetime'])
    return MOC_out

#MOC_out = ReadinMocage(foldername_as_moc)
MOC_out_jun19_h = ReadinMocage(filename_as_moc_jun,datetime.datetime(2019,6,1,0,0))
MOC_out_jul19_h = ReadinMocage(filename_as_moc_jul,datetime.datetime(2019,7,1,0,0))
MOC_out_aug19_h = ReadinMocage(filename_as_moc_aug,datetime.datetime(2019,8,1,0,0))

MOC_out_jun19 = MOC_out_jun19_h.loc[(MOC_out_jun19_h.index.hour >= 8) & (MOC_out_jun19_h.index.hour <= 14)]
MOC_out_jun19 = MOC_out_jun19.resample('D').mean()
MOC_out_jul19 = MOC_out_jul19_h.loc[(MOC_out_jul19_h.index.hour >= 8) & (MOC_out_jul19_h.index.hour <= 14)]
MOC_out_jul19 = MOC_out_jul19.resample('D').mean()
MOC_out_aug19 = MOC_out_aug19_h.loc[(MOC_out_aug19_h.index.hour >= 8) & (MOC_out_aug19_h.index.hour <= 14)]
MOC_out_aug19 = MOC_out_aug19.resample('D').mean()


def Plot6varHCHO():
    color1= "black"
    a = 0
    fig, axs = plt.subplots(nrows=1, ncols=3, sharey=True, dpi=100)
    ax = axs.flatten()
    ax[0].set_aspect('equal')
    ax[1].set_aspect('equal')
    ax[2].set_aspect('equal')
    ax[0].set_title('(a) Jun 19')# \n SRho{:.2f} \n p={:.2f}'.format(SRho05, Sp05), fontsize='small')  #volume mixing ratio = moles/moles * 10^9 -> ppbv
    plt1 = ax[0].scatter(hcho_062019, MOC_out_jun19.HCHO*10e8, scaled_WSsizes[:30], c=wd0619)  #9-15mean!
    ax[1].set_title('(b) Jul 19')# \n SRho{:.2f} \n p={:.2f}'.format(SRho05, Sp05), fontsize='small')
    plt2 = ax[1].scatter(hcho_072019, MOC_out_jul19.HCHO*10e8,  scaled_WSsizes[30:-31], c=wd0719) #s=10
    ax[2].set_title('(c) Aug 19')  # \n SRho{:.2f} \n p={:.2f}'.format(SRho05, Sp05), fontsize='small')
    plt3 = ax[2].scatter(hcho_082019, MOC_out_aug19.HCHO * 10e8, scaled_WSsizes[-31:], c=wd0819)  # s=10
    ax[0].set_ylabel("HCHO_mod [ppb] ", size="small")
    ax[0].set_xlabel("HCHO_obs [ppb] ", size="small")
    ax[1].set_ylabel("HCHO_mod [ppb] ", size="small")
    ax[1].set_xlabel("HCHO_obs [ppb] ", size="small")
    ax[2].set_ylabel("HCHO_mod [ppb] ", size="small")
    ax[2].set_xlabel("HCHO_obs [ppb] ", size="small")
    fig.tight_layout()
    #plt.colorbar(plt1, label="WS [m/s]")
    # produce a legend with the unique colors from the scatter
    legend1 = ax[0].legend(*plt1.legend_elements(), loc="upper left", title="WD [°]")
    legend1a = ax[1].legend(*plt2.legend_elements(), loc="upper left", title="WD [°]")
    legend1b = ax[2].legend(*plt3.legend_elements(), loc="upper left", title="WD [°]")
    ax[0].add_artist(legend1)
    ax[1].add_artist(legend1a)
    ax[2].add_artist(legend1b)
    # produce a legend with a cross section of sizes from the scatter
    handles, labels = plt1.legend_elements(prop="sizes", alpha=0.6)
    handles2, labels = plt2.legend_elements(prop="sizes", alpha=0.6)
    handles3, labels = plt3.legend_elements(prop="sizes", alpha=0.6)
    labels = ["6","7","8","9","10","11","12","13","14"]
    legend2 = ax[0].legend(handles, labels, loc="upper right", title="WS [m s-1]")
    legend2a = ax[1].legend(handles2, labels, loc="upper right", title="WS [m s-1]")
    legend2b = ax[2].legend(handles3, labels, loc="upper right", title="WS [m s-1]")
    #plt.colorbar(plt1, label="WD [°]")  # , shrink=0.6,
    for ax in fig.get_axes():
        # print(ax)
        ax.set_xlim(0, 6)
        ax.set_ylim(0, 6)
    plt.show()
Plot6varHCHO()

def Plot6varO3():
    o3_jun19 = o3_1990_2020_da[datetime.datetime(2019, 6, 1, 00, 00): datetime.datetime(2019, 6, 30, 23, 00)]['AT9STEF']
    o3_jul19 = o3_1990_2020_da[datetime.datetime(2019, 7, 1, 00, 00): datetime.datetime(2019, 7, 31, 23, 00)]['AT9STEF']
    o3_aug19 = o3_1990_2020_da[datetime.datetime(2019, 8, 1, 00, 00): datetime.datetime(2019, 8, 31, 23, 00)]['AT9STEF']
    color1= "violet"
    a = 0
    fig, axs = plt.subplots(nrows=1, ncols=3, sharey=True, dpi=100)
    ax = axs.flatten()
    ax[0].set_aspect('equal')
    ax[1].set_aspect('equal')
    ax[2].set_aspect('equal')
    ax[0].set_title('(a) Jun 19')
    plt1 = ax[0].scatter(o3_jun19, MOC_out_jun19.O3*10e8, scaled_WSsizes[:30], c=wd0619) #TODO mda8 vs 9-15 mean
    ax[1].set_title('(b) Jul 19')# \n SRho{:.2f} \n p={:.2f}'.format(SRho05, Sp05), fontsize='small')
    plt2 = ax[1].scatter(o3_jul19, MOC_out_jul19.O3*10e8, scaled_WSsizes[30:-31], c=wd0719) #TODO mda8 vs 9-15 mean
    ax[2].set_title('(c) Aug 19')  # \n SRho{:.2f} \n p={:.2f}'.format(SRho05, Sp05), fontsize='small')
    plt3 = ax[2].scatter(o3_aug19, MOC_out_aug19.O3 * 10e8, scaled_WSsizes[-31:], c=wd0819)  # TODO mda8 vs 9-15 mean
    ax[0].set_ylabel("O3_mod [ppb]", size="small")
    ax[0].set_xlabel("O3_obs [μg/m³]", size="small")
    ax[1].set_ylabel("O3_mod [ppb] ", size="small")
    ax[1].set_xlabel("O3_obs [μg/m³] ", size="small")
    ax[2].set_ylabel("O3_mod [ppb] ", size="small")
    ax[2].set_xlabel("O3_obs [μg/m³] ", size="small")
    fig.tight_layout()

    # produce a legend with the unique colors from the scatter
    legend1 = ax[0].legend(*plt1.legend_elements(), loc="upper left", title="WD [°]")
    legend1a = ax[1].legend(*plt2.legend_elements(), loc="upper left", title="WD [°]")
    legend1b = ax[2].legend(*plt3.legend_elements(), loc="upper left", title="WD [°]")
    ax[0].add_artist(legend1)
    ax[1].add_artist(legend1a)
    ax[2].add_artist(legend1b)
    # produce a legend with a cross section of sizes from the scatter
    handles, labels = plt1.legend_elements(prop="sizes", alpha=0.6)
    handles2, labels = plt2.legend_elements(prop="sizes", alpha=0.6)
    handles3, labels = plt3.legend_elements(prop="sizes", alpha=0.6)
    labels = ["6", "7", "8", "9", "10", "11", "12", "13", "14"]
    legend2 = ax[0].legend(handles, labels, loc="upper right", title="WS [m s-1]")
    legend2a = ax[1].legend(handles2, labels, loc="upper right", title="WS [m s-1]")
    legend2b = ax[2].legend(handles3, labels, loc="upper right", title="WS [m s-1]")
    for ax in fig.get_axes():
        ax.set_xlim(20, 250)
        ax.set_ylim(20, 250)
    #plt.colorbar(pl1, label="WS [m/s]"
    plt.show()

Plot6varO3()

exit()
# func = lambda s: (s + z_min) * (z_range * (max_size - min_size)))-min_size
# scaled_WSsizes = [(size - z_min) / z_range * (max_size - min_size) + min_size for size in ws19]
# ((scaled_WSsizes[:30]+z_min)*(z_range*(max_size-min_size)))-min_size

# kw = dict(prop="sizes", num=5, color=scatter.cmap(0.7), fmt="$ {x:.2f}",
#          func=lambda s: np.sqrt(s / .3) / 3)
# legend2 = ax.legend(*scatter.legend_elements(**kw),
#                    loc="lower right", title="Price")
# handles, labels = plt1.legend_elements(prop="sizes", alpha=0.6)
# handles2, labels = plt2.legend_elements(prop="sizes", alpha=0.6)
# handles3, labels = plt3.legend_elements(prop="sizes", alpha=0.6)
# labels = ["6","7","8","9","10","11","12","13","14"]
# print(handles,labels)
# legend2 = ax[0].legend(handles, labels, loc="upper right", title="WS [m s-1]")
# legend2a = ax[1].legend(handles2, labels, loc="upper right", title="WS [m s-1]")
# legend2b = ax[2].legend(handles3, labels, loc="upper right", title="WS [m s-1]")
