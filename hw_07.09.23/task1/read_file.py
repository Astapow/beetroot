def read_file():
    with open("myfile.txt", 'r') as file:
        text = file.read()

    print(text)


read_file()
