""" The Challenge
Author:
Description: Aling Nena’s Sari-sari store wants a robot that will ask the
customer their total bill and payment amount and tell them their change
(for now, we can allow negative change).
"""

total_bill = input('Please enter total bill:')
payment_amount = input('Please enter payment amount:')
change =  float(payment_amount) - float(total_bill)
print('Your change is {}.'.format(change))
