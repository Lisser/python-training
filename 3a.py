#!/usr/bin/env python3

values = range(0, 128)

def format_line(n):
    return " ".join([str(n), hex(n), oct(n), chr(n)])

table = map(format_line, values)

print("\n".join(table))

# for n in values:
#     print(n, hex(n), oct(n), chr(n))
#     break
# else:
#     print("the end ")