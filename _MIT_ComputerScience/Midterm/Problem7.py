__author__ = 'lnx'

def f(a,b):
    #return a + b
    return a > b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    dict_intersect: keys are common in both d1, d2
    '''
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

    for i in d1.items():
            if i[0] in d2.keys():
                a = i[1]
                #print (i, i[0], i[1], d2[i[0]])
                b = d2[i[0]]
                #print (i, a,b)
                dict_intersect[i[0]] = f(a,b)


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
#print (dict_interdiff({}, {}))  #({}, {})
#print (dict_interdiff({1: 1}, {1: 1}))  #({1: True}, {})
#print (dict_interdiff({1: 2}, {2: 1}) ) #({}, {1: 2, 2: 1})
print (dict_interdiff({0: 0, 2: 5, 5: 2}, {0: 0, 2: 5})) #({0: 0, 2: 10}, {5: 2})
print (dict_interdiff({1: 1, 2: 2, 3: 3}, {1: 1, 2: 2, 3: 3})) #({1: 2, 2: 4, 3: 6}, {})
print (dict_interdiff({1: 1, 2: 2, 3: 3}, {1: 1, 2: 2, 3: 3})) #({1: 0, 2: 0, 3: 0}, {})
print (dict_interdiff({1: 1, 2: 2, 3: 3, 4: 4, 5: 4}, {1: 1, 2: 2, 3: 3, 4: 5})) #({1: False, 2: False, 3: False, 4: True}, {5: 4})
print (dict_interdiff({1: 1, 2: 2, 3: 3, 4: 4}, {1: 1, 2: 2, 3: 3, 4: 5, 6: 2})) #({1: False, 2: False, 3: False, 4: True}, {6: 2})
print (dict_interdiff({1: 0, 2: 1, 3: 2, 4: 3, 5: 0}, {1: 1, 2: 2, 3: 3, 4: 5, 6: 2})) #({1: True, 2: True, 3: True, 4: True}, {5: 0, 6: 2})
print (dict_interdiff({1: 1, 2: 0, 3: 0, 4: 0, 6: 0, 7: 0}, {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0})) #({1: 0, 2: 0, 3: 0, 4: 0}, {0: 1, 5: 0, 6: 0, 7: 0})
print (dict_interdiff({1: 1, 2: 2, 3: 3, 4: 5, 8: 4, 10: 0}, {9: 1, 5: 3, 6: 3, 7: 4})) #({}, {1: 1, 2: 2, 3: 3, 4: 5, 5: 3, 6: 3, 7: 4, 8: 4, 9: 1, 10: 0})
print (dict_interdiff({9: 1, 5: 3, 6: 3, 7: 4}, {1: 1, 2: 2, 3: 3, 4: 5, 8: 4, 10: 0})) #({}, {1: 1, 2: 2, 3: 3, 4: 5, 5: 3, 6: 3, 7: 4, 8: 4, 9: 1, 10: 0})
print (dict_interdiff({9: 1, 4: 4, 5: 3, 6: 3}, {1: 1, 2: 2, 3: 3, 4: 5, 8: 4, 10: 0})) #({4: 9}, {1: 1, 2: 2, 3: 3, 5: 3, 6: 3, 8: 4, 9: 1, 10: 0})
print (dict_interdiff({4: 4, 5: 3, 6: 3, 8: 4, 9: 1, 10: 0}, {1: 1, 2: 2, 3: 3, 4: 5})) #({4: 9}, {1: 1, 2: 2, 3: 3, 5: 3, 6: 3, 8: 4, 9: 1, 10: 0})