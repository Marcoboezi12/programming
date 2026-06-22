people = []

while True:

    name = input("Enter name (or quit): ")

    if name == "quit":
        break

    age = int(input("Enter age: "))

    person = {
        "name": name,
        "age": age
    }

    people.append(person)

print("\nPeople:")

for person in people:
    print(person["name"], "-", person["age"])