import random
import string

def generate_password(length=12):
    # Define character sets for password generation
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure at least one character from each set is included in the password
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Generate remaining characters for the password
    password.extend(random.choice(all_characters) for _ in range(length - 4))

    # Shuffle the characters to make the password more random
    random.shuffle(password)

    # Convert the list of characters into a string
    password_str = ''.join(password)

    return password_str

if __name__ == "__main__":
    # Generate a password with default length of 12 characters
    password = generate_password()
    print("Generated Password:", password)
