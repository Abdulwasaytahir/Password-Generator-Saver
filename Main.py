import json
import os
import random
import string
from datetime import datetime

DATA_FILE = "passwords.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def generate_password(length=16, use_upper=True, use_digits=True, use_symbols=True):
    if length < 4:
        raise ValueError("Length should be at least 4")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ""
    digits = string.digits if use_digits else ""
    symbols = string.punctuation if use_symbols else ""

    all_chars = lower + upper + digits + symbols
    if not all_chars:
        raise ValueError("No character sets selected")

    # Ensure password contains at least one of each selected type
    password = []
    password.append(random.choice(lower))
    if use_upper:
        password.append(random.choice(upper))
    if use_digits:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))

    # Fill the rest
    while len(password) < length:
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return "".join(password)


def add_entry(site, username, password, note=""):
    data = load_data()
    entry = {
        "site": site,
        "username": username,
        "password": password,
        "note": note,
        "created": datetime.utcnow().isoformat() + "Z"
    }
    data.append(entry)
    save_data(data)
    print("Saved entry for:", site)


def mask_password(pw):
    if not pw:
        return ""
    if len(pw) <= 4:
        return "*" * len(pw)
    return pw[0] + "*" * (len(pw) - 2) + pw[-1]


def view_entries(show_plain=False):
    data = load_data()
    if not data:
        print("No saved passwords.")
        return
    for i, e in enumerate(data, 1):
        print(f"{i}. Site: {e['site']}")
        print(f"   Username: {e.get('username','')}")
        print(f"   Password: {e['password'] if show_plain else mask_password(e.get('password',''))}")
        if e.get('note'):
            print(f"   Note: {e['note']}")
        print(f"   Added: {e.get('created')}")
        print("-")


def search_entries(query, show_plain=False):
    data = load_data()
    found = [e for e in data if query.lower() in e.get('site','').lower()]
    if not found:
        print("No entries found for:", query)
        return
    for i, e in enumerate(found, 1):
        print(f"{i}. Site: {e['site']}")
        print(f"   Username: {e.get('username','')}")
        print(f"   Password: {e['password'] if show_plain else mask_password(e.get('password',''))}")
        if e.get('note'):
            print(f"   Note: {e['note']}")
        print(f"   Added: {e.get('created')}")
        print("-")


def cli_menu():
    print("=== Password Generator & Saver ===")
    while True:
        print("\nChoose an option:")
        print("1) Generate a password")
        print("2) Generate + Save an entry")
        print("3) View saved passwords (masked)")
        print("4) View saved passwords (plain)")
        print("5) Search by site")
        print("6) Exit")

        choice = input("Enter choice: ").strip()
        if choice == '1':
            try:
                l = int(input("Password length (default 16): ") or 16)
                pw = generate_password(length=l)
                print("Generated password:", pw)
            except Exception as ex:
                print("Error:", ex)
        elif choice == '2':
            site = input("Site / Service name: ").strip()
            username = input("Username / Email: ").strip()
            try:
                l = int(input("Password length (default 16): ") or 16)
                pw = generate_password(length=l)
                note = input("Note (optional): ").strip()
                add_entry(site, username, pw, note)
                print("Password generated:", pw)
            except Exception as ex:
                print("Error:", ex)
        elif choice == '3':
            view_entries(show_plain=False)
        elif choice == '4':
            view_entries(show_plain=True)
        elif choice == '5':
            q = input("Search query (site name): ").strip()
            search_entries(q, show_plain=False)
        elif choice == '6':
            print("Bye — stay secure!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    try:
        cli_menu()
    except KeyboardInterrupt:
        print("\nExiting...")
