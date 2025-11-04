import random

logo = """  
888     888                888       d8b                888      
888     888                888       Y8P                888      
888     888                888                          888      
88888b. 888 8888b.  .d8888b888  888 8888 8888b.  .d8888b888  888 
888 "88b888    "88bd88P"   888 .88P "888    "88bd88P"   888 .88P 
888  888888.d888888888     888888K   888.d888888888     888888K  
888 d88P888888  888Y88b.   888 "88b  888888  888Y88b.   888 "88b 
88888P" 888"Y888888 "Y8888P888  888  888"Y888888 "Y8888P888  888 
                                     888                         
                                    d88P                         
                                  888P"                          """

print(logo)

list_of_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_hand = []
computer_hand = []
def deal_card():
    """Returns a random card from the list."""
    return random.choice(list_of_cards)
def calculate_score(hand):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)
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
def blackjack():
    for _ in range(2):
        my_hand.append(deal_card())
        computer_hand.append(deal_card())
    
    game_over = False
    
    while not game_over:
        user_score = calculate_score(my_hand)
        computer_score = calculate_score(computer_hand)
        print(f"   Your cards: {my_hand}, current score: {user_score}")
        print(f"   Computer's first card: {computer_hand[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                my_hand.append(deal_card())
            else:
                game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)
    
    print(f"   Your final hand: {my_hand}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(compare(user_score, computer_score))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    my_hand = []
    computer_hand = []
    blackjack()