p = 2^255 - 19
F = GF(p)

A = F(486662)
xP = F(9)
k = Integer(0x1337c0decafe)

C = (A + 2) / 4

def xDBL(P):
    X, Z = P
    V1 = (X + Z)^2
    V2 = (X - Z)^2
    V3 = V1 - V2
    X2 = V1 * V2
    Z2 = V3 * (V2 + C * V3)
    return X2, Z2

def xADD(P, Q, PminusQ):
    X1, Z1 = P
    X2, Z2 = Q
    Xd, Zd = PminusQ

    V1 = (X1 + Z1) * (X2 - Z2)
    V2 = (X1 - Z1) * (X2 + Z2)

    X3 = Zd * (V1 + V2)^2
    Z3 = Xd * (V1 - V2)^2
    return X3, Z3

def ladder(k, xP):
    P = (xP, F(1))
    R0 = P
    R1 = xDBL(P)

    for i in range(k.nbits() - 2, -1, -1):
        bit = (k >> i) & 1

        if bit == 0:
            R1 = xADD(R0, R1, P)
            R0 = xDBL(R0)
        else:
            R0 = xADD(R0, R1, P)
            R1 = xDBL(R1)

    X, Z = R0
    return X / Z

m = ladder(k, xP)

print(m)
print(f"crypto{{{m}}}")