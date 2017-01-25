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

#print balance
#print low
#print high
#print fixedmonthlypayment

balance_x = balance
counter = 0

for i in range(1000):
    if balance_x < 0.01:
        print "if - balance_x", balance_x, fixedmonthlypayment
        balance_x = balance
        high = (balance_x *(1+monthleyinterestrate)**12)/ 12
        fixedmonthlypayment = (high + low)/2.0
        for i in range(12):
            remainingBalance = balance_x - fixedmonthlypayment
            balance_x = remainingBalance + (monthleyinterestrate * remainingBalance)
    elif balance_x > 0.01:
        print "elif - balance_x", balance_x, fixedmonthlypayment
        balance_x = balance
        low = balance_x/12
        fixedmonthlypayment = (high + low)/2.0
        for i in range(12):
            remainingBalance = balance_x - fixedmonthlypayment
            balance_x = remainingBalance + (monthleyinterestrate * remainingBalance)
    else:
        print "else - balance_x", balance_x
        fixedmonthleypayment = round(fixedmonthlypayment,2)
        print ("Lowest Payment: ", fixedmonthlypayment)


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