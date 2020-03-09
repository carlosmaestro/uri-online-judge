# -*- coding: utf-8 -*-

pairs = []

for i in range(0, 5):
    n = int(input())
    if(n % 2 == 0):
        pairs.append(n)

print("{} valores pares".format(len(pairs)))
