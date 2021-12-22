

from datetime import datetime

start = datetime(2019,7,11,0,0,0)

min_millisecond = 26626099
min_hour = min_millisecond/(1000*60*60)
max_millisecond = 44675401
max_hour = max_millisecond/(1000*60*60)

print(min_hour, max_hour)

#Koehler et al. 2018: LST span 11:30 - 18:15 LST

#delta_time(n_elem);
#delta_time: units = "milliseconds since 2019-07-11 00:00:00";
#delta_time: standard_name = "delta time";
#delta_time: comment = "Time difference with time for each measurement";
#delta_time: long_name = "offset from the reference start time of measurement";
