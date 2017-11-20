__author__ = 'Heidelinde'

balance = 5000  #the outstanding balance on the credit card
annualInterestRate = 0.18  #annual interest rate as a decimal
monthleyinterestrate = annualInterestRate/12

monthlyPaymentRate = 0.02 #minimum monthly payment rate as a decimal



for i in range(12):
    #print i
    #print balance
    monthlyPayment = balance* monthlyPaymentRate
    remainingBalance = balance - monthlyPayment
    balance = remainingBalance + (monthleyinterestrate * remainingBalance)


#balance = (round(balance*100))/100
balance = round(balance,2)

print (balance)

#print ('Remaining balance: {:07.2f}').format(balance)
#print ('Remaining balance: {:06.1f}').format(balance)



#print ("Layername = {0} with {1:d} features(Objekten) und {1:d} fields (Attributen)").format(layerx1.name(),layerx1.featureCount(),layerx1.fields())

#AttributeError: 'NoneType' object has no attribute 'format'

#*** ERROR: Expected to find a number in the line AttributeError: 'NoneType' object has no attribute 'format'
#. ***