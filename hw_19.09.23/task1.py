class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name


class Student(Person):
    def __init__(self, attendance, assessments, first_name, last_name):
        super().__init__(first_name, last_name)
        self.attendance = attendance
        self.assessments = assessments

    def say_student(self):
        return f"My name is {self.full_name} I'm a student"


class Teacher(Person):
    def __init__(self, salary, first_name, last_name):
        super().__init__(first_name, last_name)
        self.salary = salary

    def say_teacher(self):
        return f"My name is {self.full_name} I'm a teacher and my raise is {self.salary}"


student_obj = Person("Anna", "Lavrova")
print(student_obj.full_name)

student = Student("yes", 100, 'Olecsandr', "Petrov")
print(student.say_student())
print(student.full_name)
print(student.attendance)
print(student.assessments)

teacher = Teacher(20000, "Roman", "Nevin")
print(teacher.full_name)
print(teacher.salary)
print(teacher.say_teacher())
