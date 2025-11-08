try:
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))  

    print("Select operation: \n1. /"+"/ Addition\n2. /"-"/ Subtraction\n3. /"*"/ Multiplication\n4. /"/"Division")
    option= input("Enter our choice +,-,*,/: ")

    match option:
        case "+":
            print(f"{a} + {b} = {a+b}")
        case "-":
            print(f"{a} - {b} = {a-b}")
        case "*":
            print(f"{a} * {b} = {a*b}")
        case "/":
            if b!=0:
                print(f"{a} / {b} = {a/b}") 
            else:
                print("Division by zero is not allowed.")
        case _: 
            print("Invalid operation selected.")
except Exception as e:
    print("Error:", e)
    

