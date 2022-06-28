# You are Eligible for Voter Check With Age

print("Type '0' For Program Stop!")

while True:
    age = float((input("Enter Your Age: ")))

    if (age == 0):
        print("Program Stop!")
        break

    elif (age >= 1 and age <= 17):
        print("You are Not Eligible For Voting!")

    else:
        (age >= 18)
        print("You are Eligible For Voting!")
