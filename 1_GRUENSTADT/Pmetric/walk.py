import os
path = "/home"

def enumeratepath(path=path):
    path_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            path_collection.append(fullpath)
    return path_collection

def enumeratefiles(path=path):
    file_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_collection.append(file)
    return file_collection

def enumeratedir(path=path):
    dir_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for dir in dirnames:
                dir_collection.append(dir)
    return dir_collection

if __name__ == "__main__":
    print "\nRecursive listing of all path in dir:"
    for path in enumeratepath():
        print path
    print "\nRecursive listing of all files in dir:"
    for file in enumeratefiles():
        print file
    print "\nRecursive listing of all dirs in dir:"
    for dir in enumeratedir():
        print dir
    