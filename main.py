from models.contact import Contact
from utils.file_io import save_contact, load_contacts

def main():
    print("Contact Book")
    contacts = load_contacts()
    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    contact = Contact(name, phone)
    print(f"Saved: {contact.name} - {contact.phone}")

if __name__ == "__main__":
    main()
