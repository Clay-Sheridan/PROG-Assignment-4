''' Clayton Nelson 991664284'''
# Task 3

example = [5, "hi", 7.9, 12]

def checkInteger(list):

   newList = []
   for i in list:
      if (type(i) != int):
         newList.append(False)
      else:
         newList.append(True)
      
   
   print(newList)

checkInteger(example)



