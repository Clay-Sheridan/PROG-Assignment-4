import math

class Athletes:
   KILOGRAM_PER_POUND = 0.453592
   METERS_PER_INCH = 0.0254

   def __init__(self):
      self._firstName = ''
      self._lastName = ''
      self._weight = 0
      self._height = 0
      self._bmi = math.inf
      self._condition = ''

   def run(self):
      newFirstName = input("Enter the first name of Athlete")
      newLastName = input("Enter the last name of the Athlete")

      self.setFirstName(newFirstName)
      self.setLastname(newLastName)

      weight = float(input("Enter the weight in pounds: "))
      height = float(input("Enter the height in inches: "))

      self.computeBmi(self, weight, height)

   def computeBmi(self, weight, height):
      self._weight = weight * self.KILOGRAM_PER_POUND
      self._height = height * self.METERS_PER_INCH
      self._bmi = self._weight / (math.pow(self._height, 2))

      if (18.5 < self._bmi):
         self._condition = 'underweight'

   
   def setFirstName(self, fName):
      self._firstname = fName

   def getFirstname(self):
      return self._firstName

   def setLastname(self, lName):
      self._lastname = lName

   def getLastname(self):
      return self._lastName

   def setHeight(self, newHeight):
      self._height = newHeight

   def setWeight(self, newWeight):
      self._weight = newWeight

  # def __str__(self):
     # return "Last Name: {0}, First Name: {1}, Weight: {2}, Height: {3}, and BMI: {4}".format(self.getLastname(), self.getFirstname(), )

   