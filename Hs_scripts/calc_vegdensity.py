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
#line = Codes.loc[[101]]  #also works: line2 = Codes.iloc[[101]]
index = int(VegCodes.values[0,1] - 99)
vegdens1 = Codes.iloc[index,2] #also works: vegdens1 = Codes.iloc[88,2]
#print line.head()

#AVERAGE VEGETATION PARAMETER AT SPECIFIC KM
def AverageVegParamAtKM(i):
    VegDen = 0
    VegHei = 0
    Counter = 0
    for i in VegCodes.values[i]:
        lc_code = int(i)
        if i > 0:
            index = lc_code -99
            VegDen += Codes.iloc[index,2]
            VegHei += Codes.iloc[index,1]
            Counter +=1
        else: pass
    return (VegDen/Counter), (VegHei/Counter)

#print AverageVegParamAtKM(18)

VegDenT = 0
VegDenTArray = []
VegHeiT = 0
Counter = 0
for j in range(102):
    if (AverageVegParamAtKM(j)[1] > 0):   #vegetation height treshold
        #print AverageVegParamAtKM(j)[1]
        VegDenT += AverageVegParamAtKM(j)[0]
        VegHeiT += AverageVegParamAtKM(j)[1]
        Counter += 1
        VegDenTArray.append(AverageVegParamAtKM(j)[0])
    else: pass

print (VegDenT/Counter), (VegHeiT/Counter), np.std(VegDenTArray,ddof=1), np.max(VegDenTArray), np.min(VegDenTArray)

