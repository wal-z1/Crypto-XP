import continues_fractions
import sympy
import math
N  = 7067354383

e1 = 2195338595
e2 = 6441309647
e3 = 4440683853

convs1 = continues_fractions.convergents(continues_fractions.continued_fraction(e1, e2))
convs2 = continues_fractions.convergents(continues_fractions.continued_fraction(e1, e3))
convs3 = continues_fractions.convergents(continues_fractions.continued_fraction(e2, e3))


""" for e1/e2 we get k1d2/k2d1"""
""" for e1/e3 we get k1d3/k3d1"""
""" for e2/e3 we get k2d3/k3d2"""
d1_conds = []
d3_conds = []
d2_conds = []
k1_conds = []
k2_conds = []
k3_conds = []
for i in range(len(convs1)):
  for j in range(len(convs2)):
    x = sympy.gcd(convs1[i].numerator, convs2[j].numerator)
    y  =  sympy.gcd(convs1[i].denominator, convs2[j].denominator)
    if y > 1:
      d1_conds.append(y)
    if x > 1:
      k1_conds.append(x)

for i in range(len(convs2)):
  for j in range(len(convs3)):
    x = sympy.gcd(convs2[i].denominator, convs3[j].denominator)
    y  =  sympy.gcd(convs2[i].numerator, convs3[j].numerator)
    if y > 1:
      d3_conds.append(y)
    if x > 1:
      k3_conds.append(x)

for i in range(len(convs1)):
  for j in range(len(convs3)):
    x = sympy.gcd(convs1[i].denominator, convs3[j].numerator)
    y  =  sympy.gcd(convs1[i].numerator, convs3[j].denominator)
    if y > 1:
      d2_conds.append(y)
    if x > 1:
      k2_conds.append(x)

d1_d2_withgcd1 = tuple( (x,y) for x in d1_conds for y in d2_conds if sympy.gcd(x,y) == 1)
d2_d3_withgcd1 = tuple( (x,y) for x in d2_conds for y in d3_conds if sympy.gcd(x,y) == 1)
d1_d3_withgcd1 = tuple( (x,y) for x in d1_conds for y in d3_conds if sympy.gcd(x,y) == 1)

k1_k2_withgcd1 = tuple((x,y) for x in k1_conds for y in k2_conds if sympy.gcd(x,y) == 1)
k2_k3_withgcd1 =  tuple((x,y) for x in k2_conds for y in k3_conds if sympy.gcd(x,y) == 1)
k1_k3_withgcd1 =  tuple((x,y) for x in k1_conds for y in k3_conds if sympy.gcd(x,y) == 1)

d1_cleaned = tuple(
    {x for x, _ in d1_d2_withgcd1} &
    {x for x, _ in d1_d3_withgcd1}
)
d2_cleaned = tuple(
    {y for _, y in d1_d2_withgcd1} &
    {x for x, _ in d2_d3_withgcd1}
)
d3_cleaned = tuple(
    {y for _, y in d1_d3_withgcd1} &
    {y for _, y in d2_d3_withgcd1}
)

k1_cleaned = tuple(
    {x for x, _ in k1_k2_withgcd1} &
    {x for x, _ in k1_k3_withgcd1}
)
k2_cleaned = tuple(
    {y for _, y in k1_k2_withgcd1} &
    {x for x, _ in k2_k3_withgcd1}
)
k3_cleaned = tuple(
    {y for _, y in k1_k3_withgcd1} &
    {y for _, y in k2_k3_withgcd1}
)


phi_n_candidates = []
for d1 in d1_cleaned:
  for k1 in k1_cleaned:
    if (k1 !=0) and (e1*d1 - 1) % k1 == 0 :
      phi_n_candidate = (e1*d1 - 1) // k1
      phi_n_candidates.append(phi_n_candidate)
for d2 in d2_cleaned:
  for k2 in k2_cleaned:
    if (k2 !=0) and (e2*d2 - 1) % k2 == 0 :
      phi_n_candidate = (e2*d2 - 1) // k2
      phi_n_candidates.append(phi_n_candidate)

for d3 in d3_cleaned:
  for k3 in k3_cleaned:
    if (k3 !=0) and (e3*d3 - 1) % k3 == 0 :
      phi_n_candidate = (e3*d3 - 1) // k3
      phi_n_candidates.append(phi_n_candidate)

phi_cleaned = tuple( phi for phi in phi_n_candidates if phi < N )
print(f"phi_cleaned: {phi_cleaned}")

def p_and_q_from_phi(phi, N):
  S = N - phi + 1
  delta = S*S - 4*N
  if delta < 0:
    print(f"Delta is negative: {delta}, skipping...")
    return None
  else:
    sqrt_delta = math.isqrt(delta)
    if sqrt_delta * sqrt_delta != delta:
      print(f"Delta is not a perfect square: {delta}, skipping...")
      return None
    p_cond = (S + sqrt_delta) // 2
    q_cond = (S - sqrt_delta) // 2
    if p_cond * q_cond == N:
      print(f"Found valid p and q: p={p_cond}, q={q_cond}")
      return p_cond, q_cond
  return None

for i in range(len(phi_cleaned)):
  result = p_and_q_from_phi(phi_cleaned[i], N)
  if result is not None:
    p, q = result
    print(f"Found valid p and q: p={p}, q={q}")
    break




