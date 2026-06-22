tasks = []

while True:

    print("\n1. Add task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)

    elif choice == "2":
        print("\nYour tasks:")

        for task in tasks:
            print("-", task)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option")