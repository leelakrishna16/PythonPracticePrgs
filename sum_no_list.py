#! /usr/bin/python3
n = [1,3,5,7,9,8,4]
b =sum(n)
print(b)

########second one######
list = [10,20,3,6,7,8,9]
sum = 0
for i in range(len(list)):
  sum = sum+list[i]
print('sum is', sum)

#######third###########
a = [1,3,5,6,7]
p = 0
for i in a:
  p = p+i
print(p)

######fourth######
str1 = [1,2,3,4,4,3,'e','r','g','r']
str2 = [i for i in str1 if i isinstace(i,int)]
print(sum(str2))
