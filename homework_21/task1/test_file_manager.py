import os

from pytest import fixture

from homework_21.task1.file_manager import write_to_file, MyFileManager

DATA_FILE = "tested_file.txt"


@fixture
def file_obj():
    with MyFileManager(DATA_FILE, "r") as fp:
        yield fp


@fixture(autouse=True)
def clear_storage():
    with open(DATA_FILE, "w") as fp:
        fp.write("")


def test_write_to_file():
    file_name = "tested_file.txt"
    content = "first tests"

    write_to_file(file_name, content)

    with open(file_name, "r") as file:
        assert file.read() == content

    os.remove(file_name)


def test_write_two_files():
    data_file1 = "data1.txt"
    data_file2 = "data2.txt"

    content1 = "first test"
    content2 = "last test"

    write_to_file(data_file1, content1)
    write_to_file(data_file2, content2)

    with open(data_file1, "r") as fp1, open(data_file2, "r") as fp2:
        assert fp1.read() == content1
        assert fp2.read() == content2

    os.remove(data_file1)
    os.remove(data_file2)
