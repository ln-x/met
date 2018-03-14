__author__ = 'lnx'
from pylab import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import csv

filename = '/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/Figure9_data.csv'

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

#dates = [i[0] for i in data]
#dates = datetime.datetime.strftime(%H:%M)
start = datetime.datetime(2013,07,28,0,0) #0h
stop = datetime.datetime(2013,07,28,18,8) #18:08h
delta = datetime.timedelta(minutes=1)
dates = mpl.dates.drange(start,stop,delta)

swatmM = [i[1] for i in data]
swreflM = [i[2] for i in data]
lwatmM = [i[3] for i in data]
lwstrM = [i[4] for i in data]
lwatmS = [i[5] for i in data]
lwstrS = [i[6] for i in data]
swatmS = [i[7] for i in data]

fig = plt.figure()
fig.set_figwidth(6.78)

axisrange = [735077,735078,-600,1100]
plt.axis(axisrange)
#print plt.axis()

plt.plot(dates,swatmM, linestyle='-', color = 'black', label='Sw_atm M')
plt.plot(dates,swreflM, linestyle=':', color='black', label='Sw_refl M')
plt.plot(dates,lwatmM,  linestyle='--', color='black', label='Lw_atm M')
plt.plot(dates,lwstrM,  linestyle='-.', color='black', label='Lw_stream M')
plt.scatter(dates,swatmS, marker='+', color='grey', label='Sw_atm S')
plt.scatter(dates,lwatmS, marker='x', color='grey', label='Lw_atm S')
plt.scatter(dates,lwstrS, marker='*', color='grey', label='Lw_stream S')
plt.ylabel('W m-2', fontsize='small')
plt.legend(loc=1, fontsize='small')
#plt.legend(loc=1, fontsize='12')


date_format = mpl.dates.DateFormatter('%H%M MEZ')
ax = gca()

threehours = HourLocator(range(1, 24), interval=3)

ax.xaxis.set_major_locator(threehours)
ax.xaxis.set_major_formatter(date_format)
#fig.autofmt_xdate()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

#ax.spines['bottom'].set_position(('data',0))
#ax.spines['left'].set_position(('data',0))

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')



plt.xticks(rotation='vertical', fontsize='small')
#plt.yticks(fontsize='small')



plt.subplots_adjust(bottom=.2)


plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure9.tiff', dpi=300)
plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure9.png')
plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure9.eps')

plt.show()