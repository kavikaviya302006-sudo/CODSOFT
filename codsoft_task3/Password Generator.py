import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation


    if characters == "":
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print("========== PASSWORD GENERATOR ==========")

while True:
    try:
        length = int(input("Enter password length (minimum 4): "))
        if length < 4:
            print("Password length must be at least 4.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

print("\nChoose password complexity:")
use_upper = input("Include Uppercase letters? (y/n): ").lower() == 'y'
use_lower = input("Include Lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include Numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include Special Characters? (y/n): ").lower() == 'y'

count = int(input("\nHow many passwords do you want to generate?: "))

password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

if password is None:
    print("\nError: Please select at least one character type.")
else:
    print("\nGenerated Password(s):")
    for i in range(count):
        print(f"{i+1}. {generate_password(length, use_upper, use_lower, use_digits, use_symbols)}")
