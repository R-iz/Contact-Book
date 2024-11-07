class ContactBook:
    def __init__(self):
        self.contacts = []


    def add_contact(self):
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        self.contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        print(f"Contact '{name}' added successfully!")


    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("\nContact List:")
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")


    def search_contact(self):
        search_term = input("Enter Name or Phone Number to search: ")
        found_contacts = [contact for contact in self.contacts if contact['name'] == search_term or contact['phone'] == search_term]
        if found_contacts:
            for contact in found_contacts:
                self.display_contact(contact)
        else:
            print("No contact found.")


    def display_contact(self, contact):
        print("\nContact Details:")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")


    def update_contact(self):
        search_name = input("Enter the name of the contact to update: ")
        for contact in self.contacts:
            if contact['name'] == search_name:
                print("Enter new details (leave blank to keep existing value):")
                contact['phone'] = input(f"Phone [{contact['phone']}]: ") or contact['phone']
                contact['email'] = input(f"Email [{contact['email']}]: ") or contact['email']
                contact['address'] = input(f"Address [{contact['address']}]: ") or contact['address']
                print(f"Contact '{search_name}' updated successfully!")
                return
        print("Contact not found.")


    def delete_contact(self):
        search_name = input("Enter the name of the contact to delete: ")
        for contact in self.contacts:
            if contact['name'] == search_name:
                self.contacts.remove(contact)
                print(f"Contact '{search_name}' deleted successfully!")
                return
        print("Contact not found.")


    def menu(self):
        while True:
            print("\n--- Contact Book ---")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Choose an option: ")


            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                self.search_contact()
            elif choice == "4":
                self.update_contact()
            elif choice == "5":
                self.delete_contact()
            elif choice == "6":
                print("Exiting Contact Book. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Initialize and run the contact book application
if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.menu()
