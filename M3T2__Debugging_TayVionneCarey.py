#Debugging
#June 17, 2017
#CTI-110 M3T2 - Debugging
#TayVionne Carey
#


#Determine grading variables

A_score = 90
B_score = 80
C_score = 70
D_score = 60
F_score = 50

#Prompt for grade input
score = int(input('Enter your test score:'))

#Determine the grade

if score >= A_score:
    print('Your grade is A.')

elif score >= B_score:
       print('Your grade is B.')

elif score >= C_score:
        print ('Your grade is C.')

elif score >= D_score:
       print('Your grade is D.')

else: 
    print('Your grade is F.')
          

