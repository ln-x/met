__author__ = 'lnx'
import pandas as pd
import matplotlib.pyplot as plt
import sys
from datetime import datetime
from datetime import timedelta
import numpy as np

#1) TRY TO PARSE DIRECTLY

custom_date_parser = lambda x: datetime.strptime(x, "%Y-%d-%m %H:%M:%S")

#df = pd.DataFrame(np.nan, columns=pd.date_range('00:00', '23:50', freq='10min'), index=pd.date_range('2017-10-29', '2018-03-24'))
#NO2_HMW = pd.read_csv(Luftmessnetz + "NO2_HMW_01-01-2017_19-04-2020.txt", delimiter=' ', parse_dates=["date"], date_parser=custom_date_parser)                         #date parsed correct, missing time
#NO2_HMW = pd.read_csv(Luftmessnetz + "NO2_HMW_01-01-2017_19-04-2020.txt", delimiter=' ', parse_dates=[[2,3]])                      #!NotImplementedError: file structure not yet supported
#NO2_HMW = pd.read_csv(Luftmessnetz + "NO2_HMW_01-01-2017_19-04-2020.txt", delimiter=' ', parse_dates=[['date', 'time(MEZ)']], date_parser=custom_date_parser)      #!NotImplementedError: file structure not yet supported
#NO2_HMW = pd.read_csv(Luftmessnetz + "NO2_HMW_01-01-2017_19-04-2020.txt", delimiter=' ', parse_dates={ 'date': ['date', 'time(MEZ)'] })


#2) CONSTRUCT TIMEAXIS
#2a) FROM SCRATCH - array length

x = range(len(NO2_HMW["STEF"][0::2]))
print(x)
#print(type(NO2_STEF.values))
#exit()
print(type(NO2_HMW))


#2b) TIMEDELTA

#d1 = datetime(2017, 1, 1, 00, 30)
#d2 = datetime(2020, 4, 19, 23, 30)
#delta = d2 - d1                                                                             #gives only delta
#timeaxis1 = pd.date_range(d1, d2)                                                           #gives daily timestamps:        dtype='datetime64[ns]', length=1205, freq='D') <class 'pandas.core.indexes.datetimes.DatetimeIndex'> 1205
#timeaxis2 = pd.date_range(start="2017-01-01", end="2020-04-19", freq='60min')#, periods=24) #gives wrong hourly timestamps: dtype='datetime64[ns]', length=28897, freq='60T') <class 'pandas.core.indexes.datetimes.DatetimeIndex'> 28897
#timeaxis3 = pd.date_range(start=d1, end=d2, freq='60min')#, periods=24)                     #gives correct hourly timestamps, but not taking accound of missing data  dtype='datetime64[ns]', length=28920, freq='60T') <class 'pandas.core.indexes.datetimes.DatetimeIndex'> 28920


#3) FROM COLUMN

#timeaxis5 = pd.to_datetime(NO2_HMW['date']) + pd.to_timedelta(NO2_HMW['time(MEZ)'])

#timeaxis_hours = []
#for i in range(len(NO2_HMW)):
#    timeaxis_hours.append(datetime.strptime(NO2_HMW['time(MEZ)'][i], '%H:%M'))
#print(timeaxis_hours)


#BEST SOLUTION!:
File_dt = File.set_index(pd.to_datetime(File[["year","month","day"]]))
File_dtd = File_dt.drop(columns=[['year','month','day']])

#df[["col1", "col2", "col3"]].apply(pd.to_datetime)

