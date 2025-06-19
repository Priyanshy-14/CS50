import random

def generate_password(length):
    if length < 4:
        return "Password length must be at least 4"

    # Define character sets manually
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special_chars = "!@#$%^&*()"

    # Ensure at least one character from each set
    upper = random.choice(uppercase)
    lower = random.choice(lowercase)
    digit = random.choice(digits)
    special = random.choice(special_chars)

    all_chars = uppercase + lowercase + digits + special_chars
    remaining = [random.choice(all_chars) for _ in range(length - 4)]

    password_list = list(upper + lower + digit + special + "".join(remaining))
    random.shuffle(password_list)

    return ''.join(password_list)

length = 12
print("Generated Password:", generate_password(length))
