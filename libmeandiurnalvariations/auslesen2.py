#from __future__ import print_function
import csv
import datetime as dt
import matplotlib.pyplot as plt

__author__ = 'lnx'

x = []

csv_reader = csv.reader(open('csv/inklMittlereTagesgaenge_Lafnitz20130401.csv'))

graphiken = {}  # Erstellen eines dictonaries

for line in csv_reader:
    #print line
    #print type(line), len(line)
    splitted = line[0].split(';')
    if any(c.isalpha() for c in splitted[0]):
        #print splitted
        name = splitted[0]
        listezeit = [dt.datetime.strptime(x, "%H:%M") for x in splitted[1:23]]
        graphiken[name] = {'time': listezeit}
        #print name , listezeit
    else:
        monat = int(float(splitted[0]))
        #print name, monat
        tagesdaten = [float(x) for x in splitted[1:23]]
        #print tagesdaten
        graphiken[name][monat] = tagesdaten
        #print'datenzeile'

        #print name, listezeit

#print graphiken
#print graphiken.keys()
#print graphiken['DK WT14']
#for key in  graphiken.keys():
#    print graphiken[key]

fig = plt.figure()

ax = fig.add_subplot(221)
ax.plot(graphiken['RO'][8], color='red', lw=0.5)
ax.plot(graphiken['RO'][9], color='darkred', lw=0.5)
ax.plot(graphiken['RO'][10], color='violet', lw=0.5)
ax.plot(graphiken['RO'][11], color='darkblue', lw=0.5)
#ax.plot(graphiken['RO'][12], color='blue', lw=0.5)
plt.axis([1, 23, 5, 20])
plt.setp(plt.gca(), xticklabels=[6, 12, 18], yticks=(10, 15, 20), xticks=(6, 12, 18))
plt.text(20, 18, 'I', fontsize=20)
plt.ylabel('water temperature')


#plt.ylim(0,25)

ax = fig.add_subplot(222)
ax.plot(graphiken['NS WT12'][7], color='orange', lw=0.5)
ax.plot(graphiken['NS WT12'][8], color='red', lw=0.5)
ax.plot(graphiken['NS WT12'][9], color='darkred', lw=0.5)
ax.plot(graphiken['NS WT12'][10], color='violet', lw=0.5)
#ax.plot(graphiken['NS WT12'][11], color='darkblue', lw=0.5)
plt.text(20, 18, 'II', fontsize=20)
plt.setp(plt.gca(), xticklabels=[6, 12, 18], yticks=(10, 15, 20), xticks=(6, 12, 18))
plt.axis([1, 23, 5, 20])

ax = fig.add_subplot(223)
ax.plot(graphiken['ND WT13'][7], color='orange', lw=0.5)
ax.plot(graphiken['ND WT13'][8], color='red', lw=0.5)
ax.plot(graphiken['ND WT13'][9], color='darkred', lw=0.5)
ax.plot(graphiken['ND WT13'][10], color='violet', lw=0.5)
ax.plot(graphiken['ND WT13'][11], color='darkblue', lw=0.5)
plt.axis([1, 23, 5, 20])
plt.setp(plt.gca(), xticklabels=[6, 12, 18], yticks=(10, 15, 20), xticks=(6, 12, 18))
plt.text(20, 18, 'III', fontsize=20)
plt.ylabel('water temperature')
plt.xlabel('hours')

ax = fig.add_subplot(224)
ax.plot(graphiken['DK WT14'][7], color='orange', lw=0.5)
ax.plot(graphiken['DK WT14'][8], color='red', lw=0.5)
ax.plot(graphiken['DK WT14'][9], color='darkred', lw=0.5)
ax.plot(graphiken['DK WT14'][10], color='violet', lw=0.5)
ax.plot(graphiken['DK WT14'][11], color='darkblue', lw=0.5)
plt.axis([1, 23, 5, 20])
plt.setp(plt.gca(), xticklabels=[6, 12, 18], yticks=(10, 15, 20), xticks=(6, 12, 18))
plt.text(20, 18, 'IV', fontsize=20)
plt.xlabel('hours')


# # add 'o-' in the brackets behind x,y, if you want dots for each value
# # fig.autofmt_xdate()
# plt.grid(True)
#
#plt.legend(('Jul 12', 'Aug 12', 'Sept 12', 'Oct 12', 'Nov 12'))
# plt.legend()
#
# fig.savefig('albedo.png')
plt.show()
