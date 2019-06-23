#!/usr/bin/env python

a = input()
b = input()

# split numbers into lists of digits
a1 = list(a)
b1 = list(b)

# maximize a
a1.sort(reverse=True)

if int(b) < 0:  # b < 0, minimize b
    b1.pop(0)
    b1.sort(reverse=True)
    b1.insert(0, '-')
else:
    # b > 0, maximize b (without leading zeros)
    b1.sort()
    i = 0
    while b1[i] == '0':
        i += 1
    b1.insert(0, b1.pop(i))

a2 = int(''.join(a1))
b2 = int(''.join(b1))

print(a2 - b2)
