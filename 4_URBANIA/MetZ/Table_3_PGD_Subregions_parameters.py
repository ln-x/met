# -*- coding: utf-8 -*-
import csv
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from pylab import *
from scipy import stats

outpath ='/media/lnx/Norskehavet/OFFLINE/plots'
file_PGD = '/media/lnx/Norskehavet/OFFLINE/2069PVR/PGD.nc'
f_PGD = Dataset(file_PGD, mode='r')

def PrintPGDparameter(subregion,a1,a2,b1,b2):
    D_BLD = f_PGD.variables['D_BLD'][a1:a2,b1:b2]
    D_BLD_HEIGHT = f_PGD.variables['D_BLD_HEIG'][a1:a2,b1:b2]
    D_GARDEN = f_PGD.variables['D_GARDEN'][a1:a2,b1:b2]
    FRAC_TOWN = f_PGD.variables['FRAC_TOWN'][a1:a2,b1:b2]
    WALL_O_HOR = f_PGD.variables['D_WALL_O_H'][a1:a2,b1:b2]

    print subregion, ":" , FRAC_TOWN.mean(), D_BLD.mean(), D_GARDEN.mean(), D_BLD_HEIGHT.mean(),  WALL_O_HOR.mean()
    #print subregion, ":" , D_BLD, D_GARDEN, D_BLD_HEIGHT


PrintPGDparameter("CE",51,60,81,90) #50,59,80,89
PrintPGDparameter("NO",73,82,89,98)
PrintPGDparameter("RU",57,66,128,137)
PrintPGDparameter("SA",58,67,109,118)
PrintPGDparameter("SE",37,46,99,108)
PrintPGDparameter("SX",24,33,75,84)
PrintPGDparameter("SI",31,40,68,77)
PrintPGDparameter("VW",47,56,64,73)
PrintPGDparameter("WE",62,71,73,82)

exit()