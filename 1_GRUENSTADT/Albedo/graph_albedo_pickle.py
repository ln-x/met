# coding=utf-8
__author__ = 'lnx'

import csv
import datetime as dt
import pickle

filename = 'graph_albedo_dict.pickle'

def safenumber(value):
    try:
        num = float(value)
    except ValueError:
        num = 0.0
    return num

class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value

alldata_dict = AutoVivification()

csv_dict = csv.DictReader(open('JHS_Albedo_20111005_20130102.csv'))

for line in csv_dict:  # ab Zeile zwei

    for name in csv_dict.fieldnames[1:]:
        alldata_dict[dt.datetime.strptime(line['datetime'], "%d.%m.%Y %H:%M")][name] = line[name]

with open(filename, 'w') as f:
    pickle.dump(alldata_dict,f)
