from fractions import Fraction

def continued_fraction(input_numerator, input_denominator):
    """Compute the continued fraction representation of a rational number."""
    cf = []
    x = Fraction(input_numerator, input_denominator)
    while True:
        integer_part = x.numerator // x.denominator
        cf.append(integer_part)
        remainder =  x - integer_part
        if (remainder == 0):
            break
        x = 1 / (remainder)
        if x.denominator == 1:
            cf.append(x.numerator)
            break
    return cf


continued_fraction(input_numerator=415, input_denominator=93)

def convergentcalc(a,p_n_1=1,q_n_1=0,p_n_2=0,q_n_2=1):
    """ calculate the convergents of a continued fraction representation."""
    p_n = a*p_n_1 + p_n_2
    q_n = a*q_n_1 + q_n_2
    return p_n, q_n

def convergents(cf):
    """ calculate the convergents of a continued fraction representation."""
    convs = []
    if len(cf) == 1:
        return [Fraction(cf[0], 1)]
    else:
        for i in range(len(cf)):
            if i == 0:
                p_n, q_n = convergentcalc(cf[i])
            elif i == 1:
                p_n, q_n = convergentcalc(cf[i],convs[i-1].numerator,convs[i-1].denominator,1,0)
            else:
                p_n, q_n = convergentcalc(cf[i],convs[i-1].numerator,convs[i-1].denominator,convs[i-2].numerator,convs[i-2].denominator)
            print(f"Convergent {i}: {p_n}/{q_n}")
            convs.append(Fraction(p_n, q_n))

    return convs

