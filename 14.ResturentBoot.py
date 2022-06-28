# Simple Resturent Boot

# per product price
tea = 10
copie = 20
pizza = 50
drink = 25

# information collect from customer
greating = input("Boot: HELLO, How are you?\nMine: ")

if 'you' in greating or 'u' in greating:
  print("Boot: I'm Fine.")

cus_name = input("Boot: What's your Name?\nMine: ").title()
ask_cust = input(f"Boot: Okay, \"{cus_name}\" How could i help you? \nMine: ")
cus_Prod_Select = input(f"Boot: Okay, \"{cus_name}\" Those items are available: Tea, Copie, Pizza, Drinks \nBoot: Which one you want? \nMine: ")
ask_cus_for_Prod = int(input(f"Boot: \"{cus_name}\" How Much I serve for you? \nMine: "))
ask_cus_for_deli = input(f"Boot: \"{cus_name}\" Are you take it for home delivary. (yes/no) \nMine: ")


def price_calculate():
    if 'tea' in cus_Prod_Select:
        return tea * ask_cus_for_Prod
    elif 'copie' in cus_Prod_Select:
        return copie * ask_cus_for_Prod
    elif 'pizza' in cus_Prod_Select:
        return pizza * ask_cus_for_Prod
    elif 'drink' in cus_Prod_Select:
        return drink * ask_cus_for_Prod


if ask_cus_for_deli == "yes":
    customer_address = input(f"Boot: Okay {cus_name}. Enter your address. \nMine: ")
    customer_Phone_no = input(f"Boot: Okay {cus_name}. Enter your Phone Number. \nMine: ")


    print("\nOrder Details: ")
    print("---------------------------------------")
    print(f"Your Name     : {cus_name}")
    print(f"Products Name : {cus_Prod_Select.title()}")
    print(f"Products Items: {ask_cus_for_Prod}")
    print(f"Your Address  : {customer_address.title()}")
    print(f"Your Phone No : {customer_Phone_no}")
    print(f"Total Bill    : {price_calculate()}")

    print("Welcome, Come again!")

else:

    print("\nOrder Details: ")
    print("_______________________________")
    print(f"Your Name     : {cus_name}")
    print(f"Products Name : {cus_Prod_Select.title()}")
    print(f"Products Items: {ask_cus_for_Prod}")
    print(f"Total Bill    : {price_calculate()}")

    print("Welcome, Come again!")
