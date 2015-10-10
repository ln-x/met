import csv
import os 
import shutil

def prepare_inflows(name):
	# power_plants correspond to datas about the power plant 
	# for each p in power_plants, p=(position of the withdrawal flows (km), percentage of Burg inflows, position of the corresponding value of temp in each row of txt_temp_eau)
	power_plants=[(34.5,81.4,119), (32,34.3,124), (29,50,130), (24,98.6, 140), (20.5,98.6, 148), (17.5, 98.6, 153)] 
	percent1=8.7
	with open("Data\\"+name+"\\inputfiles\\Inflows_P_I1.csv",'rb') as inflows : 
				with open('fichier.csv','wb') as fichier : 
					with open("Data\\"+name+"\\outputfiles\\Temp_H2O.txt",'r') as temp_eau : 
						txt_temp_eau=temp_eau.read()
						txt_temp_eau=txt_temp_eau.split("\n")
						for indice in range(0,6) : 
							del txt_temp_eau[0]
						readerinflow=csv.reader(inflows,delimiter=',',quotechar='|')
						writer=csv.writer(fichier, delimiter=',',quotechar='|')
						i=False
						memo={}
						for (row1,row2) in zip(readerinflow, txt_temp_eau) : 
							valeur_row=row1
							if i : 
								for p in power_plants : 
									valeur_1percent=float(row1[1])/percent1
									inflow=p[1]*valeur_1percent
									valeur_row.append(str(inflow)[:6])
									if str(row2[p[2]*14:p[2]*14+7]) != '' : 
										valeur_row.append(str(row2[p[2]*14:p[2]*14+7]))
										memo[p[0]]=str(row2[p[2]*14:p[2]*14+7]);
									else : 
										valeur_row.append(memo[p[0]])
							else : 
								for station in range(14,20) : 
									valeur_row.append("#"+str(station)+"     Inflow Rate (cms)")
									valeur_row.append("#"+str(station)+"     Inflow Temp (*C))")
							writer.writerow(valeur_row)
							i=True
	return valeur_1percent

def rewrite_accretion(new_name,val_1percent):
	power_plants=[(34.5,81.4,119), (32,34.3,124), (29,50,130), (24,98.6, 140), (20.5,98.6, 148), (17.5, 98.6, 153)] 
	with open("Pinka38\\"+new_name+"\\inputfiles\\Accretion_inputs.csv",'rU') as acc : 
		with open('fichier.csv','wb') as fichier : 
			readeracc=csv.reader(acc,delimiter=',',quotechar='|')
			writer=csv.writer(fichier, delimiter=',',quotechar='|')
			for row in readeracc : 
				valeurs_row=row
				for p in power_plants : 
					if valeurs_row[0]==str(p[0]):
						valeurs_row[3]=str(val_1percent*p[1])[:6]
				writer.writerow(valeurs_row)
	os.remove("Pinka38\\"+new_name+"\\inputfiles\\Accretion_inputs.csv")
	shutil.copyfile('fichier.csv',"Pinka38\\"+new_name+"\\inputfiles\\Accretion_inputs.csv")
	os.remove('fichier.csv')
	
def rename_control(new_name) : 
	path = "Pinka38\\"+new_name+"\\"
	with open(path+'HeatSource_Control.csv','rb') as control : 
		with open(path+'fichier.csv','wb') as fichier : 	
			reader=csv.reader(control, delimiter=',', quotechar='|')
			writer=csv.writer(fichier,delimiter=',', quotechar='|')
			for row in reader : 
				if row[0]=='2' : 
					writer.writerow([row[0],row[1],new_name])
				elif row[0]=='4' : 
					output="/home/heidi/hs/"+new_name+"/outputfiles/"
					writer.writerow([row[0],row[1],output])
				elif row[0]=='5' : 
					input="/home/heidi/hs/"+new_name+"/inputfiles/"
					writer.writerow([row[0],row[1],input])
				elif row[0]=='16' : 
					writer.writerow([row[0],row[1],'19'])
				elif row[0]=='18' :
					valeurs_row=row+['34','31.5','28.5','23.5','19.5','17"']
					valeurs_row[14]='37.5'
					writer.writerow(valeurs_row)
				elif row[0]=='41' : 
					writer.writerow([row[0], row[1], 'TRUE'])
				elif row[0]=='40' : 
					writer.writerow([row[0], row[1], 'Hyd_vel_LowFlow.csv'])
				else : 
					writer.writerow(row) 
	os.remove(path+'HeatSource_Control.csv')
	os.rename(path+'fichier.csv',path+'HeatSource_Control.csv')
	
def genere_names(start,end) : 
	names=[]
	folder1=['Lafnitz','Pinka']
	folder2=[('2016-2045','2030'),('2036-2065','2050'),('2071-2100','2085')]
	folder3=[('1jaehrl','1a'),('5jaehrl','5a'),('20jaehrl','20a'),('2003','2003'),('Max','Max')]
	folder4=['MLF','Q95']
	s_number=100; 
	veg_scenario=['STQ','V0','V100']
	for f1 in folder1 : 
		for f2 in folder2 : 
			for f3 in folder3 : 
				for f4 in folder4 : 
					for v in veg_scenario : 
						name=["S"+str(s_number), f1[0] , v, f2[1],f3[1],f4]
						name="_".join(name)
						if (s_number>=start) and (s_number<=end) : 
							names.append(name)
						s_number=s_number+1 
	return names