from hs_scripts import hs_loader

__author__ = 'lnx'
import matplotlib.pyplot as plt

filename = "/home/lnx/PycharmProjects/Messdatenauswertung/HStest/v808_20130411_c00_v01_f03/Heat_Cond.txt"
thedata = hs_loader.loadfile(filename=filename)
print 'loaded: ', thedata

date_time = [i[0] for i in thedata]
x1 = [i[1] for i in thedata]
x2 = [i[2] for i in thedata]
x3 = [i[3] for i in thedata]
x4 = [i[4] for i in thedata]

fig = plt.figure()

ax = fig.add_subplot(221)
ax.plot(date_time, x1, color='red', lw=0.5)
ax.plot(date_time, x2, color='darkred', lw=0.5)
ax.plot(date_time, x3, color='violet', lw=0.5)
ax.plot(date_time, x4, color='darkblue', lw=0.5)
#ax.plot(graphiken['RO'][12], color='blue', lw=0.5)
#plt.axis([0, 15, -15, 15])
#plt.setp(plt.gca(), xticklabels=[6, 12, 18], yticks=(10, 15, 20), xticks=(6, 12, 18))
#plt.text(20, 18, 'I', fontsize=20)
#plt.ylabel('water temperature')
#plt.ylim(-15,15)

# ax = fig.add_subplot(222)
# ax.plot(graphiken['NS WT12'][7], color='orange', lw=0.5)
# ax.plot(graphiken['NS WT12'][8], color='red', lw=0.5)
# ax.plot(graphiken['NS WT12'][9], color='darkred', lw=0.5)
# ax.plot(graphiken['NS WT12'][10], color='violet', lw=0.5)
# #ax.plot(graphiken['NS WT12'][11], color='darkblue', lw=0.5)
# plt.text(20, 18, 'II', fontsize=20)
# plt.setp(plt.gca(), xticklabels=[6, 12, 18], yticks=(10, 15, 20), xticks=(6, 12, 18))
# plt.axis([1, 23, 5, 20])
#
# ax = fig.add_subplot(223)
# ax.plot(graphiken['ND WT13'][7], color='orange', lw=0.5)
# ax.plot(graphiken['ND WT13'][8], color='red', lw=0.5)
# ax.plot(graphiken['ND WT13'][9], color='darkred', lw=0.5)
# ax.plot(graphiken['ND WT13'][10], color='violet', lw=0.5)
# ax.plot(graphiken['ND WT13'][11], color='darkblue', lw=0.5)
# plt.axis([1, 23, 5, 20])
# plt.setp(plt.gca(), xticklabels=[6, 12, 18], yticks=(10, 15, 20), xticks=(6, 12, 18))
# plt.text(20, 18, 'III', fontsize=20)
# plt.ylabel('water temperature')
# plt.xlabel('hours')
#
# ax = fig.add_subplot(224)
# ax.plot(graphiken['DK WT14'][7], color='orange', lw=0.5)
# ax.plot(graphiken['DK WT14'][8], color='red', lw=0.5)
# ax.plot(graphiken['DK WT14'][9], color='darkred', lw=0.5)
# ax.plot(graphiken['DK WT14'][10], color='violet', lw=0.5)
# ax.plot(graphiken['DK WT14'][11], color='darkblue', lw=0.5)
# plt.axis([1, 23, 5, 20])
# plt.setp(plt.gca(), xticklabels=[6, 12, 18], yticks=(10, 15, 20), xticks=(6, 12, 18))
# plt.text(20, 18, 'IV', fontsize=20)
# plt.xlabel('hours')

# fig.savefig('albedo.png')
plt.show()