import random

logo = """
 ▗▄▄▖█  ▐▌▗▞▀▚▖ ▄▄▄  ▄▄▄        ■  ▐▌   ▗▞▀▚▖    ▗▖  ▗▖█  ▐▌▄▄▄▄  ▗▖   ▗▞▀▚▖ ▄▄▄ 
▐▌   ▀▄▄▞▘▐▛▀▀▘▀▄▄  ▀▄▄      ▗▄▟▙▄▖▐▌   ▐▛▀▀▘    ▐▛▚▖▐▌▀▄▄▞▘█ █ █ ▐▌   ▐▛▀▀▘█    
▐▌▝▜▌     ▝▚▄▄▖▄▄▄▀ ▄▄▄▀       ▐▌  ▐▛▀▚▖▝▚▄▄▖    ▐▌ ▝▜▌     █   █ ▐▛▀▚▖▝▚▄▄▖█    
▝▚▄▞▘                          ▐▌  ▐▌ ▐▌         ▐▌  ▐▌           ▐▙▄▞▘          
                               ▐▌                                                
                                                                                 
                                                                                 """
print(logo)
print("Welcome to the Guessing Game!")

number_to_guess = random.randint(1, 100)
print(f"Pssst, the correct answer is {number_to_guess}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return 10
    else:
        return 5
attempts_remaining = set_difficulty()
def check_answer(guess, answer, attempts):
    if guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return attempts
while attempts_remaining > 0:
    print(f"You have {attempts_remaining} attempts remaining to guess the number.")
    player_guess = int(input("Make a guess: "))
    attempts_remaining = check_answer(player_guess, number_to_guess, attempts_remaining)
    if player_guess == number_to_guess:
        break
    elif attempts_remaining == 0:
        print("You've run out of guesses, you lose.")
    else:
        print("Guess again.")
