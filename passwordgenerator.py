import random
import string

def generate_password(length):
    # Define the character sets to use in the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Combine all character sets
    all_characters = lower + upper + digits + special

    # Ensure the password has at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random characters
    if length > 4:
        password.extend(random.choice(all_characters) for _ in range(length - 4))

    # Shuffle the list to prevent a predictable pattern
    random.shuffle(password)

    # Join the list into a single string
    return ''.join(password)

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired length for the password: "))
        if length < 4:
            print("Password length should be at least 4 characters.")
        else:
            password = generate_password(length)
            print("Generated password:", password)
    except ValueError:
        print("Please enter a valid number.")
