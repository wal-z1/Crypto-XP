import continues_fractions
import math
p = 1009
q = 1013

n = p * q
phi_n = (p - 1) * (q - 1)

d = 5
e = 816077

print(continues_fractions.continued_fraction(e, n))
convs = continues_fractions.convergents(continues_fractions.continued_fraction(e, n))
print(convs)
for i in range(len(convs)):
    k = convs[i].numerator
    print(f"k: {k}")
    d_cond = convs[i].denominator
    print(f"d_cond: {d_cond}")
    if (k !=0) and (e*d_cond - 1) % k == 0 :
        print(f"Found valid k and d_cond: k={k}, d_cond={d_cond}")
        phi_n_candidate = (e*d_cond - 1) // k
        print(f"phi_n_candidate: {phi_n_candidate}")
        S = n - phi_n_candidate + 1
        delta = S*S - 4*n
        if delta < 0:
            print(f"Delta is negative: {delta}, skipping...")
            continue
        else:
            sqrt_delta = math.isqrt(delta)
            if sqrt_delta * sqrt_delta != delta:
                print(f"Delta is not a perfect square: {delta}, skipping...")
                continue
            p_cond = (S + sqrt_delta) // 2
            q_cond = (S - sqrt_delta) // 2
            if p_cond * q_cond == n:
                print(f"Found valid p and q: p={p_cond}, q={q_cond}")
                break
