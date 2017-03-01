# -*- coding: utf-8 -*-
"""
"""
# Initialize Qt resources from file resources.py
# import resources
import sys                                                          # for this main application needed!
import os.path
#import ogr
#from osgeo import gdal, osr
#from osgeo.gdalconst import *
import numpy as np
import glob

class Clip:
    """Main implementation for testing. Usage without QGIS."""
    def __init__(self, dsm_path, dem_path, ndsm_path):
        """Constructor.
        """
        self.dsm = dsm_path
        self.dem = dem_path
        self.ndsm = ndsm_path
        self.scale = None
        self.gdal_dsm = None
        self.dsm = None
        self.gdal_dgm = None
        self.dgm = None
        self.dgsm = None   # for difference of dsm and dgm

    def start_progress(self):
        self.gdal_dsm = gdal.Open(dsm)
        self.dsm = self.gdal_dsm.ReadAsArray().astype(np.float)
        self.gdal_dgm = gdal.Open(dem)
        self.dgm = self.gdal_dgm.ReadAsArray().astype(np.float)

        # load raster
        gdal.AllRegister()

        self.ndsm = self.dsm - self.dgm
        saveraster(self.gdal_dsm, (self.data_path + self.dsmlayernew), self.dgsm)


def saveraster(gdal_data, filename, raster):
    rows = gdal_data.RasterYSize
    cols = gdal_data.RasterXSize

    outDs = gdal.GetDriverByName("GTiff").Create(filename, cols, rows, int(1), GDT_Float32)
    outBand = outDs.GetRasterBand(1)

    # write the data
    outBand.WriteArray(raster, 0, 0)
    # flush data to disk, set the NoData value and calculate stats
    outBand.FlushCache()
    outBand.SetNoDataValue(-9999)

    # georeference the image and set the projection
    outDs.SetGeoTransform(gdal_data.GetGeoTransform())
    outDs.SetProjection(gdal_data.GetProjection())

#if __name__ == '__main__':
#    raster = Clip()
#    raster.start_progress()

# Path to dsm files
dsm_path = r"D:\\_URBANIA\\Geodata\\DOM\\2_raw\\singletiles\\raster"
# Path to dem files
dem_path = r"D:\\_URBANIA\\Geodata\\DGM\\2_raw\\" #TODO: presently in wrong resolution, and each file in own folder!
# Path where to put ndsm
ndsm_path = r"D:\\_URBANIA\Geodata\\DOM\\2_raw\\singletiles\\raster_ndsm"

filelist = glob.glob(dsm_path + "\\*.tif")
print filelist
filelist_dem = glob.glob(dem_path + "\\*.tif")

for i in range(len(filelist)):
    outRaster = ndsm_path + "\\" + os.path.split(filelist[i])[1][:-3] + "tif"
    print outRaster
    #raster = Clip(filelist[i], filelist_dem[file], ndsm_path)
    #raster.start_progress()


#for i in files:
#    raster = Clip()

#data_path = '/home/lnx/0_TEB/_Input/TESTdata/SOLWEIG_Wien35_4/'
#dgmlayer = '35_4_05m_DGM.tif'
#dsmlayer = '35_4_DOM.tif'
#dsmlayernew = '35_4_DSM_DGM_diff.tif'