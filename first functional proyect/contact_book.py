contacts = []
try:
    file = open("contacts.txt", "r")

    for line in file:
        line = line.strip()
        name, phone, email = line.split(",")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)

    file.close()

except FileNotFoundError:
    pass
while True:

    print("\n1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. delete contact")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)

        print("Contact added!")

        file = open("contacts.txt", "a")
        file.write(name + "," + phone + "," + email + "\n")
        file.close()

    elif choice == "2":

        print("\nContacts:")

        for contact in contacts:
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print()

    elif choice == "3":

        search_name = input("Search name: ")

        for contact in contacts:
            if contact["name"] == search_name:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])

    elif choice == "4":

        print("\nContacts:")

        for index, contact in enumerate(contacts):
         print(index, "-", contact["name"])

        delete_index = int(input("Enter contact number to delete: "))

        contacts.pop(delete_index)

        print("Contact deleted!")

    elif choice == "5":
        print("Goodbye!")
        break