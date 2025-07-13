import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password has at least one of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest with random choices
    all_chars = lowercase + uppercase + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the result
    random.shuffle(password)

    return "".join(password)

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            password = generate_password(length)
            print(f"Generated Password: {password}")
        except ValueError:
            print("Please enter a valid number.")

        choice = input("Generate another password? (yes/no): ").lower()
        if choice != 'yes':
            print("Thank you for using the password generator!")
            break

# Run the program
if __name__ == "__main__":
    main()
