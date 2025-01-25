import math

a = float(input("Enter Side A: "))
b = float(input("Enter Side B: "))


c = math.sqrt (pow(a,2) + pow(b,2))

print(f"The Hypotenuse of the triangle with sides {a} and {b} is: {round(c,2)} cm")

