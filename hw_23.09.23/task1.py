import re


class Email:
    def __init__(self, email):
        self.email = email
        self.validate()

    def validate(self):
        correct = r'^[a-zA-Z0-9]+(?:\.[a-zA-Z0-9])*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]{2,}$'
        if not re.match(correct, self.email):
            raise ValueError("Invalid email address")


email_valid = Email("dddd@gmail.com")
email_valid2 = Email("abc-d@mail.com")
email_valid3 = Email("abc.def@mail.cc")

email_invalid = Email("abc.def@mail")
email_invalid2 = Email("abc#def@mail.com")
email_invalid3 = Email("abc-@mail.com")
