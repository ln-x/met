# -*- coding: utf-8 -*-
__author__ = 'lnx'
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
#from pylab import *
import csv

'''This file plots 2D maps of SURFEX.nc files.  
This is the cleaned version of the script, for all comments see Fig4_plotSURFFEXDIFF_nc1.py
For hourly loop look at Fig5_plotSURFEX_nc1_hourly.py'''

outputpath = '/media/lnx/Norskehavet/OFFLINE/'

##pgd_file = '/media/lnx/Norskehavet/OFFLINE/20150804_FR_Ref/PGD.nc'
pgd_file = '/media/lnx/Norskehavet/OFFLINE/NEW_2069OPT/dx345/PGD.nc'
forc = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201508/Ref_Heidi_Lu_2015_1stRun/wrfout_d03_2015-08-05_18_00_00.nc'
file = '/media/lnx/Norskehavet/OFFLINE/old/20150804_FR_Ref/SURF_ATM_DIAGNOSTICS.OUT.nc'
file1 = '/media/lnx/Norskehavet/OFFLINE/old/20150804_FR_Ref/TEB_DIAGNOSTICS.OUT.nc'
#file2 = '/media/lnx/Norskehavet/OFFLINE/old/20150804_FR_Spr/TEB_DIAGNOSTICS.OUT.nc'
ref69_tebD = '/media/lnx/Norskehavet/OFFLINE/NEW_2069REF/dx345/TEB_DIAGNOSTICS.OUT.nc'
##file3 = '/media/lnx/Norskehavet/OFFLINE/old/20150804_FR_Opt/TEB_DIAGNOSTICS.OUT.nc'
opt69_surf = '/media/lnx/Norskehavet/OFFLINE/NEW_2069OPT/dx345/SURF_ATM_DIAGNOSTICS.OUT.nc'
opt69_tebD = '/media/lnx/Norskehavet/OFFLINE/NEW_2069OPT/dx345/TEB_DIAGNOSTICS.OUT.nc'
Bezirksgrenzen ="/media/lnx/Norskehavet/OFFLINE/Georef/BEZIRKSGRENZEOGD/BEZIRKSGRENZEOGDPolygon"
Bezirke = "/media/lnx/Norskehavet/OFFLINE/Georef/POL_BEZ_050/POL_BEZ_050Polygon"
Naturschutzgebiete = "/media/lnx/Norskehavet/OFFLINE/Georef/NSGEB050/NSGEB050"

pgd = Dataset(pgd_file, mode='r')
f = Dataset(forc, mode='r')
fh = Dataset(file, mode='r')
fh1 = Dataset(file1, mode='r')
#fh2 = Dataset(file2, mode='r')
f_ref69_tebD = Dataset(ref69_tebD, mode='r')
f_opt69_surf = Dataset(opt69_surf, mode='r')
f_opt69_tebD = Dataset(opt69_tebD, mode='r')

hour = 12
index = 6+(4*24)+hour #start: 5., min. 3 Tage Spinnoff
#print index

lons = f.variables['XLONG'][1]  #lon (199x)135x174
lats = f.variables['XLAT'][1]   #lat (199x)135x174

xx = fh.variables['xx'][:]  #shape: (174,)
yy = fh.variables['yy'][:]  #shape: (135,)

XX = pgd.variables['XX'][:]  #shape: (174,)
YY = pgd.variables['YY'][:]  #shape: (135,)

print xx.shape, yy.shape
#lons2= lons[1,:]
#lats2= lats[:,1]

FRAC_TOWN = pgd.variables['FRAC_TOWN']#[index]
print "FRAC_TOWN", FRAC_TOWN.shape
#print FRAC_TOWN
Tair = fh.variables['T2M'][index]
print Tair.shape
Tair_opt69 = f_opt69_surf.variables['T2M'][index]
#print Tair_opt69.shape


UTCIsun = fh1.variables['UTCI_OUTSUN'][index]
UTCIshade = fh1.variables['UTCI_OUTSHAD'][index]
#UTCIsun2 = fh2.variables['UTCI_OUTSUN'][index]
#UTCIshade2 = fh2.variables['UTCI_OUTSHAD'][index]
UTCIsun_ref69 = f_ref69_tebD.variables['UTCI_OUTSUN'][index]
UTCIsha_ref69 = f_ref69_tebD.variables['UTCI_OUTSHAD'][index]
UTCIsun_opt69 = f_opt69_tebD.variables['UTCI_OUTSUN'][index]
UTCIsha_opt69 = f_opt69_tebD.variables['UTCI_OUTSHAD'][index]
HVAC = fh1.variables['HVAC_CL'][index]
#HVAC2 = fh2.variables['HVAC_CL'][index]
UTCI_units = fh1.variables['UTCI_OUTSUN'].units
HVAC_units = fh1.variables['HVAC_CL'].units

fh.close()
#fh2.close()
f_opt69_surf.close()
f_opt69_tebD.close()
pgd.close()

m = Basemap(width=57943,height=44955,\
            #rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            #resolution='l'
            )
#lon, lat = np.meshgrid(lons2, lats2)
xi, yi = m(lons, lats)
m.readshapefile(Bezirksgrenzen,'NAMEK')
m.readshapefile(Bezirke,'PBNAME')
#m.readshapefile(Naturschutzgebiete,'PBNAME')

#exit()

'''UTCI'''

#dUTCIsun = UTCIsun2-UTCIsun
#dUTCIshade = UTCIshade2-UTCIshade
dUTCIsun_opt69 = UTCIsun_opt69-UTCIsun_ref69
dUTCIsha_opt69 = UTCIsha_opt69-UTCIsha_ref69
cmap = plt.cm.get_cmap('RdBu', 11)  # 11 discrete colors

#"""
print FRAC_TOWN
cs = plt.contourf(xx,yy,FRAC_TOWN)
#cs = m.pcolor(xi,yi,np.squeeze(FRAC_TOWN))
#cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
#cbar.set_label(u"-")
#plt.title('FRAC_TOWN Opt')
#figname = outputpath + "FRAC_TOWN Opt" + str(hour)+ ".png"
#plt.savefig(figname)
plt.show()
exit()
#"""
"""
cs = plt.contourf(xx,yy,Tair_opt69)
#cs = m.pcolor(xi,yi,np.squeeze(Tair))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"K")
plt.title('Tair Opt 2069-07-04 12UTC')
figname = outputpath + "Tair_Opt_20690704_" + str(hour)+ ".png"
plt.savefig(figname)
"""
#plt.show()
#exit()


"""
cs = plt.contourf(xx,yy,Tair)
#cs = m.pcolor(xi,yi,np.squeeze(Tair))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"K")
plt.title('Tair Ref 2015-08-10 12UTC')
figname = outputpath + "Tair_Ref_20150810_" + str(hour)+ ".png"
plt.savefig(figname)
#exit()

cs = plt.contourf(xx,yy,UTCIsun)
#cs = m.pcolor(xx,yy,np.squeeze(UTCIsun))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('UTCIsun Ref 2015-08-10 12UTC')
figname = outputpath + "UTCI_OUTSUN_Ref_20150810_" + str(hour)+ ".png"
plt.savefig(figname)

cs = plt.contourf(xx,yy,UTCIshade)
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
plt.title('UTCIshade Ref 2015-08-10 12UTC')
figname = outputpath + "UTCI_OUTSHADE_Ref_20150810_" + str(hour)+ ".png"
plt.savefig(figname)
#plt.show()

levels=[-4,-3,-2,-1,0,1,2,3,4]

cs = plt.contourf(xx,yy,dUTCIsun, levels, extend="both")
plt.title('dUTCIsun Spr-Ref 2015-08-10 12UTC')
plt.colorbar(cs)
cbar.ax.set_ylabel(u'dUTCI [°C]')
figname = outputpath + "dUTCIsu_Spr-Ref_" + str(hour)+ ".png"
plt.savefig(figname)
plt.show()

cs1 = plt.contourf(xx,yy,dUTCIshade,levels, extend="both")
plt.title('dUTCIshade Spr-Ref 2015-08-10 12UTC')
plt.colorbar(cs1)
cbar.ax.set_ylabel(u'dUTCI [°C]')
figname = outputpath + "dUTCIsh_Spr-Ref_" + str(hour)+ ".png"
plt.savefig(figname)
plt.show()

cs = plt.contourf(xx,yy,UTCIsun_Opt)
#cs = m.pcolor(xx,yy,np.squeeze(UTCIsun))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('UTCIsun Ref 2015-08-10 12UTC')
figname = outputpath + "UTCI_OUTSUN_Opt_20150810_" + str(hour)+ ".png"
plt.savefig(figname)

cs = plt.contourf(xx,yy,UTCIshade_Opt)
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
plt.title('UTCIshade Ref 2015-08-10 12UTC')
figname = outputpath + "UTCI_OUTSHADE_Opt_20150810_" + str(hour)+ ".png"
plt.savefig(figname)

cs2 = plt.contourf(xx,yy,dUTCIsun_Opt,levels, extend="both")
plt.title('dUTCIsun Opt-Ref 2015-08-10 12UTC')
plt.colorbar(cs2)
cbar.ax.set_ylabel(u'dUTCI [°C]')
figname = outputpath + "dUTCIsu_Opt-Ref_" + str(hour)+ ".png"
plt.savefig(figname)
plt.show()

cs3 = plt.contourf(xx,yy,dUTCIshade_Opt,levels, extend="both")
plt.title('dUTCIshade Opt-Ref 2015-08-10 12UTC')
plt.colorbar(cs3)
cbar.ax.set_ylabel(u'dUTCI [°C]')
figname = outputpath + "dUTCIsh_Opt-Ref_" + str(hour)+ ".png"
plt.savefig(figname)
plt.show()


abslevels = [30,32.5,35,37.5,40,42.5, 45,47.5,50,52.5, 55]

cs2 = plt.contourf(xx,yy,UTCIsun_opt69, abslevels, extend="both")#,  vmin=28, vmax=60)
#cs = m.pcolor(xx,yy,np.squeeze(UTCIsun))
cbar2 = m.colorbar(cs2, location='bottom', pad="10%")#, extend="both")
cbar2.set_label(u"°C")
plt.title('UTCIsun Opt 2069-07-04 12UTC')
figname2 = outputpath + "UTCI_OUTSUN_Opt_20690704_" + str(hour)+ ".png"
plt.savefig(figname2)

cs3 = plt.contourf(xx,yy,UTCIsha_opt69, abslevels, extend="both")# vmin=28, vmax=60)
cbar3 = m.colorbar(cs3, location='bottom', pad="10%")#, extend="both")
cbar3.set_label(u"°C")
plt.title('UTCIshade Opt 2069-07-04 12UTC')
figname3 = outputpath + "UTCI_OUTSHADE_Opt_20690704_" + str(hour)+ ".png"
plt.savefig(figname3)
#plt.show()
"""
levels=[-4,-3,-2,-1,0,1,2,3,4]
"""
cs4 = plt.contourf(xx,yy,dUTCIsun_opt69, levels, extend="both")
plt.title('dUTCIsun Opt-Ref 2069-07-04 12UTC')
cbar4 = m.colorbar(cs4, location='bottom')#, pad="10%")#, extend="both")
#plt.colorbar(cs)
cbar4.set_label(u'dUTCI [°C]')
figname = outputpath + "dUTCI_OUTSUN_Opt-Ref_20690704_" + str(hour)+ ".png"
plt.savefig(figname)
#plt.show()
exit()
#"""
cs5 = plt.contourf(xx,yy,dUTCIsha_opt69,levels, extend="both")
plt.title('dUTCIshade Opt-Ref 2069-07-04 12UTC')
cbar5 = m.colorbar(cs5, location='bottom')#, pad="10%")#, extend="both")
#plt.colorbar(cs1)
cbar5.set_label(u'dUTCI [°C]')
figname = outputpath + "dUTCI_OUTSHADE_Opt-Ref_20690704_" + str(hour)+ ".png"
plt.savefig(figname)
#plt.show()

exit()
#m.drawlsmask(land_color='coral',ocean_color='aqua',lakes=True)
#m.bluemarble()
#m.shadedrelief()
#m.etopo()
#plt.show()
