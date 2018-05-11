#! /usr/bin/python3
tuplex = ((2,'q'),(3,'r'),(4,'g'))
print(dict((y, x) for x,y in tuplex))
tp = (100,200,4,7,8,9)
td = {i for i in tp}
print(td)
l = [('x',1),('x',2),('x',3),('y',2),('y',5)]
d = {}
for a,b in l:
  d.setdefault(a,[]).append(d)
print(d)
