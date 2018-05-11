#! /usr/bin/python3
x = range(1500, 2700)
for i in x:
 if(i%7==0 and i%5==0):
   print(i)

print(*[x for x in range(1500,2700) if (x%7 == 0 and x%5 == 0)])

nl = []
for x in range(1500,2700):
  if(x%7 == 0 and x%5 == 0):
    nl.append(str(x))
print(','.join(nl))
