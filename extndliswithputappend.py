#! /usr/bin/python3
x = [10,20,30,40]
y = [90,60,40]
x[:0] = y
print(x)

########2nd###########
import itertools
x = [10,20,30,40]
y = [40,50,60]
print(list((x, y)))

##########3rd############

a1= [10,30,40]
a2 = [40,50,60]
a3 = a1 + a2
print(a3)
