file = open("tasks.txt", "r")

content = file.read()

print("Your tasks:")
print(content)

file.close()
