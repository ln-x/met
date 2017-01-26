__author__ = 'Heidelinde'
#given:
balance = 999999  #the outstanding balance on the credit card
annualInterestRate = 0.18  #annual interest rate as a decimal

monthleyinterestrate = annualInterestRate/12
fixedmonthlypayment_lowerbound = balance/12  #reasonable lower bound
fixedmonthlypayment_upperbound = (balance *(1+monthleyinterestrate)**12)/ 12

low = fixedmonthlypayment_lowerbound
high = fixedmonthlypayment_upperbound
fixedmonthlypayment = (high + low)/2.0

print fixedmonthlypayment

balance_x = balance
counter = 0
while counter < 100:
    print balance_x
    counter += 1
    print counter
    if balance_x > 0.01:
        print "if - balance_x", balance_x, fixedmonthlypayment
        high = fixedmonthlypayment
        fixedmonthlypayment = (high + low)/2.0
        balance_x = balance
        for i in range(12):
            remainingBalance = balance_x - fixedmonthlypayment
            balance_x = remainingBalance + (monthleyinterestrate * remainingBalance)
    elif balance_x < 0.01:
        print "elif - balance_x", balance_x, fixedmonthlypayment
        balance_x = balance
        low = fixedmonthlypayment
        fixedmonthlypayment = (high + low)/2.0
        for i in range(12):
            remainingBalance = balance_x - fixedmonthlypayment
            balance_x = remainingBalance + (monthleyinterestrate * remainingBalance)
    else:
        print "else - balance_x", balance_x
        fixedmonthleypayment = round(fixedmonthlypayment,2)
        print ("Lowest Payment: ", fixedmonthlypayment)
        break


print ("Lowest Payment: ", fixedmonthlypayment)

"""

    if balance_x < 0.01:
        print "if - balance_x", balance_x, fixedmonthlypayment
      high = fixedmonthlypayment
        fixedmonthlypayment = (high + low)/2.0  balance_x = balance

        for i in range(12):
            remainingBalance = balance_x - fixedmonthlypayment
            balance_x = remainingBalance + (monthleyinterestrate * remainingBalance)
    elif balance_x > 0.01:
        print "elif - balance_x", balance_x, fixedmonthlypayment
        balance_x = balance
        low = fixedmonthlypayment
        fixedmonthlypayment = (high + low)/2.0
        for i in range(12):
            remainingBalance = balance_x - fixedmonthlypayment
            balance_x = remainingBalance + (monthleyinterestrate * remainingBalance)
    else:
        print "else - balance_x", balance_x
        fixedmonthleypayment = round(fixedmonthlypayment,2)
        print ("Lowest Payment: ", fixedmonthlypayment)

"""


"""
Test Case 1:
      balance = 320000
      annualInterestRate = 0.2

      Result Your Code Should Generate:
	      -------------------
     Lowest Payment: 29157.09 (i get 29591.5477987)
"""

"""
     Test Case 2:
     balance = 999999
     annualInterestRate = 0.18

     Result Your Code Should Generate:
     -------------------
     Lowest Payment: 90325.03 (i get 91483.87)
"""