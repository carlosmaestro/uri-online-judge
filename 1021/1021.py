# -*- coding: utf-8 -*-
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR')

default_notas = [
    100, 50, 20, 10, 5, 2
]

default_moedas = [
    1, 0.50, 0.25, 0.10, 0.05, 0.01
]


value = float(input())

print("NOTAS:")

for nota in default_notas:

    count = int(value / nota)

    print("{} nota(s) de R$ {},00".format(count, nota))
    value -= count * nota

print("MOEDAS:")

for moeda in default_moedas:

    count = int(value / moeda)

    print("{} moeda(s) de R$ {:,2F} ".format(count, moeda))
    value -= count * moeda
