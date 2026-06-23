while True:

    try:
        number = int(input("Enter a number: "))

        print("You entered:", number)

        break

    except ValueError:
        print("Please enter a valid number")
        