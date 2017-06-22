#Sum of Numbers
#June 22, 2017
#CTI-110 M4HW1 - Sum of Numbers
#TayVionne Carey
#

#Initialize an accumulator variable.

total = 0.0
number = 1.0

#Get the numbers and accumulate them.
while number > 0:
  number = int(input('Enter a postive number: '))
  total = total + number
if number > 0:
    total = total + number

#Display total.
    
print('Total is', total)
