import random

logo = """
 ▗▄▄▖█  ▐▌▗▞▀▚▖ ▄▄▄  ▄▄▄        ■  ▐▌   ▗▞▀▚▖    ▗▖  ▗▖█  ▐▌▄▄▄▄  ▗▖   ▗▞▀▚▖ ▄▄▄ 
▐▌   ▀▄▄▞▘▐▛▀▀▘▀▄▄  ▀▄▄      ▗▄▟▙▄▖▐▌   ▐▛▀▀▘    ▐▛▚▖▐▌▀▄▄▞▘█ █ █ ▐▌   ▐▛▀▀▘█    
▐▌▝▜▌     ▝▚▄▄▖▄▄▄▀ ▄▄▄▀       ▐▌  ▐▛▀▚▖▝▚▄▄▖    ▐▌ ▝▜▌     █   █ ▐▛▀▚▖▝▚▄▄▖█    
▝▚▄▞▘                          ▐▌  ▐▌ ▐▌         ▐▌  ▐▌           ▐▙▄▞▘          
                               ▐▌                                                
                                                                                 
                                                                                 """
# Welcome message
print(logo)
print("\n" + "=" * 50 + "\n")
print("Welcome to the Guessing Game!\n")
print("=" * 50 + "\n")
print("I'm thinking of a number between 1 and 100.")

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)
#print(f"Pssst, the correct answer is {number_to_guess}")

# Function to set difficulty level
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': \n").lower()
    print("\n" + "x" * 50 + "\n")
    if level == "easy":
        return 10
    else:
        return 5
attempts_remaining = set_difficulty()

# Function to check the player's guess
def check_answer(guess, answer, attempts):
    if guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print("\n" + "$" * 50 + "\n")
        print(f"!!! You got it! The answer was {answer} !!!")
        print("\n" + "$" * 50 + "\n")
        return attempts

# Game loop
while attempts_remaining > 0:
    print(f"You have {attempts_remaining} attempts remaining to guess the number.")
    player_guess = int(input("Make a guess: "))
    attempts_remaining = check_answer(player_guess, number_to_guess, attempts_remaining)
    if player_guess == number_to_guess:
        break
    elif attempts_remaining == 0:
        print("You've run out of guesses, you lose.")
    else:
        print("Guess again." + "\n" + "x" * 50 + "\n")
