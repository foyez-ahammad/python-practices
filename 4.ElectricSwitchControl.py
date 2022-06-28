# Electric Ligth Control Using Switch
help = (" Those are instructions:\n'on'    -For Light On. \n 'off'   -For Light Off. \n 'sleep' -For Sleeping. \n 'help'  -For User Instraction. ")
print(help)

mode = " "
ligth = False

while mode != "sleep":
    mode = input("Enter Light Mode: ").lower()

    if mode == 'on':
        if ligth:
            print("Already Light On!")
        else:
            ligth = True
            print("light Turend On!")

    elif mode == 'off':
        if not ligth:
            print("Already Light Off!")
        else:
            ligth = False
            print("light Turend Off!")

    elif mode == 'sleep':
        print("I'm Sleeping!")
        break

    elif mode == 'help':
        print(help)

    else:
        print("Wrong Command. Please Type 'help'. (if you don't understand)")
