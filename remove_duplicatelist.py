#! /usr/bin/python3
t = [1,2,1,2,3,3,4,4,5,6,7,7,6,5,8,9,9,8]
s = []
for i in t:
  if i not in s:
    s.append(i)
print(s)

l = [1,2,1,2,3,3,4,4,5,6,7,7,6,5,8,9,9,8]
dup_list = [i for n,i in enumerate(l) if i not in l[:n]]
print(dup_list)

mylist = [1,2,1,2,3,3,4,4,5,6,7,7,6,5,8,9,9,8]
cleanlist = []
[cleanlist.append(x) for x in mylist if x not in cleanlist]
print(cleanlist)
numbers = [1,2,1,2,3,3,4,4,5,6,7,7,6,5,8,9,9,8]
duplicateNumbers = []
uniqueNumbers = []
for number in numbers:
  if number not in uniqueNumbers:
    uniqueNumbers.append(number)
  else:
    duplicateNumbers.append(number)
print('List ater duplicates removed:', uniqueNumbers)
print('Duplicate in the original list:', duplicateNumbers)

