from tkinter import *
from tkinter import messagebox

class Application(Frame):
   def __init__(self, master = None):
      Frame.__init__(self, master)
      self.name = StringVar()       #varible for entry widget
      self.gender = StringVar()     #varialble for the radio button
      self.pack()
      self.grid()
      self.showGUI()

   def showGUI(self):
      self.nameLabel = Label(self, text = 'First Name')
      self.nameLabel['bg'] = 'blue'
      self.nameLabel['fg'] = 'white'
      self.nameLabel.grid(row = 1, column = 2)

      self.nameEntry = Entry(self, textvariable = self.name)
      self.nameEntry.grid(row = 1, column = 3)

      self.genderLabel = Label(self, text = 'Gender')
      self.genderLabel.grid(row= 3, column= 2)

      self.radioMale = Radiobutton(self, text = 'M')
      self.radioMale['variable'] = self.gender
      self.radioMale['value'] = 'Male'
      self.radioMale.grid(row= 3, column=3)

      self.radioFemale = Radiobutton(self, text = 'F', variable = self.gender, value= 'Female')
      self.radioFemale.grid(row= 3, column= 4)

      self.buttonDisplay = Button(self, text = 'Display Name')
      self.buttonDisplay['command'] = self.display
      self.buttonDisplay.grid(column= 3, row= 5)


   def display(self):
      myName = self.name.get()
      gender = self.gender.get()

      self.information = messagebox.showinfo(title = 'Details', message = 'Name: ' + myName + '\n' + 'Gender: ' + gender)





root = Tk()
root.title('GUI Application Demo')
root.geometry('300x200')
app = Application(master = root)
app.mainloop()

