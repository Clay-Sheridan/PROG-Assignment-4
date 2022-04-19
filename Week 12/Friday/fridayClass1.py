'''
fileRef = open('olympics.txt', 'r')
lines = fileRef.readlines()
print(lines)
fileRef.close()
'''

#fileRef = open('school_prompt2.txt', 'r')
#numChar = len(fileRef.read())
#print(numChar)

'''
fileRef2 = open('travel_plans2.txt', 'r')
numLines = len(fileRef2.readlines())
print(numLines)
'''

#Create a string called firstForty that is comprised of the first 40 characters of emotion_words2.txt
'''
fileRef = open('emotion_words2.txt', 'r')
firstForty = fileRef.read(40)
print(firstForty)
'''

#fileRef = open('olympics.txt', 'r')
#for line in fileRef.readlines():
#   values = line.split(',')
#   print(values[0] + ' from ' + values[3] + ' is competing in the ' + values[4] + ' event')
#fileRef.close()

'''
fileRef = open('test1.txt', 'w')
for index in range(16):
   fileRef.write(str(index) + '\n')
fileRef.close()
'''

#Create a file called squared_numbers1.txt that
'''
fileRef = open('squared_numbers.txt', 'w')
for index in range(1, 13):
   fileRef.write(str(index * index) + '\n')
fileRef.close()
'''
'''
fileRef = open('subfolder/olympics1.txt', 'r')
lines = fileRef.readlines()
#print(lines)
fieldnames = lines[0].strip().split(',')
print(fieldnames)

for line in lines[1:]:
   values = line.strip().split(',')
   if values[5] != 'NA':
      print('{}: {}; {}'.format(values[0], values[4], values[5]))
   

fileRef.close()
'''

#Write the three fields on the file named reduced_olympics.csv which are Name, Age, Sport and also write all these values in the file
olympians = [("John Aalberg", 31, "Cross Country Skiing"), ("Minna Maarit Aalto", 30, "Sailing"), ("Win Valdemar", 54, "Art Competitions"), ("Wakako Abe", 18, "Cycling")]

fileRef = open('reduced_olympics.csv', 'a')
for olympian in olympians:
   fileRef.write('Name: {}, Age: {}, Sport: {}'.format(olympian[0], olympian[1], olympian[2]) + '\n')
fileRef.close()

