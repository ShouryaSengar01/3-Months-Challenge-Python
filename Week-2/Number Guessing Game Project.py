lowest = 1
highest = 100
answer = random.randint(lowest, highest)
number = random.randint(lowest, highest)
guesses = 0
is_running = True

print("Python Number Guessing Game")
choice = input("Press 'Y' to Start the Game else press 'N'")

if choice == "Y":
    print(f"Select a Number between {lowest} and {highest}")
    while is_running:
        guess = input("Enter your Guess: ")

        if guess.isdigit():
            guess = int(guess)
            guesses +=1

            if guess < lowest or guess > highest:
                print(f"That Number is out of range.\nPlease Select a Number between {lowest} and {highest}")
            elif guess < answer:
                print("LOW!!!")
            elif guess > answer:
                print("HIGH!!!")
            else:
                print(f"BRAVO! The Number was {answer}")
                print(f"Number of guesses: {guesses}")
                is_running = False        
        else:
            print(f"{guess} is not a number")
            print(f"Please Select a Number between {lowest} and {highest}")
else:
    exit()
