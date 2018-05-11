#! /usr/bin/python3
s=input('Enter the string to count the characters :')
l=list(s)
d={}
for m in l:
  d[m]=l.count(m)
print(d)
##########2nd#############
x=input('Enter thr string :')
count={}
for i in x:
 if i in count:
   count[i]+=1
   print(count[i])
 else:
   count[i]=1
 a=count.items()
for k,v in a:
 print(k,':',v,'',end='')

###########3rd##############
s=input('Enter thr string :')
print({x:list(s).count(x) for x in list(s)})
############4th##############
s=input('Enter thr string :')
dict={}
for i in s:
 count=0
 for j in s:
   if i==j:
     count = count+1
     dict[i]=count
print(dict)
