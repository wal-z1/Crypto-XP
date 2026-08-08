
a = int(input("Enter a number: "))
p = int(input("Enter a prime number: "))
def find_for_prime_modsqrt(p, a):
  if p % 4 == 3:
    return power_mod(a, (p + 1) // 4, p)
  else:
    return None
print(find_for_prime_modsqrt(p, a))
