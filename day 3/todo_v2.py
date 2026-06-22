tasks = []

while True:

    task = input("Enter a task (or type quit): ")

    if task == "quit":
        break

    tasks.append(task)

print("Your tasks:")
print(tasks)