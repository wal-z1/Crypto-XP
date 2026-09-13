p = 9739
F = GF(p)
E = EllipticCurve(F, [497, 1768])

x_Qa = 4726
Q = E.lift_x(x_Qa)

shared_secret = (6534 * Q)

print(shared_secret)