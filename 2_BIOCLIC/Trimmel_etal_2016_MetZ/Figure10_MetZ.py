__author__ = 'lnx'
from pylab import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import csv

filename = '/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/Figure10_data.csv'

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

start = datetime.datetime(2013,8,2,0,0)
stop = datetime.datetime(2013,8,9,1,0)
delta = datetime.timedelta(hours=1)
dates = mpl.dates.drange(start,stop,delta)

WTMea = [i[1] for i in data] #error: -1.9/+2.1
WTSim = [i[2] for i in data] #error: +/-0.2
airT = [i[3] for i in data]  #error: +/-0.2
#discharge = [i[4] for i in data]  #error: +/-0.2
WTMea_minmax = [i[5] for i in data]  #error: +/-0.2
WTSim_minmax = [i[6] for i in data]  #error: +/-0.2
airT_minmax = [i[7] for i in data]  #error: +/-0.2
WTMea = [float(i) for i in WTMea]
WTSim = [float(i) for i in WTSim]
airT = [float(i) for i in airT]

WTMea_minmax = [float(i) for i in WTMea_minmax]
WTSim_minmax = [float(i) for i in WTSim_minmax]
airT_minmax = [float(i) for i in airT_minmax]

print WTMea_minmax

# Find the slope and intercept of the best fit line
slope,intercept=np.polyfit(dates,WTMea,1)
slope2,intercept2=np.polyfit(dates,WTSim,1)

# Create a list of values in the best fit line
ablineWTMea = []
ablineWTSim = []
for i in dates:
  ablineWTMea.append(slope*i+intercept)

for i in dates:
  ablineWTSim.append(slope2*i+intercept2)

fig = plt.figure()
fig.set_figwidth(6.78)


axisrange = [735082,735088,15,40] #2 - 8 August 2013
plt.axis(axisrange)

lower_error = -1.9
upper_error = 2.1
asymmetric_error = [lower_error, upper_error]

plt.plot(dates,WTMea, linestyle='--', color = 'black', label='WT observed')
plt.errorbar(dates,WTMea_minmax, linestyle=' ', color = 'black', yerr=0.2)
plt.plot(dates,WTSim, linestyle='-.', color='black', label='WT predicted')
#plt.errorbar(dates,WTSim, linestyle=' ', color='black', label='WT predicted', yerr=asymmetric_error)
plt.errorbar(dates,WTSim_minmax, linestyle=' ', color='black', yerr=2)
plt.plot(dates, ablineWTSim, color ='grey', label='WT observed - slope')
plt.plot(dates, ablineWTMea, color ='black', label='WT predicted - slope')
plt.plot(dates,airT,  linestyle=':', color='black', label='air temp observed')
plt.errorbar(dates,airT_minmax, linestyle=' ', color='black', yerr=0.2)
#plt.scatter(dates,discharge, marker='x', color='grey', label='discharge')
plt.ylabel('degC', fontsize='small')
plt.legend(loc=1, ncol=3, fontsize='small')

date_format = mpl.dates.DateFormatter('%d %B %Y')
ax = gca()

days = DayLocator(range(2, 9), interval=1)
ax.xaxis.set_major_locator(days)
ax.xaxis.set_major_formatter(date_format)

plt.xticks(rotation='vertical', fontsize='small')
plt.subplots_adjust(bottom=.3)
#fig.autofmt_xdate()

plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure10.tiff', dpi=300)
plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure10.png')
plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure10.eps')

plt.show()