from athletes import Athletes

class Olympics:
   def __init__(self):
      self._location = ''
      self._year = 0
      self._listOfAthletes = []

   def run(self):
      location = input("Enter the location of the event: ")
      self.setLoctaion(location) # Reminder: create mutator method

      year = int(input("Enter the year for this event: "))
      self.setYear(year) # Reminder


      '''This is to create list of Athletes'''

      numOfAthlete = int(input("Enter the number of athletes: "))
      for athlete in numOfAthlete:
         athlete = Athletes()
         athlete.run()
         self._listOfAthletes.append(athlete)
         print(self._listOfAthletes)

   def setLoctaion(self, location):
         self._location = location
         
   def getLocation(self):
         return self._location

   def setYear(self):
      pass

   def getYear(self):
      pass