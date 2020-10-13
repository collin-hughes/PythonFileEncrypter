import passwordManager
import getpass
from enum import Enum
from Crypto.Protocol.KDF import scrypt

class FunctionType(Enum):
    FILES = 0
    PASSWORD = 1

def main():  
    masterPass = getpass.getpass("Enter master password: ")
    masterPass = scrypt(masterPass, "generatepassword" ,key_len = 24, N = 2**14, r = 8, p = 1)

    running = True

    while(running):
        for item in list(FunctionType):
            print(item.value, "|", (item.name).capitalize())
        
        choice = input("Enter an option or 'Q' to quit: ")
        
        if choice == "q" or choice == "Q":
            running = False
            print("Exiting...")

        elif int(choice) == 0:
            print("Loading file manager...")

        elif int(choice) == 1:
            print("Loading password manager...")
            passwordManager.Run(masterPass)

        else:
            print("Invalid choice!")

main()