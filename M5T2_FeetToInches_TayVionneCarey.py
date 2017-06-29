#Feet to Inches
#June 29, 2017
#CTI-110 M5T2_FeetToInches
#TayVionne Carey
#

#Constance for the number of inches per foot.
inches_per_foot = 12

#main function
def main ():
    #Get number of feet from user.
    feet = int(input('Enter a number of feet: '))

    #Convert that to inches.
    print(feet, 'equals', feet_to_inches(feet), 'inches.')
    
#The feet_to_inches function coverts feet to inches.
def feet_to_inches(feet):
    return feet * inches_per_foot

# Call the main function.
main ()

