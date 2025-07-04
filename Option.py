def hello(to="User"):
    print("Hello, \U0001F600" + to + "!\U0001F600")

def greetings():
    name = input("What's your name? ")
    hello(name)

def calculator():
    print("Welcome to the Calculator!")
    X = float(input("Enter the first number: "))
    operation = input("Choose an operation (+, -, *, /): ")
    Y = float(input("Enter the second number: "))
    if operation == "+":
        result = X + Y
    elif operation == "-":
        result = X - Y
    elif operation == "*":
        result = X * Y
    elif operation == "/":
        if Y == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = X / Y
    else:
        print("Invalid operation. Please try again.")
        return
    print(f"The result of {X} {operation} {Y} is: {result}")

def exit_program():
    print("Exiting the program. Goodbye! \U0001F44B")
    exit()

def menu():
    while True:
        print("Welcome to my first projects!")
        print("1. Greetings")
        print("2. Calculator")
        print("3. Exit")
        choice = input("Please choose an option (1-3): ")

        if choice == "1":
            greetings()
        elif choice == "2":
            calculator()
        elif choice == "3":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

menu()