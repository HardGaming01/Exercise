#!/usr/bin/env python
# -*-coding:utf-8 -*-

list_1 = [str(i) for i in range(0, 101) if i % 2 == 0 and i % 3 == 0 and i % 5 == 0]
list_2 = [str(i) for i in range(0, 101) if i % 2 == 0 or i % 3 == 0 or i % 5 == 0]
print ";".join(list_1)
print ";".join(list_2)
