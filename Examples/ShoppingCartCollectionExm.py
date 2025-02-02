#Shopping cart example of collection

foods = ['apple', 'banana', 'orange', 'grape', 'mango']
prices = [1, 2, 3, 4, 5]
total = 0

while True:
    print('Foods:')
    for i in range(len(foods)):
        print(i, foods[i], prices[i])
    print('Total:', total)
    print('Enter the food index to add to cart or -1 to checkout')
    index = int(input())
    if index == -1:
        break
    total += prices[index]