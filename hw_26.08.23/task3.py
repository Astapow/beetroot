one_hundred_numbers = []

count = 0
while count < 100:
    count += 1
    if count % 7 == 0 and count % 5 != 0:
        one_hundred_numbers.append(count)

print(one_hundred_numbers)
