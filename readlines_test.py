file = open("tasks.txt", "r")

tasks = file.readlines()

file.close()

tasks.pop(1)

print(tasks)