'''Challenge: A year is a leap year if it is divisible by 4; however, if the year can be evenly divided by 100, it 
is NOT a leap year, unless the year is also evenly divisible by 400 then it is a leap year. Write code that 
asks the user to input a year and output True if it’s a leap year, or False otherwise. Use if statements. '''

year1 = int(input("Enter a random year: "))
year2 = int(input("Enter a random year: "))

def isLeapYear(year):
   if(year % 4 == 0) and (year % 100 != 0):
      print("This is a leap year")
   elif((year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0)):
      print("This is a leap year")
   else:
      print("This is not a leap year")

isLeapYear(year1)
isLeapYear(year2)

