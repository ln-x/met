from __future__ import division
import Image, sys, os
import walk

files = walk.enumeratefiles(os.getcwd())
photos =[]
a =[]
##results = []

for file in files:
    if file.endswith('.jpg'):
        photos.append(file)
#print photos

##outputfile = open('results.txt','w')

for foto in photos:
	im = Image.open(foto)
	pix = im.load()
	
	colors=()
	count = 0
	
	width, height = im.size
	
	#Calculation of Pixelpercentage
	col = im.getcolors(width*height)
	for c in col:
		if c[1][1] < 140:
			count += c[0]	
	
	percent = count/(width * height)

	#Calculation of Pixelheight and width

	xmax = 0
	ymax = 0
	xmin = width
	ymin = height
		
	for x in range(100, width):
		for y in range(100 , height):
			color = pix[x,y]	
			r, g, b = color
			if g < 100:
				if x < xmin:
					xmin = x
				if y < ymin:
					ymin = y
				if x > xmax:
					xmax = x
				if y > ymax:
					ymax = y
					
	hoehe = ymax - ymin
	breite = xmax - xmin	
	
	#Angabe realer Breite des Bildes!
	hoehecm = (hoehe/height)*50
	breitecm = (breite/width)*30
	
	#Output
	print foto , " has", count," green pixels (equals ",percent,"*100% of total px)" 
	print "ca.",hoehe," Px hoch; ",breite," Px breit (Gesamtpx hoch/breit:",height,",",width,")"
	print "ca.", hoehecm,"cm hoch und", breitecm, "cm breit."
	
##	results.append(percent)
##	outputfile.close()
##
##
##for m in results:
##	print m
##	outputfile.write(m[0] + '\n')
##outputfile.close()


