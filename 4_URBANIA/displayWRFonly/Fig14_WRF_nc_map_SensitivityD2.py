# -*- coding: utf-8 -*-
__author__ = 'lnx'
from netCDF4 import Dataset
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import sys

outpath ='/media/lnx/Norskehavet/WRF-TEB-NC_Files/201708/Sensitivity_Runs/D2/'
file = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201708/Sensitivity_Runs/Ref-run/wrfout_d02_2017-07-31_18_00_00.nc'
file1 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201708/Sensitivity_Runs/03a-Sensitivity-run-1/wrfout_d02_2017-07-31_18_00_00.nc'
file2 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201708/Sensitivity_Runs/3b-Sensitivity-run-2/wrfout_d02_2017-07-31_18_00_00.nc'
file3 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201708/Sensitivity_Runs/3c-Sensitivity-run-3/wrfout_d02_2017-07-31_18_00_00.nc'
file4 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201708/Sensitivity_Runs/3d-Sensitivity-run-4/wrfout_d02_2017-07-31_18_00_00.nc'

fh = Dataset(file, mode='r')
fh1 = Dataset(file1, mode='r')
fh2 = Dataset(file2, mode='r')
fh3 = Dataset(file3, mode='r')
fh4 = Dataset(file4, mode='r')

'''time + 2dvariables'''
lons = fh.variables['XLONG'][1]  #lon (147x)135x174 #print len(lons), len(lons[1])
lats = fh.variables['XLAT'][1]  #lat (147x)135x174  #print len(lats), len(lats[1])

tair = fh.variables['T2'][:] #147x135x174
tair1 = fh1.variables['T2'][:] #147x135x174
tair2 = fh2.variables['T2'][:] #147x135x174
tair3 = fh3.variables['T2'][:] #147x135x174
tair4 = fh4.variables['T2'][:] #147x135x174
#print tair.shape

tsur = fh.variables['TSK'][:] #147x135x174
tsur4 = fh4.variables['TSK'][:] #147x135x174

cldfr = fh.variables['CLDFRA'][:] #(37, 39, 135, 174)
cldfr4 = fh4.variables['CLDFRA'][:]
cldfrSUM = cldfr.sum(axis=1)
#print cldfrSUM.shape
#print cldfrSUM[16][:30][:30]

qcloud = fh.variables['QCLOUD'][:] #(37, 39, 135, 174)
qcloud4 = fh4.variables['QCLOUD'][:]
qcloudSUM = qcloud.sum(axis=1)
qcloudSUM4 = qcloud4.sum(axis=1)

swup = fh.variables['SWUPB'][:]
swup2 = fh2.variables['SWUPB'][:]
swup3 = fh3.variables['SWUPB'][:]
swdown = fh.variables['SWDOWN'][:]
swdown4 = fh4.variables['SWDOWN'][:]
alb = fh.variables['ALBEDO'][:]
alb2 = fh2.variables['ALBEDO'][:]
alb3 = fh3.variables['ALBEDO'][:]
H = fh.variables['HFX'][:] #upward heat flux= sensible heat flux?
H2 = fh2.variables['HFX'][:] #upward heat flux= sensible heat flux?
H3 = fh3.variables['HFX'][:] #upward heat flux= sensible heat flux?

LE = fh.variables['LH'][:]
LE3 = fh3.variables['LH'][:]

lwup = fh.variables['LWUPB'][:]
lwup2 = fh2.variables['LWUPB'][:]
lwdown = fh.variables['LWDNB'][:]
lwdown4 = fh4.variables['LWDNB'][:]

lwdownT = fh.variables['LWDNT'][:]
lwdownT4 = fh4.variables['LWDNT'][:]
swdownT = fh.variables['SWDNT'][:]
swdownT4 = fh4.variables['SWDNT'][:]

tair_units = fh.variables['T2'].units
lwup_units = fh.variables['LWUPB'].units
swup_units = fh.variables['SWUPB'].units
LE_units = fh.variables['LH'].units
pblh_units = fh.variables['PBLH'].units
swdown_units = fh.variables['SWDOWN'].units
qcloud_units = fh.variables['QCLOUD'].units

fh.close()
fh2.close()

'''>>>!!! CHECK CORRECT UNITS, TITLE, RANGE and FIGNAME'''
"""
timestep=18
tair_diff = tair2[timestep] - tair[timestep]
m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
xi, yi = m(lons, lats)
cmap=plt.cm.get_cmap('bwr',11)  #RdBu: Red to Blue, bwr: blue white red
cs = m.pcolor(xi, yi, np.squeeze(tair_diff),cmap=cmap)
#day = int(round(timestep-6 / 24, 0))
plt.title("TC-Ref: Tair 1 Aug 2017 12 UTC")
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(tair_units)
# plt.title(r'$\delta$ sw rad balance $\alpha_{r}:0.30-0.15$ day %s UTC %s' %(str(day), str(hour)))
#plt.clim(-2, 2)

figname = outpath + "Tair_Ref_" + str(timestep) + "_WRFTEB_Ref_2017_tair.png"
#plt.savefig(figname)
#plt.show()
#"""
#exit()

timeslices = 37

for i in range(timeslices):
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(tsur[i]), cmap=cmap)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(tair_units)
  plt.title((r'Tsur Ref %d') %i)
  #plt.clim(-0.5,0.5)
  figname = outpath + "Tskin_" + str(i) + "_WRFTEB_Ref.png"
  plt.savefig(figname)
  plt.clf()

for i in range(timeslices):
  Tsur_diff = tsur4[i]-tsur[i]
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(Tsur_diff), cmap=cmap)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(tair_units)
  plt.title((r'$\delta$ Tskin HighAlb-Ref %d') %i)
  #plt.clim(-0.5,0.5)
  figname = outpath + "TSK_" + str(i) + "_WRFTEB_HighAlb-Ref.png"
  plt.savefig(figname)
  plt.clf()

exit()
"""
for i in range(timeslices):
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(qcloudSUM[i]))#, cmap=cmap)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(qcloud_units)
  plt.title((r'Cloud Water Mixing Radio Ref %d') %i)
  #plt.clim(0,12)
  figname = outpath + "QCLOUD_" + str(i) + "_WRFTEB_Ref.png"
  plt.savefig(figname)
  plt.clf()
exit()


for i in range(timeslices):
  qcloudSUM_diff = qcloudSUM4[i]-qcloudSUM[i]
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(qcloudSUM_diff))#, cmap=cmap)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(swdown_units)
  plt.title((r'$\delta$ Cloud Water Mixing Ratio HighAlb-Ref %d') %i)
  #plt.clim(0,12)
  figname = outpath + "QCLOUD_" + str(i) + "_WRFTEB_HighAlb-Ref.png"
  plt.savefig(figname)
  plt.clf()
exit()
"""
"""
for i in range(timeslices):
  SWdownT_diff = swdownT4[i]-swdownT[i]
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(SWdownT_diff))#, cmap=cmap)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(swdown_units)
  plt.title((r'$\delta$ SWDN Top HighAlb-Ref %d') %i)
  #plt.clim(0,12)
  figname = outpath + "SWDNT_" + str(i) + "_WRFTEB_HighAlb-Ref.png"
  plt.savefig(figname)
  plt.clf()
exit()
"""
"""
for i in range(timeslices):
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(cldfrSUM[i]))#, cmap=cmap)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(swdown_units)
  plt.title((r'CLDFR Ref %d') %i)
  plt.clim(0,12)
  figname = outpath + "CLDFR_" + str(i) + "_WRFTEB_Ref.png"
  plt.savefig(figname)
  plt.clf()
#exit()

for i in range(timeslices):
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(cldfr4[i]), cmap=cmap)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(swdown_units)
  plt.title((r'CLDFR HighAlb %d') %i)
  #plt.clim(-0.5,0.5)
  figname = outpath + "CLDFR_" + str(i) + "_WRFTEB_HighAlb.png"
  plt.savefig(figname)
  plt.clf()

exit()
"""

for i in range(timeslices):
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(lwdown[i]), cmap=cmap)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(swdown_units)
  plt.title((r'LWDOWN Ref %d') %i)
  #plt.clim(-0.5,0.5)
  figname = outpath + "LWDOWN_" + str(i) + "_WRFTEB_Ref.png"
  plt.savefig(figname)
  plt.clf()

for i in range(timeslices):
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(lwdown4[i]), cmap=cmap)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(swdown_units)
  plt.title((r'LWDOWN HighAlb %d') %i)
  #plt.clim(-0.5,0.5)
  figname = outpath + "LWDOWN_" + str(i) + "_WRFTEB_HighAlb.png"
  plt.savefig(figname)
  plt.clf()

#exit()

for i in range(timeslices):
  LWdown_diff = lwdown4[i]-lwdown[i]
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(LWdown_diff), cmap=cmap)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(swdown_units)
  plt.title((r'$\delta$ LWDOWN HighAlb-Ref %d') %i)
  #plt.clim(-0.5,0.5)
  figname = outpath + "LWDOWN_" + str(i) + "_WRFTEB_HighAlb-Ref.png"
  plt.savefig(figname)
  plt.clf()

#exit()


for i in range(timeslices):
  SWdown_diff = swdown4[i]-swdown[i]
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(SWdown_diff), cmap=cmap)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(swdown_units)
  plt.title((r'$\delta$ SWDOWN HighAlb-Ref %d') %i)
  #plt.clim(-0.5,0.5)
  figname = outpath + "SWDOWN_" + str(i) + "_WRFTEB_HighAlb-Ref.png"
  plt.savefig(figname)
  plt.clf()
  #plt.show()

for i in range(timeslices):
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(swdown[i]), cmap=cmap)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(swdown_units)
  plt.title((r'SWDOWN Ref %d') %i)
  #plt.clim(-0.5,0.5)
  figname = outpath + "SWDOWN_" + str(i) + "_WRFTEB_Ref.png"
  plt.savefig(figname)
  plt.clf()

#exit()

for i in range(timeslices):
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(swdown4[i]), cmap=cmap)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(swdown_units)
  plt.title((r'SWDOWN HighAlb %d') %i)
  #plt.clim(-0.5,0.5)
  figname = outpath + "SWDOWN_" + str(i) + "_WRFTEB_HighAlb.png"
  plt.savefig(figname)
  plt.clf()

for i in range(timeslices):
  tair_diff = tair1[i]-tair[i]
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(tair_diff), cmap=cmap)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(tair_units)
  plt.title((r'$\delta$ tair Dens-Ref %d') %i)
  plt.clim(-0.5,0.5)
  figname = outpath + "Tair_" + str(i) + "_WRFTEB_Dens-Ref.png"
  plt.savefig(figname)
  plt.clf()
  #plt.show()

#exit()

"""
for i in range(timeslices):
  tair_diff = tair2[i]-tair[i]
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(tair_diff), cmap=cmap)
  plt.title((r'$\delta$ tair TC-Ref %d') %i) #day %s UTC %s' %(str(day), str(hour)))
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(tair_units)
  plt.clim(-2,2)
  figname = outpath + "Tair_" + str(i) + "_WRFTEB_TC-Ref.png"
  plt.show()
  #plt.savefig(figname)
"""
"""
for i in range(timeslices):
  tair_diff = tair3[i]-tair[i]
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(tair_diff), cmap=cmap)
  plt.title((r'$\delta$ tair Unseal-Ref %d') %i)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(tair_units)
  plt.clim(-2,2)
  figname = outpath + "Tair_" + str(i) + "_WRFTEB_Unseal-Ref.png"
  plt.show()
"""

for i in range(timeslices):
  tair_diff = tair4[i]-tair[i]
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(tair_diff), cmap=cmap)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(tair_units)
  plt.title((r'$\delta$ tair HighAlb-Ref %d') %i)
  plt.clim(-2,2)
  figname = outpath + "Tair_" + str(i) + "_WRFTEB_HighAlb-Ref.png"
  plt.savefig(figname)
  plt.clf()
  #plt.show()

exit()

for i in range(timeslices):
  LE_diff = LE3[i]-LE[i]
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(LE_diff), cmap=cmap)
  plt.title((r'$\delta$ LE Unseal-Ref %d') %i)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(lwup_units)
  plt.clim(-150,150)
  figname = outpath + "LWup_" + str(i) + "_WRFTEB_Iso-Ref.png"
  plt.show()

exit()
for i in range(timeslices):
  lwup_diff = lwup2[i] -lwup[i]
  #Q_diff = (swdown2-swup2[i])-(swdown[i]-swup[i])
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(lwup_diff), cmap=cmap)
  plt.title((r'$\delta$ lwup Iso-Ref %d') %i)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(swup_units)
  plt.clim(-15,15)
  #figname = outpath + "swup_" + str(i) + "_WRFTEB_Unseal-Ref.png"
  plt.show()




