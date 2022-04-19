'''
Mon Mar 7 2022
Week 8
Analysis of Algo's
'''
import random

array = []
numCount = int(random.random() * 10)
print(numCount)
for i in range(numCount + 1):
   array.append(i)
print(array)

def reverse(array):
   revArr = []
   revArr[0] = array[::]
