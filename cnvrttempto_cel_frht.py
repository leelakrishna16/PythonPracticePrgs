#! /usr/bin/python3
#n = input('choose your temperature whether you want to convert f or c')
#n1 = int(input('Enter the value \n')
#if(n == c):
#  cel = (((5*n1)-160)9)
#  print(cel,'celecius)
#elif(n == f):
#  far = ((n1*9)/5)+32
#  print(far,'farenheit')
#else:
#print('Enter the wrong input:')

quess = input('Would you like to enter in Celsius or Farenheit?:').strip().lower()
if quess == 'f':
   value = int(input('What is the value of Farenheit?'))
   celsius = 5*(value-32)/9
   print('the Temprature in Celsius is {} degress'.format(celsius))
else:
   value_2 = int(input('What is the value of Celsius?'))
   farenheit = (9*value_2 + 160)/5
   print('the Temprature in Farenheit is {} degress'.format(farenheit))
