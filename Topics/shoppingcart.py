#shopping cart

item = input("what item would you like yo buy:")
price = float(input("what is the price of the item:"))
quantity = int(input("how many would you like to buy:"))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is ${total}")