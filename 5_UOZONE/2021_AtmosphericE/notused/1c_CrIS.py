# -*- coding: utf-8 -*-
__author__ = 'lnx'
import numpy as np
import pandas as pd
from netCDF4 import Dataset
from datetime import datetime, timedelta

start = datetime(2013, 1, 1, 0, 00)
end = datetime(2013, 12, 1, 0, 00)

Jan = datetime(2013, 1, 31, 0, 00)
Apr = datetime(2013, 4, 30, 0, 00)
Jul = datetime(2013, 7, 31, 0, 00)
Oct = datetime(2013, 10, 31, 0, 00)

"""
#1) EXTRACT CrIS ISOPRENE DATA:
infile2 = '/windata/DATA/remote/satellite/SuomiNNP_CrIS/201310_CrIS_Isoprene.nc'
#global isoprene data: find Vienna
nci = Dataset(infile2)
print(nci.variables['lat'][69]) #48LAT
print(nci.variables['lon'][79]) #15LON
print(nci.variables['Isop'][69,79])
#exit()
"""
#[molec/cm²] CrIS retrieved isoprene column density for [69/78] LAT48/LON15
iso_2013_01 = 843505200000000.0  #for [69/79]- LAT48/LON17.5: 3045126200000000.0
iso_2013_04 = 581560250000000.0  #for [69/79]- LAT48/LON17.5:  370901870000000.0
iso_2013_07 = 247324400000000.0  #for [69/79]- LAT48/LON17.5: 2049826000000000.0
iso_2013_10 = 319617700000000.0  #for [69/79]- LAT48/LON17.5: 4079812300000000.0

"""
#2) MONTHLY PBL Height in [m]:
starttime = datetime(2007, 1, 1, 0, 00)
wrfc_time_construct = np.array([starttime + timedelta(hours=i) for i in range(87673)])
#Jans indexes for Vienna gridpoint:
wrf_vie_i=109
wrf_vie_j=58 
path1 = '/windata/DATA/models/boku/wrf_chem/reanalysis/era-interim/HCera_9km_2007-16_ATTR/model_base_results/'  #for other variables see: part48/wrfout../ index: 110, 59 =>
f_pblh = Dataset(path1 + 'HC2007t16-W-E-Cam-TNO3ATTR_zmla.nc', mode='r') #DRY_DEP_LEN (bio_emissions_dimensions_stag: ozone = 6)
PBLH = f_pblh.variables['zmla'][:,wrf_vie_j,wrf_vie_i]
pblh = pd.Series(PBLH[:],index=wrfc_time_construct)
pblh_d = pblh.resample('D').mean()
pblh_m = pblh.resample('M').mean()

pblh_dmax = pblh.resample('D').max()
pblh_dmax_mean = pblh_dmax.resample('M').mean()

print(pblh_m[start:end])
#2013-01-31    304.424469 
#2013-02-28    373.783325
#2013-03-31    502.387085
#2013-04-30    646.482544
#2013-05-31    726.711243
#2013-06-30    728.487915
#2013-07-31    883.234009
#2013-08-31    699.101257
#2013-09-30    553.947571
#2013-10-31    319.748627
#2013-11-30    333.975800
print(pblh_dmax_mean[start:end])
#2013-01-31     498.907867
#2013-02-28     745.905090
#2013-03-31    1013.396057
#2013-04-30    1482.740356
#2013-05-31    1511.288086
#2013-06-30    1459.963623
#2013-07-31    1766.218140
#2013-08-31    1608.325439
#2013-09-30    1190.809570
#2013-10-31     786.463562
#2013-11-30     611.065552
#exit()
"""
pblh_2013_jan = 304.424469 #max 498.907867 #mean 304.424469
pblh_2013_apr = 646.482544 #max 1482.740356 #mean 646.482544
pblh_2013_jul = 883.234009 #max 1766.218140 #mean 883.234009
pblh_2013_oct = 319.748627 #max 786.463562 #mean 319.748627

"""
3) CONVERSION TO MIXING RATIO (PPB)
molecm2 = 247324400000000.0 #molec/cm2
molecm3 = molecm2/100000  # assume distribution only in the PBL (1km - 1000m - 100 000cm)
ppb = molecm3/2.46E+10   #http://cires1.colorado.edu/jimenez-group/Press/2015.05.22-Atmospheric.Chemistry.Cheat.Sheet.pdf
                        #Values at 1 atm and 298 K (Ref: Finlayson Pitts & Pitts, p. 34
print(ppb)  #0.100538373984
"""

#TODO: ratio ground surface to total isoprene in PBL!

iso_ppb_201301 = (iso_2013_01/(pblh_2013_jan*100))/2.46E+10
iso_ppb_201304 = (iso_2013_04/(pblh_2013_apr*100))/2.46E+10
iso_ppb_201307 = (iso_2013_07/(pblh_2013_jul*100))/2.46E+10
iso_ppb_201310 = (iso_2013_10/(pblh_2013_oct*100))/2.46E+10

print(iso_ppb_201301, iso_ppb_201304, iso_ppb_201307, iso_ppb_201310)
#1.12634931682488 0.3656813441989192 0.1138298264777753 0.4063376144190389

"""
4) COMPARISON CrIS vs WRFCHEM ISO MIXING RATIOS
"""
starttime = datetime(2013, 1, 9, 1, 00)
wrfc_time_construct = np.array([starttime + timedelta(hours=i) for i in range(14400)])

file = '/windata/DATA/models/boku/wrf_chem/reanalysis/era-interim/HCera_9km_2007-16_ATTR/wrfout_d01_2013-01-09_01_2014-09-01_01_ex.nc'
fh = Dataset(file, mode='r')
wrfc_iso = fh.variables["iso"][:,0,0,0]
wrfc_iso = pd.Series(wrfc_iso[:],index=wrfc_time_construct) #wrfc_o3_d =wrfc_o3.resample('D').mean() #TODO Only valid with DatetimeIndex, TimedeltaIndex or PeriodINdex, but got instance of 'Index'
wrfc_iso_m =wrfc_iso.resample('M').mean()
#print(wrfc_iso_m[start:end]*1000)
#2013-01-31    0.014408
#2013-02-28    0.008968
#2013-03-31    0.010226
#2013-04-30    0.034232
#2013-05-31    0.076607
#2013-06-30    0.215246
#2013-07-31    0.275418
#2013-08-31    0.216512
#2013-09-30    0.098904
#2013-10-31    0.064013
#2013-11-30    0.021266

print("2013 JAN: CrIS=", iso_ppb_201301, "WRFC=", wrfc_iso_m[Jan]*1000, "CrIS-WRFC=", iso_ppb_201301-wrfc_iso_m[Jan]*1000)
print("2013 APR: CrIS=", iso_ppb_201304, "WRFC=", wrfc_iso_m[Apr]*1000, "CrIS-WRFC=", iso_ppb_201304-wrfc_iso_m[Apr]*1000)
print("2013 JUL: CrIS=", iso_ppb_201307, "WRFC=", wrfc_iso_m[Jul]*1000, "CrIS-WRFC=", iso_ppb_201307-wrfc_iso_m[Jul]*1000)
print("2013 OCT: CrIS=", iso_ppb_201310, "WRFC=", wrfc_iso_m[Oct]*1000, "CrIS-WRFC=", iso_ppb_201310-wrfc_iso_m[Oct]*1000)

#LAT48/LON17.5: max PBL
#2013 JAN: CrIS= 0.687277782859509 WRFC= 0.01440767664462328 CrIS-WRFC= 0.6728701062148857
#2013 APR: CrIS= 0.15943897711721614 WRFC= 0.03423210364417173 CrIS-WRFC= 0.1252068734730444
#2013 JUL: CrIS= 0.05692296534998777 WRFC= 0.2754184533841908 CrIS-WRFC= -0.21849548803420304
#2013 OCT: CrIS= 0.16520268781243685 WRFC= 0.06401279097190127 CrIS-WRFC= 0.10118989684053559
#2013 JUL: CrIS= 0.1423074133749694 WRFC= 0.2754184533841908 CrIS-WRFC= -0.1331110400092214

#LAT48/LON17.5: mean PBL
#2013 JAN: CrIS= 1.12634931682488 WRFC= 0.01440767664462328 CrIS-WRFC= 1.1119416401802567
#2013 APR: CrIS= 0.3656813441989192 WRFC= 0.03423210364417173 CrIS-WRFC= 0.33144924055474745
#2013 JUL: CrIS= 0.1138298264777753 WRFC= 0.2754184533841908 CrIS-WRFC= -0.1615886269064155
#2013 OCT: CrIS= 0.4063376144190389 WRFC= 0.06401279097190127 CrIS-WRFC= 0.3423248234471376
#2013 JUL: CrIS= 0.28457456619443827 WRFC= 0.2754184533841908 CrIS-WRFC= 0.009156112810247474

#LAT48/LON15: mean PBL
#2013 JAN: CrIS= 1.12634931682488 WRFC= 0.01440767664462328 CrIS-WRFC= 1.1119416401802567
#2013 APR: CrIS= 0.3656813441989192 WRFC= 0.03423210364417173 CrIS-WRFC= 0.33144924055474745
#2013 JUL: CrIS= 0.1138298264777753 WRFC= 0.2754184533841908 CrIS-WRFC= -0.1615886269064155
#2013 OCT: CrIS= 0.4063376144190389 WRFC= 0.06401279097190127 CrIS-WRFC= 0.3423248234471376

ratioSURFACE_PBL = 2.5  #realistic: 1.5?, fit to wrfchem: 2.5?
print("2013 JUL: CrIS=", iso_ppb_201307*ratioSURFACE_PBL, "WRFC=", wrfc_iso_m[Jul]*1000, "CrIS-WRFC=", (iso_ppb_201307*ratioSURFACE_PBL)-wrfc_iso_m[Jul]*1000)
#2013 JUL: CrIS= 0.28457456619443827 WRFC= 0.2754184533841908 CrIS-WRFC= 0.009156112810247474
