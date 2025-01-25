#Compunt interest calculator

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Please enter a positive number")

while rate <= 0:
    rate = float(input("Enter the rate amount: "))
    if rate <= 0:
        print("Please enter a positive number")

while time <= 0:
    time = int(input("Enter time: "))
    if time <= 0:
        print("Time cannot be negative or zero")

total = principal * pow((1 +rate/100), time)
print(f"Balance after {time} year/s is ${total:.2f}")
