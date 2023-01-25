from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import randint, choice 


def safe_pass() -> str:
    # Set variable responible for password length
    n = randint(2, 4)

    # Choose random characters of all kind and create random password at least 8 characters long 
    return ''.join([''.join([choice(ascii_lowercase), choice(ascii_uppercase), choice(digits), choice(punctuation)]) for _ in range(n)])
