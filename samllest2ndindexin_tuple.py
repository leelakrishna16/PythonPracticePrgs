#! /usr/bin/python3
x = [(4,1),(1,2),(4,5)]
print(min(x, key=lambda n:(n[1], -n[0])))

#######2nd#########
from operator import itemgetter
def samallest_tuple():
 l1 = [(4,1),(1,3),(6,0)]
 l1 = sorted(l1,key=itemgetter(1))
 return l1
y=samallest_tuple()
print(y[0])
