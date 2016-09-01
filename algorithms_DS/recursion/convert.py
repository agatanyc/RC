from __future__ import division
"""Convert an integer to a string at any base."""

def convert(n, base):
    string = '0123456789ABCDEF'
    if n < base:
        return string[n]
    else:
        return convert(n // base, base) + string[n % base]

if __name__ == '__main__':
    assert convert(10, 2) == '1010'
    assert convert(10, 16) == 'A'
    assert convert(10, 16) != '1'

