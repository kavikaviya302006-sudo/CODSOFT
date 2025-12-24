contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts available.\n")
    else:
        for name, details in contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
        print()

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        details = contacts[name]
        print(f"\nName: {name}")
        print(f"Phone: {details['Phone']}")
        print(f"Email: {details['Email']}")
        print(f"Address: {details['Address']}\n")
    else:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")

        contacts[name]["Phone"] = phone
        contacts[name]["Email"] = email
        contacts[name]["Address"] = address
        print("Contact updated successfully!\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found.\n")

def menu():
    while True:
        print("---- Contact Book ----")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Thank you!")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
