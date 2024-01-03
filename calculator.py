def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y!=0:
        return x/y
    else:
        return "Error : Division by zero"
def calculator():
    operations = {
        '1': add,
        '2': substract,   
        '3': multiply,
        '4':divide

    }
    print("1. Additon")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    choice=input("ENter the choice(1/2/3/4):")
    if choice in operations:
        num1=float(input("enter your first number:"))
        num2=float(input("enter your second number:"))
        result= operations[choice](num1,num2)
        print(f"Result: {result}")
    else:
        print("invalid input.")
if __name__== "__main__":
    calculator()