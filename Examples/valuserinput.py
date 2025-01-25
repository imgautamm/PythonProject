#validate user input

username = input("Enter your username: ")

if len(username) > 10:
    print("Username must be at least 10 characters")
elif not username.find(" "):
        print("Username must not contain spaces")
elif not username.isalnum():
    print("Username must contain only letters and numbers")
elif not username.isspace():
        print("Username must not contain spaces")
else:
    print(f"Your username is {username}")