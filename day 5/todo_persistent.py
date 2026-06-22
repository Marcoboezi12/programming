while True:

    print("\n1. Add task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        task = input("Enter a task: ")

        file = open("tasks.txt", "a")
        file.write(task + "\n")
        file.close()

        print("Task saved!")

    elif choice == "2":

        file = open("tasks.txt", "r")

        content = file.read()

        print("\nYour tasks:")
        print(content)

        file.close()

    elif choice == "3":

        print("Goodbye!")
        break

    else:

        print("Invalid option")