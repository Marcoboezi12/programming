people = []

while True:

    print("\n1. Add person")
    print("2. View people")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        name = input("Enter name: ")
        age = int(input("Enter age: "))

        person = {
            "name": name,
            "age": age
        }

        people.append(person)

    elif choice == "2":

        print("\nPeople:")

        for person in people:
            print(person["name"], "-", person["age"])

    elif choice == "3":

        print("Goodbye!")
        break

    else:
        print("Invalid option")