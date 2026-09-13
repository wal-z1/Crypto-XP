string = """
Intercepted from Alice: {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0x8ada017401ccfa36"}

Intercepted from Bob: {"B": "0xd4f7a4bb3ba70d1f"}


Intercepted from Alice: {"iv": "2b8032f04c549645b6afae10224fc493", "encrypted_flag":"d9360e1d5897304b3fcbf7c7715d7068816b43d49c710633c77914a7bf6efbbf"}

"""
p = 0xde26ab651b92a129
g = 2
A = 0x8ada017401ccfa36
B = 0xd4f7a4bb3ba70d1f

F = GF(p)
a = F(A).log(F(g))

shared_secret = F(B)^a

print("Shared secret:", shared_secret)
