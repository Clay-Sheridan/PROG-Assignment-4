'''Rain Challenge Program'''

resps = []
percent_rain = int(input('Enter the probability of rain (%): '))

if (percent_rain > 90):
   resps.append('Bring an Umbrella!')
   print(resps)
elif (percent_rain > 80):
   resps.append('Good for the Flowers?')
   print(resps)
elif (percent_rain > 50):
   resps.append('Watch for Clouds!')
   print(resps)
else:
   resps.append('Nice day Today!')
   print(resps)