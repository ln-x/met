__author__ = 'Heidelinde'
#given:
balance = 3926  #the outstanding balance on the credit card
annualInterestRate = 0.2  #annual interest rate as a decimal

monthleyinterestrate = annualInterestRate/12

fixedmonthlypayment = 0
balance_x = balance
while balance_x > 0:
    fixedmonthlypayment += 10
    balance_x = balance
    for i in range(12):
        remainingBalance = balance_x - fixedmonthlypayment
        balance_x = remainingBalance + (monthleyinterestrate * remainingBalance)
        print balance_x

print ("Lowest Payment: ", fixedmonthlypayment)

