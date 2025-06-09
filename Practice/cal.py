try:
    x = int(input("Operand 1: "))
except (EOFError, KeyboardInterrupt):
    print("\nExiting...")
    exit()
except ValueError:
    print("Invalid input. Exiting...")
    exit()

result = x

try:
    while True:
        exp = input("Expression (e.g. + 5): ").strip()
        if not exp:
            continue

        try:
            y, z = exp.split()
            z = int(z)

            match y:
                case "+":
                    result += z
                case "-":
                    result -= z
                case "*":
                    result *= z
                case "/":
                    result /= z
                case "**":
                    result **= z
                case "//":
                    result //= z
                case _:
                    print("Invalid operator")
                    continue

            print("Result:", result)

        except ValueError:
            print("Invalid format! Use: <operator> <number>")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")

except (EOFError, KeyboardInterrupt):
    print("\nExiting...")
