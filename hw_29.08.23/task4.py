day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

number_of_the_week = {i + 1: day[i] for i in range(len(day))}
day_of_the_week = {day[i]: i + 1 for i in range(len(day))}

print(number_of_the_week)
print(day_of_the_week)
