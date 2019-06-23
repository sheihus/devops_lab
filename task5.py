#!/usr/bin/env python

s = input()
dict0 = dict.fromkeys(s)  # dictionary from string

for c in dict0:
    dict0.update({c: s.count(c)})  # count symbols

list = sorted(dict0.items(), key=lambda x: (-x[1], x[0]))

for i in list[:3]:
    print("%s %d" % i)  # print 3 first
