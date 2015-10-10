import fonctions38 
import shutil
import os

start = 256
end = 279
names=fonctions38.genere_names(start, end)

for name in names : 
	new_name=name[:4]+"b"+name[4:]
	shutil.copytree("Data\\"+name+"\\","Pinka38\\"+new_name+"\\")
	print(new_name)
	val_1percent=fonctions38.prepare_inflows(name)
	shutil.copyfile("fichier.csv","Pinka38\\"+new_name+"\\inputfiles\\Inflows_P_I1.csv"); 
	os.remove('fichier.csv')
	fonctions38.rewrite_accretion(new_name, val_1percent)
	fonctions38.rename_control(new_name)