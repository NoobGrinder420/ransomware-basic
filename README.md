# Basic Ransomware

## Overview

This project is a simulated ransomware script designed for educational and cybersecurity research purposes only. It demonstrates file encryption and decryption using Python.&#x20;



Please use this responsibly — unauthorized use on real systems is illegal and unethical.

## Project Structure

```
.
├── computer/         # Test folder containing files for encryption/decryption
├── evil.py           # The "ransomware" script that encrypts files
├── hero.py           # The "rescue" script that decrypts files
├── README.md         # Project documentation
```

## How It Works

- **evil.py:**

  - Scans the `computer/` folder.
  - Encrypts all files using a generated encryption key.
  - Hides the encryption key in a `.hiddenkey.key` file.

    (is normally sent to hacker)
  - Demands a ransom for the key.

- **hero.py:**

  - Asks the user for the password that was provided by the hacker

    after meeting his demands
  - Retrieves the password and checks its validity.
  - Decrypts the encrypted files if the key is correct.

## Prerequisites

- Python 3.8+
- `cryptography` library: Install via pip

```bash
pip install cryptography
```

## Downloading the ransomware:

To clone this project from GitHub, run the following command:

```bash
git clone "https://github.com/NoobGrinder420/ransomware-basic.git"
cd "ransomware-basic"
```

## Usage

**1. Run the "evil" script to lock all the computer data:**

```bash
python3 evil.py
```

**2. (Optional) View the hidden key:**

```bash
cat .hiddenkey.key
```

**3. Run the "hero" script to unlock all the computer data:**

```bash
python3 hero.py
```

**4. Enter the password to auto-get the decryption key from .hiddenkey.key**

```
sigma
```

## Disclaimer

This project is strictly for educational purposes. Do not use this code for malicious activities. The author is not responsible for any misuse of this project.

