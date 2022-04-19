from tkinter import *
from tkinter import messagebox

class Application(Frame):
   def __init__(self, master = None):
      Frame.__init__(self, master)
      self.pack()
      self.createWidgets()


   def createWidgets(self):
      #create a button
      self.hiButton = Button(self)
      self.hiButton['text'] = 'Hello \n How are you ?'
      self.hiButton['command'] = self.sayHi
      self.hiButton.pack()

      #create a second button
      self.quitButton = Button(self, text = 'Quit', command = root.destroy, fg = 'red')
      self.quitButton.pack

   def sayHi(self):
      self.dialog = messagebox.showinfo(title = 'Greetings !', message = 'Hey there ! Nice and Sunny Day !')


root = Tk()
root.geometry('300x300')
app = Application(master = root)
app.mainloop()


