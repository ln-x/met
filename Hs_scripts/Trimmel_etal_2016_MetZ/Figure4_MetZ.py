__author__ = 'lnx'
from pylab import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import csv

filename = '/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/Figure4_data.csv'

data = []
try:
    with open(filename) as f:
        for line in f:
            reader = csv.reader(f)
            #header = reader.next()
            data = [row for row in reader]

except csv.Error as e:
    print "Error"
    sys.exit(-1)

x = [float(i[0]) for i in data]
y = [float(i[1]) for i in data]

slope,intercept=np.polyfit(x,y,1)

# Create a list of values in the best fit line
abline = []
for i in x:
  abline.append(slope*i+intercept)

fig = plt.figure()
fig.set_size_inches(3.39,2.54)

axisrange = [0.2,1,0,-250]
plt.axis(axisrange)

plt.scatter(x,y, marker='o', color = 'black')
plt.plot(x,abline, linestyle='-', color='black')

plt.ylabel('evaporation heat flux [W m-2]', fontsize='small')
plt.xlabel('view to sky [%]',  fontsize='small')
plt.xticks(fontsize='small')
plt.yticks(fontsize='small')
#print intercept, slope
plt.text(0.3,-220,'$f(x)= -198.3x - 15.9$',  fontsize='small')
plt.text(0.3,-200, '$R^2=0.908$', fontsize='small' )

plt.tight_layout()


plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure4.tiff',
        dpi=300, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None)

plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure4.png')
plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure4.eps')

plt.show()