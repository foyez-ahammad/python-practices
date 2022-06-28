# Check Odd or Even Number

print("Type 'Ctrl+C' For Program Stoping.\n")

while True:

    number = int(input("Enter Number: "))

    if (number % 2) == 0:
        print(f"Answer: {number} is Even!")

    else:
        print(f"Answer: {number} is Odd!")