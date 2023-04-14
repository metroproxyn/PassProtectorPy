"""
This file was created for testing the cryptography module,
if you had any issues with installing it previously.
"""
from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Create a Fernet object with the key
fernet = Fernet(key)

# Encrypt a message
message = b"Hello, world!"
encrypted = fernet.encrypt(message)

# Decrypt the message
decrypted = fernet.decrypt(encrypted)

# Print the original message and the decrypted message
print("Original message: ", message)
print("Decrypted message: ", decrypted)