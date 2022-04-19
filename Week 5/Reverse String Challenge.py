'''reverse string challenge'''

from types import MethodWrapperType


string = input('enter your message: ')

str_list = list(string)
str_list_reverse = list(string)

print('Original Message:' + string)

reverseIndex = len(string) - 1

newString = ''

for index in range(len(string)):
   str_list[index] = str_list_reverse[reverseIndex]
   reverseIndex = reverseIndex - 1
   newString = newString + str_list[index]
print('Reversed Message:' + newString)

