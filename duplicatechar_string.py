#! /usr/bin/python3
chars = 'abcdefghijklmnopqrstuvxyz'
check_string = 'i am checking this string to see how many times each character appears'
for char in chars:
   count = check_string.count(char)
   if count > 1:
     print(char,count)

count = {}
for s in check_string:
  if count.has_key(s):
    count[s] += 1
  else:
    count[s] = 1
for key in count:
  if count[key] > 1:
    print(key,count[key])
