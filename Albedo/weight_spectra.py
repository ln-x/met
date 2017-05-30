# -*- coding: utf-8 -*-
import os, csv
import datetime as dt
#import matplotlib.pyplot as plt
import pandas as pd

directory = u"D:\\_URBANIA\\METDATA\\GerhardPeharz_Johanneum\\2_raw"
base_filename = "ASTMG173"
suffix = ".csv"
spectrum = os.path.join(directory, base_filename + suffix)
#csv_reader = csv.reader(open(spectrum))
#headers = csv_reader.next()  # liest erste zeile - nächster zugriff ab zeile 2
#print headers

meas1 = "2017_04_21_Reflexion_Betonproben.txt"
meas2_diff = "2017_05_26_Betonproben_R_DIFF.txt"
meas2_tis = "2017_05_26_Betonproben_R_TIS.txt" #TIS = total integrated sphere

Spec1 = pd.read_csv(spectrum, skiprows=1, sep='\s+', index_col='Wavelength') #, parse_dates="Datetime"


#GEHWEGE:
#MV1_02_2 Normalbeton, Besenstrich
#MV2_01_2 Normalbeton hell, Besenstrich

#NICHT BEFAHRBAHRE BETONFLAECHEN:
#MVI_01_1 Normalbeton, glatt abgezogen

#SICHTBETONMAUER
#MV1_02_1 Normalbeton Schalfläche
#MV2_01_1 Normalbeton hell Schalfläche
#MV2_02_1 Normalbeton hell Schalfläche

#STRASSEN IM NIEDERRANGIGEN NETZ
#MV3_01_2 Straßenbeton, Besenstrich
#MV4_01_2 Straßenbeton hell, Besenstrich

#STRASSEN IM HOCHRANGINGEN NETZ
#MV3_03_2 Straßenbeton, Waschbetonstruktur
#MV4_03_2 Straßenbeton, hell, Waschbetonstruktur

#NICHT BEFAHRBARE BETONFLÄCHEN
#MV3_02_1 Straßenbeton, glatt abgezogen