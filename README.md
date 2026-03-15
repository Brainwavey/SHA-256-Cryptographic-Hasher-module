# SHA-256 Cryptographic Hasher 🔐

A Python-based Object-Oriented Programming (OOP) module built for the Brainwavey / Fathom OS architecture. This tool demonstrates core cybersecurity principles by converting raw text into unbreakable cryptographic hashes.

## 🧠 Concepts Demonstrated
* **Object-Oriented Design:** Blueprint creation, state management, and encapsulation using Python classes.
* **Cryptographic Hashing:** Utilizing Python's built-in `hashlib` to execute standard cybersecurity encryption.
* **Data Encoding:** Translating human-readable string inputs into raw computer bytes (`utf-8`) for algorithmic processing.
* **Hexadecimal Digestion:** Converting mathematical output back into readable 64-character hexadecimal formats.

## 🚀 How It Works
The script initializes a `CryptoHasher` object that waits for user input. 
1. The user inputs a target password or secure string into the terminal.
2. The `generate_hash()` method encodes the string and pushes the bytes through the SHA-256 algorithm.
3. The final output displays both the original text and the permanent, irreversible 64-character hash.

## 💻 Tech Stack
* Python 3
* `hashlib` (Standard Library)
