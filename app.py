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


if __name__ == "__main__":
    print("Simple Calculator")
    print("Operations: add, subtract, multiply, divide")

    num1 = float(input("Enter first number: "))
    operation = input("Enter operation (add/subtract/multiply/divide): ").strip().lower()
    num2 = float(input("Enter second number: "))

    if operation == "add":
        result = add(num1, num2)
    elif operation == "subtract":
        result = subtract(num1, num2)
    elif operation == "multiply":
        result = multiply(num1, num2)
    elif operation == "divide":
        result = divide(num1, num2)
    else:
        print("Invalid operation.")
        raise SystemExit

    print(f"Result: {result}")
