#!/usr/bin/env python3

def calc_avg (numbers):
    return (len(numbers), sum(numbers) / len(numbers))

l=[ 1, 5, 2, 33, 5, 16, 7 ]

avg = calc_avg(l)

avg
