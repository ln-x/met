# ---------------------------------------------------------------------------
# Batch_ConvertDEM.py
# Created on: 01-11-2005
# Created by: WCL 
# ---------------------------------------------------------------------------

# Import system modules
import win32com.client, os, sys, string

#Instantiate the geoporcessor
gp = win32com.client.Dispatch("esriGeoprocessing.GPDispatch.1")

# Allow output to overwrite...
gp.OverwriteOutput = 1

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Conversion Tools.tbx")

# set workspace...
workspace = sys.argv[1]
gp.workspace =  workspace

gp.AddMessage("Workspace = " + workspace)

# Gets a list of files in the workspace
filenames=os.listdir(gp.workspace)
filenames=[filename.lower()
for filename in filenames
if (filename[-4:].lower()==".dem" and filename[0]!="-")]
for filename in filenames:
    
    # Define OutRaster filename truncating .dem from filename and InDEM as filename
    InDEM = gp.workspace + "\\" + filename
    OutRaster = gp.workspace + "\\" + filename[:-4]
    gp.AddMessage("Successfully created InDEM " + InDEM + "and OutRaster  " + OutRaster)
    
    # For each file, process DEM to Raster...
    try:
        gp.DEMToRaster_conversion(InDEM,OutRaster,"FLOAT","1")
    except:
        gp.GetMessages()

gp.RefreshCatalog(gp.workspace)        