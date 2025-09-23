# PyCalculator

logo = ('''
 _____________________
|  _________________  |
| |          GREY   | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def muliply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {"+" : add,
"-" : subtract,
"*" : muliply,
"/" : divide}

def calculator():
    print(logo)
    should_accumulate = True
    num1 = float(input("Enter the first number : "))

    while should_accumulate:
        for symbol in operation:
            print(symbol)
        ops = input("Enter the operation (+,-,*,/) : ")
        num2 = float(input("Enter the second number : "))
        answer = operation[ops](num1, num2)
        print(f"{num1} {ops} {num2} = {answer}")

        choice = input(f"Type 'y' to continue with {answer} or type 'n' to start a new calculation...")

        if choice == "y":
            num1 = answer
        elif choice == "n":
            should_accumulate = False
            print("\n" * 20)
            calculator()
calculator()