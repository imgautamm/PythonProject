#Conditional Expression in Python

num = int(input("Enter a number: "))
a = 5
b = 6

#result = "Even" if num % 2 == 0 else "Odd"

max_num = a if a > b else b
min_num = a if a < b else b

print(f"The maximum number is: {max_num}")
print(f"The minimum number is: {min_num}")