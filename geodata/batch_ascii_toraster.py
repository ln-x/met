# Import system modules  
import arcgisscripting, os  

# Create the Geoprocessor object  
gp = arcgisscripting.create()  
import arcpy  
import os  
import glob  

# Path to ascii files  
filepath = r"D:\\_URBANIA\\Geodata\\DOM\\singletiles\\asc"  
# Path where to put rasters  
outFolder = r"D:\\_URBANIA\Geodata\\DOM\\singletiles\\raster"  

ascList = glob.glob(filepath + "\\*.asc")  
print ascList  

for ascFile in ascList:  
    outRaster = outFolder + "\\" + os.path.split(ascFile)[1][:-3] + "tif"  
    print outRaster  
    arcpy.ASCIIToRaster_conversion(ascFile, outRaster, "FLOAT") 
