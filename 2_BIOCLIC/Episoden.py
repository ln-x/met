import os
import shutil
import csv 
import datetime as dt
import matplotlib.pyplot as plt
import numpy


Names=["1jaehrl","5jaehrl","20jaehrl",\
"2003","Max"]
switch=["MLF","Q95"]

for name in Names : 
	for s in switch : 
		path1="/home/lnx/2_Documents/_BioClic/BC/ClimateSzenarios/Episoden/Pinka/2036-2065/"+name+"/"+s+"/Boundary_Conditions.csv"
		t,q,wt = ([] for i in range(3))
		csv_reader = csv.reader(open(path1))
		next(csv_reader)

		for line in csv_reader:
			#t.append(dt.datetime.strptime(line[0],"%d, %m, %Y %H:%M")
			q.append(float(line[1]))
			wt.append(float(line[2]))
		print name, s, numpy.mean(wt), numpy.min(wt), numpy.max(wt), numpy.mean(q)


	fig = plt.figure()
	ax = fig.add_subplot(111)
	bp = plt.boxplot(q)

# ax.plot(wt,color='blue',marker = '.', lw=0.0, label='wt')

# plt.ylim(0,1.0)
# plt.xlabel('time')
# plt.ylabel('wt')
# #plt.grid(True)
# plt.legend()
# #fig.savefig('albedo.png')
plt.show()
		
		
		
		
		
		
		    
		#path1="/run/media/heidi/STACHEKEY/049_with_errors/"+name+"/049/"+s+"/"
		#path2="/home/heidi/hs/"+name+s+"/"
		#print path2
			
		#shutil.copytree(path1,path2) 
		#os.chdir(path2)
				
		#with open('HeatSource_Control.csv','rb') as control : 
			#with open('fichier.csv','wb') as fichier :
				#reader=csv.reader(control, delimiter=',', quotechar='|')
				#writer=csv.writer(fichier,delimiter=',', quotechar='|')
				#for row in reader : 
					#if row[0]=='2' : 
						#writer.writerow([row[0],row[1],name+"_049_"+s])
					#elif row[0]=='4' : 
						#output=path2"outputfiles/"
						#writer.writerow([row[0],row[1],output])
					#elif row[0]=='5' : 
						#input=path2"inputfiles/"
						#writer.writerow([row[0],row[1],input])
					#else : 
				#writer.writerow(row)
		#os.remove('HeatSource_Control.csv')
		#os.rename('fichier.csv','HeatSource_Control.csv')
		#execfile("Start_HS.py")
		#shutil.rmtree(path1+"outputfiles/")
		#shutil.copytree(path2+"ouputfiles/",path1+"outputfiles/")
		#os.chdir("/home/heidi/hs")
		#shutil.rmtree(path2)
		
		
		