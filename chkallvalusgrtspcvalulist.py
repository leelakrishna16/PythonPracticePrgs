#! /usr/bin/python3
l = [1,2,3,5,6,7,8,9,10,11]
s = int(input('Enter the no:'))
l2 = []
l3 = []
for i in l:
   if i > s:
     l2.append(i)
   else:
     l3.append(i)
print('The greter nos than specifi no are', l2)
print('The lesser nos than specific no are', l3)

########2nd############

list1=[110,220,221,333,550]
list2=[12,15,22,33]
print(all(x >= 200 for x in list1))
print(all(x >= 25 for x in list2))
