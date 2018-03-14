#from __future__ import print_function
import datetime as dt

import matplotlib.pyplot as plt

import csv

__author__ = 'lnx'

x = []
# gs,r1,r2,r3,r4,r5,r6,r7,r9,r10,r11 = [],[],[],[],[],[],[],[],[],[],[],[]
#r12,r14,r15,r16,r17,r18,a1,a2,a3,a4 = [],[],[],[],[],[],[],[],[],[]
#a5,a6,a7,a9,a10,a11,a12,a14,a15,a16,a17,a18 = [],[],[],[],[],[],[],[],[],[],[],[]



csv_reader = csv.reader(open('/home/lnx/Documents/_BioCLIC/_Messungen/inklMittlereTagesgaenge.csv'))

graphiken ={}

for line in csv_reader:
    #print line
    #print type(line), len(line)
    splitted = line[0].split(';')
    if any(c.isalpha() for c in splitted[0]):
        #print splitted
        name = splitted[0]
        listezeit = [dt.datetime.strptime(x,"%H:%M") for x in splitted[1:23]]
        graphiken[name] = {'time':listezeit}
        #print name , listezeit
    else:
        monat = int(float(splitted[0]))
        #print name, monat
        tagesdaten = [float(x) for x in splitted[1:23]]
        #print tagesdaten
        graphiken[name][monat] = tagesdaten
        #print'datenzeile'

    #print name, listezeit

print graphiken
print graphiken.keys()
print graphiken['DK WT14']
for key in  graphiken.keys():
    print graphiken[key]

fig = plt.figure()

ax = fig.add_subplot(221)
ax.plot(graphiken['GL WT17'][7], 'o-', color='orange', lw=0.5)
ax.plot(graphiken['GL WT17'][8], color='red', lw=0.5)
ax.plot(graphiken['GL WT17'][9], color='darkred', lw=0.5)
ax.plot(graphiken['GL WT17'][10], color='violet', lw=0.5)
#ax.plot(graphiken['MAYR WT9']['time'],graphiken['MAYR WT9'][11], color='darkblue', lw=0.5)
plt.setp(plt.gca(), xticklabels=[6,12,18], yticks=(5,10,15,20,25), xticks=(6,12,18))
plt.text(20,20, 'I', fontsize=20)
plt.axis([1,23,0,25])
plt.ylabel('water temperature')


#plt.ylim(0,25)

ax = fig.add_subplot(222)
ax.plot(graphiken['MAYR WT9'][7], 'o-', color='orange', lw=0.5)
ax.plot(graphiken['MAYR WT9'][8], color='red', lw=0.5)
ax.plot(graphiken['MAYR WT9'][9], color='darkred', lw=0.5)
ax.plot(graphiken['MAYR WT9'][10], color='violet', lw=0.5)
#ax.plot(graphiken['MAYR WT9']['time'],graphiken['MAYR WT9'][11], color='darkblue', lw=0.5)
plt.setp(plt.gca(), xticklabels=[6,12,18], yticks=(5,10,15,20,25), xticks=(6,12,18))
plt.text(20,20, 'II', fontsize=20)
plt.axis([1,23,0,25])

ax = fig.add_subplot(223)
ax.plot(graphiken['DK WT14'][7], 'o-', color='orange', lw=0.5)
ax.plot(graphiken['DK WT14'][8], color='red', lw=0.5)
ax.plot(graphiken['DK WT14'][9], color='darkred', lw=0.5)
ax.plot(graphiken['DK WT14'][10], color='violet', lw=0.5)
ax.plot(graphiken['DK WT14'][11], color='darkblue', lw=0.5)
plt.text(20,20, 'III', fontsize=20)
plt.axis([1,23,0,25])
plt.ylabel('water temperature')
plt.xlabel('hours')

ax = fig.add_subplot(224)
ax.plot(graphiken['DD WT15']['time'],graphiken['DD WT15'][7], 'o-', color='orange', lw=0.5)
ax.plot(graphiken['DD WT15']['time'],graphiken['DD WT15'][8], color='red', lw=0.5)
ax.plot(graphiken['DD WT15']['time'],graphiken['DD WT15'][9], color='darkred', lw=0.5)
ax.plot(graphiken['DD WT15']['time'],graphiken['DD WT15'][10], color='violet', lw=0.5)
ax.plot(graphiken['MAYR WT9']['time'],graphiken['MAYR WT9'][11], color='darkblue', lw=0.5)
plt.axis([0,25,0,25])
plt.setp(plt.gca(), xticklabels=[6,12,18], yticks=(5,10,15,20), xticks=(6,12,18))
plt.text(20,20, 'IV', fontsize=20)

# # add 'o-' in the brackets behind x,y, if you want dots for each value
# # fig.autofmt_xdate()

# plt.grid(True)
#
#plt.legend(('Jul 12', 'Aug 12', 'Sept 12', 'Oct 12', 'Nov 12'))
# plt.legend()
#
# fig.savefig('albedo.png')
plt.show()
