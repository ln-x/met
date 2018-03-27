# -*- coding: cp1252 -*-

from __future__ import division
import Image, sys, os
import walk

files = walk.enumeratefiles(os.getcwd())
photos =[]
a =[]
##results = []

for file in files:
    if file.endswith('.JPG'):
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
        if c[1][1] > 100:
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
            if g > 100:
                if x < xmin:
                    xmin = x
                if y < ymin:
                    ymin = y
                if x > xmax:
                    xmax = x
                if y > ymax:
                    ymax = y
                    
    pfhoehe = ymax - ymin
    pfbreite = xmax - xmin  
    
    #Angabe realer Breite des Originalhintergrundes in cm
    hintergrundbreite = 50
    pfbreitecm = (pfbreite/width)*hintergrundbreite
    seitenverhaeltnis = height/width
    pfhoehecm = pfbreitecm*seitenverhaeltnis
    gesamtflaeche = hintergrundbreite * (seitenverhaeltnis*hintergrundbreite)
    
    #Output
    
    area = percent*gesamtflaeche #Gesamtflaeche A4 = 21.0cm × 29.7cm = 623.70cm2
    print foto,",",area,"cm2,",pfhoehecm,"cm hoch,", pfbreitecm,"cm breit"
    
    # print foto , " has", count," green pixels (equals ",percent,"*100% of total px)" 
    # print "ca.",pfhoehe," Px hoch; ",pfbreite," Px breit (Gesamtpx hoch/breit:",height,",",width,")"
    # print "ca.", pfhoehecm,"cm hoch und", pfbreitecm, "cm breit."
    
    
##  results.append(percent)
##  outputfile.close()
##
##
##for m in results:
##  print m
##  outputfile.write(m[0] + '\n')
##outputfile.close()


