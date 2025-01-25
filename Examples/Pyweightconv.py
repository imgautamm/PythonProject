#Python weight converter


weight=float(input("Enter your weight: "))
unit=input("Is your weight in (L)bs or (K)g: ")

if unit == "K":
    weight=weight * 2.205
    unit = "Lbs"
    print(f"Your weight is {round(weight, 1)} {unit}")
elif unit =="L":
    weight=weight / 2.205
    unit = "Kg"
    print(f"Your weight is {round(weight, 1)} {unit}")
else:
    print("Invalid unit")