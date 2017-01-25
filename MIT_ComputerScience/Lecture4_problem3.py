__author__ = 'Heidelinde'
#given:
balance = 320000  #the outstanding balance on the credit card
annualInterestRate = 0.2  #annual interest rate as a decimal

monthleyinterestrate = annualInterestRate/12
fixedmonthlypayment_lowerbound = balance/12  #reasonable lower bound
fixedmonthlypayment_upperbound = (balance *(1+monthleyinterestrate)**12)/ 12

low = fixedmonthlypayment_lowerbound
high = fixedmonthlypayment_upperbound
fixedmonthlypayment = (high + low)/2.0

print balance
print low
print high
print fixedmonthlypayment

balance_x = balance

counter = 0
#while abs(balance_x) > 0.01:
while abs(balance_x) > 100:
        #balance_x = balance
        for i in range(12):
            remainingBalance = balance_x - fixedmonthlypayment
            balance_x = remainingBalance + (monthleyinterestrate * remainingBalance)
            print i, balance_x



        print counter, balance_x
        if balance_x < 0:
            high = fixedmonthlypayment
            fixedmonthlypayment = (high + low)/2.0
        else:
            low = fixedmonthlypayment
            fixedmonthlypayment = (high + low)/2.0
        counter +=1
        print fixedmonthlypayment

print ("Lowest Payment: ", fixedmonthlypayment)


###WORKS -

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


fixedmonthlypayment = 0
balance_x = balance
while balance_x > 0:
    fixedmonthlypayment += 1
    balance_x = balance
    for i in range(12):
        remainingBalance = balance_x - fixedmonthlypayment
        balance_x = remainingBalance + (monthleyinterestrate * remainingBalance)
    print balance_x

print ("Lowest Payment: ", fixedmonthlypayment)
