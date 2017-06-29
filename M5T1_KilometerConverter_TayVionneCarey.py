#Kilometer Converter
#June 29, 2017
#CTI-110 M5T1_KilometerConverter
#TayVionne Carey
#

#The main fucntion gets a distance in kilometers and calls
#the show_miles function to convert it. 
conversion_factor = 0.6214

def main ():
    #Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    #Display the distance converted to miles.
    show_miles(kilometers)

#The show_miles function converts the parameter km from
#kilometers to miles and displayes the result.

def show_miles (km):
    #Calculate miles.
    miles = km * conversion_factor


#Display the miles.
    print(km, 'kilometers equals', miles, 'miles.')

#Call the main function.
main ()
