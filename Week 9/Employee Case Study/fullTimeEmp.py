from employee import Employee

class FullTimeEmp(Employee):
   def __init__(self):
      self._annualPay = 0.0
      self._unpaidLeaveDays = 0.0
      self._pay = 0.0

   
   def calculatePay(self):
      paymentPerDay = self._annualPay / 365
      self._pay = (self._annualPay / 26) - (self._unpaidLeaveDays * paymentPerDay)
      return self._pay

   def toString(self):
      self.calculatePay()
      return super().toString() + "    " + " Annual Pay: " + str(self._annualPay) + " Unpaid Leave Days: " + str(self._unpaidLeaveDays)


