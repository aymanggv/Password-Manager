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
2. **Generate your key (only once)**
   Uncomment and run the following function once to generate your encryption key:
   ```python
   def write_key():
    key = Fernet.generate_key()
    with open ("key.key", "wb") as key_file:
        key_file.write(key)
   ```
3. **Run the main script**
   ```bash
   python password_manager.py
   ```

## ✍️ Usage

When prompted, type:
- add → to add a new account and password
- view → to view saved account passwords
- q → to quit the program

## 🔒 Note

- Do not delete key.key or you will lose access to all encrypted passwords.
- This is a basic local project and not suitable for production use without further security measures.


