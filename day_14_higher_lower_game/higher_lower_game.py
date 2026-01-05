import random
import os
import time
import game_data

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

LOGO = """
                                                               
                                                               
.   .         .                      .                         
|   |  o      |                      |                         
|---|  .  .-..|--. .-. .--.   ____   |    .-..  .    ._.-. .--.
|   |  | (   ||  |(.-' |             |   (   )\  \  / (.-' |   
'   '-' `-`-`|'  `-`--''             '---'`-'  `' `'   `--''   
          ._.'                                                 
                                                               
"""

#
DIV = "-" * 60

# Format imported data for display
def format_data(account):
    """Takes the account data and returns the printable format (without follower count)."""
    return f"{account['name']}, a {account['description']}, from {account['country']}"

# Check if user is correct
def check_answer(guess, a_followers, b_followers):
    """Returns True if user guess is correct."""
    if a_followers > b_followers:
        return guess == 'a'
    return guess == 'b'

def play_round():
    score = 0
    account_b = random.choice(game_data.data)

    while True:
        account_a = account_b
        account_b = random.choice(game_data.data)
        while account_a == account_b:
            account_b = random.choice(game_data.data)

        clear_screen()
        print(LOGO)
        print(f"Score: {score}")
        print(DIV)
        print(f"Compare A: {format_data(account_a)}")
        print("     VS")
        print(f"Compare B: {format_data(account_b)}")
        print(DIV)

        # input validation
        guess = ""
        while guess not in ("a", "b"):
            guess = input("Who has more followers? Type 'A' or 'B': ").strip().lower()

        a_count = account_a['follower_count']
        b_count = account_b['follower_count']
        is_correct = check_answer(guess, a_count, b_count)

        clear_screen()
        print(LOGO)

        # reveal counts and result
        print(DIV)
        print(f"A: {format_data(account_a)} — Followers: {a_count}")
        print(f"B: {format_data(account_b)} — Followers: {b_count}")
        print(DIV)

        if is_correct:
            score += 1
            print(f"✅ Correct! Current score: {score}")
            time.sleep(2.0)
        else:
            print(f"❌ Wrong. Final score: {score}")
            break

    return

def main():
    clear_screen()
    print(LOGO)
    print("Welcome to the Higher Lower Game!\n")
    time.sleep(0.8)

    while True:
        play_round()
        again = ""
        while again not in ("y", "n"):
            again = input("\nPlay again? (y/n): ").strip().lower()
        if again == "n":
            clear_screen()
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()

