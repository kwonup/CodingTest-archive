from fractions import Fraction
a,b = map(int,input().split())
c,d = map(int,input().split())
f=Fraction(a,b) + Fraction(c,d)
print(f.numerator,f.denominator)