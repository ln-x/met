# -*- coding: UTF-8 -*-

from __future__ import division  
import sys, os
import walk

min_x = 108 #int(sys.argv[1])
max_x = 190 #int(sys.argv[2])
min_y = 134 #int(sys.argv[3])
max_y = 222 #int(sys.argv[4])
path = '/media/x'

outputfile = open('results.txt','w')

files = walk.enumeratepath(os.getcwd())
# files = walk.enumeratpath(path)

slices = []
mittelwerte = []

for file in files:
    if file.endswith('.dat'):
        slices.append(file)
        print file


print slices

for slice in slices:
	file = open(slice, 'r')
	print 'file : ', slice
	data = file.readlines()
	werte = data[1:]
	#print werte
	zahlen = []
	for zeile in werte:
		zw = zeile.split()
		#print zw
		zahlen.append((float(zw[0]),float(zw[1]),float(zw[2])))
	t_sum = 0
	t_n = 0

	for werttup in zahlen:
		#print werttup
		if werttup[0] > min_x and werttup[0] < max_x and werttup[1] > min_y and werttup[1] < max_y:
			t_n += 1
			t_sum += werttup[2]
			#print werttup
			line = str(werttup[0]) + ' ' +str(werttup[1]) + ' ' + str(werttup[2]) + '\n'
			#print line
			#outputfile.write(line)

	#print 'Die Summe der Temperaturen beträgt: ', t_sum
	mw = t_sum/t_n
	tmw = str(mw)
	#print 'Der Mittelwert beträgt:', tmw
	mittelwerte.append((slice,tmw))
	file.close()

#print mittelwerte	

for m in mittelwerte:
	#print m
	outputfile.write(m[0][26:] + ' = ' + m[1] + '\n')
outputfile.close()


