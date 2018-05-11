#! /usr/bin/python3
milist = [{},{},{}]
mlist1 = [{1,2},{},{}]
print(all(not d for d in milist))
print(all(not d for d in mlist1))

#######2nd##########

def isemptyDictList(l):
  for i in l:
   if(len(i) == 0):
     return True
   else:
    return False
#########3rd#########

x =[{},{},{}]
y = [{1,2},{},{}]
if len(x) & len(y) == 0:
  print('The list dictionary x and y are empty')
elif len(x) == 1:
  print('The list dictionary x contain value')
else:
  print('The list dictionart y contains values')
