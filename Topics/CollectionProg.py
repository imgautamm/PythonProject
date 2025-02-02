#Collection
#1. List  => []     => Mutable  => Duplicate
#2. Tuple => ()    => Immutable => Duplicate
#3. Set  => {}   => Mutable => Unique
#4. Dictionary => {key:value} => Mutable => Unique


fruits = ['apple','banana','cherry','dates','apple','banana','cherry','dates']
#print (dir(fruits))
#print(len(fruits))
#print(fruits)
#print(fruits[::3])
#print(fruits[1:5])
#print("apple" in fruits)

#fruits.append('grapes')
#fruits.insert(0,'grapes')
#fruits.clear()
#print(fruits.index("banana"))
#print(fruits.count('apple'))
for fruit in fruits:
    print(fruit)