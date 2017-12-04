# -*- coding: utf-8 -*-
__author__ = 'lnx'

#11034 Wien-Innere Stadt 162201  481154 177
#11035 Wien-Hohe Warte   162123  481455 198
#11036 Schwechat         163411  480637 183
#11037 Gross-Enzersdorf  163333  481159 154
#11040 Wien-Unterlaa     162510  480730 200
#11042 Wien-Stammersdorf 162420  481821 191
#11077 Brunn am Gebirge  161612  480625 291
#11080 Wien-Mariabrunn   161346  481225 225
#11090 Wien-Donaufeld    162553  481526 160

#coord = [162201,481154]

def calc_coordinates(coord):
    latlon = []
    for i in coord:
        deg = float(str(i)[0:2])
        min = float(str(i)[2:4])
        sec = float(str(i)[4:])
        coor_deg = deg + min/60 + sec/3600
        #print coor_deg
        latlon.append(coor_deg)
    return latlon

print "11034 Wien-Innere Stadt", calc_coordinates([162201,481154])
print "11035 Wien-Hohe Warte", calc_coordinates([162123,481455])
print "11036 Schwechat", calc_coordinates([163411,480637])
print "11037 Gross-Enzersdorf", calc_coordinates([163333, 481159])
print "11040 Wien-Unterlaa", calc_coordinates([162510,480730])
print "11042 Wien-Stammersdorf", calc_coordinates([162420,481821])
print "11077 Brunn am Gebirge", calc_coordinates([161612,480625])
print "11080 Wien-Mariabrunn", calc_coordinates([161346,481225])
print "11090 Wien-Donaufeld", calc_coordinates([162553,481526])


"""    
xx_center = 87x = 16.372°
yy_center = 67.5y = 48.2414245° 
1 degree = 111.325km 
0.00328° = 333m = 1x = 1y
"""
latlon = calc_coordinates([162201,481154])
dxx = (latlon[0] -16.372)/0.00328
dyy = (latlon[1] -48.2414245)/0.00328

print dxx, dyy

xx = 87 + dxx
yy = 67.5 + dyy

print xx,yy