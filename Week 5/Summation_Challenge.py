'Summation Task'


def sumTo(n):
   sum = 0
   index = 1
   
   while n >= index:
       sum += index
       index += 1
   print(sum)   

sumTo(6)