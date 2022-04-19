''' Clayton Nelson 991664284'''
# Task 2

def enterPasssword():
   password = input('Enter a new password: ')
   if (len(password) < 6):
      print('Passowrd cannot be less than 6 characters')
      enterPasssword()
   else:
      confirm = input('Confirm your password: ')
      if (password == confirm):
         print('Your new password is: ' + confirm)
      else:
         print('Passwords do not match!')
         enterPasssword()
   
enterPasssword()