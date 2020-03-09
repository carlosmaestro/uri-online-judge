# -*- coding: utf-8 -*-

default_notas = [
    100, 50, 20, 10, 5, 2, 1
]

value = int(input())
print(value)
for nota in default_notas:

    count = int(value / nota)

    print("{} nota(s) de R$ {},00".format(count, nota))
    value -= count * nota
