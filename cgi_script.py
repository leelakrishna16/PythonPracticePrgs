#! /usr/bin/python3

print('Content-type:text|html\n\n')
import cgi,cgitb
form = cgi.FieldStorage()
my_string = form.getvalue('madam')
if(my_string):
   my_string = my_string.repalce(' ','')
   my_string = ''.join(e for e in my_string if e.isalnum())
   my_string = my_string.lower()
   rev_string = my_string[::-1]
   if(my_string == rev_string):
     print('palinedrome')
   else:
     print('not palindrome')
