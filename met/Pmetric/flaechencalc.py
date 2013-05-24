from __future__ import division
import Image, sys, os
import walk

files = walk.enumeratefiles(os.getcwd())
print files
photos =[]
#percentage = []

for file in files:
    if file.endswith('.jpg'):
        photos.append(file)
print photos

#outputfile = open('percentages.txt','w')

for foto in photos:
	im = Image.open(foto)
	colors=()
	count = 0
	#print "hello ", foto, ' in process' 

	width, height = im.size
		
	#version3
	col = im.getcolors(width*height)
	for c in col:
		print c
		if c[1][1] < 140:
			count += c[0]
	
	#version 2
	##data = list(im.getpixel
	##for d in data:
	##	if d[1] > 100:
	##		count +=1
	
	#version 1
	##for x in range(width):
	##	for y in range(height):
	##		color = im.getpixel((x,y))
	##		r, g, b = color
	##		if g > 50:
	##			count += 1

	#print foto , ' has green pixels: ', count
	percent = count/(width * height)
	#print 'percentage: ', count/(width * height)
	print foto,", ",percent
	
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
