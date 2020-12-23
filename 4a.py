#!/usr/bin/env python3

n = 2 ** 1000

l = str(n)

l_without_5 = l.replace('5', '')

l_without_5

count = len(l) - len(l_without_5)

count