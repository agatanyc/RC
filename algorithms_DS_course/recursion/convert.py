from __future__ import division
"""Convert an integer to a string at any base."""

def convert(n, base):
    string = '123456789ABCDEF'
    if n < base:
        return string[n]
    else:
        return convert(n // 2, base) + string[n % base]

if __name__ == '__nmae__':
    assert convert(10, 2) == '1010'

