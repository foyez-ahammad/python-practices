from random import randint
random_number = randint(1, 20)
gusses_time = 0

while True:
    guesse_number = int(input('Guess Number 1-30: '))
    gusses_time = gusses_time + 1

    if guesse_number == random_number:
        print('You guessed it right!')
        break
    elif guesse_number > random_number:
        print('You guessed it wrong! Enter a smaller number')
    elif guesse_number < random_number:
        print("You guessed it wrong! Enter a larger number")

print(f'You guessed the number in {gusses_time} guesses')
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(gusses_time < hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(gusses_time))