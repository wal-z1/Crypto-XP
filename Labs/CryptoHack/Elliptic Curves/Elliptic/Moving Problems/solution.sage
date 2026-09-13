p = 1331169830894825846283645180581
a = -35
b = 98
E = EllipticCurve(GF(p), [a, b])
G = E(479691812266187139164535778017 , 568535594075310466177352868412 )

Gn = G.order()
k = 1
while p^k % Gn != 1:
    k += 1
print("k is the embedding", k)

## alice

A = E(1110072782478160369250829345256 , 800079550745409318906383650948 )
print("Alice's public key is:", A)
print("Defining new curve mod p^k and the points on it")
Ek = EllipticCurve(GF(p ^ k), [a, b])
Gk = Ek(G)
Ak = Ek(A)
Rk = Ek.random_point()
print("Random point in the extended field is:", Rk)
# find T of order n through the random point generated in the extended Field
m = Rk.order()
d = gcd(m, Gn)
Tk = (m // d) * Rk
print("T is of order n:", Tk)
##error check

assert Tk.order() == d
assert (Gn*Tk).is_zero() ## d is equal to n
print("T is of order n:", Tk)
g = Gk.weil_pairing(Tk, Gn)
q = Ak.weil_pairing(Tk, Gn)
print("g is:", g)
print("q is:", q)
found_key = q.log(g)
print("The private key is:", found_key)
print("success!")

## The private key is: 29618469991922269

