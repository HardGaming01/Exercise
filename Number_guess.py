#-*-coding:utf-8 -*-
from random import randint

record = open("record")
score = record.read().split()
record.close()

game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times > 0:
    avg_times = float(total_times)/game_times
else:
    avg_times = 0

print"你一共玩了%d次，最快用了%d轮，平均每局%.2f轮。" % (game_times, min_times, avg_times)


random_num = randint(1, 1000)
print "在1到1000之间猜一个数字吧："
guess = input(">>")
timer = 0
while guess != random_num:
    if guess < random_num:
        print "\n太小了"
        timer += 1
    if guess > random_num:
        print "\n太大了"
        timer += 1
    print "\n再试试？"
    guess = input(">>")
print "BINGO！你用了%d猜到这个数字！" % timer

game_times += 1
if timer < min_times:
    min_times = timer
total_times += timer
result = "%d %d %d" % (game_times, min_times, total_times)
record.write(result)
