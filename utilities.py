import json
from Crypto.Hash import SHA256
from os import path, mkdir
from Crypto.Protocol.KDF import scrypt
from base64 import b64encode, b64decode

def GenerateKey(password):
    masterKey = scrypt(password, "generatepassword" ,key_len = 24, N = 2**14, r = 8, p = 1)
    return masterKey

def AuthenticatePassword(password):

    data = {
    }

    if(not path.exists("config/")):
        mkdir("config")

    if(path.exists("config/masterconfig.json")):

        hashedPass = SHA256.new()

        # Hash the message
        hashedPass.update(password.encode("utf-8"))

        with open("config/masterconfig.json") as f:
            data = json.load(f)

            trueHashedPass = data["hash"]

        if(hashedPass.hexdigest() == trueHashedPass):
            return True, True

        else:  
            return False, False

    else:
        hashedPass = SHA256.new()

        # Hash the message
        hashedPass.update(password.encode("utf-8"))

        with open("config/masterconfig.json", "w") as f:

            data["hash"] = hashedPass.hexdigest()
            
            json.dump(data, f)

        return True, False
