from termcolor import colored
import random
print("WELCOME TO THE GAME OF ROCK PAPER AND SCISSORS")
options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a Choice(rock, paper , scissors): ")
    
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print(colored("It's a Tie", "blue" ))
    elif player == "rock" and computer == "scissors":
        print(colored("You've Won", "green"))
    elif player == "paper" and computer == "rock":
        print(colored("You've Won", "green"))
    elif player == "scissors" and computer == "rock":
        print(colored("You've Won", "green"))
    else:
        print(colored("You Lose", "red"))
    
    if not input("Play again? y/n\n=>").lower() == "y":
        running = False

print("Thanks For Playing, Have a Good Day.")
