#!/usr/bin/env python
n = int(input())
list = []
for i in range(n):
    s = input().split()
    command = s[0]
    args = s[1:]  # arguments

    if command == "print":
        runcom = "print(list)"
    else:
        runcom = "list." + command + "(" + ",".join(args) + ")"

    eval(runcom)
