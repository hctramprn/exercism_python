from string import ascii_lowercase

# Check if two numbers are coprime
def is_coprime(a, m):
    while m != 0:
        a, m = m, a % m
    return a == 1

# Encode the plain text using an affine cipher
def encode(plain_text, a, b):
    # Check if a and len(ascii_lowercase) are coprime
    if is_coprime(a, len(ascii_lowercase)):
        characters = ''
        # Remove spaces from the plain text
        plain_text = plain_text.replace(' ', '')
        # Loop for each character in plain text
        for char in plain_text:
            if char.lower() in ascii_lowercase:
                x = ascii_lowercase.index(char.lower())
                # Apply the encoding operation of the affine cipher
                new_index = (a * x + b) % len(ascii_lowercase)
                new_char = ascii_lowercase[new_index]
                characters += new_char
            elif char.isdigit():
                characters += char
            else:
                continue

        # Split the encoded characters into groups of 5
        characters_lst = [characters[i:i+5] for i in range(0, len(characters), 5)]
        # Return the encoded string
        return ' '.join(characters_lst)
    else:
        raise ValueError("a and m must be coprime.")

# Decode the ciphered text using an affine cipher
def decode(ciphered_text, a, b):
    # Check if a and len(ascii_lowercase) are coprime
    if is_coprime(a, len(ascii_lowercase)):
        mmi = 0
        # Find the modular multiplicative inverse (mmi) of a
        for x in range(1, len(ascii_lowercase)):
            if (a * x) % len(ascii_lowercase) == 1:
                mmi = x
                break

        characters = ''
        # Remove spaces from the ciphered text
        ciphered_text = ciphered_text.replace(' ', '')
        for char in ciphered_text:
            if char.lower() in ascii_lowercase:
                y = ascii_lowercase.index(char.lower())
                # Apply the decoding operation of the affine cipher
                original_index = mmi * (y - b) % len(ascii_lowercase)
                original_char = ascii_lowercase[original_index]
                characters += original_char
            elif char.isdigit():
                characters += char
            else:
                continue

        # Return the decoded string
        return characters
    else:
        raise ValueError("a and m must be coprime.")
