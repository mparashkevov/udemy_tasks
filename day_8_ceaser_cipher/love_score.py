from os import name


name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

    true_count = sum(combined_names.count(letter) for letter in "true")
    love_count = sum(combined_names.count(letter) for letter in "love")

    love_score = int(f"{true_count}{love_count}")
    print(f"You calculated love score is {love_score}.")
    if (love_score < 10) or (love_score > 90):
        print("Your score is so low or so high, you go together like coke and mentos.")
    elif (40 <= love_score <= 50):
        print("Your score is average, you are alright together.")
    else:
        print("Your score is decent.")

calculate_love_score(name1, name2)