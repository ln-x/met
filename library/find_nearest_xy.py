# -*- coding: utf-8 -*-
__author__ = 'lnx'
import numpy as np

def find_nearest_xy(array1, value1, array2, value2, array3):
   array1 = np.asarray(array1)
   array2 = np.asarray(array2)
   idx = (np.abs(array1 - value1)+np.abs(array2 - value2)).argmin()
   return array3[idx] #, array1[idx], array2[idx], idx