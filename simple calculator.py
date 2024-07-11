while True:

    num1 = input("Enter first number : ")
    num1 = float(num1)

    num2 = input("Enter second number : ")
    num2 = float(num2)

    ope = input("Enter the operator : ")

    if ope == "+":
        print(num1+num2)

    elif ope == "-":
        print(num1-num2)

    elif ope == "*":
        print(num1*num2)

    elif ope == "/":
        print(num1/num2)

    elif ope == "^":
        print(num1**num2)

    elif ope == "%":
        print(num1 % num2)

    elif ope == "//":
        print(num1//num2)

    else:
        print("THE OPERATOR YOU ENTERED IS INVALID.PLEASE TRY AGAIN!")

    print()
