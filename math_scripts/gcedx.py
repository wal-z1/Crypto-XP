import sympy
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
a,b ,g = sympy.gcdex(x,y)

print(a,b,g)