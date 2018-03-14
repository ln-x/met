__author__ = 'lnx'

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from pandas import DataFrame

path = "/home/lnx/PycharmProjects/HS/"
DFM = '61.000'

#year = [2013, 2030, 2050, 2085]
#veg = [' ', 'V0', 'V100']

files = ['298_P500_STQ_2013_MLF_p/outputfiles_orig/Temp_H2O.txt',
            '298_P500_V0_2013_MLF_p/outputfiles/Temp_H2O.txt',
            '298_P500_V100_2013_MLF_p/outputfiles/Temp_H2O.txt',
            'S190_P_STQ_2030_1a_MLF/outputfiles/Temp_H2O.txt',
            'S191_P_V0_2030_1a_MLF/outputfiles/Temp_H2O.txt',
            'S192_P_V100_2030_1a_MLF/outputfiles/Temp_H2O.txt',
            'S196_P_STQ_2030_5a_MLF/outputfiles/Temp_H2O.txt',
            'S197_P_V0_2030_5a_MLF/outputfiles/Temp_H2O.txt',
            'S198_P_V100_2030_5a_MLF/outputfiles/Temp_H2O.txt',
            'S203_P_V0_2030_20a_MLF/outputfiles/Temp_H2O.txt',
            'S204_P_V100_2030_20a_MLF/outputfiles/Temp_H2O.txt',
            'S214_P_STQ_2030_Max_MLF/outputfiles/Temp_H2O.txt',
            'S202_P_STQ_2030_20a_MLF/outputfiles/Temp_H2O.txt',
            'S215_P_V0_2030_Max_MLF/outputfiles/Temp_H2O.txt',
            'S216_P_V100_2030_Max_MLF/outputfiles/Temp_H2O.txt',
            'S220_P_STQ_2050_1a_MLF/outputfiles/Temp_H2O.txt',
            'S221_P_V0_2050_1a_MLF/outputfiles/Temp_H2O.txt',
            'S222_P_V100_2050_1a_MLF/outputfiles/Temp_H2O.txt',
            'S226_P_STQ_2050_5a_MLF/outputfiles/Temp_H2O.txt',
            'S227_P_V0_2050_5a_MLF/outputfiles/Temp_H2O.txt',
            'S228_P_V100_2050_5a_MLF/outputfiles/Temp_H2O.txt',
            'S232_P_STQ_2050_20a_MLF/outputfiles/Temp_H2O.txt',
            'S233_P_V0_2050_20a_MLF/outputfiles/Temp_H2O.txt',
            'S234_P_V100_2050_20a_MLF/outputfiles/Temp_H2O.txt',
            'S244_P_STQ_2050_Max_MLF/outputfiles/Temp_H2O.txt',
            'S245_P_V0_2050_Max_MLF/outputfiles/Temp_H2O.txt',
            'S246_P_V100_2050_Max_MLF/outputfiles/Temp_H2O.txt',
            'S250_P_STQ_2085_1a_MLF/outputfiles/Temp_H2O.txt',
            'S251_P_V0_2085_1a_MLF/outputfiles/Temp_H2O.txt',
            'S252_P_V100_2085_1a_MLF/outputfiles/Temp_H2O.txt',
            'S256_P_STQ_2085_5a_MLF/outputfiles/Temp_H2O.txt',
            'S257_P_V0_2085_5a_MLF/outputfiles/Temp_H2O.txt',
            'S258_P_V100_2085_5a_MLF/outputfiles/Temp_H2O.txt',
            'S262_P_STQ_2085_20a_MLF/outputfiles/Temp_H2O.txt',
            'S263_P_V0_2085_20a_MLF/outputfiles/Temp_H2O.txt',
            'S264_P_V100_2085_20a_MLF/outputfiles/Temp_H2O.txt',
            'S274_P_STQ_2085_Max_MLF/outputfiles/Temp_H2O.txt',
            'S275_P_V0_2085_Max_MLF/outputfiles/Temp_H2O.txt',
            'S276_P_V100_2085_Max_MLF/outputfiles/Temp_H2O.txt']

for f in files:
        if "V0" in f:
            veg = "V0"
        elif "V100" in f:
            veg = "V100"
        else:
            veg = "STQ"

        if "2013" in f:
            year = "2013"
        elif "2030" in f:
            year = "2030"
        elif "2050" in f:
            year = "2050"
        else:
            year = "2085"
        #print year, veg
        name = ['WT',year,veg]
        name = "_".join(name)
        print name
        name = pd.read_csv(path + f, skiprows=6, sep='\s+')#, index_col='Datetime', parse_dates='Datetime')

        name = name.ix[240:359].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column  1.July-3.Aug: 744+72=816h
        #name1 = name[DFM]
        name = np.array(name[DFM]) #select only reference station Unterwart DFM 61km ~ DFS 39
        #print max(name1)
        #print name2
        #break

        name = name.ravel()

        name_stresshours = 0
        for i in name:
            #print i
            if i >= 20:
                #print "into if condition"
                name_stresshours += 1
            else:
                pass


        print year,veg,DFM, ": Tmax: %g, stresshours: %d (of %d total hours)" % (max(name),  name_stresshours, len(name))
        #print name

        #break

#quit()

matrix = [0,1,2,3,4,5,6,7,8,9,10,11,12]
matrix[0] = [max(WT_2013_V0) , max(WT_2013_STQ), max(WT_2013_V100)]
matrix[1] = [max(WT_1a_2030_V0), max(WT_1a_2030_STQ), max(WT_1a_2030_V100)]
matrix[2] = [max(WT_5a_2030_V0), max(WT_5a_2030_STQ), max(WT_5a_2030_V100)]
matrix[3] = [max(WT_20a_2030_V0), max(WT_20a_2030_STQ), max(WT_20a_2030_V100)]
matrix[4] = [max(WT_max_2030_V0), max(WT_max_2030_STQ), max(WT_max_2030_V100)]
matrix[5] = [max(WT_1a_2050_V0), max(WT_1a_2050_STQ), max(WT_1a_2050_V100)]
matrix[6] = [max(WT_5a_2050_V0), max(WT_5a_2050_STQ), max(WT_5a_2050_V100)]
matrix[7] = [max(WT_20a_2050_V0), max(WT_20a_2050_STQ), max(WT_20a_2050_V100)]
matrix[8] = [max(WT_max_2050_V0), max(WT_max_2050_STQ), max(WT_max_2050_V100)]
matrix[9] = [max(WT_1a_2085_V0), max(WT_1a_2085_STQ), max(WT_1a_2085_V100)]
matrix[10] = [max(WT_5a_2085_V0), max(WT_5a_2085_STQ), max(WT_5a_2085_V100)]
matrix[11] = [max(WT_20a_2085_V0), max(WT_20a_2085_STQ), max(WT_20a_2085_V100)]
matrix[12] = [max(WT_max_2085_V0), max(WT_max_2085_STQ), max(WT_max_2085_V100)]

outpd = pd.DataFrame(matrix, index=['2013','2030_1a','2030_5a','2030_20a','2030_max',
                     '2050_1a','2050_5a','2050_20a','2050_max','2085_1a','2085_5a','2085_20a','2085_max'],
                    columns =['V0','STQ','V100'])

print outpd
outpd.to_csv('/home/lnx/max_DFM61.csv')

diff = outpd - max(WT_2013)

diff_sp = outpd
diff_sp['V0'] = outpd['V0']- max(WT_2013_V0)
diff_sp['STQ'] = outpd['STQ']- max(WT_2013)
diff_sp['V100'] = outpd['V100']- max(WT_2013_V100)

diff.to_csv('/home/lnx/diff_DFM61.csv')
diff_sp.to_csv('/home/lnx/diff_sp_DFM61.csv')

matrix = [0,1,2,3,4,5,6,7,8,9,10,11,12]
matrix[0] = [mean(WT_2013_V0) , mean(WT_2013_STQ), mean(WT_2013_V100)]
matrix[1] = [mean(WT_1a_2030_V0), mean(WT_1a_2030_STQ), mean(WT_1a_2030_V100)]
matrix[2] = [mean(WT_5a_2030_V0), mean(WT_5a_2030_STQ), mean(WT_5a_2030_V100)]
matrix[3] = [mean(WT_20a_2030_V0), mean(WT_20a_2030_STQ), mean(WT_20a_2030_V100)]
matrix[4] = [mean(WT_max_2030_V0), mean(WT_max_2030_STQ), mean(WT_max_2030_V100)]
matrix[5] = [mean(WT_1a_2050_V0), mean(WT_1a_2050_STQ), mean(WT_1a_2050_V100)]
matrix[6] = [mean(WT_5a_2050_V0), mean(WT_5a_2050_STQ), mean(WT_5a_2050_V100)]
matrix[7] = [mean(WT_20a_2050_V0), mean(WT_20a_2050_STQ), mean(WT_20a_2050_V100)]
matrix[8] = [mean(WT_max_2050_V0), mean(WT_max_2050_STQ), mean(WT_max_2050_V100)]
matrix[9] = [mean(WT_1a_2085_V0), mean(WT_1a_2085_STQ), mean(WT_1a_2085_V100)]
matrix[10] = [mean(WT_5a_2085_V0), mean(WT_5a_2085_STQ), mean(WT_5a_2085_V100)]
matrix[11] = [mean(WT_20a_2085_V0), mean(WT_20a_2085_STQ), mean(WT_20a_2085_V100)]
matrix[12] = [mean(WT_max_2085_V0), mean(WT_max_2085_STQ), mean(WT_max_2085_V100)]

outpd = pd.DataFrame(matrix, index=['2013','2030_1a','2030_5a','2030_20a','2030_max',
                     '2050_1a','2050_5a','2050_20a','2050_max','2085_1a','2085_5a','2085_20a','2085_max'],
                    columns =['V0','STQ','V100'])

print outpd
outpd.to_csv('/home/lnx/mean_DFM61.csv')

diff = outpd - mean(WT_2013)

diff_sp = outpd
diff_sp['V0'] = outpd['V0']- mean(WT_2013_V0)
diff_sp['STQ'] = outpd['STQ']- mean(WT_2013)
diff_sp['V100'] = outpd['V100']- mean(WT_2013_V100)

diff.to_csv('/home/lnx/mean_diff_DFM61.csv')
diff_sp.to_csv('/home/lnx/mean_diff_sp_DFM61.csv')

quit()

# # Solution 1, using up and csv: works :-)
# statmatrix = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
# statmatrix[0] = ["period","episode","V0_max", "STQ_max", "V100_max"]
# statmatrix[1] = ["2013", " ", 26.55 , 24.74, 22.37]
# #statmatrix[1] = ["2013", " ", max(WT_2013_V0), max(WT_2013), max(WT_2013_V100)]
# statmatrix[2] = ["2030", "1a", max(WT_1a_2030_V0), max(WT_1a_2030), max(WT_1a_2030_V100)]
# statmatrix[3] = ["2030", "5a", max(WT_5a_2030_V0), max(WT_5a_2030), max(WT_5a_2030_V100)]
# statmatrix[4] = ["2030", "20a", max(WT_20a_2030_V0), max(WT_20a_2030), max(WT_20a_2030_V100)]
# statmatrix[5] = ["2030", "max", max(WT_max_2030_V0), max(WT_max_2030), max(WT_max_2030_V100)]
# statmatrix[6] = ["2050", "1a", max(WT_1a_2050_V0), max(WT_1a_2050), max(WT_1a_2050_V100)]
# statmatrix[7] = ["2050", "5a", max(WT_5a_2050_V0), max(WT_5a_2050), max(WT_5a_2050_V100)]
# statmatrix[8] = ["2050", "20a", max(WT_20a_2050_V0), max(WT_20a_2050), max(WT_20a_2050_V100)]
# statmatrix[9] = ["2050", "max", max(WT_max_2050_V0), max(WT_max_2050), max(WT_max_2050_V100)]
# statmatrix[10] = ["2085", "1a", max(WT_1a_2085_V0), max(WT_1a_2085), max(WT_1a_2085_V100)]
# statmatrix[11] = ["2085", "5a", max(WT_5a_2085_V0), max(WT_5a_2085), max(WT_5a_2085_V100)]
# statmatrix[12] = ["2085", "20a", max(WT_20a_2085_V0), max(WT_20a_2085), max(WT_20a_2085_V100)]
# statmatrix[13] = ["2085", "max", max(WT_max_2085_V0), max(WT_max_2085), max(WT_max_2085_V100)]
#out = np.array(statmatrix)
#out = np.transpose(out)
#with open('/home/lnx/test_file.csv', 'w') as csvfile:
#    writer = csv.writer(csvfile)
#    [writer.writerow(r) for r in out]


##Solution 2 - using np and npsabetext - doenst work - strings!
#out1 = out.reshape(14,5)
#out = np.arange(45).reshape((9,5))
#np.savetxt('/home/lnx/Table3_Stats.txt', out) #TypeError: float argument required, not numpy.string_

##Solution 3 - using no and write() doenst work  - numbers!
#output = open('/home/lnx/Table3_Stats.txt','w')
#output.write("\n".join(str(i) for i in WT_2013))
#output.write(i for i in statmatrix) #TypeError: expected a character buffer object
#output.close()

##Solution 4 - pd and write() doenst work #"Expected a character buffer object, exit code 1"
#f = open('/home/lnx/2_Documents/_BioClic/_Simulationen/Figure3_stats.txt','w')
#f.write(stats)

##Solution 5 -pd to xlsx via ExcelWriter - should work, didnt try yet
#writer_orig = pd.ExcelWriter('/home/lnx/simple.xlsx', engine='xlsxwriter')
#outpd.to_excel(writer_orig, index=False, sheet_name='report')
#writer_orig.save()