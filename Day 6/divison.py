def safe_divide(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Examples
safe_divide(10, 2)
safe_divide(10, 0)
