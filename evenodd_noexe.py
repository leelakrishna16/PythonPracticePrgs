#! /usr/bin/python3
number = int(input('Enter the number: '))
if number % 2 == 0 and number != 0:
    print('Even number')
elif number == 0:
    print('zero is neither even,not odd.')
else:
    print('odd number')
number = int(input('Enter the number: '))
for number in range(1, number):
    if number % 2 == 0 and number != 0:
       print('Even number', number)
    elif number == 0:
        print('zero is neither even,not odd.', number)
    else:
        print('odd number', number)
