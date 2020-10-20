import passwordManager
import getpass
import utilities
from enum import Enum

class FunctionType(Enum):
    FILES = 0
    PASSWORD = 1

def main():
    print("=" * 80)  
    masterPass = getpass.getpass("Enter master password: ")
    
    if(utilities.AuthenticatePassword(masterPass)):
        running = True
        masterKey = utilities.GenerateKey(masterPass)
    
    else:
        running = False

    while(running):
        print("=" * 80)
        print("Encryption Options:")
        for item in list(FunctionType):
            print(item.value, "|", (item.name).capitalize())
        
        print("=" * 80)
        choice = input("Enter an option or 'Q' to quit: ")
        print("=" * 80)

        if choice == "q" or choice == "Q":
            running = False
            print("Exiting...")

        elif int(choice) == 0:
            print("Loading file manager...")
            #fileManager.Run(masterKey)

        elif int(choice) == 1:
            print("Loading password manager...")
            passwordManager.Run(masterKey)

        else:
            print("Invalid choice!")

    print("=" * 80)
    input("Press ENTER to close...")

main()