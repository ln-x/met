import fonctions38 

with open('names.txt','wb') as names : 
	tab=fonctions38.genere_names(100,279) 
	for name in tab : 
		names.write(name+'\n \n')
