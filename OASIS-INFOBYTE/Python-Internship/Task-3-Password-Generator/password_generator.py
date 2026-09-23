import random
import string

print("===== RANDOM PASSWORD GENERATOR =====")

while True:
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Error: Password length must be at least 8 characters.")
            continue

        print("\nChoose character types:")
        print("1. Uppercase letters")
        print("2. Lowercase letters")
        print("3. Numbers")
        print("4. Symbols")

        choices = input(
            "Enter your choices separated by spaces (example: 1 2 3 4): "
        ).split()

        if len(choices) < 2:
            print("Error: Please select at least 2 character types.")
            continue

        characters = ""

        if "1" in choices:
            characters += string.ascii_uppercase

        if "2" in choices:
            characters += string.ascii_lowercase

        if "3" in choices:
            characters += string.digits

        if "4" in choices:
            characters += string.punctuation

        invalid_choices = [choice for choice in choices if choice not in ["1", "2", "3", "4"]]

        if invalid_choices:
            print("Error: Please choose only 1, 2, 3, or 4.")
            continue

        password = "".join(random.choice(characters) for _ in range(length))

        print("\nGenerated Password:", password)

        again = input("\nGenerate another password? (yes/no): ").lower()

        if again != "yes":
            print("Thank you for using the Password Generator!")
            break

    except ValueError:
        print("Error: Please enter a valid number.")
        