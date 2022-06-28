# Maximum Number Checking

print("Type 'Ctrl+C' For Program Stoping.\n")

while True:
    number_1 = float(input("Enter Number_1: "))
    number_2 = float(input("Enter Number_2: "))
    number_3 = float(input("Enter Number_3: "))

    if number_1 > number_2:
        if number_1 > number_3:
            print("Number_1 Is Maximum!")

    elif number_2 > number_3:
        print("Number_2 Is Maximum!")

    else:
        print("Number_3 Is Maximum!")









