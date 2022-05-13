def add(n1 ,n2):
  return n1+ n2 

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return(n1/n2)
 
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

num1 = int(input("What's the first number?: "))


for symbol in operations:
  print(symbol)

calculating = True
while calculating == True:
  operation_symbol = (input("Pick an operation: "))
  num2 = int(input("What's the next number?: "))
  calculate_function = operations[operation_symbol]
  answer = calculate_function(num1, num2)
  print(f"{num1} {operation_symbol} {num2} = {answer}")

  if input(f"Type 'y' to confinue with {answer}, or type 'n' to exit. :") == 'y':
    num1 = answer
  else: 
    calculating = False 
