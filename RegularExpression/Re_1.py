# -*-coding:utf-8 -*-


import re


def printFind(m):
    if m:
        print m
    else:
        print "not match"

text = "Hi, I am Shirley Hilton. I am his wife."
# 匹配Hi
m = re.findall(r"\bHi\b", text)
printFind(m)
# 贪婪匹配
m = re.findall(r"I.*e", text)
printFind(m)
# 懒惰匹配
m = re.findall(r"I.*?e", text)
printFind(m)

# Exercise
text = "site sea sue sweet see case sse ssee loses"
m = re.findall(r"\bs\S*?e\b", text)
printFind(m)
