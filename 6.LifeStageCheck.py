# Define Your Stage With Age

print("Type '0' For Program Stop!")

while True:
    age = float(input("Enter Your Age: "))

    if (age == 0):
        print("Program Stop!")
        break

    elif (age >= 1 and age <= 7):
        print("You are Child!")

    elif (age >= 8 and age <= 14):
        print("You are adolescent!")

    elif (age >= 13 and age <= 18):
        print("You are Teeneger!")

    elif (age >= 19 and age <= 26):
        print("You are Adult!")

    elif (age >= 27 and age <= 34):
        print("You are Young!")

    elif (age >= 35 and age <= 42):
        print("You are elderly!")

    elif (age >= 43 and age <= 50):
        print("You are Old!")

    else:
        print("You are Lucky! because, You Exist In Earth. ")

# Don't Take Serious. It's For Fun
