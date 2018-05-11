#! /usr/bin/python3
f = open('/home/leelakrishna/python/Learnbay/test.txt','r')
for line in f:
   line = line.replace('\n','')
f.close()

f = open('/home/leelakrishna/python/Learnbay/test.txt','r')
for line in f:
   line = line.rstrip()
   print(line)
f.close()

def chomp(s):
  if len(s):
    lines = s.splitlines(True)
    last = line.pop()
    return = ''.join(lines + last.splitlines())
  else:
    return()
