def basic_calculator():
    print("Welcome to the Basic Calculator!")
    while True:
        # 1. Get user input
        num1_str = input("Enter the first number (or 'q' to quit): ")
        if num1_str.lower() == 'q':
            print("Goodbye!")
            break

        num2_str = input("Enter the second number: ")
        op = input("Choose an operation (+, -, *, /): ")

        # 2. Convert inputs to floats, with error handling
        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            print("⚠️  Invalid number entered. Please enter numeric values.\n")
            continue

        # 3. Perform the requested operation
        if op == '+':
            result = num1 + num2
            symbol = '+'
        elif op == '-':
            result = num1 - num2
            symbol = '-'
        elif op == '*':
            result = num1 * num2
            symbol = '*'
        elif op == '/':
            if num2 == 0:
                print("⚠️  Cannot divide by zero.\n")
                continue
            result = num1 / num2
            symbol = '/'
        else:
            print(f"⚠️  Unsupported operation '{op}'. Please choose +, -, *, or /.\n")
            continue

        # 4. Display the result
        print(f"\n🎉  {num1} {symbol} {num2} = {result}\n")

if __name__ == "__main__":
    basic_calculator()
