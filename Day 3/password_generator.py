import random
import string

def generate_strong_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4")

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    characters = string.ascii_letters + string.digits + string.punctuation

    for _ in range(length - 4):
        password.append(random.choice(characters))

    random.shuffle(password)

    return ''.join(password)

# Example usage
print(generate_strong_password(16))
