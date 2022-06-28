# Simple Calculator

loop_end = int(input("How Many Time You Calculate?: "))
lopp_start = 0

def calculator():

    firstNumber = float(input("Enter First Number: "))
    secondNumber = float(input("Enter Second Number: "))
    operator = input("Enter Operator (+, -, *, /):- ")

    def result(operator, calculation):
        print(f"Your {operator} Calculation Is: {calculation}")

    if operator == "+":
        result("Addition", firstNumber + secondNumber)

    elif operator == "-":
        result("Substracsion", firstNumber - secondNumber)

    elif operator == "*":
        result("Multiplicasion", firstNumber * secondNumber)

    elif operator == "/":
        result("Division", firstNumber / secondNumber)

    else:
        print("Invalided Operator!")

while lopp_start < loop_end:
    calculator()
    lopp_start += 1