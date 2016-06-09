' Implementation of a `fraction class`.'

def gcd(m, n):
    '''Greatest common divisor.'''
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n

class Fraction(object):

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print self.num + '/' + self.den

    def __add__(self,otherfraction):

        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)

    def __eq__ (self, other):
        first_num = self.num * other.den
        second_num = self.den * other.den
        return first_num == second_num

    def __mul__(self, other):
        newnum =  self.num * other.den 
        newden = self.den * other.num
        return Fraction(newnum, newden)

    def __div__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

