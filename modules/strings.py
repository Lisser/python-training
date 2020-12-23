#!/usr/bin/env python3
 
def omkeer(s: str):
    return s[::-1]

def makeupper(s: str):
    return s.upper()
    
def doalle(l, s):
    for func in l:
        s = func(s)
    return s


if __name__ == '__main__':

    if omkeer('12345') == '54321':
        print('PASS')
    else:
        raise Exception('omkeer "12345" should match "54321"')

    if makeupper('abcde') == 'ABCDE':
        print('PASS')
    else:
        raise Exception('makeupper "abcde" should match "ABCDE"')

    l=[ omkeer, makeupper ]
    if doalle(l, "lower case test string") == 'GNIRTS TSET ESAC REWOL':
        print('PASS')
    else:
        raise Exception('')