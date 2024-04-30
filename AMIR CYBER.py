# Define the substitution cipher key
key = {'a': '3', 'b': '8', 'c': '1', 'd': '5', 'e': '7',
       'f': '0', 'g': '9', 'h': '2', 'i': '4', 'j': '6',
       'k': 'x', 'l': 'y', 'm': 'z', 'n': 'm', 'o': 'n',
       'p': 'o', 'q': 'p', 'r': 'q', 's': 'r', 't': 's',
       'u': 't', 'v': 'u', 'w': 'v', 'x': 'w', 'y': 'k',
       'z': 'l', ' ': ' '}

# Encrypt function using the substitution cipher
def encrypt(message):
    encrypted_message = ""
    for char in message.lower():
        encrypted_message += key.get(char, char)
    return encrypted_message

# Decrypt function (assuming you know the key for decryption)
def decrypt(encrypted_message):
    decrypted_message = ""
    reverse_key = {v: k for k, v in key.items()}  # Reverse the key for decryption
    for char in encrypted_message.lower():
        decrypted_message += reverse_key.get(char, char)
    return decrypted_message

# Example usage
message = "math is fun"
encrypted = encrypt(message)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted)
print("Decrypted:", decrypted)
