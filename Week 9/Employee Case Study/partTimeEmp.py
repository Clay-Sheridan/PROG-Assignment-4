from employee import Employee

class PartTimeEmp(Employee):
   def __init__(self):
      self._hourlyWage = 0.0
      self._biWeeklyHours = 0.0
      self._pay = 0.0


   def calculatePay(self):
      self._pay = self._biWeeklyHours * self._hourlyWage
      return self._pay


   def toString(self):
      self.calculatePay()
      return(super().toString() + "    " + " Hourly Wage: " + str(self._hourlyWage) + "  Bi-Weekly Hours Pay: " + str(self.calculatePay()))


   
   