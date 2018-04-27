def loadfile1(filename):
    with open(filename,"r") as f:    #Einlesen des Files in eine Liste
        alldata = f.readlines()
        #print len(alldata)
        #print type(alldata)

    data = alldata[27:-24]  #Liste ab [7:]8.Zeile der alten Liste - Beginn der Rohdaten

    splitdata = []       #splitlistcomp = [i.split() for i in data]
    for i in data:
        splitdata.append(i.split())
    print splitdata

    value = 0
    converted = []
    for i in splitdata:
        for j in i:
            #print j
            value = (float(j[:12]) - 273.15)
            #print value
            converted.append(value)
    #print converted
    return converted



def loadfile2(filename):
    with open(filename,"r") as f:    #Einlesen des Files in eine Liste
        alldata = f.readlines()
        #print len(alldata)
        #print type(alldata)

    data = alldata[27:-13]  #Liste ab [7:]8.Zeile der alten Liste - Beginn der Rohdaten

    splitdata = []       #splitlistcomp = [i.split() for i in data]
    for i in data:
        splitdata.append(i.split())
    #print splitdata

    value = 0
    converted = []
    for i in splitdata:
        for j in i:
            #print j
            value = (float(j[:12]) - 273.15)
            #print value
            converted.append(value)
    #print converted
    return converted

def loadfile3(filename):
        with open(filename, "r") as f:  # Einlesen des Files in eine Liste
            alldata = f.readlines()
            # print len(alldata)
            # print type(alldata)

        data = alldata[18:-33]  # Liste ab [7:]8.Zeile der alten Liste - Beginn der Rohdaten

        splitdata = []  # splitlistcomp = [i.split() for i in data]
        for i in data:
            splitdata.append(i.split())
        # print splitdata

        value = 0
        converted = []
        for i in splitdata:
            for j in i:
                # print j
                value = (float(j[:11]) - 273.15)
                # print value
                converted.append(value)
        # print converted
        return converted

        #loadfile(filename)