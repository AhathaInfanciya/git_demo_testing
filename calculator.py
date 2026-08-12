def add_numbers(x, y):
    return x + y


def subtract_numbers(x, y):
    return x - y


def multiply_numbers(x, y):
    return x * y


def divide_numbers(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y


def main():
    while True:
        try:
            a = float(input("Enter first number: "))
            break
        except Exception:
            print("Invalid input.Enter a valid number.")

    while True:
        try:
            b = float(input("Enter second number: "))
            break
        except Exception:
            print("Invalid input.Enter a valid number.")

    while True:
        c = input("Enter operation (+, -, *, /): ")
        if c in ["+", "-", "*", "/"]:
            break
        print("Invalid operation. Please enter +, -, * or /")

    if c == "+":
        result = add_numbers(a, b)
    elif c == "-":
        result = subtract_numbers(a, b)
    elif c == "*":
        result = multiply_numbers(a, b)
    elif c == "/":
        result = divide_numbers(a, b)

    if isinstance(result, str):
        print("Result:", result)
    elif result.is_integer():
        print("Result:", int(result))
    else:
        print("Result:", result)


if __name__ == "__main__":
    main()
