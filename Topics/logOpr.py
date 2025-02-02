#Logical Operator

temp = float(input("Enter the temperature: "))
is_raining = (input("Is it raining? (yes/no): "))

if temp > 30 or temp < 5 or is_raining:
    print("Let's stay home")
elif temp > 20 and not is_raining:
    print("Let's go for a walk")
elif temp < 25 and is_raining:
    print("Let's have a coffee")
else:
    print("Let's go out")