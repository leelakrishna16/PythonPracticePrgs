#! /usr/bin/python3
x =open('test.txt', 'r')
lines = x.readlines()
print(lines)
print(len(lines))
x.close()

files2 = open('test.txt', 'w')
for line in lines:
  files2.write(line.strip()+'')
files2.close()
