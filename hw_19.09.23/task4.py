class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.create_log(msg)

    def create_log(self, msg):
        with open('logs.txt', 'w') as file:
            file.write(msg + '\n')


try:
    raise CustomException("some error")
except CustomException as exc:
    print(exc)
