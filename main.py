import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special_chars=True):
    """Generates a random password with the specified length and character set."""

    # Define possible characters to include in the password
    lowercase_chars = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    uppercase_chars = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = string.digits                    # '0123456789'
    special_chars = string.punctuation         # '!@#$%^&*()_+-=[]{}|;:",.<>?/~`'

    # Start with lowercase characters
    char_pool = lowercase_chars

    # Add other character sets based on user preferences
    if use_uppercase:
        char_pool += uppercase_chars
    if use_digits:
        char_pool += digits
    if use_special_chars:
        char_pool += special_chars

    # Make sure we have enough variety of characters in the pool
    if not char_pool:
        print("Error: No character set selected!")
        return None

    # Generate the password by randomly selecting characters from the pool
    password = ''.join(random.choice(char_pool) for _ in range(length))

    return password

def main():
    print("Password Generator")

    # Get the desired password length from the user
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Password length must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Ask user for character preferences
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    # Generate and display the password
    password = generate_password(length, use_uppercase, use_digits, use_special_chars)

    if password:
        print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
