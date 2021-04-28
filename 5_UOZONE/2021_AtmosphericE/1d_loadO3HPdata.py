# -*- coding: utf-8 -*-
__author__ = 'lnx'
import pandas as pd
import xlrd
import matplotlib.dates
import matplotlib.pyplot as plt
import sys
from datetime import datetime, timedelta

file = "/home/lnx/Downloads/OHP_2012_2014_isoprene.xlsx"

hp = pd.read_excel(file, sheet_name="2012_FLux_10m", header="2",usecols="B",skiprows=1,parse_dates="A")
#io, sheet_name=0, header=0, names=None, index_col=None, usecols=None, squeeze=False, dtype=None, engine=None,
# converters=None, true_values=None, false_values=None, skiprows=None, nrows=None, na_values=None, keep_default_na=True,
# na_filter=True, verbose=False, parse_dates=False, date_parser=None, thousands=None, comment=None, skipfooter=0,
# convert_float=True, mangle_dupe_cols=True, storage_options=None
print(hp)
exit()

