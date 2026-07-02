from fractions import Fraction
import math
def continued_fraction():
    """Compute the continued fraction representation of a rational number."""
    cf = []
    print("please input your numerator and denominator")
    input_numerator = int(input("Numerator: "))
    input_denominator = int(input("Denominator: "))
    x =  Fraction(input_numerator, input_denominator)
    print("The continued fraction representation of", x, "is:")
    while True:
        intger_part = x.numerator // x.denominator
        print("integer part:", intger_part)
        cf.append(intger_part)
        x = 1 / (x - intger_part)
        print("new x:", x)
        if x.denominator == 1:
            cf.append(x.numerator)
            break
    print(cf)
    expr = str(cf[-1])
    for a in reversed(cf[:-1]):
      expr = f"{a} + 1/({expr})"
    print(expr)
    ## this prints like 1 + 1/(2 + 1/(3 + 1/4)) for [1,2,3,4]
    ## the following steps : first it takes the last element of the list and then it takes the second last element and adds 1 over the last element and so on until it reaches the first element of the list.


continued_fraction()