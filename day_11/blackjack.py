import random
import os
from time import sleep

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_cards(hand, hide_first=False):
    """Print cards in a more visual way"""
    if hide_first:
        return f"[X, {hand[1]}]"
    return str(hand)

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(hand):
    """Calculate score with ace handling"""
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # Blackjack
    
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
    return sum(hand)

def display_game_state(player_hand, dealer_hand, player_score, hide_dealer=True):
    """Display current game state"""
    print("\n" + "="*50)
    print(f"Your hand: {print_cards(player_hand)} (Score: {player_score})")
    if hide_dealer:
        print(f"Dealer's hand: {print_cards(dealer_hand, True)}")
    else:
        print(f"Dealer's hand: {print_cards(dealer_hand)} (Score: {calculate_score(dealer_hand)})")
    print("="*50 + "\n")

def play_blackjack():
    clear_screen()
    print(logo)
    print("\nWelcome to Blackjack!")
    sleep(1)

    player_hand = []
    dealer_hand = []
    game_over = False

    # Initial deal
    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        display_game_state(player_hand, dealer_hand, player_score)

        # Check for early game over conditions
        if player_score == 0:
            print("Blackjack! You win! 🎉")
            break
        if player_score > 21:
            print("Bust! You went over 21. You lose! 😢")
            break

        # Player's turn
        action = input("\nWhat would you like to do? (h)it or (s)tand: ").lower()
        if action == 'h':
            player_hand.append(deal_card())
            clear_screen()
            print(logo)
        elif action == 's':
            game_over = True

    # Dealer's turn
    if player_score <= 21:
        print("\nDealer's turn...")
        sleep(1)
        
        while calculate_score(dealer_hand) < 17:
            print("Dealer hits...")
            dealer_hand.append(deal_card())
            sleep(1)
            display_game_state(player_hand, dealer_hand, player_score, False)

        dealer_score = calculate_score(dealer_hand)
        print("\nFinal Results:")
        display_game_state(player_hand, dealer_hand, player_score, False)

        # Determine winner
        if dealer_score > 21:
            print("Dealer busts! You win! 🎉")
        elif dealer_score == player_score:
            print("It's a tie! 🤝")
        elif dealer_score > player_score:
            print("Dealer wins! 😢")
        else:
            print("You win! 🎉")

    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again == 'y':
        clear_screen()
        play_blackjack()

if __name__ == "__main__":
    play_blackjack()