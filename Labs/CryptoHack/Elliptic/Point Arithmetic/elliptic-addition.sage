## let
p = 9739
F = GF(9739)
E = EllipticCurve(F, [497, 1768])

def point_add(P,Q,a,p):
  if P == (0,0):
    return Q
  if Q == (0,0):
    return P

  x1, y1 = P
  x2, y2 = Q
  if x1 == x2 and (y1 + y2) % p == 0:
        return None
  if P == Q:
    num = (3* x1^2 + a) % p
    den = (2 * y1) % p
    m =  (num * inverse_mod(den, p)) % p
  else:
    num = (y2 - y1) % p
    den = (x2 - x1) % p
    m = (num * inverse_mod(den, p)) % p
  x3 = (m^2 - x1 - x2) % p
  y3 = (m * (x1 - x3) - y1) % p
  return (x3, y3)


P=(493,5564)
Q=(1539,4742)
R=(4403,5202)

print(point_add(point_add(point_add(P,P,497,p),Q,497,p),R,497,p) )

## sage way
P = E(493,5564)
Q = E(1539,4742)
R = E(4403,5202)

S = P + Q + P + R

print(S)

P = E(2339,2213)
Q = 7863 * P
print(Q.xy())

