
import netCDF4
from netCDF4 import MFDataset

#file = netCDF4.Dataset("/windata/DATA/models/boku/CAMX/BOKU2020/3_CAMXinput_MEGANout/BOKU3/megan_out_CB05_BOKU3_20200101.nc")
f = MFDataset("/windata/DATA/models/boku/CAMX/BOKU2020/3_CAMXinput_MEGANout/BOKU3/megan_out_CB05_BOKU3_20200*.nc")
print(f.variables["ISOP"][:,0,1,1])  #TERP

#data = file.variables["ISOP"][:,1,1,1]
#print(data)


#print(file["ISOP"])
#<class 'netCDF4._netCDF4.Variable'>
#float32 ISOP(TSTEP, LAY, ROW, COL)
#    long_name: ISOP
#    units: mol/s
#    var_desc:
#unlimited dimensions: TSTEP
#current shape = (25, 1, 185, 245)
#filling on, default _FillValue of 9.969209968386869e+36 used
