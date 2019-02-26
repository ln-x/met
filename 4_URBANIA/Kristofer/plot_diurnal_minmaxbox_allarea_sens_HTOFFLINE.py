# -*- coding: utf-8 -*-
from netCDF4 import Dataset
from collections import namedtuple
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
import os
import wrf
from wrf import to_np, getvar, get_basemap, latlon_coords
from functions_htOFFLINE import collect_data

"""
Creates MIN MAX Boxplots from all chosen Areas and runs

***********       WHISKERS show the whole RANGE      ***********

"""

date_2015 = '2015-08-05'
date_2069 = '2069-07-01'

domain = 'd03'
#run = 'REF_Run_2015' # reference run
#run1 = 'SPR_Run_2015' # sprawl run 
#run2 = 'OPT_Run_2015' # optimized city run
#path = '/hp4/Urbania/WRF-2019-Runs/' # runPATH
path = '/media/lnx/Norskehavet/OFFLINE/' # runPATH
#filepath = path + run + '/'
#filepath1 = path + run1 + '/'
#filepath2 = path + run2 + '/'
para = 'UTCI_OUTSHAD'
#para = 'T2M'

""" not usable days - uncomment used run """
cuttime_2069 = pd.to_datetime(['2069-7-1','2069-7-2','2069-7-3','2069-7-4','2069-7-5', '2069-7-6','2069-7-9']) # day with not usable data
cuttime_2015 = pd.to_datetime(['2015-08-05', '2015-08-06', '2015-08-07', '2015-08-08','2015-08-11', '2015-08-14']) # 2015 run

plotdir_2015 ='/media/lnx/Norskehavet/OFFLINE/plots' + date_2015 + '/'
plotdir_2069 ='/media/lnx/Norskehavet/OFFLINE/plots/' + date_2069 + '/'
plotdir_sens ='/media/lnx/Norskehavet/OFFLINE/plots/'


if not os.path.exists(plotdir_2015):
    os.makedirs(plotdir_2015)
if not os.path.exists(plotdir_2069):
    os.makedirs(plotdir_2069)
if not os.path.exists(plotdir_sens):
    os.makedirs(plotdir_sens)



region = ['NO', 'CE', 'RU', 'SA', 'SE', 'SX', 'SI', 'VW', 'WE']


region_sn = {'NO': (73,82), 
          'CE': (50,59),
          'RU': (57,66),
          'SA': (58,67),
          'SE': (37,46),
          'SX': (24,33),
          'SI': (31,40),
          'VW': (47,56),
          'WE': (62,71),
          }

region_we = {'NO': (89,98),
          'CE': (80,89),
          'RU': (128,137),
          'SA': (109,118),
          'SE': (99,108),
          'SX': (75,84),
          'SI': (68,77),
          'VW': (64,73),
          'WE': (73,82)
          }

#%%


def plot_box(data, tmin, trange, ylabel, labels, suptitle, filenam, plotdir, boxprobs, flierprops, medianprops, meanpointprobs, whiskerprops, init, showmeans=True, whis='range', param=para):
    
    fig, ax = plt.subplots(1,9, figsize=(16,9))
    #gs = gridspec.GridSpec(1, 9)
    
    ax[0] = plt.subplot(1,9,1)
    
    ax[0].boxplot([data[0][1].iloc[:,0], data[0][1].iloc[:,1],data[0][1].iloc[:,2]],
                notch=True, labels=labels, boxprops=boxprops, showfliers=True, flierprops=flierprops, 
                medianprops=medianprops, showmeans=showmeans, meanprops=meanpointprops, 
                whiskerprops=whiskerprops, whis=whis)
    #ax[idx].tick_params(axis='y', labelleft='off', labelright='on')
    
    ax[0].set_title(data[0][1].iloc[:,0].name[:2], fontsize=14)
    ax[0].set_ylabel(ylabel, fontsize=15)
    ax[0].tick_params(axis='both', labelsize=14)
    ax[0].set_ylim(tmin, tmin+trange)
    axlim = ax[0].get_ylim()
    
    ax[0].grid(True)
    
    
    for idx in range(1,len(data)):
        
        ax[idx] = plt.subplot(1,9,idx+1, sharey=ax[0])
    
        ax[idx].boxplot([data[idx][1].iloc[:,0], data[idx][1].iloc[:,1], data[idx][1].iloc[:,2]],
                    notch=True, labels=labels, boxprops=boxprops, showfliers=True, flierprops=flierprops, 
                    medianprops=medianprops, showmeans=showmeans, meanprops=meanpointprops, 
                    whiskerprops=whiskerprops, whis=whis)
        
        ax[idx].tick_params(axis='both', labelsize=14)
    
        plt.setp(ax[idx].get_yticklabels(), visible=False) #removes the ylabels from the subplots even its shared
        ax[idx].set_title(data[idx][1].iloc[:,0].name[:2], fontsize=14)
        ax[idx].set_ylim(axlim)
        ax[idx].grid(True)
    
    #fig.tight_layout()
    fig.suptitle(ylabel + suptitle, y=0.99, fontsize=14)   
    
    ax[0] = plt.gca()
    ax[0].text(0.11,0.92,'Init: ' + init, fontsize=12, transform=fig.transFigure)
        
    filename = domain + '_' + param + '_BOX_' + filenam  +".png"
    plt.savefig(plotdir + filename)

    return

def plot_box_diff(data, tmin, trange, ylabel, labels, suptitle, filenam, plotdir, boxprobs, flierprops, medianprops, meanpointprobs, whiskerprops, init, showmeans=False, whis='range', param=para):
    
    fig, ax = plt.subplots(1,9, figsize=(16,9))
    #gs = gridspec.GridSpec(1, 9)
    
    ax[0] = plt.subplot(1,9,1)
    
    ax[0].boxplot([data[0][1].iloc[:,1] - data[0][1].iloc[:,0], data[0][1].iloc[:,2] - data[0][1].iloc[:,0]],
                notch=True, labels=labels, boxprops=boxprops, showfliers=True, flierprops=flierprops, 
                medianprops=medianprops, showmeans=showmeans, meanprops=meanpointprops, 
                whiskerprops=whiskerprops, whis=whis)
    #ax[idx].tick_params(axis='y', labelleft='off', labelright='on')
    
    ax[0].set_title(data[0][1].iloc[:,0].name[:2], fontsize=14)
    ax[0].set_ylabel(ylabel, fontsize=15)
    ax[0].tick_params(axis='both', labelsize=14)
    ax[0].set_ylim(tmin, tmin+trange)
    axlim = ax[0].get_ylim()
    
    ax[0].grid(True)
    
    
    for idx in range(1,len(data)):
        ax[idx] = plt.subplot(1,9,idx+1, sharey=ax[0])
    
        ax[idx].boxplot([data[idx][1].iloc[:,1] - data[idx][1].iloc[:,0], data[idx][1].iloc[:,2] - data[idx][1].iloc[:,0]],
                    notch=True, labels=labels, boxprops=boxprops, showfliers=True, flierprops=flierprops, 
                    medianprops=medianprops, showmeans=showmeans, meanprops=meanpointprops, 
                    whiskerprops=whiskerprops, whis=whis)
        
        ax[idx].tick_params(axis='both', labelsize=14)
    
        plt.setp(ax[idx].get_yticklabels(), visible=False) #removes the ylabels from the subplots even its shared
        ax[idx].set_title(data[idx][1].iloc[:,0].name[:2], fontsize=14)
        ax[idx].set_ylim(axlim)
        ax[idx].grid(True)
    
    
    #fig.tight_layout()
    fig.suptitle(ylabel + suptitle, y=0.99, fontsize=14)   
    
    ax[0] = plt.gca()
    ax[0].text(0.11,0.92,'Init: ' + init, fontsize=12, transform=fig.transFigure)
        
    filename = domain + '_' + param + '_BOX_' + filenam  +".png"
    plt.savefig(plotdir + filename)

    return


def plot_box_sens(data1, data2, tmin, trange, ylabel, labels1, suptitle, filenam, plotdir, boxprobs1, boxprobs2, flierprops, medianprops, meanpointprobs, whiskerprops, showmeans=True, whis='range', param=para):
    
    fig, ax = plt.subplots(1,9, figsize=(16,9))
    #gs = gridspec.GridSpec(1, 9)
    
    ax[0] = plt.subplot(1,9,1)
    
    bp1 = ax[0].boxplot([data1[0][1].iloc[:,0], data1[0][1].iloc[:,1], data1[0][1].iloc[:,2]],
                notch=True, labels=labels, boxprops=boxprobs1, showfliers=True, flierprops=flierprops, 
                medianprops=medianprops, showmeans=showmeans, meanprops=meanpointprops, 
                whiskerprops=whiskerprops, whis=whis)

    bp2 = ax[0].boxplot([data2[0][1].iloc[:,0], data2[0][1].iloc[:,1], data2[0][1].iloc[:,2]],
                notch=True, labels=labels, boxprops=boxprobs2, showfliers=True, flierprops=flierprops, 
                medianprops=medianprops, showmeans=showmeans, meanprops=meanpointprops, 
                whiskerprops=whiskerprops, whis=whis)
    
    fig.legend([bp1["boxes"][0], bp2["boxes"][0]], ['2015', '2069'], loc='center right')
    #ax[idx].tick_params(axis='y', labelleft='off', labelright='on')
    
    ax[0].set_title(data1[0][1].iloc[:,0].name[:2], fontsize=16)
    ax[0].set_ylabel(ylabel, fontsize=15)
    ax[0].tick_params(axis='both', labelsize=14)
    ax[0].set_ylim(tmin, tmin+trange)
    axlim = ax[0].get_ylim()
    
    ax[0].grid(True)
    
    
    for idx in range(1,len(data1)):
        
        ax[idx] = plt.subplot(1,9,idx+1, sharey=ax[0])
        
        ax[idx].boxplot([data1[idx][1].iloc[:,0], data1[idx][1].iloc[:,1],data1[idx][1].iloc[:,2]],
                    notch=True, labels=labels, boxprops=boxprobs1, showfliers=True, flierprops=flierprops, 
                    medianprops=medianprops, showmeans=showmeans, meanprops=meanpointprops, 
                    whiskerprops=whiskerprops, whis=whis)

        ax[idx].boxplot([data2[idx][1].iloc[:,0], data2[idx][1].iloc[:,1],data2[idx][1].iloc[:,2]],
                    notch=True, labels=labels, boxprops=boxprobs2, showfliers=True, flierprops=flierprops, 
                    medianprops=medianprops, showmeans=showmeans, meanprops=meanpointprops, 
                    whiskerprops=whiskerprops, whis=whis)

        ax[idx].tick_params(axis='both', labelsize=14)
    
        plt.setp(ax[idx].get_yticklabels(), visible=False) #removes the ylabels from the subplots even its shared
        ax[idx].set_title(data1[idx][1].iloc[:,0].name[:2], fontsize=16)
        ax[idx].set_ylim(axlim)
        ax[idx].grid(True)
    
    
    #fig.tight_layout()
    fig.suptitle(ylabel + suptitle, y=0.99, fontsize=16)   
    
#    ax[0] = plt.gca()
#    ax[0].text(0.11,0.92,'Init: ' + init, fontsize=12, transform=fig.transFigure)
        
    filename = domain + '_' + param + '_BOX_' + filenam  +".png"
    plt.savefig(plotdir + filename)

    return

def plot_box_sens_diff(data1, data2, tmin, trange, ylabel, labels1, suptitle, filenam, plotdir, boxprobs1, boxprobs2, flierprops, medianprops, meanpointprobs, whiskerprops, showmeans=True, whis='range', param=para):
    
    fig, ax = plt.subplots(1,9, figsize=(16,9))
    #gs = gridspec.GridSpec(1, 9)
    
    ax[0] = plt.subplot(1,9,1)
    
    bp1 = ax[0].boxplot([data1[0][1].iloc[:,2] - data1[0][1].iloc[:,1], data2[0][1].iloc[:,2] - data2[0][1].iloc[:,1]],
                widths=(0.5, 0.5), notch=True, labels=labels, boxprops=boxprobs1, showfliers=True, flierprops=flierprops, 
                medianprops=medianprops, showmeans=showmeans, meanprops=meanpointprops, 
                whiskerprops=whiskerprops, whis=whis)
#    bp2 = ax[0].boxplot(data2[0][1].iloc[:,2] - data2[0][1].iloc[:,1],
#                notch=True, labels=labels, boxprops=boxprobs2, showfliers=True, flierprops=flierprops, 
#                medianprops=medianprops, showmeans=showmeans, meanprops=meanpointprops, 
#                whiskerprops=whiskerprops, whis=whis)
    plt.setp(bp1['boxes'][1], color='red')
#    plt.setp(bp2['boxes'], color='red')

    #    fig.legend([bp1["boxes"][0], bp2["boxes"][0]], ['2015', '2069'], loc='center right')
    #ax[idx].tick_params(axis='y', labelleft='off', labelright='on')
    
    ax[0].set_title(data1[0][1].iloc[:,0].name[:2], fontsize=16)
    ax[0].set_ylabel(ylabel, fontsize=15)
    ax[0].tick_params(axis='both', labelsize=14)
    plt.setp(ax[0].get_xticklabels(), rotation=90)
    ax[0].set_ylim(tmin, tmin+trange)
    axlim = ax[0].get_ylim()
    
    ax[0].grid(True)
    
    
    for idx in range(1,len(data1)):
        
        ax[idx] = plt.subplot(1,9,idx+1, sharey=ax[0])
        
        bp1 = ax[idx].boxplot([data1[idx][1].iloc[:,2] - data1[idx][1].iloc[:,1], data2[idx][1].iloc[:,2] - data2[idx][1].iloc[:,1]],
                    widths=(0.5, 0.5), notch=True, labels=labels, boxprops=boxprobs1, showfliers=True, flierprops=flierprops, 
                    medianprops=medianprops, showmeans=showmeans, meanprops=meanpointprops, 
                    whiskerprops=whiskerprops, whis=whis)
        plt.setp(bp1['boxes'][1], color='red')

#        ax[idx].boxplot(data2[idx][1].iloc[:,2] - data2[idx][1].iloc[:,1],
#                    notch=True, labels=labels, boxprops=boxprobs2, showfliers=True, flierprops=flierprops, 
#                    medianprops=medianprops, showmeans=showmeans, meanprops=meanpointprops, 
#                    whiskerprops=whiskerprops, whis=whis)

        ax[idx].tick_params(axis='both', labelsize=14)
    
        plt.setp(ax[idx].get_yticklabels(), visible=False) #removes the ylabels from the subplots even its shared
        plt.setp(ax[idx].get_xticklabels(), rotation=90)
        ax[idx].set_title(data1[idx][1].iloc[:,0].name[:2], fontsize=16)
        ax[idx].set_ylim(axlim)
        ax[idx].grid(True)
    
    
    #fig.tight_layout()
    fig.suptitle(ylabel + suptitle, y=0.99, fontsize=16)   
    
#    ax[0] = plt.gca()
#    ax[0].text(0.11,0.92,'Init: ' + init, fontsize=12, transform=fig.transFigure)
        
    filename = domain + '_' + param + '_BOX_' + filenam  +".png"
    plt.savefig(plotdir + filename)

    return


def plot_box_diff_runs(data, tmin, trange, ylabel, labels, suptitle, filenam, plotdir, boxprobs, flierprops, medianprops, meanpointprobs, whiskerprops, init, showmeans=True, whis='range', param=para):
    
    fig, ax = plt.subplots(1,9, figsize=(16,9))
    #gs = gridspec.GridSpec(1, 9)
    
    ax[0] = plt.subplot(1,9,1)
    
    ax[0].boxplot(data[0][1].iloc[:,2] - data[0][1].iloc[:,1],
                notch=True, labels=labels, boxprops=boxprops, showfliers=True, flierprops=flierprops, 
                medianprops=medianprops, showmeans=showmeans, meanprops=meanpointprops, 
                whiskerprops=whiskerprops, whis=whis)
    #ax[idx].tick_params(axis='y', labelleft='off', labelright='on')
    
    ax[0].set_title(data[0][1].iloc[:,0].name[:2], fontsize=14)
    ax[0].set_ylabel(ylabel, fontsize=15)
    ax[0].tick_params(axis='both', labelsize=14)
    ax[0].set_ylim(tmin, tmin+trange)
    axlim = ax[0].get_ylim()
    
    ax[0].grid(True)
    
    
    for idx in range(1,len(data)):
        
        ax[idx] = plt.subplot(1,9,idx+1, sharey=ax[0])
    
        ax[idx].boxplot(data[idx][1].iloc[:,2] - data[idx][1].iloc[:,1],
                    notch=True, labels=labels, boxprops=boxprops, showfliers=True, flierprops=flierprops, 
                    medianprops=medianprops, showmeans=showmeans, meanprops=meanpointprops, 
                    whiskerprops=whiskerprops, whis=whis)
        
        ax[idx].tick_params(axis='both', labelsize=14)
    
        plt.setp(ax[idx].get_yticklabels(), visible=False) #removes the ylabels from the subplots even its shared
        ax[idx].set_title(data[idx][1].iloc[:,0].name[:2], fontsize=14)
        ax[idx].set_ylim(axlim)
        ax[idx].grid(True)
    
    
    #fig.tight_layout()
    fig.suptitle(ylabel + suptitle, y=0.99, fontsize=14)   
    
    ax[0] = plt.gca()
    ax[0].text(0.11,0.92,'Init: ' + init, fontsize=12, transform=fig.transFigure)
        
    filename = domain + '_' + param + '_BOX_' + filenam  +".png"
    plt.savefig(plotdir + filename)

    return


med_2015, min_2015, max_2015, init_2015 = collect_data(date_2015, para, cuttime_2015, region=region, region_sn=region_sn, region_we=region_we, path=path)
med_2069, min_2069, max_2069, init_2069 = collect_data(date_2069, para, cuttime_2069, region=region, region_sn=region_sn, region_we=region_we, path=path)



#%%
""" 
PLOTTING ROUTINE

"""

labels=['REF','SPR', 'OPT']

boxprops = dict( linewidth=1.5, color='b')
flierprops = dict(marker='x', linestyle='none')
medianprops = dict(linestyle='-', linewidth=2.5, color='firebrick')
meanpointprops = dict(marker='D', markeredgecolor='black',
                  markerfacecolor='g')
whiskerprops = dict( linestyle='--', color='k')
#%%
"""
#########################    MAX PLOT    ######################################
"""

suptitle = ' daily maximum Air Temperatur at 2m height\n'
ylabel= r"$T_{2m\ max}$" +' '+ u'[°C]'
tmin = 30
trange = 10
plot_box(max_2015, tmin, trange, ylabel, labels, suptitle, 'MAX', plotdir_2015, boxprops, flierprops, medianprops, meanpointprops, whiskerprops, init_2015)
 


"""
#########################    MIN PLOT    ######################################
"""

suptitle = ' daily minimum Air Temperatur at 2m height\n'
ylabel= r"$T_{2m\ min}$" +' '+ u'[°C]'
tmin = 18
plot_box(min_2015, tmin, trange, ylabel, labels, suptitle, 'MIN', plotdir_2015, boxprops, flierprops, medianprops, meanpointprops, whiskerprops, init_2015)



"""
#########################    MIN DIFF PLOT    ######################################
"""
labels=['SPR', 'OPT']
tmin = -2
trange= 4
suptitle = ' Difference SPR/OPT - REF in daily minimum Air Temperatur at 2m height\n'

plot_box_diff(min_2015, tmin, trange, ylabel, labels, suptitle, 'MIN_DIFF', plotdir_2015, boxprops, flierprops, medianprops, meanpointprops, whiskerprops, init_2015)


#%%
"""
#########################    MAX DIFF PLOT    ######################################
"""
suptitle = ' Difference SPR/OPT - REF in daily maximum Air Temperatur at 2m height\n'
ylabel= r"$T_{2m\ max}$" +' '+ u'[°C]'

plot_box_diff(max_2015, tmin, trange, ylabel, labels, suptitle, 'MAX_DIFF', plotdir_2015, boxprops, flierprops, medianprops, meanpointprops, whiskerprops, init_2015)



"""
#########################    MAX DIFF OPT - SPR PLOT    ######################################
"""
suptitle = ' Difference OPT - SPR in daily maximum Air Temperatur at 2m height\n'
labels=[ 'OPT - SPR']

plot_box_diff_runs(max_2015, tmin, trange, ylabel, labels, suptitle, 'MAX_DIFF_OPT-SPR', plotdir_2015, boxprops, flierprops, medianprops, meanpointprops, whiskerprops, init_2015)



"""
#########################    MIN DIFF OPT - SPR PLOT    ######################################
"""
suptitle = ' Difference OPT - SPR in daily minimum Air Temperatur at 2m height\n'
labels=[ 'OPT - SPR']
ylabel= r"$T_{2m\ min}$" +' '+ u'[°C]'

plot_box_diff_runs(min_2015, tmin, trange, ylabel, labels, suptitle, 'MIN_DIFF_OPT-SPR', plotdir_2015, boxprops, flierprops, medianprops, meanpointprops, whiskerprops, init_2015)

#%%
"""
#########################    SENS MIN PLOT    ######################################
"""
suptitle = ' daily minimum Air Temperatur at 2m height\n'
labels=['REF','SPR', 'OPT']
ylabel= r"$T_{2m\ min}$" +' '+ u'[°C]'
tmin = 18
trange = 12

boxprops_2015 = dict( linewidth=1.5, color='b')
boxprops_2069 = dict( linewidth=1.5, color='r')
medianprops = dict(linestyle='-', linewidth=2.5, color='firebrick')



plot_box_sens(min_2015, min_2069, tmin, trange, ylabel, labels, suptitle, 'SENS_min', plotdir_sens, boxprops_2015, boxprops_2069, flierprops, medianprops, meanpointprops, whiskerprops, showmeans=False)

"""
#########################    SENS MAX PLOT    ######################################
"""
suptitle = '  daily maximum Air Temperatur at 2m height\n'
ylabel= r"$T_{2m\ max}$" +' '+ u'[°C]'
labels=['REF','SPR', 'OPT']

tmin = 30
trange = 14

plot_box_sens(max_2015, max_2069, tmin, trange, ylabel, labels, suptitle, 'SENS_max', plotdir_sens, boxprops_2015, boxprops_2069, flierprops, medianprops, meanpointprops, whiskerprops, showmeans=False)

#%%
"""
#########################    SENS DIFF MAX PLOT    ######################################
"""
suptitle = ' Difference OPT-SPR 2015 & 2069 daily maximum Air Temperatur at 2m height\n'
ylabel= r"$T_{2m\ max}$" +' '+ u'[°C]'
labels=[ '2015', '2069']
tmin = -2
trange = 4
boxprops_2015 = dict( linewidth=1.5, color='b')
boxprops_2069 = dict( linewidth=1.5, color='r')
medianprops = dict(linestyle='-', linewidth=2.5, color='firebrick')

plot_box_sens_diff(max_2015, max_2069, tmin, trange, ylabel, labels, suptitle, 'SENS_max_OPT-SPR', plotdir_sens, boxprops_2015, boxprops_2069, flierprops, medianprops, meanpointprops, whiskerprops, showmeans=False)

"""
#########################    SENS DIFF MIN PLOT    ######################################
"""
suptitle = ' Difference OPT-SPR 2015 & 2069 daily minimum Air Temperatur at 2m height\n'
ylabel= r"$T_{2m\ min}$" +' '+ u'[°C]'

plot_box_sens_diff(min_2015, min_2069, tmin, trange, ylabel, labels, suptitle, 'SENS_min_OPT-SPR', plotdir_sens, boxprops_2015, boxprops_2069, flierprops, medianprops, meanpointprops, whiskerprops, showmeans=False)
