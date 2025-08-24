def calculator():
    print("Welcome to Simple Calculator!")
    print("Operations: + for addition, - for subtraction, * for multiplication, / for division")
    
    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Choose operation (+, -, *, /): ")

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation! Please choose +, -, *, or /.")
                continue

            print(f"Result: {num1} {operation} {num2} = {result}")

        except ValueError:
            print("Invalid input! Please enter numeric values.")

        again = input("Do you want to calculate again? (yes/no): ").lower()
        if again != "yes":
            print("Thank you for using Simple Calculator!")
            break

if __name__ == "__main__":
    calculator()
