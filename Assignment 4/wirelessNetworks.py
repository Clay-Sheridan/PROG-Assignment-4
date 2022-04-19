class WirelessNetworks:

   ADHOC_Mode = 'ON'
   BRAND_NAME = 'Cisco'
   
   def greetMessage(self):
      self.drawLine()
      print("Welcome to the company's IoT-Based Health Systemstr\nThese are sensors of " + self.BRAND_NAME + " brand, and the Ad Hoc Mode is " + self.ADHOC_Mode)
      self.drawLine()

   def __init__(self):
      self.id = ''
      self.oxygenLevel = 0
      self.temperature = 0.0
      self.neighbours = 0
      self.distance = ()

   def setID(self, Id):
      self.id = Id

   def setOxygenLevel(self, o2Level):
      self.oxygenLevel = o2Level

   def setTemperature(self, temp):
      self.temperature = temp

   def setNeighbours(self, neighbours):
      self.neighbours = neighbours

   def drawLine(self):
      print('***************************************************************')
