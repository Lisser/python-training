# !/usr/bin/env python3

powers_of_2 = [ 2**(i + 1) for i in range(1000) ]

counts = [0] * 9

for i in powers_of_2:
    counts[int(str(i)[:1]) - 1] += 1

# print('\n'.join(map(str, powers_of_2)))
print('\n'.join(map(str, counts)))