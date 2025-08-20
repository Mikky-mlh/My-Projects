#Make a simple calculator for addition, subtraction, multiplication, average and division.
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def average(x, y):
    return (x + y) / 2

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Division by zero error"

print("Please select a operation:\n " \
      "1. Addition\n" \
      "2. Substraction\n" \
      "3. Multiplication\n" \
      "4. Division\n" \
      "5. Average\n") 

select = int(input("Select a operation from 1,2,3,4,5: "))

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print("Result: ", end="")

if select == 1:
    print(add(x, y))
elif select == 2:
    print(subtract(x, y))
elif select == 3:
    print(multiply(x, y))
elif select == 4:
    print(divide(x, y))
elif select == 5:
    print(average(x, y))
else:
    print("Invalid selection.")

