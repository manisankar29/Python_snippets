class ContactList:
    def __init__(self):
        self.contacts = {}
    
    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number
        print(f"Contact {name} added successfully!")
    
    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for name, phone_number in self.contacts.items():
                print(f"{name}: {phone_number}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Contact Details - {name}: {self.contacts[name]}")
        else:
            print(f"Contact {name} not found.")

if __name__ == "__main__":
    contact_list = ContactList()
    while True:
        print("\nContact List Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("enter the contact name: ")
            phone_number = input("Enter the phone number: ")
            contact_list.add_contact(name, phone_number)

        elif choice == "2":
            contact_list.view_contacts()

        elif choice == "3":
            name = input("Enter the contact name to search: ")
            contact_list.search_contact(name)

        elif choice == "4":
            print("Exiting the Contact List. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 to 4.")
