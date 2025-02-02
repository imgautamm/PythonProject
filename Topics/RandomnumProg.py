#Randomnumbers

import random

#print(help(random))

low = 1
high = 6
options = ("rock", "paper", "scissors")
cards = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]

#number = random.randint(1, 6)
#number = random.random()
#option = random.choice(options)
random.shuffle(cards)
print(cards)
