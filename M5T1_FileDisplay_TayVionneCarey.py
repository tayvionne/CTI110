#File Display
#July 8, 2017
#CTI-110 M5T1-File Display
#TayVionne Carey
#

#Open the file
#For each line in the file: Read the line and display it
#Close program

myfile = open('numbers.text', 'r')

#Read and display the files contents.
for line in myfile:
    number = int(line)
    print(number)

#Close the file.
    myfile.close()
