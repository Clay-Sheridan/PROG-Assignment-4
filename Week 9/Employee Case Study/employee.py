from person import Person

class Employee(Person):
   def __init__(self):
      self._empID = 'none'
      self._dept = 'none'




   def toString(self):
      return super().toString() + "    " + " Employee ID: " + str(self._empID) + "  Department: " + str(self._dept)
      