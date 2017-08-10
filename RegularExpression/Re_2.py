# -*-coding:utf-8 -*-


import re

file1 = open("PhoneNumbers.txt")
record = file1.read()
print record
numbers = re.findall(r"1[0-9]{10}", record)
print numbers
