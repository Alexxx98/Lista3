from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits
from random import randint 


def safe_pass() -> str:
    # Define special symbols
    special_symbols = "@#$%&" 
    
    # Prepare all characters needed to create a safe password
    characters = ascii_letters + digits + special_symbols

    # Get length of characters string
    char_len = len(characters)

    # Set password length
    pass_len = randint(8, 16)

    # Set safety status to False
    is_safe = False

    # Repeat password creation, until it's safe 
    while is_safe != True:
        password = [characters[randint(0, char_len - 1)] for _ in range(pass_len)]

        # Set safety checkers to False
        is_lower = False
        is_upper = False
        is_digit = False
        is_special_symbol = False

        for i in range(pass_len):
            if password[i] in ascii_lowercase:
                is_lower = True
            elif password[i] in ascii_uppercase:
                is_upper = True
            elif password[i] in digits:
                is_digit = True
            elif password[i] in special_symbols:
                is_special_symbol = True
        
        if is_lower and is_upper and is_digit and is_special_symbol:
            is_safe = True
    
    return "".join(password)