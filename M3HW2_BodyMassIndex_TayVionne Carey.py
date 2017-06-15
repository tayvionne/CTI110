#Body Mass Index
#June 15, 2017
#CTI-110 M3HW2- Body Mass Index
#TayVionne Carey
#


#Get weight and height.

weight = float(input('What is your weight in pounds?'))
height = float(input('What is your height in inches?'))

#Calculate BMI

BMI = (weight *703) /height**2
print('Your body mass index is', BMI)

if BMI >= 18.5 and BMI <= 25:
    print('You are optimal weight.')

elif BMI < 18.5:
    print('You are underweight.')

elif BMI > 25:
    print('You are overweight.')


