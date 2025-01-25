#While Loop

age  = int(input("Enter your age: "))

#while age < 0:
while not age > 0:
    print("age cannot be negative")
    age = int(input("Enter your age: "))

    print(f"You are {age} years old!")
