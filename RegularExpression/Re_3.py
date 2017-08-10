# -*-coding:utf-8 -*-


import re
text = "(021)88776543 010-55667890 02584453362 0571 66345673"
m = re.findall(r"\(0\d{2,3}\)\d{8}|0\d{2,3}[ -]?\d{8}|", text)
print m
