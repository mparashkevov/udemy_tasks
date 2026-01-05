def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
    num1 = float(input("Enter the first number: "))
    
    while True:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from above: ")
        
        num2 = float(input("Enter the next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        continue_calc = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation, or 'x' to exit: ").lower()
        
        if continue_calc == 'y':
            num1 = answer
        elif continue_calc == 'n':
            print("\n" * 30)
            calculator()
        else:
            import os
            os.system('clear')
            break

print("Welcome to the Calculator!")
calculator()
