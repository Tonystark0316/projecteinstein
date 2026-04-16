def calculator(a, b, c="add"):
    if c == "add":
        return a + b
    elif c == "sub":
        return a - b
    elif c == "div":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    elif c == "mul":
        return a * b
    else:
        return "Invalid operation"

# Example usage
num1 = float(input("Type the first number: "))
num2 = float(input("Type the second number: "))
operant = input("Type the operation (add, sub, mul, div): ").lower()

print("Result:", calculator(num1, num2, operant))