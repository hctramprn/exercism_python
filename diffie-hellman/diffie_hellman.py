from random import choice

# returns a random private key grater than 1 and less than a given p
def private_key(p):
    key = choice(range(2, p))
    return key

# returns a public key given a private key, p and g
def public_key(p, g, private):
    pub_key = (g ** private) % p
    return pub_key

# returns a secret number with the other's person public key
def secret(p, public, private):
    sec = (public ** private) % p
    return sec
