from Crypto.Cipher import AES

key = b'\xff,:\x94\xc4\xd7\xda8\xbc-\xb5\x97\xa8\x84\xd9\x93'
file_in = open("encrypted.bin", "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]


# let's assume that the key is somehow available again
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)

print(data)