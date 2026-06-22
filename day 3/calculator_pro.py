def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

number1 = float(input("First number: "))
number2 = float(input("Second number: "))

print("Addition:", add(number1, number2))
print("Subtraction:", subtract(number1, number2))
print("Multiplication:", multiply(number1, number2))
print("Division:", divide(number1, number2))