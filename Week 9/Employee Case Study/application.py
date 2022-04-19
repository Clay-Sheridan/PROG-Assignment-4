from partTimeEmp import PartTimeEmp
from fullTimeEmp import FullTimeEmp


class Application:
   def run(self):
      ptemp = PartTimeEmp()
      ptemp._name = 'Clay Nelson'
      ptemp._address = 'Toronto'
      ptemp._empID = 'F101'
      ptemp._dept = 'FAST'
      ptemp._hourlyWage = 50
      ptemp._biWeeklyHours = 88
      print(ptemp.toString())

   def run(self):
      ftemp = FullTimeEmp()
      ftemp._name = 'Andrew Nelson' 
      ftemp._address = 'Burligton'
      ftemp._empID = 322271966
      ftemp._dept = 'Management'
      ftemp._annualPay = 45000
      ftemp._unpaidLeaveDays = 10
      print(ftemp.toString())







app = Application()
app.run()