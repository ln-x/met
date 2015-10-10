import os
import shutil
import csv 

Names=["049_model","air_temp","bc_flow",\
"bc_temp","bottom_width","elevation","glorad",\
"rel_humidity","veg_density","veg_height","veg_overhang","wind"]
switch=["high","low"]

for name in Names : 
	for s in switch : 
		path1="/run/media/heidi/STACHEKEY/049_with_errors/"+name+"/049/"+s+"/"
		path2="/home/heidi/hs/"+name+s+"/"
		print path2
		shutil.copytree(path1,path2) 
		os.chdir(path2)
		with open('HeatSource_Control.csv','rb') as control : 
			with open('fichier.csv','wb') as fichier :
				reader=csv.reader(control, delimiter=',', quotechar='|')
				writer=csv.writer(fichier,delimiter=',', quotechar='|')
				for row in reader : 
					if row[0]=='2' : 
						writer.writerow([row[0],row[1],name+"_049_"+s])
					elif row[0]=='4' : 
						output=path2"outputfiles/"
						writer.writerow([row[0],row[1],output])
					elif row[0]=='5' : 
						input=path2"inputfiles/"
						writer.writerow([row[0],row[1],input])
					else : 
				writer.writerow(row)
		os.remove('HeatSource_Control.csv')
		os.rename('fichier.csv','HeatSource_Control.csv')
		execfile("Start_HS.py")
		shutil.rmtree(path1+"outputfiles/")
		shutil.copytree(path2+"ouputfiles/",path1+"outputfiles/")
		os.chdir("/home/heidi/hs")
		shutil.rmtree(path2)