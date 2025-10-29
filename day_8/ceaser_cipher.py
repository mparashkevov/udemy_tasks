#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = [chr(i) for i in range(97, 123)]  # Generates ['a' to 'z']

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter  # Keep non-alphabet characters unchanged
    print(f"The encoded text is:\n{cipher_text}")

def decrypt(plain_text, shift_amount):
    decrypt_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift_amount) % 26
            decrypt_text += alphabet[new_position]
        else:
            decrypt_text += letter
    print(f"The decoded text is:\n{decrypt_text}")

def program():
    while True:
        action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        plain_text = input("Enter your message:\n").lower()
        shift_amount = int(input("Enter shift amount:\n"))
        if action == "decode":
            decrypt(plain_text, shift_amount)
        elif action == "encode":
            encrypt(plain_text, shift_amount)
        else:
            print("Invalid action. Please type 'encode' or 'decode'.")
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if restart != "yes":
            print("Goodbye")
            break

program()
