#! /usr/bin/python3
for x in range(0,10,):
   print((9-x)*' ' + '*'.join(['*']*x))

for x in range(10,0,-1):
    print((9-x)*' ' + '*'.join(['*']*x))
