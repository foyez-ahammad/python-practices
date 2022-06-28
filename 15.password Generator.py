import random
import string

def password():
  length = int(input("Password Length: "))

  alphabets = string.ascii_letters
  numbers = string.digits
  symbols = string.punctuation
  combine_data = alphabets + numbers + symbols

  password_genarator = random.sample(combine_data, length)
  password = "".join(password_genarator)
  print("Your Password: " + password)

while True:
  password()

