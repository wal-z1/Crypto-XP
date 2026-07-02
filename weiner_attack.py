import continues_fractions

p = 31
q = 23
n = p*q
phi_n = (p-1)*(q-1)

e = 7
d = 283

print(continues_fractions.continued_fraction(e, n))
