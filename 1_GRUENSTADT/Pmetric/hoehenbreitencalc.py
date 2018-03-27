from __future__ import division
import Image, sys, os
import walk

files = walk.enumeratefiles(os.getcwd())
#print files
photos =[]
a =[]
#percentage = []

for file in files:
    if file.endswith('.jpg'):
        photos.append(file)
print photos

#outputfile = open('percentages.txt','w')

for foto in photos:
	im = Image.open(foto)
	pix = im.load()
	#print pix[x, y]	
	
	#colors=()
	#countx = 0
	#county = 0
	#print "hello ", foto, ' in process' 

	width, height = im.size
	xmax = 0
	ymax = 0
	xmin = width
	ymin = height
		
	#version 1
	for x in range(100, width):
		for y in range(100 , height):
			color = pix[x,y]	
			#pix[x, y] = value
			#color = pix.getpixel((x,y))
			r, g, b = color
			#countx += 1
			if g < 100:
				if x < xmin:
					xmin = x
				if y < ymin:
					ymin = y
				if x > xmax:
					xmax = x
				if y > ymax:
					ymax = y
					
	#print foto , ' has green pixels: ', count
	#percent = count/(width * height)
	hoehe = ymax - ymin
	breite = xmax - xmin	
	
	#Angabe realer Breite des Bildes!
	hoehecm = (hoehe/height)*50
	breitecm = (breite/width)*30
	
	#print 'percentage: ', count/(width * height)
	#print foto,", ",percent
	print foto
	print "Die Pflanzenhoehe in Pixel ist ca:",hoehe,"(Gesamtpixel hoch:",height,")"
	print "Die Pflanzenbreite in Pixel ist ca:",breite,"(Gesamtpixel breit:",width,")" 
	print "Die Pflanze ist etwa", hoehecm,"cm hoch."
	print "Die Pflanze ist etwa", breitecm,"cm breit."

#	open file in ipython
	
##    percentage.append(percent)
##	file.close()
##
##
##for m in percentage:
##	#print m
##	#outputfile.write(m[0] + '\n')
##outputfile.close()




#		colors[color]=color.get(color, 0)+1
#print ' ','\n '.join('%s'%(col, colors[col]) for col in colors)
