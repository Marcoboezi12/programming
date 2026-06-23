def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choose an option: ")

number1 = float(input("First number: "))
number2 = float(input("Second number: "))

try:

    if choice == "1":
        print("Result:", add(number1, number2))

    elif choice == "2":
        print("Result:", subtract(number1, number2))

    elif choice == "3":
        print("Result:", multiply(number1, number2))

    elif choice == "4":
        print("Result:", divide(number1, number2))

    else:
        print("Invalid option")

except ZeroDivisionError:
    print("You cannot divide by zero")
