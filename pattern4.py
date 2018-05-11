#! /usr/bin/python3
for g in range(0,11,1):
   print(g*''+(11-g)*'*')

for g in range(11,0,-1):
   print(g*''+(11-g)*'*')

n = int(input('enter the no:'))
for i in range(n,0,-1):
     print("*"*i)

n = int(input('Enter the no :'))
for i in range(0,n,1):
     print("*"*i)
