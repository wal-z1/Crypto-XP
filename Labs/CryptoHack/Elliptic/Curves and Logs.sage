p = 9739
F = GF(p)
E = EllipticCurve(F, [497, 1768])

Q_a = E(815, 3190)
nb = 1829
Q_ab = nb * Q_a

print(Q_ab)

