class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        self.create_log(msg)

    def create_log(self, msg):
        with open('logs.txt', 'a') as file:
            file.write(msg + '\n')

    def __str__(self):
        return f"CustomException {self.msg}"


try:
    raise CustomException("second err")
except CustomException as exc:
    print(exc)
