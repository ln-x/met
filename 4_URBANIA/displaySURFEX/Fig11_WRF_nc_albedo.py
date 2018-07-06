# -*- coding: utf-8 -*-
__author__ = 'lnx'
from netCDF4 import Dataset
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import sys

outpath ='/home/lnx'
file = '/media/lnx/98C4EEA4C4EE83BA/WRF-TEB-NC_Files/wrfout_d03_2015-07-13_12_00_00_nest_teb.nc'
#file2 = '/media/lnx/98C4EEA4C4EE83BA/WRF-TEB-NC_Files/wrfout_d03_2015-07-13_12_00_00_no_teb_nested.nc'
file2 = '/media/lnx/98C4EEA4C4EE83BA/WRF-TEB-NC_Files/HighAlbedo/wrfout_d03_2015-07-13_12_00_00'
file3 = '/media/lnx/98C4EEA4C4EE83BA/WRF-TEB-NC_Files/HighAlbedo0_68Roof/wrfout_d03_2015-07-13_12_00_00'

fh = Dataset(file, mode='r')
fh2 = Dataset(file2, mode='r')
fh3 = Dataset(file3, mode='r')

'''time + 2dvariables'''
lons = fh.variables['XLONG'][1]  #lon (147x)135x174
lats = fh.variables['XLAT'][1]  #lat (147x)135x174
tair = fh.variables['T2'] #147x135x174
tair_units = fh.variables['T2'].units
tair2 = fh2.variables['T2'] #147x135x174
tair3 = fh3.variables['T2'] #147x135x174

m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')

# Because our lon and lat variables are 1D,
# use meshgrid to create 2D arrays
# Not necessary if coordinates are already in 2D arrays.
print lons[0], lats[0]

exit()
'''
lon, lat = np.meshgrid(lons, lats)
xi, yi = m(lon, lat)
cs = m.pcolor(xi,yi,np.squeeze(tair[1]))

# Add Colorbar
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")

#cbar.set_label(tair_units)
cbar.set_label(tair_units)
#cbar.set_label(wind10m_units)
plt.title('2m Air Temperature STQ 2015-07-20 0UTC')
#plt.title('10m Wind Speed - 2015-07-20 18UTC')
plt.clim(21,35)
plt.show()
'''



ZAMGnames = {'11034': ['Wien-Innere Stadt',85,53], '11035':  ["Wien-Hohe Warte",83,69],
             '11036': ['Schwechat',129,25], '11037':['Gross-Enzersdorf',127,54],
             '11040': ['Wien-Unterlaa',97,29], '11042':['Wien-Stammersdorf',94,88],
             '11077': ['Brunn am Gebirge',65,24], '11080':['Wien-Mariabrunn',56,56]}
for i in ZAMGnames:
  x = ZAMGnames[i][1]
  y = ZAMGnames[i][2]
  WRFdata = tair[:,y,x]
  WRFdata_heatdays = np.array(WRFdata[12:-15])#[8:176])
  WRFdata_heatdays = WRFdata_heatdays - 273.15
  print len(WRFdata_heatdays)

  WRFdata2 = tair2[:, y, x]
  WRFdata2_heatdays = np.array(WRFdata2[12:-24])  # [8:176])
  WRFdata2_heatdays = WRFdata2_heatdays - 273.15
  print len(WRFdata2_heatdays)

  WRFdata3 = tair3[:, y, x]
  WRFdata3_heatdays = np.array(WRFdata3[12:-24])  # [8:176])
  WRFdata3_heatdays = WRFdata3_heatdays - 273.15


  try:
    '''
    Plotting
    '''
    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    #ax1.plot(ZAMG_heatdays, color='black', label=u"Ground station")
    ax1.plot(WRFdata_heatdays, color='red', label=r"WRF_TEB ($\alpha_{r}=0.15$)")  #31
    ax1.plot(WRFdata2_heatdays, color='violet', label=r"WRF_TEB ($\alpha_{r}=0.30$)")  #31
    ax1.plot(WRFdata3_heatdays, color='blue', label=r"WRF_TEB ($\alpha_{r}=0.68$)")  #31
    ax1.set_xlabel("hours[UTC]")
    ax1.set_ylabel(r"$T_{air_2m}$"u'[°C]', size="large")
    ax1.legend(loc='upper right')
    ax1.set_xlim(0, 125)
    ax1.set_ylim(15, 40)
    #myFmt = DateFormatter("%d")
    #ax1.xaxis.set_major_formatter(myFmt)
    #fig.autofmt_xdate()

    ax2 = fig.add_subplot(122)
    #plt.scatter(ZAMG_heatdays, WRFdata_heatdays, color='blue', label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
    #plt.scatter(ZAMG_heatdays, WRFdata2_heatdays, color='violet', label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i2, Bias_Forc_i2)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
    #ax2.set_xlabel(r"$T_{air_2m}$"u'[°C]', size="large")
    #ax2.set_ylabel(r"$T_{air_2m}$"u'[°C]', size="large")
    #ax2.legend(loc='upper left')
    #plt.suptitle(ZAMGnames[i] + ", 14 - 21 July 2015", size="large")#+"2m air temperature"))
    plt.suptitle(ZAMGnames[i][0] + ", 14 - 18 July 2015", size="large")#+"2m air temperature"))
    #figname = outpath + i + "WRFTEBZAMG.png"
    #plt.savefig(figname)
    plt.show()
  except:
    print("Oops!", sys.exc_info()[0], "occured.")
    pass


fh.close()
fh2.close()




