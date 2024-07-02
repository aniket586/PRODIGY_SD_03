import json
import os

# Function to load contacts from a file
def load_contacts(filename='contacts.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

# Function to save contacts to a file
def save_contacts(contacts, filename='contacts.json'):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact {name} added successfully.")

# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

# Function to edit an existing contact
def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ")
        email = input(f"Enter new email address (current: {contacts[name]['email']}): ")
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact {name} updated successfully.")
    else:
        print(f"No contact found with the name {name}.")

# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"No contact found with the name {name}.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Exiting the program. Contacts saved.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
