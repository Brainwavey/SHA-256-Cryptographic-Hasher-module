# Fathom OS: Cryptography & Breach Suite 🔐🏴‍☠️

A Python-based Object-Oriented Programming (OOP) module built for the Brainwavey / Fathom OS architecture. This repository demonstrates the complete lifecycle of cryptographic security, featuring both defensive encryption and offensive dictionary attack simulations.

## 🛠️ The Tools

### 1. The Defensive Protocol: SHA-256 Hasher (`fathom_hasher.py`)
A defensive security script that translates raw user string inputs into encoded bytes and generates an unbreakable 64-character hexadecimal SHA-256 hash.
* **Core Concept:** One-way cryptographic hashing and data encoding (`utf-8`).

### 2. The Offensive Protocol: Dictionary Attacker (`hash_cracker.py`)
An offensive security script that simulates a breach attempt on a target SHA-256 hash. It iterates through a local dictionary file (`Passwords.txt`), sanitizes the inputs, hashes each string, and compares them against the target payload to find a match.
* **Core Concept:** Automated brute-force/dictionary attacks, file handling (`with open`), and hidden data sanitization (`.strip()`).

## 🧠 Technical Skills Demonstrated
* **Object-Oriented Design:** Blueprint creation, state management, and encapsulation using Python classes.
* **Data Sanitization:** Cleaning invisible characters (`\n`) from external data sources to prevent mathematical algorithm failures.
* **File I/O:** Securely opening, reading, and closing external text files during active execution.

## 💻 Tech Stack
* Python 3
* `hashlib` (Standard Library)2. The `generate_hash()` method encodes the string and pushes the bytes through the SHA-256 algorithm.
3. The final output displays both the original text and the permanent, irreversible 64-character hash.

## 💻 Tech Stack
* Python 3
* `hashlib` (Standard Library)
