class Dog:
    def __init__(self, age):
        self.age_factor = 7
        self.age = age

    def human_age(self):
        return self.age_factor * self.age


nessi = Dog(11)
print(nessi.human_age())
