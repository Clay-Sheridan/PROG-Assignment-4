'''Challenge: Write a code that asks user to input a numeric score (0-100). In response, 
it should print out the score and corresponding letter grade, accodring to table'''

score = float(input("Enter a numeric score (0-100): "))


#resp = score + " "

if score >= 90:
   output = str(score) + " A"
elif score >= 80:
   output = str(score) + " B"
elif score >= 70:
   output = str(score) + " C"
elif score >= 60:
   output = str(score) + " D"
else:
   output = str(score) + " F"

print(output)