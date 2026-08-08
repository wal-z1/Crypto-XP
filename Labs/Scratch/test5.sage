factors = list(factor(28151 - 1))
print(factors)
#[(2, 1), (5, 2), (563, 1)]

for i in range(1, 28151):
    bol = True
    for x in [2, 5, 563]:
      bol = bol and pow(i, (28151 - 1) // x, 28151) != 1
    print("bol is", bol)
    if bol:
        print(i)
        break
