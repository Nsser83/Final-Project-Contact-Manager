import json

FILE_NAME = "contacts.json"

def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def get_valid_name():
    while True:
        name = input("Enter contact name: ").strip()
        if name:
            return name
        print("Name cannot be empty.")

def get_valid_email():
    while True:
        email = input("Enter email address: ").strip()
        if "@" in email and "." in email:
            return email
        print("Please enter a valid email address.")

def get_valid_phone():
    while True:
        phone = input("Enter phone number: ").strip()
        if phone:
            return phone
        print("Phone number cannot be empty.")

def add_contact(contacts):
    name = get_valid_name()
    phone = get_valid_phone()
    email = get_valid_email()

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact saved successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])

def search_contact(contacts):
    search_name = input("Enter name to search: ").lower().strip()

    found = False
    for contact in contacts:
        if search_name in contact["name"].lower():
            print("\nContact found:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True

    if not found:
        print("No matching contacts found.")

def delete_contact(contacts):
    name = input("Enter name to delete: ").lower().strip()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").lower().strip()

    for contact in contacts:
        if contact["name"].lower() == name:
            print("\nLeave blank if you do not want to change something.")

            new_name = input("Enter new name: ").strip()
            new_phone = input("Enter new phone number: ").strip()
            new_email = input("Enter new email address: ").strip()

            if new_name:
                contact["name"] = new_name

            if new_phone:
                contact["phone"] = new_phone

            if new_email:
                if "@" in new_email and "." in new_email:
                    contact["email"] = new_email
                else:
                    print("Invalid email. Email was not updated.")

            save_contacts(contacts)
            print("Contact updated successfully!")
            return

    print("Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            update_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()