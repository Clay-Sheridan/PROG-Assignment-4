'''Write code to assign the string "You can apply to SI!" to an output variable
if the string "SI106" is in the list of courses. If its not in the list,
assign the value "Take the course" to the variable'''

 
courses = ["ENG 100", "PROG1004", "SI106", "INFO103"]


if "SI106" in courses:
   output = "You can apply to SI!"
else:
   output = "Take SI106"

print(output)