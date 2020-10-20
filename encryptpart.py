import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from random import randint
import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

password = 'potato'
data_str = b"test"
##Change salt to not be random  
salt = get_random_bytes(16)
key = scrypt(password, salt, 16, N=2**14, r=8, p=1)


cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data_str)

print(key)

file_out = open("encrypted.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
file_out.close()




