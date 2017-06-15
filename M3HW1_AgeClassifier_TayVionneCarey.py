#Age Classifier
#June 15, 2017
#CTI-110 M3HW1 -Age Classifier
#TayVionne Carey
#

#Classify based on age input.

age = float(input('Please enter your age'))

#Clarify requirements for age category.

#If you are 1 or younger than 1

if age <= 1:
    print('You are an infant.')

#If you are older than 1 but younger than 13

elif age > 1 and age <13:
    print(' You are a child.')

#If you are at least 13, but younger than 20

elif age >= 13 and age < 20:
    print('You are a teenager.')

#If you are at least 20 or older

elif age>=20 :
        print('You are an adult')

else: 
    print('You are not in any of these categories.')
