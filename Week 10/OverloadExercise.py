class Student:
   def __init__(self, newId, newName):
      self._id = newId
      self._name = newName

   
   def __eq__(self, another):
      if (self._id == another._id):
         return True
      else:
         return False


   #def hi():
   #   print('Hi!')

   def hi(self, name = None):
      print('Hi! ' + name)

obj1 = Student(1, 'James')
obj2 = Student(1, 'Javier')

'''if (obj1 == obj2):
   print("They are the same")
else:
   print("They are not the same")
'''

obj1.hi()
obj2.hi()