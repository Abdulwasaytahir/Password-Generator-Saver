🔐 Password Generator & Saver (CLI)

A simple and powerful Command-Line Password Manager written in Python.
This tool helps you:

✔ Generate strong random passwords
✔ Save login entries (site, username, password, note, timestamp)
✔ View saved passwords (masked or plain)
✔ Search entries by site name
✔ Store everything securely in a local JSON database
✔ Zero external dependencies — works anywhere Python works!

📁 Features
🧷 Password Generator

Generate strong random passwords.

Adjustable length (default: 16).

Includes lowercase, uppercase, digits, and symbols.

Ensures at least one character from each selected category.

💾 Password Saver

Save entries in passwords.json.

Stored fields:

Site / Service name

Username / Email

Password

Notes

Timestamp (UTC)

👀 View & Search

View all saved entries (masked or plain).

Search entries by site name.

Masked mode hides sensitive passwords automatically.

🛠 No External Libraries

Uses only built-in Python modules.

📦 Installation

Make sure you have Python 3 installed.

Clone the repository:

git clone https://github.com/Abdulwasaytahir/password-manager-cli.git
cd password-manager-cli


Run the program:

python3 password_manager.py

▶ Usage

When you run the script, you'll see a menu:

=== Password Generator & Saver ===

Choose an option:
1) Generate a password
2) Generate + Save an entry
3) View saved passwords (masked)
4) View saved passwords (plain)
5) Search by site
6) Exit

1) Generate a random password

Just choose option 1 and enter the length.

2) Generate + Save

Stores the password, username, site, and note.

3) View masked passwords

Shows entries with hidden passwords like p********d.

4) View actual passwords

Displays the real passwords — use carefully.

5) Search

Find saved login details by typing a site name.

📂 Data Storage

All saved entries are stored inside:

passwords.json


Format example:

{
  "site": "github.com",
  "username": "user@example.com",
  "password": "P@ssw0rdExample",
  "note": "Work account",
  "created": "2025-01-01T10:20:30Z"
}

🛡 Security Disclaimer

This tool stores data unencrypted in a local JSON file.
For personal/local use it's fine — but not recommended for storing extremely sensitive passwords without encryption.

Future improvements may include:

File encryption

Master password

CLI export/import

🤝 Contributing

Pull requests are welcome!
If you want to add features (like encryption or UI), feel free to open an issue.

📜 License

This project is licensed under the MIT License — free to use, modify, distribute.
