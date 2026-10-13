def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculator():
    operations = {
        "1": ("Addition", add),
        "2": ("Subtraction", subtract),
        "3": ("Multiplication", multiply),
        "4": ("Division", divide),
    }

    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = input("Choose an option (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in operations:
            print("Invalid option. Please try again.")
            continue

        operation_name, operation = operations[choice]
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            result = operation(num1, num2)
            print(f"{operation_name} result: {result}")
        except ValueError as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    calculator()
