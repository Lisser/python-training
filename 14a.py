#!/usr/bin/env python3
 
def omkeer(s: str):
    return s[::-1]

def makeupper(s: str):
    return s.upper()
    
def doalle(l, s):
    for func in l:
        s = func(s)
    return s

l=[ omkeer, makeupper ]
    
print( doalle(l, "lower case string") )