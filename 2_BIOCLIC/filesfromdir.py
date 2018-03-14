# coding=utf-8
import os

__author__ = 'hpl'


def listExt(path, ext):
    l = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in [f for f in filenames if f.endswith("." + ext)]:
            l.append(os.path.join(dirpath, filename))
    return l


if __name__ == '__main__':

    path = "/home/lnx/PycharmProjects/Messdatenauswertung/HStest"
    ext = "txt"
    files = listExt(path, ext)
    print files
