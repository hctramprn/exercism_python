handshake = {0: 'jump', 1: 'close your eyes', 2: 'double blink', 3: 'wink'}


def commands(binary_str):
    secret_handshake = [handshake[i]
                        for i, num in enumerate(binary_str[1:]) if num == '1']

    if binary_str[0] == '1':
        return secret_handshake
    return secret_handshake[::-1]
