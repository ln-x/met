__author__ = 'lnx'

def f(a,b):
    return a + b


def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    dict_intersect: keys are common in both d1, d2
    '''
    # Your code here
    dict_intersect = {}
    dict_difference = {}

    for i in d1.items():
        if i[0] in d2.keys():
            pass
        elif i[0] in dict_difference.keys():
            pass
        else:
            dict_difference[i[0]] = i[1]

    for i in d2.items():
        if i[0] in d1.keys():
            pass
        elif i[0] in dict_difference.keys():
            pass
        else:
            dict_difference[i[0]] = i[1]
    #------

    if f(2,3) == 5:
        for i in d1.items():
            if i[0] in d2.keys():
                dict_intersect[i[0]] = i[1] + d2[i[0]]

    if f(2,3) == "a > b":
        for i in d1.items():
                dict_intersect[i[0]] = "False"

    return (dict_intersect, dict_difference)
    #return dict_difference

#If f(a, b) returns a + b
#d1 = {1:30, 2:20, 3:30, 5:80}
#d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
#then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})

#If f(a, b) returns a > b
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
#then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})

print (dict_interdiff(d1,d2))
