import json
import getpass
import string
import random
from os import path
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from enum import Enum

class PwordManager(Enum):
    GENERATE = 0
    NEW = 1
    UPDATE = 2
    VIEW = 3

def Run(key):
    passManager = True
    
    while(passManager):
        print("=" * 80)
        print("Password Manager Options:")
        for item in list(PwordManager):
            print(item.value, "|", (item.name).capitalize())

        print("=" * 80)        
        choice = input("Enter an option or 'Q' to quit: ")
        print("=" * 80)

        if choice == "q" or choice == "Q":
            passManager = False
            print("Exiting...")

        elif int(choice) == 0:
            print("Loading password generator...")

            length = int(input("Enter desired password length: "))
            
            incNums = input("Include numbers? (Y/N): ")

            if(incNums == 'y' or incNums == "Y"):
                incNums = True

            else:
                incNums = False
            
            incSym = input("Include symbols? (Y/N): ")

            if(incSym == 'y' or incSym == "Y"):
                incSym = True

            else:
                incSym = False
            
            print("=" * 80)
            print("Generated password:", GeneratePassword(length, incNums, incSym))

        elif int(choice) == 1:
            print("Loading entry creator...")
            CreateNewPasswordEntry(key)

        elif int(choice) == 2:
            print("Loading entry updater...")
            UpdateEntry(key)

        elif int(choice) == 3:
            print("Loading entry viewer...")
            ViewPasswordFile(key)

        else:
            print("Invalid choice!")

def CreateNewPasswordEntry(key, newEntry):
    data, exists = GetFileData(key)

    if(exists):
        entries = data["entries"]

        entries.append(newEntry)

        StoreFileData(key, data)

    else:
        CreatePasswordFile(newEntry, key)

def CreatePasswordFile(newEntry, key):
    newDictionary = {
        "entries" : [newEntry]
    }

    StoreFileData(key, newDictionary)

def GeneratePassword(length=16, numbers=True, symbols=True):
    password = ""
    
    if(numbers and symbols):
        possibilities = string.ascii_letters + string.punctuation + string.digits

    elif(numbers):
        possibilities = string.ascii_letters + string.digits

    elif(symbols):
        possibilities = string.ascii_letters + string.punctuation
        
    else:
        possibilities = string.ascii_letters

    for i in range(length):
        password += random.choice(possibilities)

    return password

def UpdateEntry(key):
    entryMap = ["service", "username", "password"]

    data, exists = GetFileData(key)

    if(exists):
        for i in range(len(data["entries"])):
            print("=" * 80)
            print("Entry", i)
            print("Service:", data["entries"][i]["service"])
            print("Username:", data["entries"][i]["username"])
            print("Password:", data["entries"][i]["password"])

        print("=" * 80)
        entryChoice = int(input("Enter entry number to change: "))

        if(entryChoice > len(data["entries"])):
            print("=" * 80)
            print("Invalid Choice. Returning to menu...")

        else:
            print("=" * 80)
            print("0| Service:", data["entries"][entryChoice]["service"])
            print("1| Username:", data["entries"][entryChoice]["username"])
            print("2| Password:", data["entries"][entryChoice]["password"])

            print("=" * 80)
            attrbChoice = int(input("Enter entry number to change: "))

            if(attrbChoice > len(entryMap)):
                print("Invalid Choice. Returning to menu...")

            else:
                print("=" * 80)

                if(attrbChoice == 2):
                    update = getpass.getpass("Enter new " + entryMap[attrbChoice] + ": ")
                else:
                    update = input("Enter new " + entryMap[attrbChoice] + ": ")
                
                data["entries"][entryChoice][entryMap[attrbChoice]] = update

                StoreFileData(key, data)

def ViewPasswordFile(key):
    data, exists = GetFileData(key)

    if(exists):
        for i in range(len(data["entries"])):
            print("=" * 80)
            print("Service:", data["entries"][i]["service"])
            print("Username:", data["entries"][i]["username"])
            print("Password:", data["entries"][i]["password"])
      
def GetFileData(key):
    if(path.exists("config/entries.json") and path.exists("config/entriesconfig.json")):
        exists = True
        
        with open("config/entriesconfig.json") as f:
            data = json.load(f)

            nonce = b64decode(data["nonce"])
            tag = b64decode(data["tag"])

            cipher = AES.new(key, AES.MODE_EAX, nonce)

            with open("config/entries.json", "rb") as f:
                data = f.read()

                data = cipher.decrypt_and_verify(data, tag).decode("utf-8")
                data = json.loads(data)

    else:
        data = None
        exists = False

    return data, exists

def StoreFileData(key, data):
    
    cipher = AES.new(key, AES.MODE_EAX)

    data = json.dumps(data)

    ciphertext, tag = cipher.encrypt_and_digest(data.encode("utf-8"))

    with open("config/entries.json", "wb") as f:
        f.write(ciphertext)

    configOptions = {
        "nonce" : b64encode(cipher.nonce).decode("utf-8"),
        "tag" : b64encode(tag).decode('utf-8') 
    }

    with open("config/entriesconfig.json", "w") as f:
        json.dump(configOptions, f)