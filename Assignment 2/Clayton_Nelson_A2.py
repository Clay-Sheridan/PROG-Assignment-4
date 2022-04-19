'''Write a Python program that places senor nodes at fixed two-dimensional positions (i.e., this
position should be randomly assigned in an area of 100 m * 100 m). Afterword, every day you
will collect one reading measured in Part Per Million (PPM). Assume the range for readings is
between 20 PPM and 50 PPM (i.e., all those readings are assumed to be whole integers). You
want to take measurements for several days. The program should compute the averaged
reading(s) for each sensor based on one or more days. You must follow the output below exactly
as this is the user requirements:'''


import random

def randomPosition():   # determines a random location for each sensor placed
   position = []                          # list containing x and y position values
   x = round(random.random() * 100, 2)    # calculates random number from 1-100, rounded to 2 decimal places
   y = round(random.random() * 100, 2)
   position.append(x)                     # add value x and y to list
   position.append(y)                     
   return(position)                       # returns coordinate


def averageCO2():    # calculate average CO2 based on input readings
   days = int(input('Enter the number of days for the readings: '))     # variable for number of rading days
   values = []    # list containing values of readings
   for i in range(1, days + 1):     # set range starting from 1, becasue readings start from day 1. Add 1 to end of range because range will not inclue (inputted variable) itself
      values.append(input('Enter the CO2 for day ' + str(i) + ': '))    # insert inputted reading values to list
   sumOfValues = 0      # represents sum of reading values (starts at 0)
   for j in values:     # for every value in values list..
      sumOfValues = sumOfValues + int(j)     # add value being iterated over to sumOfValues variable, updating it with each iteration
   average = round(float(sumOfValues / days), 2)      # divide sumOfValues by amount of days, convert to float data type, and round to 2 decimal places
   print('Rounded Average Readings: ' + str(average) + ' PPM')    # print statement displaying average readings


def toContinue():    # asks user if they want to continue 
   response = input('Would you like to continue?: (Y)es or (N)o: ').lower()      # .lower() function helps accept all variations of capitalization (yes, Yes, yEs, nO, etc..) 
   if (response == 'yes' or response == 'y'):      # if user says yes or y, re run program from start
      run()
   elif (response == 'no' or response == 'n'):     # if user says no or n, 'exit' statement prints and program is finished running
      print('Exiting Program....')
   else:
      print('Incorrect entry! Please try again')   # if user fails to type valid response, 'incorrect' statement prints  
      toContinue()                                 # recall function to give user another chance to type valid response

   
      
def run():     # main function that initiates program
   try:  
      totalSensors = int(input('Enter the number of sensors deployed across Sheridan Campus: '))      # opening prmopt
   except ValueError:      # if a string is entered rather than an integer, asks user to try again rather than crashing entire program
      print('Incorrect entry! Please try again')
      run()    # restart program
   numberOfPrompts = []                            # list of values that represent number of times user is going to be promtpted
   for i in range(1, (totalSensors) + 1):          # set the range starting from 1 --> (totalSensors variable) and added 1 at the end since range will not include inputted vairable itself
      numberOfPrompts.append(i)                    # insert all values from range into list
   if (totalSensors < 1 or totalSensors == ''):    # forces user to input an integer greater than 0
      print('Must have at least 1 sensor!')
      run()                                        # restarts program
   else:
      for i in numberOfPrompts:     # for every value in the list...
         print('This is for sensor ' + str(i) + ' at position ' + str(randomPosition()))     # tells user which sensor is being evaluated at random generated coordinate
         averageCO2()      # call averageCO2 function to calculate average CO2 level
      toContinue()         # call toContinue funtion, asking user if they want to contiune
   
     

run()