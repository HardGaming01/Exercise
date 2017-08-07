# -*- coding: utf-8 -*-
from random import sample

'''
这是一坨不知道干什么用的注释
反正他也解释不了，就随便打点东西吧

鹅鹅鹅
曲项向天歌
白毛浮绿水
红掌拨清波
'''

def ranged_random(n=100, m=10):
    record = {}
    if 1 <= m <= n:
        return sample(xrange(1, n), m)
    else:
        print "Please let 1 <= m <=n"
rand = ranged_random()
timer = 0
for i in rand:
    timer += 1
    print "%d : %d" % (timer, i)
