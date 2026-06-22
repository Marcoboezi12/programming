while True:

    print("\n1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Clear all tasks")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")

        file = open("tasks.txt", "a")
        file.write(task + "\n")
        file.close()

        print("Task saved!")

    elif choice == "2":
        file = open("tasks.txt", "r")
        tasks = file.readlines()
        file.close()

        print("\nYour tasks:")

        for index, task in enumerate(tasks):
            print(index + 1, "-", task.strip())

    elif choice == "3":
        file = open("tasks.txt", "r")
        tasks = file.readlines()
        file.close()

        print("\nYour tasks:")

        for index, task in enumerate(tasks):
            print(index + 1, "-", task.strip())

        task_number = int(input("Which task do you want to delete? "))

        tasks.pop(task_number - 1)

        file = open("tasks.txt", "w")
        file.writelines(tasks)
        file.close()

        print("Task deleted!")

    elif choice == "4":
        file = open("tasks.txt", "w")
        file.close()

        print("All tasks deleted!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option")