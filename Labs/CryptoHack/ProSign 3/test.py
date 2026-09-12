
import hashlib
from Crypto.Util.number import bytes_to_long, long_to_bytes
from ecdsa.ecdsa import Public_key, Private_key, Signature, generator_192

from datetime import datetime
from random import randrange

def sha1(data):
        sha1_hash = hashlib.sha1()
        sha1_hash.update(data)
        return sha1_hash.digest()


def sign(msg):
    g = generator_192
    n = g.order()
    for k in range(1, 3):
      m = "Current time is 9:2"
      s = int("0xd53af0afc47c97b9f9f729901ddf8c32290208a40a249f1d",16)
      h = bytes_to_long(sha1(m.encode()))
      r= int("0x188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012",16)
      r_inv = pow(r, -1, n)
      secret = ((s*k - h)*r_inv) % n
      pubkey = Public_key(g, g * secret)
      privkey = Private_key(pubkey, secret)
      hsh = hashlib.sha1()
      hsh.update(msg.encode())
      sig = privkey.sign(bytes_to_long(hsh.digest()),k)
      print({"option": "verify", "msg": msg, "r": hex(sig.r), "s": hex(sig.s)})

sign("unlock")

