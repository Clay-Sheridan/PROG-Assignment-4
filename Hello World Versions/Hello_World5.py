#Hello World V5
class HelloMessage:
   def show(self):
      helloMsg = 'Hello Programming World'
      print(helloMsg)
      courseMsg = 'Programming Principles with Python'
      print(courseMsg)
      courseNo = 10004
      print('#PROG', courseNo, sep='')

msg = HelloMessage()
msg.show()