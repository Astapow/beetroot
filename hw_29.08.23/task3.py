import random

result = [(i, i**2) for i in [random.randint(1, 10) for _ in range(3)]]

print(result)
