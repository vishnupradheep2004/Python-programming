def calculator():
    print("Simple Calculator")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5.exit")

    operation = input("Enter the number corresponding to the operation (1/2/3/4/5): ")

    if operation == '5':
        print("Exiting the calculator. Goodbye!")
        return False

    if operation not in ['1', '2', '3', '4']:
        print("Invalid operation choice. Please try again.")
        return True
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return True


   

    if operation == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error! Division by zero.")
    return True
    
    
def again():
    while True:
        if not calculator():
            break
        another_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if another_calculation != 'yes':
            print("Exiting the calculator. Goodbye!")
            break
            



again()
