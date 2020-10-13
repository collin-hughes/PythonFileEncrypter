import json
import os.path
import getpass
from os import path
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from enum import Enum

class PwordManager(Enum):
    NEW = 0
    UPDATE = 1
    VIEW = 2

def Run(key):
    passManager = True
    
    while(passManager):
        for item in list(PwordManager):
            print(item.value, "|", (item.name).capitalize())
                
        choice = input("Enter an option or 'Q' to quit: ")
                
        if choice == "q" or choice == "Q":
            passManager = False
            print("Exiting...")

        elif int(choice) == 0:
            print("Loading entry creator...")
            CreateNewPasswordEntry(key)

        elif int(choice) == 1:
            print("Loading entry updater...")

        elif int(choice) == 2:
            print("Loading entry viewer...")
            ViewPasswordFile(key)

        else:
            print("Invalid choice!")

def CreateNewPasswordEntry(key):
    service = input("Enter name of service: ")
    username = input("Enter username for service: ")
    password = getpass.getpass("Enter password for service: ")

    newEntry = {
        "service" : service,
        "username" : username,
        "password" : password
    }

    if(path.exists("/config/entries.json") and path.exists("/config/entriesconfig.json")):
        print("Entries file already exists. Adding new entry...")

        with open("entriesconfig.json") as f:
            data = json.load(f)

            nonce = b64decode(data["nonce"])
            tag = b64decode(data["tag"])

        #cipher = AES.new(key.encode("utf-8"), AES.MODE_EAX, nonce)
        cipher = AES.new(key, AES.MODE_EAX, nonce)

        with open("entries.json", "rb") as f:
            data = f.read()

            data = cipher.decrypt_and_verify(data, tag).decode("utf-8")
            data = json.loads(data)

        with open("entries.json", "w") as f:
            json.dump(data, f)

        with open("entries.json") as f:
            data = json.load(f)

            entries = data["entries"]

            entries.append(newEntry)

        with open("entries.json", "w") as f:
            json.dump(data, f)

        #cipher = AES.new(key.encode("utf-8"), AES.MODE_EAX)
        cipher = AES.new(key, AES.MODE_EAX)

        with open("entries.json", "rb") as f:
            data = f.read()

        ciphertext, tag = cipher.encrypt_and_digest(data)

        with open("entries.json", "wb") as f:
            f.write(ciphertext)

        configOptions = {
            "nonce" : b64encode(cipher.nonce).decode("utf-8"),
            "tag" : b64encode(tag).decode('utf-8') 
        }

        with open("/config/entriesconfig.json", "w") as f:
            json.dump(configOptions, f)        
        
    else:
        print("Entries file does not exists. Creating entries file...")

        CreatePasswordFile(newEntry, key)

def CreatePasswordFile(newEntry, key):
    newDictionary = {
        "entries" : [newEntry]
    }

    with open("/config/entries.json", "w") as f:
        json.dump(newDictionary, f)
    
    #cipher = AES.new(key.encode("utf-8"), AES.MODE_EAX)
    cipher = AES.new(key, AES.MODE_EAX)

    with open("/config/entries.json", "rb") as f:
        data = f.read()

    ciphertext, tag = cipher.encrypt_and_digest(data)

    with open("/config/entries.json", "wb") as f:
        f.write(ciphertext)

    configOptions = {
        "nonce" : b64encode(cipher.nonce).decode("utf-8"),
        "tag" : b64encode(tag).decode('utf-8') 
    }

    with open("/config/entriesconfig.json", "w") as f:
        json.dump(configOptions, f)

def ViewPasswordFile(key):
    if(path.exists("entries.json") and path.exists("entriesconfig.json")):
        print("Entries file already exists. Adding new entry...")

        with open("entriesconfig.json") as f:
            data = json.load(f)

            nonce = b64decode(data["nonce"])
            tag = b64decode(data["tag"])

        cipher = AES.new(key, AES.MODE_EAX, nonce)

        with open("entries.json", "rb") as f:
            data = f.read()

            data = cipher.decrypt_and_verify(data, tag).decode("utf-8")
            data = json.loads(data)

            for entry in data:
                print(data[entry])

        
