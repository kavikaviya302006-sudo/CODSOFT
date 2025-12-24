def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b


while True:
    print("\n------ Simple Calculator ------")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "7":
        print("Calculator Closed. Thank You!")
        break

    if choice in ["1", "2", "3", "4", "5", "6"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue
    else:
        print("Invalid choice! Try again.")
        continue

    if choice == "1":
        print("Result:", add(num1, num2))

    elif choice == "2":
        print("Result:", subtract(num1, num2))

    elif choice == "3":
        print("Result:", multiply(num1, num2))

    elif choice == "4":
        print("Result:", divide(num1, num2))

    elif choice == "5":
        print("Result:", modulus(num1, num2))

    elif choice == "6":
        print("Result:", power(num1, num2))
