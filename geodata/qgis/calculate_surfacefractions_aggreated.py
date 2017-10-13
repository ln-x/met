import pandas as pd
#import geopandas as gpd
import numpy as np
import numpy_groupies as npg
import dateutil
layerx1 = iface.activeLayer()
fields = layerx1.pendingFields()

##REMOVE AND ADD FIELDS
for field1 in fields:
    print field1.name(), field1.typeName()

print ""

"""
from PyQt4.QtCore import QVariant
caps = layerx1.dataProvider().capabilities()
print layerx1.dataProvider().capabilitiesString()

if caps & QgsVectorDataProvider.DeleteAttributes:
  res = layerx1.dataProvider().deleteAttributes([-2])
if caps & QgsVectorDataProvider.AddAttributes:
  res = layerx1.dataProvider().addAttributes([QgsField("area", QVariant.String), QgsField("builtfrac", QVariant.Int)])
layerx1.updateFields()

#for field1 in fields:
 #   print field1.name(), field1.typeName()
"""

#ayers = QgsMapLayerRegistry.instance().mapLayersByName('my_line') 
#ayerx1 = layers[0]
it = layerx1.getFeatures()
FMZKOBJECTs = layerx1.getFeatures()

#EDIT FEATURES
layerx1.startEditing()
for feat in FMZKOBJECTs:
    fmzkgeometry = feat.geometry()
    area = int(fmzkgeometry.area())
    #layerx1.changeAttributeValue(feat.id(), 2, 30) #This updates the third (index 2) field value to 30 for all layer features.
    layerx1.changeAttributeValue(feat.id(), 19, area)
layerx1.commitChanges()

#CREATE NUMPY MATRIX AND AGGREGATE
all_matrix=[]
request = QgsFeatureRequest()
request.setFlags(QgsFeatureRequest.NoGeometry)
for feat in layerx1.getFeatures(request):
    a=feat.attributes()[0] # > [0} F_KLASSE
    b=feat.attributes()[7] # [1]LC SUEWS
    c=feat.attributes()[9] # [2]OBJECT ID
    d=feat.attributes()[19] # [3] area
    all_matrix.append([a,b,c,d])
matrix=np.array(all_matrix)
#print matrix[:,0] #print first column
#print matrix [0] #print first row
#group_idx = matrix[:,2] #OBJECT ID
#a = matrix[:,1] #LC SUEWS
#area = matrix[:,3]
#REALAREA = npg.aggregate(group_idx, area,  func='sum', fill_value=0) # sum is default

#CREATE PANDAS DATAFRAME
#data = pd.DataFrame.from_csv('phone_data.csv')
data = pd.DataFrame(matrix)
print data 

#data.groupby('month')['duration'].sum()
#grouped = data.groupby([9])[3].sum()
grouped = data.groupby([0,2])[3].sum()

print grouped

layerx1.startEditing()
for feat in FMZKOBJECTs:
    for i in grouped:
        if feat[7] == grouped[1] and feat[7] == "built":
        layerx1.changeAttributeValue(feat.id(), 20, builtfrac)
layerx1.commitChanges()


# Convert date from string to date times
#data['date'] = data['date'].apply(dateutil.parser.parse, dayfirst=True)







"""
group_idx = np.arange(5).repeat(3)
# group_idx: array([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4])
a = np.arange(group_idx.size)
# a: array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])



x = aggregate(group_idx, a,  func='sum', fill_value=0) # sum is default
# x: array([ 3, 12, 21, 30, 39])




FMZKOBJECTs = layerx1.getFeatures()
totalarea = 0
builtarea = 0
sealedarea = 0
for feat in FMZKOBJECTs:
    fmzkgeometry = feat.geometry()
    totalarea += fmzkgeometry.area()
   #print feat.attributes()[0]
  
    if feat.attributes()[0] == 11:
        builtgeometry = feat.geometry()
        builtarea += builtgeometry.area()
    elif feat.attributes()[0] == 21:
        sealedgeometry = feat.geometry()
        sealedarea += sealedgeometry.area()
    else:
       pass

print totalarea
print builtarea
print sealedarea
builtfrac = builtarea/totalarea

print "total area = " + str(totalarea)
print "toal area built = " + str(builtarea)
print "built fraction = " + str(builtfrac)

print "2.5km x 2.5km = 6.5km2 = 6 250 000m2"
 
"""