# Calcualting total with Tip and Tax
# June 9, 2017
# CTI-110 M2HW2 - Tip Tax Total
# TayVionne Carey
#

total_meal = float(input(' Enter total meal cost: '))

#Calculate the tip as 18 percent of total cost.
tip = total_meal * 0.18

#Display the tip.
print(' The tip is $' , format(tip,',.2f'))


total_meal = float(input(' Enter total meal cost: '))

#Calculate the sales tax as 7 percent of total cost.
tax = total_meal * 0.07

#Display the sales tax.
print(' The sales tax is $', format(tax, ',.2f'))
