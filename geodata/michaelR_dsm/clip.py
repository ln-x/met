# -*- coding: utf-8 -*-
"""
"""
# Initialize Qt resources from file resources.py
# import resources
import sys                                                          # for this main application needed!
import os.path
from osgeo import gdal, osr
from osgeo.gdalconst import *
import numpy as np



class Clip:
    """Main implementation for testing. Usage without QGIS."""

    def __init__(self):
        """Constructor.

        """
        # initialize plugin directory
        #self.plugin_dir = os.path.dirname(__file__)             # not needed for testing

        #self.data_path = 'D:/Michael/Documents/Studium/Doktorat/UMEP/umep-3d/SEBE/SEBEdata/'
        self.data_path = 'C:/Users/ReveszM/Doktorat/02_Simulationen/03_UMEP_Stadtklimasimulation/BOKU-Schwackhoefer_albedo/'
        self.dgmlayer = 'BOKU_dgm.tif'
        self.dsmlayer = 'BOKU_dom.tif'
        #self.dsmlayernew = '34-2_35-1_clipped_dom-clip2.tif'
        self.dsmlayernew = 'BOKU-dom-dgm-diff.tif'
        #-340282346638528859811704183484516925440
        #34-2_35-1_clipped_dgm-clip2.tif
        #dom-subtract-dgm-clip.tif

        self.scale = None
        self.gdal_dsm = None
        self.dsm = None
        self.gdal_dgm = None
        self.dgm = None
        #self.gdal_dgsm = None   # for difference of dsm and dgm
        self.dgsm = None   # for difference of dsm and dgm


    def start_progress(self):
        filepath_dsm = self.data_path + self.dsmlayer
        filepath_dgm = self.data_path + self.dgmlayer
        self.gdal_dsm = gdal.Open(filepath_dsm)
        self.dsm = self.gdal_dsm.ReadAsArray().astype(np.float)
        self.gdal_dgm = gdal.Open(filepath_dgm)
        self.dgm = self.gdal_dgm.ReadAsArray().astype(np.float)
        #sizex = self.dsm.shape[0]
        #sizey = self.dsm.shape[1]

        #print sizex, sizey
        #np.savetxt((self.data_path + self.dsmlayernew + '.txt'), self.dsm, fmt='%d')

        # Get latlon from grid coordinate system
        # old_cs = osr.SpatialReference()
        ## dsm_ref = dsmlayer.crs().toWkt()
        ## old_cs.ImportFromWkt(dsm_ref)
        # old_cs.ImportFromWkt(self.gdal_dsm.GetProjectionRef())
        #
        # wgs84_wkt = """
        # GEOGCS["WGS 84",
        #     DATUM["WGS_1984",
        #         SPHEROID["WGS 84",6378137,298.257223563,
        #             AUTHORITY["EPSG","7030"]],
        #         AUTHORITY["EPSG","6326"]],
        #     PRIMEM["Greenwich",0,
        #         AUTHORITY["EPSG","8901"]],
        #     UNIT["degree",0.01745329251994328,
        #         AUTHORITY["EPSG","9122"]],
        #     AUTHORITY["EPSG","4326"]]"""
        #
        # new_cs = osr.SpatialReference()
        # new_cs.ImportFromWkt(wgs84_wkt)
        #
        # transform = osr.CoordinateTransformation(old_cs, new_cs)
        # width = self.gdal_dsm.RasterXSize
        # height = self.gdal_dsm.RasterYSize
        # geotransform = self.gdal_dsm.GetGeoTransform()
        # minx = geotransform[0]
        # miny = geotransform[3] + width*geotransform[4] + height*geotransform[5]
        # lonlat = transform.TransformPoint(minx, miny)
        # lon = lonlat[0]
        # lat = lonlat[1]
        # self.scale = 1 / geotransform[1]

        # load raster
        gdal.AllRegister()

        self.dgsm = self.dsm - self.dgm
        saveraster(self.gdal_dsm, (self.data_path + self.dsmlayernew), self.dgsm)


def saveraster(gdal_data, filename, raster):
    rows = gdal_data.RasterYSize
    cols = gdal_data.RasterXSize

    # outDs = gdal.GetDriverByName("GTiff").Create(folder + 'shadow' + tv + '.tif', cols, rows, int(1), GDT_Float32)
    outDs = gdal.GetDriverByName("GTiff").Create(filename, cols, rows, int(1), GDT_Float32)
    # outDs = gdal.GetDriverByName(gdal_data.GetDriver().LongName).Create(filename, cols, rows, int(1), GDT_Float32)
    outBand = outDs.GetRasterBand(1)

    # write the data
    outBand.WriteArray(raster, 0, 0)
    # flush data to disk, set the NoData value and calculate stats
    outBand.FlushCache()
    outBand.SetNoDataValue(-9999)

    # georeference the image and set the projection
    outDs.SetGeoTransform(gdal_data.GetGeoTransform())
    outDs.SetProjection(gdal_data.GetProjection())


# ### template to create a Qt Main Window:
# qtCreatorFile = ""  # Enter file here.
#
# Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
#
#
# class MyApp(QtGui.QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         QtGui.QMainWindow.__init__(self)
#         Ui_MainWindow.__init__(self)
#         self.setupUi(self)
#
#
# if __name__ == "__main__":
#     app = QtGui.QApplication(sys.argv)
#     window = MyApp()
#     window.show()
#     sys.exit(app.exec_())


if __name__ == '__main__':
    raster = Clip()
    raster.start_progress()