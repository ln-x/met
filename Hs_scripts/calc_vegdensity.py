__author__ = 'lnx'
import pandas as pd
import numpy as np

Codes = pd.read_csv("/home/lnx/PycharmProjects/HS/S274_P_STQ_2085_Max_MLF/inputfiles/LC_codes.csv", index_col=['Code'], sep=',')
Data = pd.read_csv("/home/lnx/PycharmProjects/HS/S274_P_STQ_2085_Max_MLF/inputfiles/LC_data.csv", index_col=['Stream_KM'], sep=',')
VegCodes = pd.DataFrame()
VegCodes = Data.iloc[:,5:69] #other methods: del Data['Longitude', ..] OR #Data.drop(Data.columns[[0,1,...]],inplace=True, axis=1)

#Replace each LC_Code (columns Veg1_NE bis Veg9_NW) in Data with "Density (0-1)" from Codes
#print Codes.head()
#print VegCodes.values[0,1]
line = Codes.loc[[101]]  #also works: line2 = Codes.iloc[[101]]
index = int(VegCodes.values[0,1] - 99)
vegdens1 = Codes.iloc[index,2] #also works: vegdens1 = Codes.iloc[88,2]
#print line.head()

VegDens = pd.DataFrame()
for i in VegCodes.values[0]:
    print i
    lc_code = int(i)
    index = int(VegCodes.values[0, lc_code] - 99)
    #print index
    #VegDens.values[0,i] = Codes.values[index,2]

print VegDens
    #VegDens.values[0,i] = Codes.values[int(Data.values[0,i]),2]

#for i in Stream_KM:
#
#    Data.Veg1_NE[0]
