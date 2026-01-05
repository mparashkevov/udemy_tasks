import random

user_cards = []
computer_cards = []
computer_score = -1
user_score = -1

# Choose a random card from the deck
def deal_card():
    list_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(list_of_cards)
    return card

# Deal the initial cards
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# Calculate the score
def calculate_score(score):
    # Check for a blackjack (a hand with only 2 cards: ace + 10)
    if sum(score) == 21 and len(score) == 2:
        return 0
    # Check for an 11 (ace). If the score is over 21, remove the 11 and replace it with a 1
    if 11 in score and sum(score) > 21:
        score.remove(11)
        score.append(1)
    return sum(score)

# Initialize hands
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f"   Your cards: {user_cards}, current score: {user_score}")
print(f"   Computer's first card: {computer_cards[0]}")

game_over = False
while not game_over:
    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(f"   Your cards: {user_cards}, current score: {user_score}")
        else:
            game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
print(f"   Your final hand: {user_cards}, final score: {user_score}")
print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "Win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"
print(compare(user_score, computer_score))
while input("Do you want to play a game of Blackjack? Type 'y' or ' n': ") == 'y':
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    game_over = False
    while not game_over:
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                print(f"   Your cards: {user_cards}, current score: {user_score}")
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    
