import os
import pandas as pd
import shutil
import csv
from BIOCLIC import hs_loader

Names=["049_model","air_temp","bc_flow",\
"bc_temp","bottom_width","elevation","glorad",\
"rel_humidity","veg_density","veg_height","veg_overhang","wind"]
switch=["high","low"]

# path="/home/lnx/PycharmProjects/HS/049_with_errors/"+name+"/049_"+s+"/outputfiles/Temp_H2O.txt"
# x, header, data = hs_loader.loadfile(filename=path)
# data = pd.DataFrame(data)
# data = data.set_index(0)
# daily_max = data.resample('D', how ='max')
# daily_max = daily_max.ix['2013-08-02':'2013-08-08', '12':'83'] #[12:83]
# daily_max = daily_max.mean()
# daily_max = daily_max.mean()


output = open('/home/lnx/Errors.txt','w')



for name in Names : 
	for s in switch : 
		path="/home/lnx/PycharmProjects/HS/049_with_errors/"+name+"/049_"+s+"/outputfiles/Temp_H2O.txt"
		x, header, data = hs_loader.loadfile(filename=path)
		data = pd.DataFrame(data)
		data = data.set_index(0)
		daily_max = data.resample('D', how ='max')
		daily_max = daily_max.ix['2013-08-02':'2013-08-08', '12':'83'] #[12:83]
		daily_max = daily_max.mean()
		daily_max = daily_max.mean()
		error = 23.064685119 - daily_max
		out = [x, str(daily_max), s, str(error)]
		print out
		output.write("\n".join(str(i) for i in out))

output.close()
