import random

first_number = random.randint(10, 20)
second_number = random.randint(1, 10)

equation_signs = "+-*/%"
random_sign = random.choice(equation_signs)

user_input = input(
                    f"{first_number} {random_sign} {second_number}"
                    f"\nif your answer contains a fractional part, enter 2 digits after the comma"
                    f"\nWrite your answer: "
                    )

if random_sign == "+":
    correct_answer = first_number + second_number
elif random_sign == "-":
    correct_answer = first_number - second_number
elif random_sign == "*":
    correct_answer = first_number * second_number
elif random_sign == "/":
    correct_answer = round(first_number / second_number, 2)
elif random_sign == "%":
    correct_answer = first_number % second_number

try:
    user_answer = float(user_input)
    if user_answer == correct_answer:
        print("You WON!")
    else:
        print(f"Wrong. The correct answer is {correct_answer}.")
except ValueError:
    print("Invalid input. Please enter a number.")

