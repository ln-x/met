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
        self.difflayer = '35_4_DSM_DGM_diff.tif'
        self.masklayer = '35_4_bkm_buffer_05m_mask_5001.tif'
        self.vegdsmlayer = 'vegdsm.tif'

        self.scale = None
        self.gdal_diff = None
        self.diff = None
        self.gdal_mask = None
        self.mask = None
        self.vdsm = None   # for vegetation dsm


    def start_progress(self):
        filepath_diff = self.data_path + self.difflayer
        filepath_mask = self.data_path + self.masklayer
        self.gdal_diff = gdal.Open(filepath_diff)
        self.diff = self.gdal_diff.ReadAsArray().astype(np.float)
        self.gdal_mask = gdal.Open(filepath_mask)
        self.mask = self.gdal_mask.ReadAsArray().astype(np.float)

        # load raster
        gdal.AllRegister()

        self.vdsm = self.diff * abs(1-self.mask)
        saveraster(self.gdal_diff, (self.data_path + self.vegdsmlayer), self.vdsm)


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