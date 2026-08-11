p = 2**255 - 19
F = GF(p)

A = F(486662)
xP = F(9)
zP = F(1)
P = (xP, zP)
k = 0x1337c0decafe

C = (A + 2) / 4

def xDBL(P):
    X, Z = P
    V1 = (X + Z)^2
    V2 = (X - Z)^2
    V3 = V1 - V2
    X2 = V1 * V2
    Z2 = V3 * (V2 + C * V3)
    return (F(X2), F(Z2))


def xADD(P, Q, PminusQ):
    X1, Z1 = P
    X2, Z2 = Q
    Xd, Zd = PminusQ
    U1 = (X1 + Z1) * (X2 - Z2)
    U2 = (X1 - Z1) * (X2 + Z2)
    X3 = ((U1 + U2)**2) / 4
    Z3 = ((U1 - U2)**2) / 4
    return (F(X3), F(Z3))


def montgomery_ladder(k, P):
  R0, R1 = P, xDBL(P)
  for i in range(k.bit_length() - 2, 0, -1):
    k_inbinary = bin(k)[2:]
    k_inbinary[k.bit_length()-1] = '1'
    if k_inbinary[i] == '0':
      R1 = xDBL(R1)
      R0 = xDBL(R0)
    else:
      R0 = xDBL(R0)
      R1 = xDBL(R1)
  return R0

