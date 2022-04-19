class Person:
   def __init__(self, name, address):
      self._name = name
      self._address = address

   
   def toString(self):
      return 'Name: ' + self._name + '  Address: ' + self._address