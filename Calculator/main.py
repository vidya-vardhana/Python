try:
    a= int(input("Enter the first number: "))
    b= int(input("Enter the second number: "))

    print("Select operation:\n+ For Addition\n- For Subtraction\n* For Multiplication\n/ For Division")
    operation=input("Enter the Operation")

    match operation:
        case "+":
            print(f"The sum is: {a+b}")
        case "-":
            print(f"The difference is: {a-b}")
        case "*":
            print(f"The product is: {a*b}")
        case "/":
            if b!=0:
                print(f"The quotient is:  {a/b}")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation selected.")

except Exception as e:
    print(f"An error occurred: {e}") 

