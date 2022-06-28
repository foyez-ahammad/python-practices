first_name = input("Enter Your First Name: ")
second_name = input("Enter Your Second Name: ")
full_name = first_name + " " + second_name

print(f"Your Full Name: {full_name}")
print(f"Title Case Full Name: {full_name.title()}")
print(f"Upper Case Full Name: {full_name.upper()}")

replace_second_name = input("Replace Your Second Name: ")

print(f"{full_name.title()} your full name is {first_name.title() + ' ' + replace_second_name.title()}")