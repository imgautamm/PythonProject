import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
}

dice = []
total =0
num_of_dice = int(input("Enter the number of dice: "))

#random.randint(1,6)

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

#print the dice in differnt lines
#for die in range(num_of_dice):
#   for line in dice_art.get(dice[die]):
#       print(line)

#print the dice in same line
for line in range (5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

 #Calculate the total
for die in dice:
    total+=die

print(f"total: {total}")
