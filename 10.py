# !/usr/bin/env python3

fname = "verhaal.txt"

f = open(fname, "rt")

lines = f.readlines()
rev = reversed(lines)
for line in rev:
    print(line, end='')