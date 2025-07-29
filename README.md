# 🔐 Simple Password Manager (Python)

This is a basic password manager built with Python using the `cryptography` library. It lets you **store** and **retrieve** encrypted passwords for different accounts locally.

## 🧠 How It Works

- **Encryption**: Passwords are encrypted using `Fernet` symmetric encryption.
- **Storage**: Encrypted passwords are stored in a plain text file (`passwords.txt`).
- **Key Management**: A unique encryption key is stored in `key.key` and used to encrypt/decrypt the passwords.

## ⚙️ Features

- Add new account passwords securely
- View stored passwords (decrypted)
- Simple CLI interface for usage

## 📂 File Structure

- `key.key` → stores your secret encryption key (generated once)
- `passwords.txt` → holds your encrypted account-password data
- `password_manager.py` → main script with `add`, `view`, and encryption logic

## 🛠️ Getting Started

1. **Install dependencies**
   ```bash
   pip install cryptography
   ```
2. 
