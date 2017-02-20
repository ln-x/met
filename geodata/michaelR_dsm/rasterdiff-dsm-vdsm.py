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
        self.data_path = '/home/lnx/0_TEB/_Input/TESTdata/SOLWEIG_Wien35_4/'
        self.dsmlayer = '35_4_DOM.tif'
        self.vdsmlayer ='vegdsm.tif'
        self.dsmlayernew = 'dsm_woveg.tif'
        #self.vdsmlayer = 'BOKU-vegdsm.tif'
        #self.dsmlayernew = 'BOKU-dsm-woveg.tif'

        self.scale = None
        self.gdal_dsm = None
        self.dsm = None
        self.gdal_vdsm = None
        self.vdsm = None
        self.dsmnew = None   # for difference of dsm and dgm


    def start_progress(self):
        filepath_dsm = self.data_path + self.dsmlayer
        filepath_vdsm = self.data_path + self.vdsmlayer
        self.gdal_dsm = gdal.Open(filepath_dsm)
        self.dsm = self.gdal_dsm.ReadAsArray().astype(np.float)
        self.gdal_vdsm = gdal.Open(filepath_vdsm)
        self.vdsm = self.gdal_vdsm.ReadAsArray().astype(np.float)

        # load raster
        gdal.AllRegister()

        self.dsmnew = self.dsm - self.vdsm
        saveraster(self.gdal_dsm, (self.data_path + self.dsmlayernew), self.dsmnew)


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