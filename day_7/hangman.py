#Import random module
import random
from hangman_words import animals

#Start of the game Hangman
print("Welcome to Hangman!")
print("Guess the animal name!\n")

#Select a random animal name from the list
guess_random_animal = random.choice(animals)

placeholder = ""
word_length = len(guess_random_animal)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
used_latters = []
number_of_attempts = 6

while not game_over:

    #User input for guessing a letter
    user_guess = input("Guess a letter: ").lower()

    #Allow the user 6 attempts to guess the animal name
    display = ""
    for letter in guess_random_animal:        
        if letter == user_guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
    
        else:
            display += "_"
            used_latters.append(user_guess)

    if user_guess not in guess_random_animal:
        number_of_attempts -= 1
        print(f"Wrong guess. You have {number_of_attempts} attempts left.")
        if number_of_attempts == 0:
            game_over = True
            print(f"Game Over! The correct animal name was '{guess_random_animal}'.")
            break
    print(display)
    if "_" not in display:
        game_over = True
        print("Congratulations! You've guessed the animal name correctly.")
