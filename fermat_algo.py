import math
from sympy import isprime

N = 31*91
def fermat_factorization(n):

  x = math.ceil(2*math.sqrt(n))
  y = math.sqrt(x*x - 4*n)

  p = (x + y) / 2
  q = (x - y) / 2

  if int(p)*int(q) == n:
    return int(p), int(q)

  while True:
  ## until we have an interger
    x += 1
    y = math.sqrt(x*x - 4*n)
    p = (x + y) / 2
    q = (x - y) / 2

    if y == int(y):
        break

  return int(p), int(q)

print(fermat_factorization(N))

