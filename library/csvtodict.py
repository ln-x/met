# coding=utf-8
__author__ = 'lnx'

import csv
import datetime as dt
import pickle

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

def CsvToDict(csv_filename, datetimeformat):

    alldata_dict = AutoVivification()
    csv_dict = csv.DictReader(open(csv_filename, "rU"))

    print csv_dict.fieldnames
    for line in csv_dict:  # ab Zeile zwei

        for name in csv_dict.fieldnames[1:]:
            alldata_dict[dt.datetime.strptime(line['datetime'],datetimeformat)][name] = line[name]




    return alldata_dict


if __name__ == '__main__':

    filename = '/home/lnx/PycharmProjects/Messdatenauswertung/Albedo/JHS_Albedo_20111005_20130102.csv'
    print 'Länge der Daten'
    print len(CsvToDict(filename, "%d.%m.%Y %H:%M"))