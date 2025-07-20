from os import name


def greetings():
    name = input("Please enter your name:").strip().title()
    name = " ".join(name.split())
    print(f"Hello, {name}! Welcome To My Second Project!")
    if name == "":
        print("You didn't enter a name, so I will call you User!")
        name = "User"

def calculator_simple(x, operation, y):
    if operation == "+":
        return x + y
    elif operation == "-":
        return x - y
    elif operation == "*":
         return x * y
    elif operation == "/":
         if y == 0:
            return "Error: Division by zero is not allowed."
         return x / y
    else:  
        return "invalid operator. Please Use The available operators: +, -, *, /, %"

def riches_category(income):
      print("Welcome to the Riches Category!")
      if income < 25000:
          return "Lower Class.\U0001F622"
      elif 25000 <= income < 50000:
          return "Working Class.\U0001F4BC"
      elif 50000 <= income < 150000:
          return "Middle Class.\U0001F3E0"
      elif 150000 <= income < 250000:
          return "Upper-Middle Class.\U0001F4B8"
      elif 250000 <= income < 500000:
          return "Upper Class.\U0001F48E"
      else:
          return "man you have to help the poor, you are rich! ahhahahah \U0001F602 "
      
def exit_program():
      print(f"Exiting the program. Goodbye! \U0001F44B")
      exit()

def main():
            running = True
            while running:
               print("\033[1mWELCOME TO MY IMPROVE PROJECTS! LOL\033[0m")
               print("1. \033[1mGreetings to User\033[0m")
               print("2. \033[1mCalculator\033[0m")
               print("3. \033[1mWhat Category of Riches are you in?\033[0m")
               print("4. \033[1mExit\033[0m")
               choice = input("Please enter your choice (1-4): ")

               if choice == "1":
                  greetings()

               elif choice == "2":
                  print ("\033[1mWelcome to the Simple Calculator!\033[0m"
                        "\n\033[3mYou can perform basic operations like addition, subtractions, multiplication, and division.\033[0m")
                  x = int(input("Enter a Number To Perform Calculations: "))
                  operation = input("Choose An Operation (+ ,- ,* , / , % ): ")
                  y = int(input("Enter Second Number: "))
                  result = calculator_simple(x, operation, y)
                  print(f"{x} {operation} {y} = {result}")

               elif choice == "3":
                  print("\033[1mWelcome to the Riches Category!\033[0m \n\033[1mYour Category Of Riches Is Determined By Your Income\033[0m")
                  income = float(input("Please enter your yearly income: "))
                  result = riches_category(income)
                  print(f"Your yearly income is {income} "
                        f"\nThat mean Your category of riches is: {result}")

               elif choice == "4":
                  exit_program()
                  running = False
               else:
                  print("Invalid choice. Please choose 1-4.")

if __name__ == "__main__":
      main()
