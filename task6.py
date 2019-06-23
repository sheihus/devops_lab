#!/usr/bin/env python


def ip_to_bin(ip):
    a = ip.split(".")
    s = ""
    for i in a:
        s += format(int(i), '08b')
    return int(s)


n = int(input())  # count of subnets
subnets = []
for i in range(n):
    subnets.append(ip_to_bin(input()))

m = int(input())  # count of IP pairs
pairs = []
for i in range(m):
    pair = input().split()
    pairs.append((ip_to_bin(pair[0]), ip_to_bin(pair[1])))

for i in pairs:  # checking for all pairs
    c = 0
    for j in subnets:  # in all subnets
        if i[0] & j == i[1] & j:
            c += 1
    print(c)
