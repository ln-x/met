# coding=utf-8
import csv
import datetime as dt
import matplotlib.pyplot as plt

def safenumber(value):
    try:
        num = float(value)
    except ValueError:
        num = 0.0
    return num


#Definition von Listen für die einzelnen Datenspalten
#x: Zeit, gs: Globalstrahlung auf Feld 13, 8: frei
x_s, x_c, gs_s, gs_c = ([] for i in range(4))

#Referenzflaechen: 2: Blech, 7: Folie (schwarz), 10: Kies
r2, a2_s, a2_c, r7, a7_s, a7_c, r10, a10_s, a10_c = ([] for i in range(9))

r1, r3, r4, r5, r6, r9, r11 = ([] for i in range(7))
r12, r14, r15, r16, r17, r18, a1_s, a1_c, a3_s, a3_c, a4_s, a4_c = ([] for i in range(12))
a5, a6, a9, a11_s, a11_c, a12, a14, a15, a16, a17, a18 = ([] for i in range(11))

#1: 7cm Pflanzsubstrat Bauder ext. + 5cm EPS Drain
#3: 10cm Pflanzsubstrat RE leicht + 2cm Drain Speicher
#4: 10cm Pauliberg +10cm Agroperl
#5: 15cm Pauliberg + 15cm Agroperl
#6: ZinCo
#9: 7cm Claylith organ. + 5cm Claylith Drain
#11: 7cm Pflanzsubstrat RE leicht + 5cm LiaDrain
#12: 12cm Pauliberg	SlrkW_Avg
#14: 7cm Rath
#15: 7cm Claylith organ. + 5cm Claylith Drain
#16: 7cm Claylith organ. + 5cm Claylith Drain
#17: 7cm Recycling Ziegel + 5cm Recycling Ziegel
#18: 15cm Recycling Ziegel + 5cm Recycling Ziegel

#Einschränken des Zeitraumes
startdate = dt.date(2012, 3, 1)
enddate = dt.date(2012, 9, 30)
starttime = dt.time(8, 40, 0)
endtime = dt.time(15, 5, 0)
#print startdate, enddate, starttime, endtime

#Einlesen der csv-Dateien in das Objekt "csv_reader"
#csv_reader = csv.reader(open('JHS_Albedo_20111005_20130102.csv'))
#headers = csv_reader.next()  # liest erste Zeile in Liste namens "header" - nächster Zugriff ab Zeile 2
#print headers

csv_dict = csv.DictReader(open('JHS_Albedo_20111005_20130102.csv'))
print csv_dict.fieldnames

#Iterieren über "csv_reader"
for line in csv_dict:  # ab Zeile zwei wegen .next() call oben!
    #csv_dict.next()
    actualtimestamp = dt.datetime.strptime(line['datetime'], "%d.%m.%Y %H:%M")

    if startdate <= actualtimestamp.date() <= enddate \
            and starttime <= actualtimestamp.time() <= endtime:

        #Definiere Grenze für "sonnige Tage" zB 0.5 = 500W direkte Sonneneinstrahlung
        if float(line['gs']) > 0.5:
            x_s.append(dt.datetime.strptime(line['datetime'], "%d.%m.%Y %H:%M")) #1.Element aus Zeile an Liste "x" anhängen
            gs_s.append(safenumber(line['gs'])) #2.Element aus Zeile an Liste "gs" anhängen
            #r3_s.append(float(line[5]))
            a11_s.append(safenumber(line['a11'])) #extensiv
            a4_s.append(safenumber(line['a4'])) #intensiv
            a2_s.append(safenumber(line['a2'])) #Blech
            a7_s.append(safenumber(line['a7'])) #Teerpappe
            a10_s.append(safenumber(line['a10'])) #Kies

        #Definiere Grenze für "bewölkte Tage" zB 0.3 = 300W direkte Sonneneinstrahlung
        elif float(line['gs']) < 0.1:
            x_c.append(dt.datetime.strptime(line['datetime'], "%d.%m.%Y %H:%M")) #1.Element aus Zeile an Liste "x" anhängen
            gs_c.append(safenumber(line['gs'])) #2.Element aus Zeile an Liste "gs" anhängen
            #r3_c.append(float(line[5]))
            a11_c.append(safenumber(line['a11'])) #extensiv
            a4_c.append(safenumber(line['a4'])) #intensiv
            a2_c.append(safenumber(line['a2'])) #Blech
            a7_c.append(safenumber(line['a7'])) #Teerpappe
            a10_c.append(safenumber(line['a10'])) #Kies
            '''
			r2.append(float(line[3]))
			r3.append(float(line[4]))
			r4.append(float(line[5]))
			r5.append(float(line[6]))
			r6.append(float(line[7]))
			r7.append(float(line[8]))
			r9.append(float(line[9]))
			r10.append(float(line[10]))
			r11.append(float(line[11]))
			r12.append(float(line[12]))
			r14.append(float(line[13]))
			r15.append(float(line[14]))
			r16.append(float(line[15]))
			r17.append(float(line[16]))
			r18.append(float(line[17]))
			a1.append(float(line[18]))
			a2.append(float(line[19]))
			a3.append(float(line[20]))
			a4.append(float(line[21]))
			a5.append(float(line[22]))
			a6.append(float(line[23]))
			a7.append(float(line[24]))
			a9.append(float(line[25]))
			a10.append(float(line[26]))
			a11.append(float(line[27]))
			a12.append(float(line[28]))
			a14.append(float(line[29]))
			a15.append(float(line[30]))
			a16.append(float(line[31]))
			a17.append(float(line[32]))
			a18.append(float(line[33]))
'''

#TESTBEREICH ANFANG
#xx = dt.timedelta(hours = 1 ) + dt.timedelta(minutes = 10)
#print xx
#mean_a4_c = sum(a4_c)/len(a4_c)
#print mean_a4_c
#exit()
#TESTBEREICH ENDE

fig = plt.figure()
ax = fig.add_subplot(121)
#ax.plot(x_s, gs_s, color='orange', marker='.', lw=0.0, label='gs')
#ax.plot(x,r3,color='red',lw=0.5, label='r3')
ax.plot(x_s, a11_s, color='orange', marker='.', lw=0.0, label='ext')
ax.plot(x_s, a4_s, color='green', marker='.', lw=0.0, label='int.')
ax.plot(x_s, a2_s, color='blue', marker='.', lw=0.0, label='foil')
ax.plot(x_s, a7_s, color='black', marker='.', lw=0.0, label='tar')
ax.plot(x_s, a10_s, color='lightblue', marker='.', lw=0.0, label='cobble')
plt.ylim(0, 0.4)
plt.xlabel('time')
plt.ylabel('albedo[%]')
plt.grid(True)

ax = fig.add_subplot(122)
#ax.plot(x_c, gs_c, color='orange', marker='.', lw=0.0, label='gs')
#ax.plot(x,r3,color='red',lw=0.5, label='r3')
ax.plot(x_c, a11_c, color='orange', marker='.', lw=0.0, label='ext')
ax.plot(x_c, a4_c, color='green', marker='.', lw=0.0, label='int')
ax.plot(x_c, a2_c, color='blue', marker='.', lw=0.0, label='foil')
ax.plot(x_c, a7_c, color='black', marker='.', lw=0.0, label='tar')
ax.plot(x_c, a10_c, color='lightblue', marker='.', lw=0.0, label='cobble')
plt.ylim(0, 0.4)
plt.xlabel('time')
plt.ylabel('albedo[%]')
plt.grid(True)

# add 'o-' in the brackets behind x,y, if you want dots for each value
fig.autofmt_xdate()

#plt.legend(('label1', 'label2'))
plt.legend()

#fig.savefig('albedo.png')
plt.show()