#! /usr/bin/python3

n1 = [[10,20],[40],[30,56,25],[10,20],[33],[40]]
n2 = []
for i in n1:
  if i not in n2:
    n2.append(i)
print(n2)

#########2nd############

import itertools
num = [[10,20],[40],[30,56,25],[10,20],[33],[40]]
print('Orginal List', num)
num.sort()
new_num = list(num for num,_ in itertools.groupby(num))
print('New list', new_num)
