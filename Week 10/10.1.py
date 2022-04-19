class Application:
   def printInfo(self, name, age = 18):
      '''This is passed information.
         Uses default argument age = 18
      '''

      # age = 19
      print('Name: ', name)
      print('Age: ', age)

   # variable lngth arguments
   def sum(sel, *numbers):
      sum = 0.0
      for value in numbers:
         sum += value
      return sum

   @staticmethod
   def printInfo():
      print('***Welcome to the System!***')

program = Application()
# program.printInfo(name = 'KNJM', age = 20)
# print(program.sum(1, 2, 3))
Application.printInfo()