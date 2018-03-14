__author__ = 'Heidelinde'

def Can_HW(Wall_o,PBLD):

    #Wall_O_HOR =
    #BDL =

    PCAN_HW_RATI= 0.5 * Wall_o / (1 - PBLD )
    return PCAN_HW_RATI

#building height does not enter!
print (Can_HW(2.1, 0.25))
print (Can_HW(2.1, 0.5))
print (Can_HW(2.1, 0.75))
print (Can_HW(1.1, 0.75))



def Wall_o(PCAN_HW_RATI, PBLD):
    WallO = ((PCAN_HW_RATI*(1-PBLD))/0.5)
    return WallO


