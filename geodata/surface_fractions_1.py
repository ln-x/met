from geodata.qgis.core import *
from geodata.qgis.gui import  *
#include <qgsvectorlayer.h>

#take reclassified file (preprocessed with R script)
#vector1 = iface.activeLayer()
FMZK_name = r"D:/_URBANIA/GEODATA/FMZK/SURFACE_FRACTIONS/Reclassified/15_3_FMZK.shp"
FMZK = QgsVectorLayer(FMZK_name,"F_KLASSE", "ogr")

#FMZK = QgsVectorLayer(FMZK_name, "LC_suews", "ogr")
if not FMZK.isValid():
    print "Layer FMZK failed to load!"


#layer = iface.addVectorLayer("/path/to/shapefile/file.shp", "layer name you like", "ogr")
layer = iface.addVectorLayer(r"D:/_URBANIA/GEODATA/FMZK/SURFACE_FRACTIONS/Reclassified/15_3_FMZK.shp", "F_KLASSE", "ogr")
if not layer:
  print "Layer failed to load!"

print FMZK.featureCount()

#take CutRealNutzPolygon  (preprocessed with R script)
CutREAL_name = r"D:/_URBANIA/GEODATA/FMZK/SURFACE_FRACTIONS/cutREAL/15_3_FMZK.shp"
CutREAL = QgsVectorLayer(CutREAL_name, "OBJECT_ID", "ogr")
if not CutREAL.isValid():
    print "Layer CutREAL failed to load!"


#union 
#"console usage": processing.runalg('qgis:union', input, input2, output)
#processing.runalg('qgis:union', FMZK, CutREAL, FMZKREAL)



#for feature in FMZK.getFeatures():
#   #variant1
#   #print feature.attribute("AREA")
#   #variant2
#   geometrie1 = feature.geometry()
#   gesamtflaeche1 += geometrie1.area()
#   print geometrie1.area()
#
#for feature in FMZK.getFeatures():
#   print feature.geometry()