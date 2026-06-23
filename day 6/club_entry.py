age = int(input("Age: "))
has_id = input("Do you have ID? (yes/no): ")

if age >= 18 and has_id == "yes":
    print("Entry allowed")

else:
    print("Entry denied")