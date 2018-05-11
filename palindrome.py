#! /usr/bin/python3
my_str = 'aEiouvL'
#my_str = my_str.casefold()
#rev_str = reversed(my_str)
#if list(my_str) == list(rev_str):
#  print('It is a plaindrome')
#else:
#  print('it`s not plaindrome')


print('Enter a word')
my_string = str(input())
my_string = my_string.replace(' ','')
my_string = ''.join(e for e in my_string if e.isalnum())
my_string = my_string.lower()
rev_string = my_string[::-1]
if(my_string == rev_string):
  print('It`s palindrome')
else:
  print('It`a not palindrome')
