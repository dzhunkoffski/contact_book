import os

def save_contact(contact):
    # Mistake: Opened file in 'r' (read) mode instead of 'a' (append)
    with open("contacts.txt", "r") as f:  
        f.write(f"{contact.name},{contact.phone}\n")  # This will raise an error

def load_contacts():
    contacts = []
    if os.path.exists("contacts.txt"):
        with open("contacts.txt") as f:
            for line in f:
                name, phone = line.strip().split(',')
                contacts.append((name, phone))
    return contacts
