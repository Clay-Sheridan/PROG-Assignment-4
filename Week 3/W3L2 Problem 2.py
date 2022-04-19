'''Wrtie a program the checks averae weight of luggage'''

total_weight = int(input('Enter total weight of luggage (lbs): '))
num_of_pieces = int(input('Enter number of luggage pieces: '))

average_weight = total_weight / num_of_pieces

if (average_weight >= 100):
   print("You will need to pay $100 surcharge")

elif (average_weight >= 50):
   print("You will need to pay $50 surcharge")

else: 
   print('No charges!')