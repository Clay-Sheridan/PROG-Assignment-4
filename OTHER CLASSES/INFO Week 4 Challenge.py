'''Write and test a python prgram that, given the number of bits, outputs the equivalent
number of kilobytes and megabytes.'''

bytes = int(input("Enter number of bytes: "))

kilobytes = bytes / (2 ** 10) 
megabytes = bytes / (2 ** 20)

print(str(bytes) + ' = ' + str(kilobytes) + 'Kb, and ', str(megabytes) + 'Mb')