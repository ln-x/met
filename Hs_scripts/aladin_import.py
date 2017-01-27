import pandas as pd
import matplotlib.pyplot as plt
import csv


path = '/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden_new/Pinka/ganzeZeitreihe/'

WT = pd.read_csv(path+'Pinka_Hundsmuehlbach_Aladin_WT_daily_new.txt', sep=';', parse_dates=['YYYYMMSS HH:MM:SS'])
WT = WT.set_index('YYYYMMSS HH:MM:SS')
WT_monthly = WT.resample('M',how='mean')
WT_monthly_max = WT.resample('M',how='max')
#WT_August = WT['08']

print WT_monthly


#print WT_monthly['2012-07':'2100-01']

#f = open('/home/lnx/Monatsmittel_Hundsmuehlbach.csv', 'w')
#f.write(WT_monthly)
#f.close()

writer_orig = pd.ExcelWriter('/home/lnx/Monatsmittel_Hundsmuehlbach.xlsx', engine='xlsxwriter')
WT_monthly.to_excel(writer_orig, index=False, sheet_name='report')
writer_orig.save()

quit()




fig = plt.figure()

#plt.title('WT monthly')
plt.plot(WT_monthly['WTmax'], color='blue', lw=0.5)
#plt.plot(Rkm, Tmax, color='red', lw =0.5)

plt.ylabel('water temperature[degC]')
plt.xlabel('time [month]')

plt.show()
