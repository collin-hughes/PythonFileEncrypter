from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# ==================================================
# HASHING
# Create a hash object
hash = SHA256.new()

# Message to be hashed
message = b"This is a message"

# Hash the message
hash.update(message)

# Print the original message
print(message.decode("utf-8"))

# Print the hashed message
print("This is the hashed message:", (hash.hexdigest()))

# ==================================================
# AES Encryption
# Generate a random key of 16 bytes
key = get_random_bytes(16)

# Create a EAX AES object
cipher = AES.new(key, AES.MODE_EAX)

# Encrypt the message and return the ciphertext and the tag
ciphertext, tag = cipher.encrypt_and_digest(message)

# Extract the nonce from the cipher
nonce = cipher.nonce

# Print the cipher text
print(ciphertext)

# Create a decryption EAX AES object
cipher = AES.new(key, AES.MODE_EAX, nonce)

# Print the decrypted message
print(cipher.decrypt_and_verify(ciphertext, tag).decode("utf-8"))

# ==================================================
# AES Encryption from File
textFileIn = open()