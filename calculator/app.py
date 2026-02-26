
from calculator.operations import Calculator

import logging 

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class CalculatorApp:
    def __init__(self):
        self.calculator = Calculator()
        self.history = []

    def show_menu(self):
        print("\nSimple Calculator")
        print("-------------------")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. View History")
        print("7. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter choice (1-7): ")

            if choice == "7":
                print("Thank you for using calculator!")
                break
            elif choice == "6":
                self.show_history()
                continue
            self.perform_operation(choice)

    def show_history(self):
        if not self.history:
            print("No history yet.")
        else:
            print("\nCalculator History:")
            for item in self.history:
                print(item)

    def perform_operation(self, choice):
        try:
            num1 = float(input("Enter first nnumber: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = self.calculator.add(num1, num2)
                expression = f"{num1} + {num2} = {result}"
            elif choice == "2":
                result = self.calculator.subtract(num1, num2)
                expression = f"{num1} - {num2} = {result}"
            elif choice == "3":
                result = self.calculator.multiply(num1, num2)
                expression = f"{num1} * {num2} = {result}"
            elif choice == "4":
                result = self.calculator.divide(num1, num2)
                expression = f"{num1} / {num2} = {result}"
            elif choice == "5":
                result = self.calculator.power(num1, num2)
                expression = f"{num1} ** {num2} = {result}"
            else:
                print("Invalid choice")
                return
            
            print("Result: ", result)
            logging.info(expression)
            self.history.append(expression)

        except ValueError:
            print("Invalid number entered!")
        except ZeroDivisionError as e:
            print(e)


