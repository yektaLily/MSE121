def calculate_formula(a, b, c):
    x = (c - b)/a
    return x

a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

print("Value of x is ", calculate_formula(a,b,c))
