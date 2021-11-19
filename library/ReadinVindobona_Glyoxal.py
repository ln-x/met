# -*- coding: utf-8 -*-
__author__ = 'lnx'
import datetime
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

#* Day of Year 1993
#* Uhrzeit [UT]
#* Uhrzeit [LT]
#* Sonnen-Zenitwinkel [ø]
#* Sonnen-Azimutwinkel [ø]
#* LineOfSight [ø]
#* Blick-Azimutwinkel [ø]
#* Bezugs-Sonnen-Zenitwinkel [ø]
#* Bezugs-Sonnen-Azimutwinkel [ø]
#* Bezugs-LineOfSight [ø]
#* Schraege Saeule O3 [Molek / cmý]
#* Fit-Fehler O3 [%]
#* Schraege Saeule NO2 [Molek / cmý]
#* Fit-Fehler NO2 [%]
#* Schraege Saeule O4 [Molek / cmý]
#* Fit-Fehler O4 [%]
#* Schraege Saeule CHOCHO [Molek / cmý]
#* Fit-Fehler CHOCHO [%]
#* Schraege Saeule NO3 [Molek / cmý]
#* Fit-Fehler NO3 [%]
#* Schraege Saeule H2O [Molek / cmý]
#* Fit-Fehler H2O [%]
#* Schraege Saeule RING [Molek / cmý]
#* Fit-Fehler RING [%]
#* Schraege Saeule Offset [Molek / cmý]
#* Fit-Fehler Offset [%]
#* Bezugsspektrum
#* Fit-Fehler Bezugsspektrum [%]
#* Shift Bezug [nm]
#* Squeeze Bezug
#* Chisquare
#* RMS
#* Iterationen
#* Spikes
#* Intensitaet
#* CI (424.50-425.50)/(439.50-440.50)
#* Intensity_1 (439.50-440.50)
#* Intensity_2 (439.50-440.50)
#* Integrationszeit
#* Daten vom 01.01.2020 Off-Axis Wien_VetMed LOS:  90.00 Azim:   0.00
#* Spektrometer P
#* Polynom 5-ten Grades
#* Keine Glaettung
#* Maximal 600 Iterationen im Fit; Konvergenzkriterium  1.000E-0008
#* SVD_TOL =  1.000E-0008
#* Bezugsspektrum:  (1)      ungefaltet Bezugszeit: 06:08:56:74 ??.??.???? LOS: 180.00 Azim:   0.00
#* Fraunhoferkalibration auf C:\DOAS\VINDOBONA_VetMed\ref\CROSS-SECTIONS\CINDI-2_xs\RAW\SAO2010_SOLREF_AIR_LINPOL001NM.RAW
#* Fraunhofershift = -0.041 nm, Fraunhofersqueeze = 1.000
#* Spektren: C:\DOAS\VINDOBONA_VetMed\pc\JAN2020\200101AP.PC
#*     O3 : SFIT    C:\DOAS\VINDOBONA_VetMed\ref\CROSS-SECTIONS\CINDI-2_xs\RAW\O3_223K_SDY_AIR_LINPOL001NM.RAW   0.000 <= SHIFT <=  0.000 ;  1.000 <= SQUEEZE <=  1.000; n_poly = 3; I0_SC =  1.000E+0020
#*    NO2 : SFIT    C:\DOAS\VINDOBONA_VetMed\ref\CROSS-SECTIONS\CINDI-2_xs\RAW\NO2_298K_VANDAELE_SPLINE001NM.RAW   0.000 <= SHIFT <=  0.000 ;  1.000 <= SQUEEZE <=  1.000; n_poly = 3; I0_SC =  1.000E+0017
#*     O4 : SFIT    C:\DOAS\VINDOBONA_VetMed\ref\CROSS-SECTIONS\CINDI-2_xs\RAW\O4_THALMAN_VOLKAMER_293K_INAIR_LINPOL001NM.RAW   0.000 <= SHIFT <=  0.000 ;  1.000 <= SQUEEZE <=  1.000; n_poly = 2
#* CHOCHO : SFIT    C:\DOAS\ref\cross\download\Interpoliert\CHOCHO_296K_SPIETZ.RAW   0.000 <= SHIFT <=  0.000 ;  1.000 <= SQUEEZE <=  1.000; n_poly = 0
#*    NO3 : SFIT    C:\DOAS\VINDOBONA_VetMed\ref\CROSS-SECTIONS\CINDI-2_xs\RAW\NO2A_220P298K_VANDAELE_VIS_SPLINE001NM_Zeros5nm.RAW   0.000 <= SHIFT <=  0.000 ;  1.000 <= SQUEEZE <=  1.000; n_poly = 3; I0_SC =  1.000E+0017
#*    H2O : SFIT    C:\DOAS\VINDOBONA_VetMed\ref\CROSS-SECTIONS\CINDI-2_xs\RAW\H2O_HITEMP_2010_390-700_296K_1013MBAR_AIR_BIN001NM.RAW   0.000 <= SHIFT <=  0.000 ;  1.000 <= SQUEEZE <=  1.000; n_poly = 3
#*   RING : SFIT    C:\DOAS\VINDOBONA_VetMed\ref\CROSS-SECTIONS\CINDI-2_xs\RAW\RING_QDOASCALC_HIGHRESSAO2010_NORM_LINPOL001NM.RAW   0.000 <= SHIFT <=  0.000 ;  1.000 <= SQUEEZE <=  1.000; n_poly = 3
#* Offset : SFIT                        1 / I_akt normalised  -0.100 <= SHIFT <=  0.100 ;  1.000 <= SQUEEZE <=  1.000; n_poly = 4
#*  Bezug : SCONST                          ZS_FILE_SYNC_INT  -0.500 <= SHIFT <=  0.500 ;  0.980 <= SQUEEZE <=  1.020; n_poly = 0
#* Faltung aller *.RAW Referenzen mit Spaltfunktion, (N = 31)!
#* Spaltfunktion Offset-korrigiert!
#* RAW-Ringspektrum aus Quotient ohne ln berechnet!
#* Fenster: 433.00 ... 458.00 nm (433.07 ... 457.92 nm)
#* Kein Offset des Fensters
#* Fitmodus: NOON
#* Erzeugt am  22.04.2020 um 08:51:40 von NLIN_D 7.64 (16.03.2018)
#*day-of-year-1993 time time_LT zenith_angle solar-azimuth-angle los viewing-azimuth-angle ref-zenith-angle ref-azimuth-angle ref-LOS a[O3] sig[O3] a[NO2] sig[NO2] a[O4] sig[O4] a[CHOCHO] sig[CHOCHO] a[NO3] sig[NO3] a[H2O] sig[H2O] a[RING] sig[RING] a[Offset] sig[Offset] a[Bezug] sig[Bezug] sh[Bezug] sq[Bezug] chisq rms it spikes ints ci ints1 ints2 expt


def loadfile(foldername, filename, chocho_date):
    chocho = []
    timeaxis = []
    file = foldername+'/'+filename
    #print(file)

    #VERS0
    #f = open('/windata/DATA/remote/ground/maxdoas/chocho2020/201009CP.CHOCHO_Vis_sync','r')  # We need to re-open the file
    #print("TEST")
    #data = f.read()
    #print("TEST")

    #print(data)
    #f.close()

    #VERS1
    with open(file,"r",encoding="ascii", errors="surrogateescape") as f:    #Einlesen des Files ab Zeile 67
        #print(f) #<_io.TextIOWrapper name='/windata/DATA/remote/ground/maxdoas/chocho2020/200925SP.CHOCHO_Vis_sync' mode='r' encoding='UTF-8'>
        alldata = f.readlines()[67:]
    #print(alldata)

    #VERS2
    #alldata = np.loadtxt(StringIO(file), skiprows=77)[:, 1:]
    #print(alldata)

    #VERS3
    #with open(file, 'r') as current:
    #    lines = current.readlines()
    #if not lines:
    #    print('FILE IS EMPTY')
    #else:
    #    for line in lines:
    #        print(line)


    #exit()
    splitdata = []  # splitlistcomp = [i.split() for i in data]
    for i in alldata:
            splitdata.append([float(x) for x in i.split()])
    for j in splitdata:
            # TODO if j[2]  horizontal optical path length <25 or >75 percentil
            #if j[1] < 75:  #FILTER: only take values where Solar zenith is above 75°
            hour, frac = str(j[1]).split('.')  # split bei '.' #TODO make preciser
            #print(hour,frac)
            minute = (int(frac[:2])/100)*60
            #print(minute)
            date_time = chocho_date + datetime.timedelta(hours=int(hour)) + datetime.timedelta(minutes=minute) # + datetime.timedelta(seconds=second)
            #print(date_time)
            timeaxis.append(date_time)
            chocho.append(j[14])
            #else:
            #   pass
    chocho_dft = pd.DataFrame({'datetime': timeaxis, 'chocho': chocho})
    chocho_dft['datetime'] = pd.to_datetime(chocho_dft['datetime'])
    chocho_dft = chocho_dft.set_index(['datetime'])
    return(chocho_dft)

def loadfileALL(foldername):
    files = os.listdir(foldername)
    #print(files)
    appended_dataD = []
    appended_dataK = []
    for i in range(len(files)):
        try:
            #splitlistcomp = [j.split() for j in files[i]]
            day = str(files[i][4:6])# splitlistcomp[3:4]
            month = str(files[i][2:4])#splitlistcomp[2:3]
            year = "20"+ str(files[i][0:2]) #splitlistcomp[:2]
            axis = str(files[i][6:7]) #splitlistcomp[:2]
            #print(day,month,year,axis)
            chocho_date = datetime.datetime(year=int(year),month=int(month), day=int(day))
            #print(chocho_date)
            #exit()
            if axis == "D":
                data_chocho_D = loadfile(foldername=foldername, filename=files[i], chocho_date=chocho_date)
            elif axis == "K":
                data_chocho_K = loadfile(foldername=foldername, filename=files[i], chocho_date=chocho_date)
            else:
                pass
            #print("LOADFILE PASSED")
            #print(data_chocho)
            appended_dataD.append(data_chocho_D)
            appended_dataK.append(data_chocho_K)
        except:
            pass
    #exit()
    chochoD = pd.concat(appended_dataD)
    chochoK = pd.concat(appended_dataK)
    #hOPL_25 = hcho['hOPL'].quantile(q=0.25, interpolation='linear')
    #hOPL_75 = hcho['hOPL'].quantile(q=0.75, interpolation='linear')
    #isJFM1 = (hcho['hOPL'] < hOPL_75) & (hcho['hOPL'] > hOPL_25)
    #hcho_f = hcho[isJFM1]
    chochoD_dmax = chochoD.resample('D').max()
    chochoK_dmax = chochoK.resample('D').max()
    #chocho_d = chocho_f.resample('D').mean()
    #chocho_m = chocho_dmax.resample('M').mean()

    chochoD.to_csv("/home/heidit/Downloads/chocho.csv")
    return(chochoD_dmax['chocho'],chochoK_dmax['chocho'])

if __name__ == '__main__':
    #f = open('/windata/DATA/remote/ground/maxdoas/chocho2020/201009CP.CHOCHO_Vis_sync','r',encoding="ascii", errors="surrogateescape")  # We need to re-open the file
    #print("TEST")
    #data = f.readlines()[90:]
    #print("TEST")
    #print(data)

    foldername = "/windata/DATA/remote/ground/maxdoas/chocho2020"
    chochoD_dmax, chochoK_dmax = loadfileALL(foldername)
    print(chochoK_dmax)
