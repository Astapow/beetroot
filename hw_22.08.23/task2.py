user_input = input("Enter your number: ")

if user_input.isdigit() and len(user_input) == 10:
    print("Your number is ok")
else:
    print("Number entered incorrectly")
