class MyFileManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.counter = 0

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        self.counter += 1
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.counter -= 1
        if self.counter == 0:
            print(f"file {self.file_name} closed")

        if exc_type is not None:
            print(f"An error occurred: {exc_type}, {exc_val}")
            return True


def write_to_file(file_name, content):
    with MyFileManager(file_name, "w") as fp:
        fp.write(content)


with MyFileManager("test.txt", "w") as fp:
    fp.write("hello")

with MyFileManager("second.txt", "w") as fp:
    fp.write("second file")
