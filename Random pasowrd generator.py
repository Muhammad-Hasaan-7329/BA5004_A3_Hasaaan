import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 for complexity.")

    # Ensure at least one character from each category
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)

    # Fill the remaining characters
    remaining = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length - 4))

    # Combine and shuffle
    password_list = list(lowercase + uppercase + digit + symbol + remaining)
    random.shuffle(password_list)

    return ''.join(password_list)

# Display password requirements
print("Password Requirements:")
print("- Minimum length: 4 characters")
print("- Must include at least one lowercase letter")
print("- Must include at least one uppercase letter")
print("- Must include at least one digit")
print("- Must include at least one special character\n")

# Ask user for password length
try:
    user_length = int(input("Enter desired password length: "))
    password = generate_password(user_length)
    print("Generated password:", password)
except ValueError:
    print("Please enter a valid number greater than or equal to 4.")
