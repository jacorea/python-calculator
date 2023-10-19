# Imports
from replit import clear
from art import logo 
# add function
def add(n1,n2):
  return n1 + n2

# subtract function
def subtract(n1,n2):
  return n1 - n2

# multiply function
def multiply(n1,n2):
  return n1 * n2

# divide function
def divide(n1,n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
cont_calc = True


def calculator():
  """
  This function is the calculator. Takes no parameters, but asks users for inputs"""
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(f"{symbol}")
  cont_calc = True

  while cont_calc:
    operation = input("Choose an operation from the line above: ")
    num2 = float(input("What's the second number?: "))
    answer = operations[operation](num1,num2)
    print(f"{num1} {operation} {num2} = {answer}")
    cont_calc = input(f" Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") 
    if cont_calc == 'y':
      num1= answer
    else:
      cont_calc = False
      clear()
      calculator()

calculator()
