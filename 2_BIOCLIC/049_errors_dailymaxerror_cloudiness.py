import os
import pandas as pd
import shutil
import csv
from BIOCLIC import hs_loader

output = open('/home/lnx/Errors_cloudiness.txt','w')

path1="/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Simulations_Archive/013_P_V_A0_B1_C2_201307010829_cloud0/outputfiles/Temp_H2O.txt"
path2="/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Simulations_Archive/014a_P_V_A0_B1_C2_201307010829_cloud1/outputfiles/Temp_H2O.txt"

path = [path1, path2]

for i in path:
	x, header, data = hs_loader.loadfile(filename=i)
	data = pd.DataFrame(data)
	data = data.set_index(0)
	daily_max = data.resample('D', how ='max')
	daily_max = daily_max.ix['2013-08-02':'2013-08-08', '12':'83'] #[12:83]
	daily_max = daily_max.mean()
	daily_max = daily_max.mean()
	print daily_max
	#error = 23.064685119 - daily_max
	#out = [x, str(daily_max), s, str(error)]
	#print out
	#output.write("\n".join(str(i) for i in out))

#output.close()
