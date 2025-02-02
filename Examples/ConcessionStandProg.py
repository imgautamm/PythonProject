#Concession stand Program for Dictionary

menu = {"hotdog":2.50,
        "popcorn":3.00,
        "soda":1.50,
        "candy":2.00,
        "water":1.00,
        "chips":1.50}

cart = []
total = 0

print("---------MENU---------")
for key, value in menu.items():
    print(f"{key:10} - ${value:.2f}")
print("----------------------")

while True:
        food = input("Select an Item (q to quit): ").lower()
        if food == "q":
            break
        elif menu.get(food) is not None:
                cart.append(food)

print("---------YOUR ORDER---------")
for food in cart:
    total += menu.get(food)
    print (food, end="\n")

print("---------RECEIPT---------")

print(f"Total: ${total:.2f}")
