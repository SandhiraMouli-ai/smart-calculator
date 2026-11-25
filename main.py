def calculate(a, operator, b):
    if operator == "+": return a + b
    if operator == "-": return a - b
    if operator == "*": return a * b
    if operator == "/":
        if b == 0: raise ValueError("Cannot divide by zero")
        return a / b
    raise ValueError("Unsupported operator")

if __name__ == "__main__":
    try:
        a = float(input("First number: "))
        op = input("Operator (+, -, *, /): ")
        b = float(input("Second number: "))
        print("Result:", calculate(a, op, b))
    except ValueError as error:
        print("Error:", error)
