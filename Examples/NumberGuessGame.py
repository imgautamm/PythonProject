#number guessing game

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = False

print ("Welcome to the number guessing game!")
print(f"Guess a number between {lowest_num} and {highest_num}")
while is_running == False:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print ("The number you entered is out of range.")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess > answer:
            print("Higher guess! TRY AGAIN!!")
        elif guess < answer:
            print("Lower guess! TRY AGAIN!!")
        else:
            print("CORRECT GUESS!")
            print(f"Number of guesses: {guesses}")
            is_running =False

    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")