#! /usr/bin/python3

word = input('Enter the word to reverse')
for char in range(len(word)-1,-1,-1):
  print(word[char],end='')
print('\n')

######2nd###########
word = input('Enter the word')
print(word[-1::-1])
######3rd######
x = input('Enter the word')
print(*(reversed(x)))
######4th######

