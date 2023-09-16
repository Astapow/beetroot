import os

current_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(current_dir, "myfile.txt")


def write_file():
    with open(os.path.join(current_dir, "myfile.txt"), 'w') as file:
        file.write("Hello file world!")


write_file()
