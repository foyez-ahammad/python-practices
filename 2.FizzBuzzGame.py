# FizzBuzz Game
print("\nType 'Ctrl+C' For Program Stoping.\n")
# play_time = int(input('How many times you want to play this: '))

while True:
    num = float(input("Enter Number: "))

    if (num % 3) == 0 and (num % 5) == 0:
        print("FizzBuzz!")

    elif (num % 3) == 0:
        print("Fizz!")

    elif (num % 5) == 0:
        print("Buzz!")

    else:
        print("Not FizzBuzz")
