# exceptions_example.py
try:
    x = int(input("Enter a number: "))
    print("Reciprocal:", 1/x)
except ValueError:
    print("Invalid integer")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Done")
