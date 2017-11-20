import numpy as np
layerx1 = iface.activeLayer()

###ACCESS FIELDS:
#vectorlayer:
"""
print ("Layername = {0} with {1:d} features(Objekten) und {1:d} fields (Attributen)").format(layerx1.name(),layerx1.featureCount(),layerx1.fields())
#rasterlayer:
#print ("bandCount {1:d} , width  {1:d} , height {1:d}, extent{1:d}, rasterUnitsperPixelX {1:d}").format(layerx1.bandCount(),layerx1.width(),layerx1. height(), layerx1.extent(), layerx1.UnitesPerPixelX())

print layerx1.name() 
print layerx1.featureCount() 
print layerx1.fields() 
print layerx1.pendingFields()
"""
fields = layerx1.pendingFields()
#print fields

"""
for field1 in fields:
 #   print field1.name(), field1.typeName()
"""
print fields.field(0).name()  #(0): print the 1st field name
print fields.field(0).type() #?
print fields.field(0).typeName()  #Integer/Str,...
print fields.field(0).precision() 
print fields.field(0).length() 

###ACCESS VALUES:
FMZKOBJECTs = layerx1.getFeatures()

attable = []

for feat in FMZKOBJECTs:
    attrs = feat.attributes()
    attable.append(attrs)
    #print attrs[1]   #print column 2 of attribute table

print attable[0] #get first row, all columns
print attable[1]
print attable[2]
print attable[0][1] #get first rows, second column

attable = np.array(attable)
print attable[:,0]  #get all rows, first column

    
"""
totalarea = 0
for FMZKOBJECT in FMZKOBJECTs:
    fmzkgeometry = FMZKOBJECT.geometry()
    print fmzkgeometry
    totalarea += fmzkgeometry.area()

print "total area of all FMZK Objects:" + str(totalarea)
print "2.5km x 2.5km = 6.5km2 = 6 250 000m2"
"""