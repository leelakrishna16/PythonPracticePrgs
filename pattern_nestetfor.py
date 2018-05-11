#! /usr/bin/python3
n=6
for i in range(1,n+1):
  for j in range(i):
    print('*',end='')
  print('')
for i in range(n,0,-1):
   for j in range(i):
     print('*',end='')
   print('')

##########2n###########
for i in range(6):
 print(i*'*')
for j in range(4,0,-1):
  print(j*'*')

##########3rd##########
for i in range(1):
  for x in range(1,6):
    print('*'*x)
  while x>0:
    x-=1
    print(x*'*')
