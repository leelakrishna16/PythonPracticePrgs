#! /usr/bin/python3
import random
guess = random.randint(1,9)
print(guess)
while(True):
  user_input = int(input('Please guess any number between 1 and 9:'))
  if(user_input<0):
    print('The number is beyond limits')
  if(user_input>0):
    print('The number is beyond limits')
  if user_input == guess:
    break
print('Well guessed')

########2nd############
import random
randNumber = random.randint(1,9)
userguess=int(input('Guess the number between 1 and 9:'))
while userguess!=randNumber:
  userguess=int(input('tryagain:'))
print('Wellguessed')

########3rd########

import random
guess,target = random.randint(1,10),random.randint(1,10)
while target != guess:
   guess = int(input('Guess a number between 1 and 10: '))
print('Wellguessed')
 
########4th  ########
import random
target_num, guess_num = random.randint(1,10),0
while target_num != guess_num:
  guess_num = int(input('Guess a number between a and 10 :'))
print('well guessed!')
