from encodings.punycode import T
from os import name


print("Welcome to the secret auction program.")
name = input("What is your name?: ")
bid = int(input("What is your bid?: $"))

auction_dict = {}
auction_dict[name] = bid
more_bidders = ""
while True :
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bidders == "yes":
        print("\n" * 100)
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        auction_dict[name] = bid
    else:
        break

highest_bid = 0
winner = ""
for bidder in auction_dict:
    bid_amount = auction_dict[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
print(f"The winner is {winner} with a bid of ${highest_bid}")
