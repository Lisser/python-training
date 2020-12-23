# !/usr/bin/env python3

fname = "limerick.txt"

f = open(fname, "rb")

linecount = 0
wordcount = 0
charcount = 0
bytecount = 0

for linebuf in f:
    linecount += 1
    wordcount += len(linebuf.strip().split())
    charcount += len(linebuf.decode('utf-8'))
    bytecount += len(linebuf)
    print(linebuf)

f.close()

print("{:>3} {:>3} {:>3} {:>3} {:}".format(linecount, wordcount, charcount, bytecount, fname))

# print("File: {:}".format(fname))
# print("Regels: {:}".format(linecount))
# print("Woorden: {:}".format(wordcount))
# print("Chars: {:}".format(charcount))
