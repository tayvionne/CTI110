#Bug Collector
#June 17,2017
#CTI-110 M4T1 - Bug Collector
#TayVionne Carey
#

#Pseudo code
#Set total = 0
#For each of 5 days: Input bugs collected for a day, Add bugs collected to total
#Display total

#Initialize the accumulator.
total = 0

#Get the bugs collected for each day.

for day in range(1, 6):
    #Prompt the user.

    print('Enter the bugs collected on day', day)
    #Input the number of bugs.
    bugs = int(input())
    #Add bugs to total
    total = total + bugs

#Display the total bugs.
    print('You collected a total of', total, 'bugs.')

