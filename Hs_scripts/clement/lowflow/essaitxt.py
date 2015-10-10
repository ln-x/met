

name="S214_P_STQ_2030_Max_MLF"
with open("Data//"+name+"//outputfiles//Temp_H2O.txt",'r') as temp_eau : 
	txt_temp_eau=temp_eau.read()
	txt_temp_eau=txt_temp_eau.split("\n")
	for indice in range(0,6) : 
		del txt_temp_eau[0]
	print(txt_temp_eau[1][119*14:119*14+7])
	print(txt_temp_eau[1][124*14:124*14+7])
	print(txt_temp_eau[1][130*14:130*14+7])
	print(txt_temp_eau[1][140*14:140*14+7])
	print(txt_temp_eau[1][148*14:148*14+7])
	print(txt_temp_eau[1][153*14:153*14+7])