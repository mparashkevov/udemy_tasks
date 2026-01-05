programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}
# Adding a new item with user prompt to the dictionary
programming_dictionary["Variable"] = "A container for a value that can change."
print()

# Retrieving an item from the dictionary
print(programming_dictionary)
print()

# Wipeing an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)
# print()

# Editing an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)
print()

# Adding a user input to the dictionary
# user_key = input("Enter a new programming term: ")
# user_value = input("Enter the definition of the term: ")
# programming_dictionary[user_key] = user_value
# print(programming_dictionary)
# print()

# Looping through a dictionary
for key in programming_dictionary:
    print(f"{key}: {programming_dictionary[key]}")