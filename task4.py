#!/usr/bin/env python

n = int(input())
max_age = 0
index = -1
for i in range(n):
    s = input().split()
    if s[1] == '1':  # male
        age = int(s[0])
        if age > max_age:
            max_age = age
            index = i + 1
print(index)
