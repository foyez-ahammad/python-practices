# Number Guissing Game

from random import randint

print("Enter Number In '1 to 10'.")

while True:
    random_number = randint(1, 10)
    user_number = int(input("Enter Number: "))
    print('Computer: ', random_number)

    if random_number == user_number:
        print("You own!")
        break

    else:
        print("You lose!")
