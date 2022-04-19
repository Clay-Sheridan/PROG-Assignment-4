'''
Week 8 
March 8 2022
'''

class Cars:
   #These are the class variables
   rimSize = 18
   numOfTires = 4

   def __init__(self, make, numDoors, operation,):
      # These are instance variables
      self._make = make
      self._numDoors = numDoors
      self._operation = operation
      self._custRimSize = self.rimSize + 3

   def switchOff(self):
      #self._make = ''
      if self._operation == 'ON':
         self._operation = 'OFF'

   def __str__(self):
       return "Make: {0},\nNumber of Doors: {1},\nOperation: {2}".format(self._make, self._numDoors, self._operation)
   

car1 = Cars('Honda', 4, 'ON')
car1.switchOff()
print(car1)
print(car1.rimSize)

car2 = Cars('Toyota', 2, 'OFF')
print(car2)
print(car2.rimSize)