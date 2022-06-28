# Hand Cricket Game

from random import randint

score = 0

while True:
    player = int(input("Player: ")) #taking player input
    computer = randint(1, 6) # generate random number [1 to 6]
    # when player enter upto 6 it work
    if player > 6 or player < 1:
        print("Oops! Enter valid Value in 1-6.")
        continue

    else:
        # if, Computer Not Equal Player. it increase player runs
        if player != computer:
            score = score + player
            print(f"Computer: {computer}")

            # when player get 50 runs it work
            if score >= 50:
                print(f"Wow! You Got {score} Run.")

            # when player get 100 runs it work
            elif score >= 100:
                print(f"Congrates! You Got {score} Run.")

        # When Computer Equal Player it work
        else:
            print(f"Computer: {computer}")
            print("Out!!!")
            break

# when player out it work
print(f"Your Total Score: {score}")
