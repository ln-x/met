__author__ = 'Heidelinde'
#given:
#balance = 999999  #the outstanding balance on the credit card
#annualInterestRate = 0.18  #annual interest rate as a decimal

balance = 320000
annualInterestRate = 0.2

monthleyinterestrate = annualInterestRate/12
fixedmonthlypayment_lowerbound = balance/12  #reasonable lower bound
fixedmonthlypayment_upperbound = (balance *(1+monthleyinterestrate)**12)/ 12

low = fixedmonthlypayment_lowerbound
high = fixedmonthlypayment_upperbound
fixedmonthlypayment = (high + low)/2.0

print high, low, fixedmonthlypayment

new_balance = balance
counter = 0
keep_going = True
while counter < 100:
#while keep_going == True:
    #print balance_x
    new_balance = balance
    counter += 1
    print counter
    for i in range(12):
            #print i, new_balance
            remainingBalance = new_balance - fixedmonthlypayment
            new_balance = remainingBalance + (monthleyinterestrate * remainingBalance)
    if new_balance > 0.01:
        print "payed not enough"
        low = fixedmonthlypayment
        fixedmonthlypayment = (high + low)/2.0

    elif new_balance < 0.01:
        print "payed too much"
        high = fixedmonthlypayment
        fixedmonthlypayment = (high + low)/2.0
        print "elif - balance_x", fixedmonthlypayment, new_balance
    else:
        fixedmonthleypayment = round(fixedmonthlypayment,2)
        print ("Lowest Payment: ", fixedmonthlypayment)
        print "else - balance_x", new_balance
        keep_going = False

fixedmonthlypayment = round(fixedmonthlypayment,2)
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