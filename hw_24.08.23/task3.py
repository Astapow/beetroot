import random

user_input = input("Enter text: ").lower()

count = 0
random_strings = []

while count < 5:
    random_string = ''.join(random.choice(user_input) for _ in range(len(user_input)))
    random_strings.append(random_string)
    count += 1

result = ', '.join(random_strings)

print(result)
