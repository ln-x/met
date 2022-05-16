import os
from datetime import datetime
from netCDF4 import Dataset
import numpy as np
import pandas as pd

def loadCAMXALL(pathbase_camx,x,y):
    foldername = pathbase_camx + '/3_CAMXinput_MEGANout/'
    files = os.listdir(foldername)
    files = sorted(files)
    appended_IsopC = []
    appended_TerpC = []
    appended_MethC = []
    appended_ParC = []
    appended_XylC = []
    appended_OleC = []
    dateaxis=[]
    for i in range(len(files)):
        day = str(files[i][-5:-3])  # splitlistcomp[3:4]
        month = str(files[i][-7:-5])  # splitlistcomp[2:3]
        year = "20" + str(files[i][-9:-7])  # splitlistcomp[:2]
        #print(day,month,year)
        date = datetime(year=int(year), month=int(month), day=int(day))
        #print(date)
        #exit()
        IsopC, TerpC, MethC, ParC, XylC, OleC = loadfileCAMX(foldername=foldername, filename=files[i], date=date, x=x, y=y)
        appended_IsopC.append(IsopC)
        appended_TerpC.append(TerpC)
        appended_MethC.append(MethC)
        appended_ParC.append(ParC)
        appended_XylC.append(XylC)
        appended_OleC.append(OleC)
        dateaxis.append(date)
    Bio_Emis = pd.DataFrame({'datetime': dateaxis, 'Isop': appended_IsopC, 'Terp': appended_TerpC, 'Meth': appended_MethC,
                             'Par': appended_ParC, 'Xyl': appended_XylC, 'Ole': appended_OleC})
    Bio_Emis['datetime'] = pd.to_datetime(Bio_Emis['datetime'])  # , unit='D')
    Bio_Emis = Bio_Emis.set_index(['datetime'])

    return Bio_Emis

def loadfileCAMX(foldername, filename, date, x, y):
    file = foldername + "/" + filename
    f = Dataset(file, mode='r')
    Meth = f.variables["MEOH"][:, 0, y, x]  # ISOP(TSTEP, LAY, ROW, COL) ; [mol/s]
    Isop = f.variables["ISOP"][:, 0, y, x]
    Terp = f.variables["TERP"][:, 0, y, x]
    Par = f.variables["PAR"][:, 0, y, x]
    Xyl = f.variables["XYL"][:, 0, y, x]
    Ole = f.variables["OLE"][:, 0, y, x]

    #print(Meth)
    #Tflag = f.variables["TFLAG"][0, 0, 0]  # TSTEP, VAR, DATE-TIME flags 0:YYYYDDD, 1:HHMMSS
    # hourly values in daily files, "ISOP", "TERP", "PAR", "XYL", "OLE", "NR", "MEOH", "CH4", "NH3", "NO", "ALD2",
    # "ETOH", "FORM", "ALDX", "TOL", "IOLE", "CO", "ETHA", "ETH",  [mol/s]
    #date_time = hcho_date + datetime.timedelta(hours=int(hour)) + datetime.timedelta(minutes=minute) # + datetime.timedelta(seconds=second)
    #timeaxis.append(date_time)
    #hcho_dft = pd.DataFrame({'datetime': timeaxis, 'hcho': hcho, 'sza': sza,'hOPL': hOPL})
    #hcho_dft['datetime'] = pd.to_datetime(hcho_dft['datetime'])#, unit='D')
    #print("to_datetime", hcho_dft['datetime'])
    #hcho_dft = hcho_dft.set_index(['datetime'])
    return(np.mean(Isop), np.mean(Terp), np.mean(Meth), np.mean(Par), np.mean(Xyl), np.mean(Ole))

def loadCAMXALL_DD(pathbase_camx,x,y):
    foldername = pathbase_camx + '/4_CAMXoutput/depn/'
    #file = pathbase_camx_1819 + '4_CAMXoutput/depn/CAMx.v6.50_URBI_CMAQ_EQSAM.' + year + month + day + '.depn.grd01.nc'
    files = os.listdir(foldername)
    files = sorted(files)
    appended_DD = []
    appended_DV = []
    dateaxis=[]
    for i in range(len(files)):
        day = str(files[i][-16:-14])  # splitlistcomp[3:4]
        month = str(files[i][-18:-16])  # splitlistcomp[2:3]
        year = "20" + str(files[i][-20:-18])  # splitlistcomp[:2]
        #print(day,month,year)
        date = datetime(year=int(year), month=int(month), day=int(day))
        #print(date)
        #exit()
        DD, DV = loadfileCAMX_DD(foldername=foldername, filename=files[i], date=date, x=x, y=y)
        appended_DD.append(DD)
        appended_DV.append(DV)
        dateaxis.append(date)
    DDep_O3 = pd.DataFrame({'datetime': dateaxis, 'DD': appended_DD, 'DV': appended_DV})
    DDep_O3['datetime'] = pd.to_datetime(DDep_O3['datetime'])  # , unit='D')
    DDep_O3 = DDep_O3.set_index(['datetime'])

    return DDep_O3

def loadfileCAMX_DD(foldername, filename, date, x, y):
    file = foldername + "/" + filename
    f = Dataset(file, mode='r')
    DD = f.variables["O3_DD"][:, 0, y, x]
    # float O3_DD(TSTEP, LAY, ROW, COL);  long_name = "Dry dep mass"; units = "mol ha-1";
    # O3_DD: var_desc = "O3 dry deposited mass";
    # O3_DD: coordinates = "latitude longitude";
    DV = f.variables["O3_DV"][:, 0, y, x] #"O3 dry deposition velocity"; "m s-1";
    return(np.mean(DD), np.mean(DV))

if __name__ == '__main__':
    pathbase_camx = "/windata/DATA/models/boku/CAMX/2018-2019"
    camx3_y_vie_is1819 = 53
    camx3_x_vie_is1819 = 102
    Bio_Emis = loadCAMXALL(pathbase_camx, camx3_x_vie_is1819, camx3_y_vie_is1819)
    #print(Bio_Emis)