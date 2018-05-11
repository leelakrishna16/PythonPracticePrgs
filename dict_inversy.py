#! /usr/bin/python3
dict1 = {'book1':'pyton','book2':'java','book3':'shell','book3':'perl','book4':8777}
new_dict = dict(zip(dict1.values(),dict1.keys()))
print(new_dict)

#######2nd#########
dict1 = {'book1':'pyton','book2':'java','book3':'shell','book3':'perl','book4':8777}
print({v: k for k, v in dict1.items()})
