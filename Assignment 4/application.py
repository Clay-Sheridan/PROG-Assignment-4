from wirelessNetworks import WirelessNetworks

class Application:
   def __init__(self):
      self.listSensors = []
      self.totalSensors = 0
      self.sensorDict = {}


      network = WirelessNetworks()
      network.greetMessage()


      self.createSensors()
   

   def createSensors(self): # creates each sensor along with prompts for sensor info
      while True:
         try:
            numOfSensors = int(input("Enter the number of sensors: "))
            break
         except:
            print("This is an invalid entry for the number of sensors")
      self.setTotalSensors(numOfSensors)

      self.drawLine() # separates blocks of lines in output

      for sensor in range(1, self.totalSensors + 1): # creation of sensors based on variable
         sensor = WirelessNetworks()

         # prompts user for 
         id = (input('Enter the sensor ID: ')) 
         while any(char.isnumeric() for char in id): # loops through input serching for numeric characters
            print("This is an invalid entry for the sensor ID!")
            self.drawLine()
            id = input('Enter the sensor ID: ')
         sensor.setID(id) # sets sensor object's ID to variable
         
         # this prompts user for number of neighbouring sensors as an integer value
         while True:
            try:
               numOfNeighbours = int(input("Enter the number of neighbours: "))
               break
            except:
               print("This is an invalid entry for the number of neighbours!")
         sensor.setNeighbours(numOfNeighbours)

         for neighbour in range(1, sensor.neighbours + 1):
            neighbour = WirelessNetworks()

            neighbourId = input("Enter the neighbour for sensor " + sensor.id + ": ")
            while any(char.isalpha() == False for char in neighbourId):
               print("This is an invalid entry for the neighbour's name and/or distance!")
               neighbourId = input("Enter the neighbour for sensor " + sensor.id + ": ")
            neighbour.setID(neighbourId)
         
            self.convertToDict(sensor, neighbour)

         while True:
            try:
               o2Level = int(input("Enter the Oxygen level in %: "))
               break
            except:
               print("This is an invalid entry for the oxygen level!")
         sensor.setOxygenLevel(o2Level)

         while True:
            try:
               temp = float(input("Enter the temperature measurement: "))
               break
            except:
               print("This is an invalid entry for the temperature!")
         sensor.setTemperature(temp)

         self.listSensors.append(sensor)
         self.drawLine()

      self.findPath()
         




   def convertToDict(self, sensor, neighbour):
      dist = (neighbour.id, int(input("Enter the distance (m) to " + sensor.id + ": ")))
      if sensor.id not in self.sensorDict:
         self.sensorDict[sensor.id] = [dist]
      else:
         self.sensorDict[sensor.id].append(dist)
     


   def findPath(self):
      source = input("Enter the source sensor: ")
      path = [source]
      dest = input("Enter the destination sensor: ")
      pathList = self.sensorDict[source]
      firstPath = pathList[0]
      for id, distance in pathList:
         if distance > firstPath[1]:
            firstPath = (id, distance)
      path.append(firstPath[0])
      self.findPathHelper(firstPath[0], dest, path)
      print("Path = " + str(path))



   def findPathHelper(self, source, dest, path):
      if source == dest:
         return True
      newPathList = self.sensorDict[source]
      newPathList.pop(0)
      if len(newPathList) == 0:
         print("The destination is not found")
      else:
         newPathList.sort(key=lambda x:x[1])
         newFurthestPath = max(newPathList)
         path.append(newFurthestPath[0])
         return(self.findPathHelper(newFurthestPath[0], dest, path))



   def setTotalSensors(self, sensorCount):
      self.totalSensors = sensorCount


   def drawLine(self):
      print('_*__*__*__*__*__*__*__*__*__*__*_')


app = Application()