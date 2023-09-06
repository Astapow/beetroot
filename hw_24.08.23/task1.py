import random

user_input = input("select number between 1 and 10: ")
random_number = random.randint(1, 10)

if user_input == str(random_number):
    print("You WON")
else:
    print(f"you lose. number was {random_number}")
