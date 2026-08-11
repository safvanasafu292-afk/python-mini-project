def calculator():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /): ")

        if op == '+':
            print("Result:", a + b)

        elif op == '-':
            print("Result:", a - b)

        elif op == '*':
            print("Result:", a * b)

        elif op == '/':
            print("Result:", a / b)

        else:
            raise ValueError("Invalid operator!")

    except ValueError as e:
        print("Error:", e)

    except ZeroDivisionError:
        print("Error: Division by zero not allowed!")

    finally:
        print("Thank you for using the calculator.")

calculator()