task = input("Enter a task: ")

file = open("tasks.txt", "a")

file.write(task + "\n")

file.close()

print("Task saved!")