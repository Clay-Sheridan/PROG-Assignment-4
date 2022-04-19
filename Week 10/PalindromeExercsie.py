
def isPalindrome(first, second, testStr):
   firstElement = first
   secondElement = second

   if (firstElement >= secondElement):
      return True
   elif (testStr[firstElement] != testStr[secondElement]):
      return False
   else:
      firstElement += 1
      secondElement -= 1
      return (isPalindrome(firstElement, secondElement, testStr))

myString = 'noon'
firstElement = 0
secondElement = len(myString) - 1

print(isPalindrome(firstElement, secondElement, myString))
