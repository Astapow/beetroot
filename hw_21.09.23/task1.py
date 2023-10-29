class Animal:
    def talk(self):
        return "class animal"


class Dog(Animal):
    def talk(self):
        return "gav-gav"


class Cat(Animal):
    def talk(self):
        return "may-may"


def chose_who_talk(animal):
    return animal.talk()


cat = Cat()
dog = Dog()

print(chose_who_talk(cat))
print(chose_who_talk(dog))
