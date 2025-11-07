# Coffee Machine Program with Animated Progress Bar

# Imports
import sys
import time
import os

# Dictionary holding menu data for different coffee types and their ingredients/costs
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 2.0,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 3.0,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 4.5,
    }
}

# Starting resources in the coffee machine
STARTING_RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

# Coffee machine start sequence
def coffee_machine_start_sequence():
    print("Starting the coffee machine...")
    animate_progress_bar(duration=3)
    clear_screen()
    print("Coffee machine is ready to use!")



# Reset resources to starting values
def reset_resources():
    global resources
    resources = STARTING_RESOURCES.copy()
    print("Resources have been reset to starting values.")

# Initial resources in the coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

# Print current resource report
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")

# Check if resources are sufficient for the order
def is_resource_sufficient(order_ingredients):
    """Returns True if resources are sufficient to make the drink or False if not."""
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# Process coins inserted by the user
def get_coin_input(prompt):
    while True:
        try:
            value = input(prompt)
            return float(value) if value else 0.0
        except ValueError:
            print("Invalid input. Please enter a number or press Enter to skip.")

# Process coins and calculate total inserted money
def process_coins():
    print("Please insert coins. Press Enter to skip any coin type.")
    quarters = get_coin_input("How many quarters? ") * 0.25
    dimes = get_coin_input("How many dimes? ") * 0.10
    nickels = get_coin_input("How many nickels? ") * 0.05
    pennies = get_coin_input("How many pennies? ") * 0.01
    total = round(quarters + dimes + nickels + pennies, 2)
    print(f"Total inserted: ${total}")
    return total

# Check if the transaction is successful
def is_transaction_successful(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
    resources["money"] += drink_cost
    return True

# def make_coffee(drink_name, order_ingredients):
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
    
#     print(f"Preparing your {drink_name}...")
#     for percent in range(0, 101, 10):
#         time.sleep(0.5)  # Simulates time delay
#         sys.stdout.write(f"\rProgress: {percent}%")
#         sys.stdout.flush()
#     print("\nHere is your {0}. Enjoy!".format(drink_name))

# Animated progress bar for coffee preparation
def animate_progress_bar(duration=2, steps=20):
    for i in range(steps + 1):
        percent = int((i / steps) * 100)
        bar = '█' * i + '-' * (steps - i)
        sys.stdout.write(f'\rPreparing: |{bar}| {percent}%')
        sys.stdout.flush()
        time.sleep(duration / steps)
    print()  # Move to next line after completion

# Make the coffee and update resources
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    
    print(f"Preparing your {drink_name}...")
    animate_progress_bar(duration=3)  # 3 seconds total
    print(f"Here is your {drink_name}. Enjoy!")

# Clear the console screen when coffee machine is turned off
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Main coffee machine function
# def coffee_machine():
#     while True:
#         choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
#         if choice == "off":
#             print("Turning off the coffee machine. Goodbye!")
#             animate_progress_bar(duration=3)
#             clear_screen()
#             break
#         elif choice == "report":
#             print_report()
#         elif choice in MENU:
#             drink = MENU[choice]
#             if is_resource_sufficient(drink["ingredients"]):
#                 payment = process_coins()
#                 if is_transaction_successful(payment, drink["cost"]):
#                     make_coffee(choice, drink["ingredients"])
#         else:
#             print("Invalid selection. Please choose espresso, latte, or cappuccino.")

def coffee_machine():
    coffee_machine_start_sequence()
    drink_options = {
        "1": "espresso",
        "2": "latte",
        "3": "cappuccino"
    }

    while True:
        print("\nPlease choose your drink:")
        for key, drink in drink_options.items():
            price = MENU[drink]["cost"]
            print(f'Press "{key}" for {drink} with price ${price}')
        print('Press "4" to view machine status')
        print('Press "5" to turn off the machine')
        print('Press "6" to reset machine resources')

        choice = input("Your selection: ").lower()

        if choice == "5":
            print("Turning off the coffee machine. Goodbye!")
            animate_progress_bar(duration=3)
            clear_screen()
            break
        elif choice == "4":
            print_report()
        elif choice == "6":
            reset_resources()
        elif choice in drink_options:
            drink_name = drink_options[choice]
            drink = MENU[drink_name]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(drink_name, drink["ingredients"])
        else:
            print("Invalid selection. Please choose a valid number or command.")

# Run the coffee machine
coffee_machine()