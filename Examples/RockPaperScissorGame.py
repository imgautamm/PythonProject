#Rock Paper Scissor Game
import random

options = ("rock", "paper", "scissors")

running = True

while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter rock, paper, or scissors: ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("Player wins!")
    elif player == "paper" and computer == "rock":
        print("Player wins!")
    elif player == "scissors" and computer == "paper":
        print("Player wins!")
    else:
        print("Computer wins!")

    play_again =input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        running = False
print("Goodbye!")