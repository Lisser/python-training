#!/usr/bin/env python3

values = range(0, 128)

def format_line(n):
    return " ".join([
        str(n),
        hex(n),
        oct(n),
        ("" if n < 32 else '"' + chr(n) + '"')
    ])

table = map(format_line, values)

print("\n".join(table))
