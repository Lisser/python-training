# !/usr/bin/env python3

fname = "verhaal.txt"

f = open(fname, "rt")

linecount = 0
wordcount = 0
charcount = 0

for linebuf in f:
    linecount += 1
    wordcount += len(linebuf.strip().split())
    charcount += len(linebuf)
    print(linebuf, end='')

f.close()

print("File: {:}".format(fname))
print("Regels: {:}".format(linecount))
print("Woorden: {:}".format(wordcount))
print("Chars: {:}".format(charcount))
