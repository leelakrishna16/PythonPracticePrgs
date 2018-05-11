#! /usr/bin/python3
for num in range(2,101):
    if all(num%i != 0 for i in range(2,num)):
        print(num)
for num in range(2,50):
    prime = True
    for i in range(2,num):
        if(num%i==0):
           prime = False
    if prime:
       print(num)
for num in range(1,20):
  for i in range(2,num):
      if(num%i==0):
        break
      else:
          print(num)
          break
noprimes = [j for i in range(2,10) for j in range(i*2,50,i)]
primes = [x for x in range(2,50) if x not in noprimes]
print(primes)
