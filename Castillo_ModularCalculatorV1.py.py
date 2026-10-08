def add_numbers(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2


def subtract_numbers(num1, num2):
    """Returns the difference of two numbers."""
    return num1 - num2


def multiply_numbers(num1, num2):
    """Returns the product of two numbers."""
    return num1 * num2


def divide_numbers(num1, num2):
    """Returns the quotient of two numbers."""
    if num2 == 0:
        return "Cannot divide by zero."
    return num1 / num2


# Main program
def main():
    # Ask the user to enter two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Ask the user to choose an operation
    print("Choose operation:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")

    choice = input("Enter choice: ")

    # Call the correct function based on choice
    if choice == '1':
        result = add_numbers(num1, num2)
    elif choice == '2':
        result = subtract_numbers(num1, num2)
    elif choice == '3':
        result = multiply_numbers(num1, num2)
    elif choice == '4':
        result = divide_numbers(num1, num2)
    else:
        result = "Invalid selection."

    print("Result:", result)


if __name__ == "__main__":
    main()
