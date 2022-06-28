# You are Eligible for Driving Licence Check With Age

print("Type '0' For Program Stop!")

while True:
    age = float(input("Enter Your Age: "))

    if (age == 0):
        print("Program Stop!")
        break

    elif (age >= 1 and age <= 10):
        print("You are Too Child. You Cann't Drive Properly!")

    elif (age >= 10 and age <= 17):
        print("You are Not Eligible For Driving Licence!")

    elif (age >= 18 and age <= 40):
        print("You are Eligible For Driving Licence!")

    elif (age >= 41 and age <= 50):
        print("You are Eligible For Driving Licence. But, You are too Late!")

    else:
        (age >= 51)
        print("You are Eligible For Driving Licence. But, You are too Old. It's Risky!")

