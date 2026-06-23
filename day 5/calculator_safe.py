while True:

    try:

        number1 = float(input("First number: "))
        number2 = float(input("Second number: "))

        print("Result:", number1 + number2)

        break

    except ValueError:

        print("Please enter valid numbers")
        